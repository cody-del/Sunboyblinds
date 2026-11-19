# Sunboy website architecture

Proposed structure, November 19, 2026. This is a plan and an unpublished page scaffold. The website now has 20 HTML routes: 15 indexable pages and five noindex layout previews for Service Area and the four counties. Editorial outlines stay outside `dist/`, Netlify's publish directory.

## Recommended foundation

Use one primary Sunboy website with a shared product catalog and a separate layer for local operations. Start with Tampa Bay. Add a reusable location page when a real additional operation is ready, using the same structure for company-owned and future franchise locations.

This keeps the current product URLs stable and makes room for local teams, contact details, coverage, product availability, project photos, reviews, and consultation routing.

```mermaid
flowchart TD
    Brand["Sunboy website"] --> Catalog["Shared product catalog"]
    Brand --> Company["Services, About, Contact"]
    Brand --> Proof["Our Work, Reviews, FAQs"]
    Brand --> Coverage["Service Area: where Sunboy works"]
    Brand --> Locations["Locations: local operating teams"]
    Catalog --> Shades["Shades and individual products"]
    Catalog --> Blinds["Blinds and individual products"]
    Catalog --> Drapes["Drapes and SmartDrape"]
    Locations --> Tampa["Tampa Bay market record"]
    Locations --> Future["Future real operating markets"]
    Coverage -. "assigned to an operating market" .-> Tampa
```

The diagram describes relationships, not a sequence of clicks. The dropdown continues to offer direct links to categories and products.

## Pages to build next

| Page | Proposed URL | Purpose | Current state |
| --- | --- | --- | --- |
| Services | `/services/` | Explain the confirmed consultation and installation offer | Unpublished outline |
| About | `/about/` | Introduce the real company and team | Unpublished outline |
| Service Area | `/service-area/` | Explain confirmed four-county coverage | Published layout preview; noindex |
| Our Work | `/our-work/` | Show actual completed Sunboy projects | Unpublished outline; original projects needed |
| Reviews | `/reviews/` | Present authentic reviews and their sources | Unpublished outline; verified sources needed |
| FAQs | `/faqs/` | Answer real consultation, installation and product questions | Unpublished outline |
| Privacy | `/privacy/` | Explain the actual forms, providers and data use | Unpublished outline; complete around the chosen setup |

Service Area now opens its page layout through a normal navigation link. The county selector opens four matching county layouts. Services and About remain the next page templates to build; their navigation items still use detail dialogs.

The source outlines contain section placeholders and inputs needed. The owner has authorized the five service-area layouts as publicly viewable noindex previews:

- [Services outline](drafts/services.md)
- [About outline](drafts/about.md)
- [Service Area outline](drafts/service-area.md)
- [Our Work outline](drafts/our-work.md)
- [Reviews outline](drafts/reviews.md)
- [FAQs outline](drafts/faqs.md)
- [Privacy outline](drafts/privacy.md)

## Shared product library

Keep the existing category and product URLs:

- `/shades/` with Roller, Solar, Honeycomb, Woven Wood, and Roman Shade pages.
- `/blinds/` with Horizontal and Vertical Blind pages.
- `/drapes/` links to the existing `/indoor/smartdrape/` product page.
- `/outdoor/exterior-retractable-screens/`.

The existing homepage, contact page, accessibility page, catalog pages, and SmartDrape redirect remain in place. There is no URL migration in this architecture change.

Each future market can reference its available product IDs. Product information stays centrally maintained. If a particular local offering later merits a separate page, decide that from its actual purpose and evidence rather than generating a city-by-product grid by default.

Shutters remain a confirmation item: they appear in the earlier approved homepage row, but were absent from the latest detailed product lineup. A `/shutters/` route is reserved conditionally; no new offering page is published.

## Local operations and service areas

| Page type | Example or pattern | What belongs there |
| --- | --- | --- |
| Operating-market directory | `/locations/` | A useful selector for real operating markets, once needed |
| Local operation | `/locations/fl/tampa-bay/` | The real local team, contacts, available products, coverage, work and reviews |
| City coverage | `/service-area/{city-state}/` | Confirmed coverage, useful local details and links to the responsible operation |
| Project | `/our-work/{project-slug}/` | Original work tied to a product, city and operating market |

The initial Tampa Bay market serves Pinellas, Hillsborough, and Manatee counties, plus parts of southern Polk County. This remains one operating market. Its location-page route is reserved now, with an [unpublished outline](drafts/tampa-bay-market.md). No other market, office, address, local phone or Google Business Profile is invented.

At launch, the homepage and Service Area page can explain the initial Tampa Bay coverage. A separate Tampa Bay operation page becomes useful when it has distinct local team/contact/project information, and before the homepage evolves into a broader brand page as other markets open. Avoid making two pages interchangeable.

A city page describes where the team works. It does not imply a staffed office or a separate business location. City routes include the state in their slug to distinguish places with the same name. Their assignment to a stable market ID can change without changing the city's URL.

