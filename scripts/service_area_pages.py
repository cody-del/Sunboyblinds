"""Render the owner-authorized Service Area and county layout previews."""
from html import escape


def county_selector(counties):
    links = ''.join(
        f'<li><a href="{page["url"]}"><span>{escape(page["county"])}</span>'
        '<span class="county-link-detail">View service area</span></a></li>'
        for page in counties)
    return f'''<section class="coverage-county-menu" aria-labelledby="county-menu-title">
      <div class="coverage-menu-heading"><img src="/assets/sunboy-sunseal.svg" alt="" width="700" height="700"><h2 id="county-menu-title">Choose your county.</h2></div>
      <ul>{links}</ul>
    </section>'''


def photo_placeholder():
    return '''<div class="coverage-hero-placeholder">
      <img src="/assets/sunboy-sunseal.svg" alt="" width="700" height="700">
      <span>Local photo placeholder</span>
    </div>'''


def product_groups(catalog):
    groups = []
    for category in catalog['categories']:
        links = ''.join(
            f'<li><a href="/{item["category"]}/{item["slug"]}/">{escape(item["title"])}</a></li>'
            for item in catalog['products'] if item['category'] == category['slug'])
        groups.append(f'<div><h3><a href="/{category["slug"]}/">{escape(category["title"])}</a></h3><ul>{links}</ul></div>')
    for item in sorted(catalog['products'], key=lambda product: product['category'] == 'outdoor'):
        if item['category'] not in ('shades', 'blinds'):
            groups.append(f'<div><h3><a href="/{item["category"]}/{item["slug"]}/">{escape(item["title"])}</a></h3></div>')
    return f'''<section class="catalog-content coverage-products" aria-labelledby="coverage-products-title">
      <h2 id="coverage-products-title">Window treatments for your home.</h2>
      <div class="coverage-product-groups">{''.join(groups)}</div>
    </section>'''


def local_placeholders():
    return '''<section class="catalog-content coverage-draft-grid" aria-label="Local information">
      <div class="coverage-draft-block"><h2>In your neighborhood.</h2><p>Local area details placeholder.</p><div class="coverage-placeholder-lines" aria-hidden="true"><span></span><span></span></div></div>
      <div class="coverage-draft-block"><h2>Customer reviews.</h2><p>Review placeholder.</p><div class="coverage-placeholder-lines" aria-hidden="true"><span></span><span></span></div></div>
    </section>
    <section class="catalog-content coverage-projects" aria-labelledby="coverage-projects-title">
      <h2 id="coverage-projects-title">Local projects.</h2>
      <div class="coverage-gallery"><div class="coverage-photo-slot">Project photo placeholder</div><div class="coverage-photo-slot">Project photo placeholder</div><div class="coverage-photo-slot">Project photo placeholder</div></div>
    </section>'''


def area_navigation(counties, current):
    links = ''.join(
        f'<li><a href="{page["url"]}"' + (' aria-current="page"' if page['url'] == current else '')
        + f'>{escape(page["county"])}</a></li>' for page in counties)
    return f'''<nav class="coverage-area-navigation" aria-label="County service areas"><a class="coverage-back-link" href="/service-area/">All service areas</a><ul>{links}</ul></nav>'''


CTA = '''<section class="catalog-consultation" aria-labelledby="catalog-cta-title">
  <div><h2 id="catalog-cta-title">Schedule a free in-home consultation.</h2><p>Professional installation across our service area.</p></div>
  <a class="sunboy-button catalog-button" href="/contact/">Book a Consultation</a>
</section>'''


def render(document, save, breadcrumbs, plan, catalog):
    counties = [page for page in plan['pages']
                if page['type'] == 'coverage_county' and page['status'] in ('preview', 'live')]
    hub = next(page for page in plan['pages'] if page['id'] == 'service-area')
    if hub['status'] not in ('preview', 'live'):
        return 0
    names = [page['county'].removesuffix(' County') for page in counties]
    assert names, 'Service Area needs at least one published county layout'
    if len(names) == 1:
        coverage = names[0] + ' County'
    else:
        coverage = (', '.join(names[:-1]) + (', and ' if len(names) > 2 else ' and ')
                    + names[-1] + ' counties')
    crumbs, schema = breadcrumbs([(hub['url'], 'Service Area')])
    content = f'''<section class="catalog-hero" aria-labelledby="catalog-title"><div class="catalog-hero-inner">
      <div class="catalog-intro">{crumbs}<h1 id="catalog-title">Our service area.</h1><p>Serving {escape(coverage)} with free in-home consultations and professional installation.</p><a class="sunboy-button catalog-button" href="/contact/">Book a Consultation</a></div>
      {county_selector(counties)}
    </div></section>{product_groups(catalog)}{local_placeholders()}'''
    save(hub['url'], document('Service Area',
         f'Sunboy Blinds serves {coverage}. Explore our service areas and book a free in-home consultation.',
         hub['url'], content, schema, preview=hub['status'] == 'preview',
         body_class='catalog-page coverage-page', cta=CTA))
    for page in counties:
        county = escape(page['county'])
        crumbs, schema = breadcrumbs([(hub['url'], 'Service Area'), (page['url'], page['county'])])
        content = f'''<section class="catalog-hero" aria-labelledby="catalog-title"><div class="catalog-hero-inner">
          <div class="catalog-intro">{crumbs}<h1 id="catalog-title">{county}.</h1><p>Sunboy offers free in-home consultations and professional window treatment installation in {county}.</p><a class="sunboy-button catalog-button" href="/contact/">Book a Consultation</a></div>
          {photo_placeholder()}
        </div></section>{product_groups(catalog)}{local_placeholders()}{area_navigation(counties, page['url'])}'''
        save(page['url'], document(f'Window Treatments in {page["county"]}',
             f'Sunboy Blinds serves {page["county"]} with free in-home consultations and professional window treatment installation.',
             page['url'], content, schema, preview=page['status'] == 'preview',
             body_class='catalog-page coverage-page', cta=CTA))
    return 1 + len(counties)
