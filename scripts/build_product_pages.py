"""Render the catalog and synchronize shared navigation without dependencies."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
ORIGIN = 'https://sunboyblinds.netlify.app'
VERSION = 'product-navigation-2'
DATA = json.loads((ROOT / 'src/catalog.json').read_text())
PRODUCTS = {item['slug']: item for item in DATA['products']}
HEADER = (ROOT / 'src/partials/header.html').read_text().strip()
FOOTER = (ROOT / 'src/partials/footer.html').read_text().strip()
INFO = (ROOT / 'src/partials/info-dialog.html').read_text().strip()


def url(item):
    return f'/{item["category"]}/{item["slug"]}/'


def picture(item, lazy=False):
    if not item.get('image'):
        return ''
    return (f'<img src="/assets/products/{escape(item["image"])}" '
            f'alt="{escape(item["alt"])}" width="800" height="700" '
            f'loading="{"lazy" if lazy else "eager"}" decoding="async">')


def card(item):
    return (f'<li><a class="catalog-card" href="{url(item)}" aria-labelledby="card-{item["slug"]}">{picture(item, True)}'
            f'<h3 id="card-{item["slug"]}">{escape(item["title"])}</h3><p>{escape(item["summary"])}</p></a></li>')


def breadcrumbs(crumbs):
    entries = [('/', 'Home')] + crumbs
    parts = []
    schema = []
    for i, (path, label) in enumerate(entries, 1):
        if i == len(entries):
            parts.append(f'<li><span aria-current="page">{escape(label)}</span></li>')
        else:
            parts.append(f'<li><a href="{path}">{escape(label)}</a></li>')
        schema.append({'@type': 'ListItem', 'position': i, 'name': label,
                       'item': ORIGIN + path})
    html = '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>' + ''.join(parts) + '</ol></nav>'
    structured = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': schema}
    return html, json.dumps(structured, ensure_ascii=False).replace('<', '\\u003c')


CTA = '''<section class="catalog-consultation" aria-labelledby="catalog-cta-title">
  <div><h2 id="catalog-cta-title">Schedule a free in-home consultation.</h2><p>Professional installation for homes across Tampa Bay.</p></div>
  <a class="sunboy-button catalog-button" href="/contact/">Book a Consultation</a>
</section>'''


def document(title, description, path, content, schema):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#6db2e4">
  <title>{escape(title)} — Sunboy Blinds</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{ORIGIN}{path}">
  <link rel="preload" href="/assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/styles.css?v={VERSION}">
  <script src="/app.js?v={VERSION}" defer></script>
  <script type="application/ld+json">{schema}</script>
</head>
<body class="catalog-page" id="top">
  <a class="skip-link" href="#main">Skip to content</a>
  {HEADER}
  <main id="main">{content}{CTA}</main>
  {FOOTER}
  {INFO}
</body>
</html>
'''


def save(path, html):
    target = DIST / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)


for category in DATA['categories']:
    path = f'/{category["slug"]}/'
    crumbs, schema = breadcrumbs([(path, category['title'])])
    items = [p for p in DATA['products'] if p['category'] == category['slug']]
    content = f'''<section class="catalog-hero" aria-labelledby="catalog-title"><div class="catalog-hero-inner">
      <div class="catalog-intro">{crumbs}<h1 id="catalog-title">{category['title']} for your<br> Tampa Bay home.</h1><p>{escape(category['intro'])}</p><a class="sunboy-button catalog-button" href="#compare">Explore {category['title'].lower()}</a></div>
      <div class="catalog-photo">{picture(category)}</div>
    </div></section>
    <section class="catalog-content" id="compare" aria-labelledby="compare-title"><div class="catalog-section-intro"><h2 id="compare-title">{escape(category['heading'])}</h2><p>{escape(category['body'])}</p></div>
      <ul class="catalog-grid catalog-grid-{"two" if len(items)==2 else "four"}">{''.join(card(item) for item in items)}</ul>
    </section>'''
    save(path, document(f'{category["title"]} in Tampa Bay', category['intro'], path, content, schema))

for item in DATA['products']:
    path = url(item)
    parent = next((c for c in DATA['categories'] if c['slug'] == item['category']), None)
    trail = [(f'/{parent["slug"]}/', parent['title'])] if parent else []
    crumbs, schema = breadcrumbs(trail + [(path, item['title'])])
    photo = f'<div class="catalog-photo">{picture(item)}</div>' if item.get('image') else ''
    solo = ' catalog-hero-solo' if not photo else ''
    related = [PRODUCTS[slug] for slug in item['related']]
    related_html = (f'<section class="catalog-related" aria-labelledby="related-title"><h2 id="related-title">'
                    f'{"Compare more " + parent["title"].lower() if parent else "Explore indoor options"}</h2>'
                    f'<ul class="catalog-grid catalog-grid-{"three" if len(related)==3 else "two"}">{"".join(card(p) for p in related)}</ul></section>') if related else ''
    content = f'''<section class="catalog-hero{solo}" aria-labelledby="catalog-title"><div class="catalog-hero-inner">
      <div class="catalog-intro">{crumbs}<h1 id="catalog-title">{escape(item['title'])}</h1><p>{escape(item['intro'])}</p><a class="sunboy-button catalog-button" href="/contact/">Book a Consultation</a></div>{photo}
    </div></section>
    <section class="catalog-content catalog-details" aria-labelledby="details-title"><div><h2 id="details-title">{escape(item['heading'])}</h2><p>{escape(item['body'])}</p></div><div class="catalog-consider"><h2>What to consider</h2><ul>{''.join('<li>' + escape(point) + '</li>' for point in item['consider'])}</ul></div></section>
    {related_html}'''
    description = f'{item["title"]} for Tampa Bay homes. {item["summary"]} Schedule a free in-home consultation with Sunboy Blinds.'
    save(path, document(f'{item["title"]} in Tampa Bay', description, path, content, schema))

# Keep the authored homepage/contact content while updating shared navigation.
for relative in ['index.html', 'contact/index.html', 'accessibility/index.html']:
    target = DIST / relative
    text = target.read_text()
    if relative != 'accessibility/index.html':
        header = HEADER.replace('href="/contact/"', 'href="#contact-form"') if relative.startswith('contact/') else HEADER
        text = re.sub(r'<header class="navbar">.*?</header>', lambda _: header, text, flags=re.S)
    footer = FOOTER.replace('href="/accessibility/"', 'href="/accessibility/" aria-current="page"') if relative.startswith('accessibility/') else FOOTER
    if relative.startswith('contact/'):
        footer = footer.replace('<a href="/contact/">Contact</a>', '<a href="/contact/" aria-current="page">Contact</a>')
    text = re.sub(r'<footer class="site-footer".*?</footer>', lambda _: footer, text, flags=re.S)
    text = re.sub(r'(/styles\.css\?v=)[^"\s]+', rf'\g<1>{VERSION}', text)
    text = re.sub(r'(/app\.js\?v=)[^"\s]+', rf'\g<1>{VERSION}', text)
    page_path = '/' if relative == 'index.html' else '/' + str(Path(relative).parent) + '/'
    canonical = f'<link rel="canonical" href="{ORIGIN}{page_path}">'
    if 'rel="canonical"' in text:
        text = re.sub(r'<link rel="canonical"[^>]+>', lambda _: canonical, text)
    else:
        text = text.replace('</head>', canonical + '\n</head>')
    target.write_text(text)

paths = ['/' + str(p.relative_to(DIST).parent).replace('.', '').strip('/') + '/' for p in DIST.rglob('index.html')]
paths = sorted(set('/' if path == '//' else path for path in paths))
urls = ''.join(f'<url><loc>{ORIGIN}{escape(path)}</loc></url>\n' for path in paths)
(DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
(DIST / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n')
print(f'Rendered {len(DATA["categories"])} category pages and {len(PRODUCTS)} product pages; sitemap has {len(paths)} URLs.')
