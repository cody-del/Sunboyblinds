"""Check the route plan against the static site without publishing drafts."""
from pathlib import Path
from collections import Counter
import json
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

for page in pages:
    url = page['url']
    assert url.startswith('/') and url.endswith('/') and '?' not in url and '#' not in url, url
    assert '..' not in Path(url).parts, url
    assert page['status'] in {'live', 'draft', 'reserved', 'conditional'}, page['id']
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
    if page['status'] == 'live':
        assert target.is_file(), (url, 'missing live page')
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
assert deployed_urls == live_urls, ('live route inventory mismatch', deployed_urls ^ live_urls)
origin = plan['configured_site_origin'].rstrip('/')
sitemap_urls = {node.text for node in ET.parse(DIST / 'sitemap.xml').getroot().iter()
                if node.tag.endswith('loc')}
assert sitemap_urls == {origin + url for url in live_urls}, 'Sitemap differs from live route plan'

for market in markets['markets']:
    page = by_id.get(market['page_id'])
    assert page is not None and page.get('market_id') == market['id'], market['id']

counts = Counter(page['status'] for page in pages)
print(f'Architecture passed: {len(pages)} route records, {counts["live"]} live pages, '
      f'{counts["draft"]} draft pages, {counts["reserved"]} reserved pages, '
      f'{counts["conditional"]} conditional page. No planned routes are published.')
