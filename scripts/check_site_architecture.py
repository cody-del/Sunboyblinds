"""Check the route plan against the static site without publishing drafts."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
plan = json.loads((ROOT / 'architecture/routes.json').read_text())
markets = json.loads((ROOT / plan['markets_file']).read_text())
pages = plan['pages']
ids = [page['id'] for page in pages]
urls = [page['url'] for page in pages]
assert not [key for key, count in Counter(ids).items() if count > 1], 'Duplicate page IDs'
assert not [key for key, count in Counter(urls).items() if count > 1], 'Duplicate planned URLs'
assert plan['publication']['live_directory'] == 'dist'
assert plan['publication']['include_in_live_sitemap'] == ['live']
market_ids = {market['id'] for market in markets['markets']}
assert plan['default_market_id'] in market_ids
by_id = {page['id']: page for page in pages}
live_urls = set()
preview_urls = set()


class RobotsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot'):
            tokens = re.split(r'[,\s]+', attrs.get('content', '').lower())
            self.noindex |= 'noindex' in tokens or 'none' in tokens

for page in pages:
    url = page['url']
    assert url.startswith('/') and url.endswith('/') and '?' not in url and '#' not in url, url
    assert '..' not in Path(url).parts, url
    assert page['status'] in {'live', 'preview', 'draft', 'reserved', 'conditional'}, page['id']
    parent = page['parent_id']
    assert parent is None or parent in by_id, (page['id'], 'missing parent')
    ancestors = {page['id']}
    while parent:
        assert parent not in ancestors, (page['id'], 'parent cycle')
        ancestors.add(parent)
        parent = by_id[parent]['parent_id']
    if page.get('market_id'):
        assert page['market_id'] in market_ids, page['id']
    target = DIST / url.strip('/') / 'index.html'
    if page['status'] in ('live', 'preview'):
        assert target.is_file(), (url, 'missing live page')
        robots = RobotsParser()
        robots.feed(target.read_text())
        if page['status'] == 'preview':
            assert robots.noindex, (url, 'layout preview must have noindex')
            preview_urls.add(url)
        else:
            assert not robots.noindex, (url, 'live page has unexpected noindex')
            live_urls.add(url)
    else:
        assert not target.exists(), (url, 'unpublished page exists in live output')
    if page.get('draft_file'):
        draft = ROOT / page['draft_file']
        assert draft.is_file(), draft
        assert not draft.resolve().is_relative_to(DIST.resolve()), draft

deployed_urls = set()
for path in DIST.rglob('index.html'):
    relative = path.relative_to(DIST).parent.as_posix()
    deployed_urls.add('/' if relative == '.' else f'/{relative}/')
assert deployed_urls == live_urls | preview_urls, ('published route inventory mismatch', deployed_urls ^ (live_urls | preview_urls))
origin = plan['configured_site_origin'].rstrip('/')
sitemap_urls = {node.text for node in ET.parse(DIST / 'sitemap.xml').getroot().iter()
                if node.tag.endswith('loc')}
assert sitemap_urls == {origin + url for url in live_urls}, 'Sitemap differs from live route plan'

for market in markets['markets']:
    page = by_id.get(market['page_id'])
    assert page is not None and page.get('market_id') == market['id'], market['id']

counts = Counter(page['status'] for page in pages)
print(f'Architecture passed: {len(pages)} route records, {counts["live"]} live pages, '
      f'{counts["preview"]} noindex previews, {counts["draft"]} draft pages, '
      f'{counts["reserved"]} reserved pages, {counts["conditional"]} conditional page. '
      'Only live routes appear in the sitemap.')