Google's Business Profile guidance distinguishes service coverage from separately staffed operating locations. Separate service-business profiles require eligible real locations with separate staff and service areas; adding website city pages does not establish that eligibility. [Google Business Profile guidelines](https://support.google.com/business/answer/3038177?hl=en)

City pages should help someone in that city, supported by actual coverage and local material. Google identifies substantially similar regional/city pages that funnel users to a common destination as examples of doorway abuse. This is a reason to plan useful local pages selectively, not a rule that all city pages are inappropriate. [Google's doorway policy](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse)

## Confirmed launch coverage

The owner confirmed three full counties and partial coverage in southern Polk County on November 19, 2026. “Hillsboro” was interpreted as Hillsborough County using the [official Hillsborough County name](https://hcfl.gov/).

| County | Planned coverage page | Outline |
| --- | --- | --- |
| Pinellas County | `/service-area/pinellas-county-fl/` | [Draft outline](drafts/pinellas-county-fl.md) |
| Hillsborough County | `/service-area/hillsborough-county-fl/` | [Draft outline](drafts/hillsborough-county-fl.md) |
| Manatee County | `/service-area/manatee-county-fl/` | [Draft outline](drafts/manatee-county-fl.md) |
| South Polk County — south side only | `/service-area/south-polk-county-fl/` | [Draft outline](drafts/south-polk-county-fl.md) |

These are county coverage pages for the same initial operation. They do not establish four branches. The owner requested placeholder layouts, so the four county pages and Service Area overview are now published for review with noindex, follow and excluded from the XML sitemap. Add useful local material before promoting them to indexable pages. City pages can be considered later without duplicating every product across every city.

## Data that allows expansion

[markets.json](markets.json) contains a single initial Tampa Bay record, with unknown details left empty. Its stable market ID is `tampa-bay-fl`. The structure has room for:

- The operating team/entity and ownership model.
- Verified contacts, customer-visit model and hours.
- Confirmed launch counties, with room for city/postal-code details later.
- Local product availability referencing the shared catalog.
- Original projects and verified review sources.
- The destination for consultation requests.

The record does not assume an office, a public address, a franchise operator or an active form destination. Online form delivery stays deferred as previously requested.

Later, the shared `/contact/` journey can receive validated market/product context and route the request to that market's configured destination. The visible three-field form does not change in this planning phase. Requests without a determined market need a defined central handling path before routing is activated.

Future local editors can maintain their own market information while brand/product content stays centrally controlled. That is a future permissions requirement, not an implemented CMS or account system.

## Reserved for later

- `/locations/` and real market pages when the directory and local operation content are useful.
- `/resources/` and individual guides when original content is ready to maintain.
- `/franchise/` only when an actual approved franchise offer exists.
- Separate service-detail pages only when there is a confirmed service and a distinct reason for the page.

The business can start with one local operation. Reserving these routes does not make franchise language part of the customer-facing site today.

## Placeholder and publishing approach

Keep unbuilt outlines outside the public build. Five owner-authorized layout previews are now available through normal links for review; each has noindex, follow and is excluded from the XML sitemap. The preview status is separate from both live/indexable pages and unbuilt drafts. Promote a preview to live only when the placeholder sections have been completed and its indexing directive is updated. All remaining drafts stay unpublished.

If a hosted review environment is needed later, use a controlled preview. A `noindex` rule can control search indexing when Google can crawl it; it is not access control, and a robots.txt block can prevent Google from seeing the rule. The five review layouts use per-page noindex; robots.txt still permits crawling so search engines can see that directive. [Google's indexing guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing)

## Next steps

1. Confirm the final business domain. The current configured origin is the Netlify subdomain; no business domain has been supplied here. Launch coverage is already confirmed at county level.
2. Review the five Service Area/county layout previews, then build Services and About in the same design.
3. Replace county placeholders with useful local details, actual projects and verified review material; select city pages later as useful local material becomes available.
4. Complete supporting pages and connect the consultation form when its actual destination is chosen.
5. Reuse the market template when a real new operation opens. Review shared Tampa Bay-specific wording before introducing a broader brand homepage and catalog presentation.

## Source files and validation

- [routes.json](routes.json): 15 indexable routes, five published noindex previews, other proposed pages, statuses, parent relationships, reserved patterns and navigation plan.
- [markets.json](markets.json): initial operating-market record and future routing requirements.
- [drafts/](drafts/): twelve unpublished page outlines, including four coverage hubs.

Run `python3 scripts/check_site_architecture.py` from the repository root to verify route uniqueness, parent relationships, market references, live-file/sitemap coverage, exclusion of unbuilt draft routes from live output, and noindex/sitemap exclusion for the five layout previews. This is a project consistency check; it is not a ranking forecast or a full SEO audit.

South Polk is explicitly partial coverage: only parts of the southern side are served. Specific towns and ZIP codes have not been confirmed. Sarasota has been removed from the current plan; its former preview URL redirects to the Service Area overview. The Indoor dropdown now groups SmartDrape beneath a clickable Drapes category heading.
