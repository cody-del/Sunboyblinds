# Hero verification — November 16, 2026

Scope: homepage hero, shared navbar, native dialogs, mobile menu and accessibility route. Engineering target: WCAG 2.2 AA for changed components; this is not a full conformance assessment.

- JavaScript syntax check, Git whitespace check and local link/media existence checks passed.
- Original retired desktop/mobile video copies verified by SHA-256 against the read-only John Crawford source.
- Rendered in the ChatGPT in-app browser at the desktop viewports (1110px, 1280px and 1431px during the session), 390px and 320px. No horizontal overflow at 390px or 320px.
- Verified latest user-supplied H1 stays exactly two lines at desktop, 390px and 320px, 92px desktop navbar and 78px mobile navbar.
- Manually checked background pause, film open/close, Escape dismissal, focus return, mobile menu expansion and Service Area detail dialog.
- Checked the accessibility route by direct navigation at 320px.
- Reduced-motion, data-saver and offscreen behavior implemented. A real OS reduced-motion preference change was not exercised.
- Screen-reader testing, real browser zoom and an automated axe scan were not performed. This remains a scoped hero prototype, not a full site launch assessment.
- Consultation/contact destination and monitored assistance contact details are not supplied. No form submissions or messages were sent.

Latest centered hero: two CTA designs and the requested Google/Facebook five-star badge treatments. CTA buttons remain disabled and badges unlinked pending real destinations. Ratings were not verified; no review counts were invented. These are design elements for the private preview.

## Button styling revision — November 16, 2026

- Sampled the supplied logo's dominant blue: RGB 109, 178, 228 / #6DB2E4. Updated the shared button color and browser theme color.
- Replaced raised edges with flat pill shapes, white lettering and a subtle highlight contained inside the button face. Removed bottom/side shadows in desktop and mobile rules.
- Rendered at 1280px and 320px. Both blue buttons report RGB 109, 178, 228 backgrounds, white text and no box shadow. No horizontal overflow at 320px.
- The exact requested light blue with white lettering has approximately 2.3:1 text contrast, below WCAG AA text thresholds. This requested visual treatment remains a private prototype; brand/design review must resolve the text contrast before a public launch. No AA conformance claim is made.

## Navigation typography revision — November 16, 2026

- Replaced navbar typography with self-hosted Manrope, supplied with its OFL license. Desktop labels are 15px/500; mobile menu labels are 17px/500.
- Split Indoor and Outdoor and added Services on desktop and mobile. Each opens the appropriate detail panel.
- Checked desktop at 1280px, the full navigation at 961px, and the collapsed menu at 320px. No overflow or overlapping header items in these states.
- Verified Indoor, Outdoor and Services using Enter, Escape dismissal, and focus return. Mobile Services returns focus to the closed menu toggle.
- Added matching CSS/JavaScript asset revisions so older cached navigation logic is refreshed with the new labels.
- Scoped change: navigation only. Hero copy, hero typography, video and button colors are unchanged. Previously recorded prototype limits remain.

## Pendant and consultation section — November 16, 2026

- Inserted a white circle (351, 434; radius 240) underneath the existing blue vector artwork. The shared 510×510 viewBox ensures backing/artwork scale together. The backing is inset from the outer badge extent; there is no separate CSS backing to drift at breakpoints.
- Displayed the SVG as a 164px desktop pendant overlapping the hero/section boundary; observed a square 118px badge on 320px mobile.
- Added left trust list and right form; stacked them on mobile. No horizontal overflow at 320px, and input fields remain inside the form card.
- Moved the narrow-mobile video pause control above the pendant so their bounds do not overlap. Decorative pendant ignores pointer events.
- Verified hero CTA navigation to the form. Filled the form with synthetic data: invalid email and ZIP were detected, valid replacements cleared the invalid fields. No requests were sent.
- Destination remains unknown. Form submission remains disabled with a submit guard; no fake success state or external side effects.
- New full-page desktop and mobile screenshots saved. Screen-reader and real browser zoom checks remain untested; existing prototype limitations remain.

## Sun seal and section colors — November 16, 2026

- White section background and exact logo-blue form panel verified from rendered styles; form copy uses dark ink and inputs remain white. Dark form text on blue exceeds 4.5:1, and the input borders exceed 3:1 against blue. The existing hero-button contrast limitation is unchanged.
- New supplied seal separated into outer rays and stationary face/frame SVG layers, both sharing viewBox 1.3 83.7 700 700. White backing radius 247 stays inside the fixed blue ring radius 252 and scales in the same coordinate system.
- Browser confirmed ray transform is an animated matrix and face transform is none. Enter toggles Pause animation / Play animation, and animation state switches running / paused independently of the face.
- At 320px the pendant wrapper is 148×148, the consultation anchor leaves the full seal visible, and no horizontal overflow occurs. Control/trust spacing and video-control clearance checked.
- Reduced motion is implemented through the shared matchMedia setting and preference-change listener; a real OS preference change was not exercised. Native pause/resume was tested.
- Screen-reader review remains untested; form routing is still unconfigured and submission disabled.

## Full blue consultation section — November 17, 2026

- Section background now shares the same #6DB2E4 variable as the form and sun. Dark ink trust text/checks and white inputs remain readable; dividers use a subtle ink tint.
- Rendered styles confirmed matching RGB 109, 178, 228 section/form backgrounds at 1280px and 320px, white fields, and no horizontal overflow.
- Scope limited to colors and CSS revision. Animation, form behavior and existing prototype limitations are unchanged.

## Shared subtle motion control — November 17, 2026

- Removed the dedicated control beneath the sun, its styles and associated event handlers. Reduced the spacing previously reserved for it.
- Existing hero control now says Pause motion / Play motion and shares one preference state across video and rays. Offscreen pausing does not alter the user's chosen motion state. Reduced-motion and data-saver defaults remain respected.
- Control is now a quieter 32px-high translucent pill; keyboard focus remains clearly visible.
- Browser keyboard checks: pause stops the video and rays, navigating to the consultation section keeps both paused, resume restarts both, and the face remains untransformed. No browser errors during these checks.
- At 320px: one motion control remains, no under-sun control is present, target height is 32px and no horizontal overflow occurs. Accessibility instructions updated for the shared control.

## Slower sun rotation — November 17, 2026

- Doubled the ray animation duration from 45 seconds to 90 seconds per revolution, halving its speed. Only the timing and CSS asset revision changed. Source and whitespace checks passed; prior layout and shared-control checks remain applicable.

## Compact section and consistent typography — November 18, 2026

- Replaced form heading with the user-supplied “Schedule a free in-home consultation.” and removed the old introduction. Free in-home consultation is a user-supplied offer; no other terms added.
- Unified text typography to Manrope. Browser styles confirmed the same family on the hero, nav, trust heading, form heading, labels and fields. Headings use 800, trust points/labels 700, and navigation 600. Deeper ink #15384D improves contrast with unchanged blue.
- Aligned the two columns at the top, reduced gap from 88px to 56px, removed redundant form padding and tightened field/outer spacing. Rendered desktop section height is about 747px.
- At 1280px, both columns begin at the same vertical position and the new form heading wraps cleanly. At 320px, the form is 276px wide and there is no horizontal overflow.
- Hero H1 remains exactly two lines at desktop and 320px: its height is twice the computed line height. Form labels render at 14px, with 16px input text.
- Copy remains literal HTML. Animation and form routing behavior are unchanged; submission is still disabled pending a destination. Prior prototype limitations remain.

## Simple balanced homepage section — November 18, 2026

- Removed ZIP, interest and project-detail fields. Only Full name, Email and Phone remain, all required with name/email/tel autocomplete. Submit copy is Request Consultation.
- Kept Manrope and softened the section typography to 700 for the centered heading and 600 for trust points/labels. Removed the competing left heading and converted the consultation heading to a shared H2 in literal HTML.
- Replaced repeated checks with four original, matching SVG line icons (installation/window, turnaround/clock, in-house/person and satisfaction/smiling sun). Icons are decorative beside their text; no extra business claims added.
- At 1280px, both columns are 456px wide and centered about the sun badge. The section is about 626px high, compared with about 747px before this revision. The entire form is visible in the captured section view.
- At 320px, there is no horizontal overflow; the shared title wraps to two lines. Empty fields are invalid, an invalid email is detected, and synthetic valid values clear all invalid fields. No live submission sent.
- Form submission remains disabled pending its destination. Existing motion, private access and other prototype limitations are unchanged.

## Larger Sunboy trust icons — November 18, 2026

- Replaced the small generic line icons with four custom SVG assets: a sunlit blind, a clock using the supplied seal rays, the supplied Sunboy mascot, and a smiling sun using the same rays. Navy outlines and white interiors match the section; source brand artwork is unchanged.
- Enlarged icon boxes from 32px to 48px on desktop and from 28px to 40px on mobile. Retained the approved heading, columns, labels and form.
- Browser checks at 1280px and 320px confirmed all four assets load at the intended size. At 320px, all trust labels remain on one line and document width equals viewport width. Icons have empty alt text because the adjacent HTML labels convey their meaning.
- Saved the desktop section screenshot. Git whitespace and SVG parsing checks passed. Existing form, motion and private-preview behavior are unchanged.

## Illustrated white SVG trust set — November 18, 2026

- Installed the approved illustrated drill and clock, a revised construction helmet with more realistic shell/rim/attachment contours, and a plain geometric sun without a face. Each sits beside its matching trust label.
- Converted the white illustration planes into SVG paths with even-odd cutouts. All four SVGs contain only white paint, no background rectangle, black/blue paint, embedded bitmap, script, or external references. Blue visible within the artwork is the actual section background. Combined SVG size is about 133KB.
- Enlarged boxes to 56px desktop and 44px mobile to retain illustration detail. Trust labels remain literal HTML, and decorative icons retain empty alt text.
- Visually checked the desktop consultation section in native Google Chrome, including all four loaded icons, transparent interior openings, title, labels and form placement. Browser integration was unavailable; the native mobile check was interrupted by user browser activity, so no new mobile-browser pass is claimed. Narrow-screen CSS sizing was reviewed against the existing 320px layout.
- SVG XML/white-only paint checks, asset existence and Git whitespace checks passed. Form, motion controls, copy and private access remain unchanged.

## White illustrated icons and asterisk labels — November 18, 2026

- Included the existing approved white drill, clock, hard hat and sun SVG illustrations from the icon side chat. Their transparent cutouts keep the section blue visible. Boxes are 56px on desktop and 44px on mobile.
- Removed the visible all-fields-required introduction and marked Full name, Email and Phone with asterisks. Native required attributes, autocomplete and empty-field validation remain. Asterisks are decorative for assistive technology; labels remain associated with their inputs.
- Browser checks at 1280px and 320px confirmed all four illustrations load, three starred labels appear, and there is no horizontal overflow. All trust labels remain on one line at 320px. Empty required fields still report valueMissing. Desktop and mobile screenshots saved.
- Git whitespace and SVG parsing checks passed. This was a scoped visual/form-label check; no screen-reader session, automated accessibility audit or live submission was performed. Form routing remains unconfigured and submission disabled.

## Supplied heading artwork and form cleanup — November 18, 2026

- Replaced the consultation heading's visible font rendering with the user-supplied white SVG lettering. Retained the same text as an HTML H2 accessible name. A mobile SVG reuses the exact path artwork in two centered lines at the space after “free.”
- Removed the stars from Email and Phone, retaining the star beside Full name per the user's clarification. All three native required attributes remain. No all-fields-required sentence exists in the source.
- Local browser checks at 1280px and 320px show the supplied artwork, the intended labels, and no horizontal overflow. The mobile heading uses the two-line SVG.
- The previously open hosted preview still showed the older form after reload, despite the prior deployment's success result. This revision therefore requires direct verification of the hosted heading and labels after publication.
- Scope is heading artwork and labels; form routing remains unconfigured and submission disabled. Screen-reader testing and a full accessibility audit were not performed.

## Navy consultation heading — November 18, 2026

- Recolored the supplied desktop heading artwork and its two-line mobile derivative to #15384D, matching the section's ink text. The white originals and Downloads source are unchanged.
- Preserved heading wording, HTML accessible name, artwork geometry, responsive layout, trust icons and form labels. No all-fields-required introduction was reintroduced.
- Both navy SVGs parse successfully; their path data is identical to the corresponding white artwork. Git whitespace checks passed.

## Four-category product section — November 18, 2026

- Added an informational product section after the consultation area with the user-requested Shades, Blinds, Shutters and Exterior Shades labels. Labels and headings are literal HTML. Original SVG window illustrations use the Sunboy palette and do not represent specific manufacturer products or installations.
- Kept the section white, with four equal desktop columns and two columns at 860px and below. No new buttons, product-page placeholders, animation or unsupported product claims were introduced.
- Browser checks at 1280px confirmed four 262px columns at the same vertical position. At 320px, the grid has two 129px columns, all labels fit and document width equals viewport width. All four illustration assets load.
- SVG XML and Git whitespace checks passed. This was a scoped visual/responsive check; no screen-reader session or full-site accessibility audit was performed. Existing form and contact limitations remain unchanged.

## Real product photography — November 18, 2026

- Replaced all four product illustrations with real manufacturer product photographs from the matching Graber / Springs Window Fashions galleries. The category row now shows roller shades, horizontal blinds, plantation shutters and outdoor roller shades. Source URLs are recorded in product-photo-sources.json.
- Removed the rejected product SVG assets. Kept the approved four-column desktop layout, category labels, white section background and two-column mobile layout. Added short descriptive photo alternatives after visually inspecting each image.
- All four WebP files are 800×700 pixels and total about 305KB. Local browser checks at 1280px and 320px confirmed that they load, preserve matching crops and cause no horizontal overflow. Desktop remains four 262px columns; narrow mobile remains two 129px columns.
- Git whitespace checks passed. No product specifications, brand dealership claims, or Sunboy installation claims were added. Existing form and contact limitations are unchanged. Screen-reader testing and a full accessibility audit were not performed.

## Classic sitewide footer — November 18, 2026

- Replaced the minimal footer on the homepage and accessibility route with a shared classic navy design: white-styled supplied logo, Tampa Bay description, Products and Explore navigation columns, a consultation CTA and copyright/accessibility/back-to-top row. The original logo file is unchanged.
- Product links use real homepage category anchors. Consultation links use the existing section. Unverified phone/email/address/social and nonexistent policy pages were not added.
- Local browser checks at 1280px show four footer columns and no horizontal overflow. At 320px, navigation uses two 126px columns; logo width is 200px, CTA height is 48px with 13px text, and the page fits the viewport. Checked the footer on both page layouts.
- Keyboard checks: product and consultation links reached the intended targets; Accessibility opened its route; Tab showed a 3px blue focus ring on Back to top; Enter returned scroll position to zero. A product link from the accessibility footer returned to the correct homepage anchor. Current-page Accessibility state is present on that route.
- Git whitespace checks passed. No screen-reader session or full-site accessibility audit was performed. Existing form and contact limitations remain unchanged.

## Navy navigation theme — November 18, 2026

- Changed the navbar to footer navy #15384D, with the existing supplied logo styled white in CSS and white navigation labels. The original logo asset, navbar geometry and hero remain unchanged.
- Gave the flat navbar button a deeper brand blue #3278A5 with white text and no light overlay; calculated text contrast is approximately 4.8:1. Hover and active colors are darker. Other site buttons retain their existing styles.
- Matched the mobile menu panel and menu toggle to navy/white. At 1280px and 320px, rendered styles match the intended colors and there is no horizontal overflow. The accessibility-page header uses the same navy background with white Back to home text.
- At 320px, the menu opens, Enter activates Indoor, Escape dismisses its dialog and focus returns to the menu toggle. Checked the visible desktop and expanded mobile navigation.
- Git whitespace checks passed. Scope is the navigation theme; no full-site accessibility audit or screen-reader session was performed. Existing prototype form/contact limitations remain unchanged.

## White header and consistent baby-blue buttons — November 18, 2026

- Restored the white navbar, original blue logo styling and navy navigation text, including the mobile menu. Shared header CSS also applies to the accessibility page. Footer remains navy.
- Removed the navbar's darker button colors and the shared blue-button gradient overlays. Header, hero and footer blue CTA backgrounds now all use the existing --sky value #6DB2E4; hover adds a text underline without changing the fill.
- Browser checks at 1280px confirmed all three blue buttons render RGB 109,178,228 with no background image. Header is white, text is navy and logo has no filter. At 320px, the opened mobile menu is white/navy, the header button remains the same blue, and document width equals viewport width.
- Git whitespace checks passed. This restores the user's exact requested light-blue/white-text combination; the previously recorded approximately 2.3:1 white-text contrast limitation remains. No accessibility conformance claim, screen-reader session or full-site audit is implied. Existing form/contact limitations remain unchanged.

## Navy consultation submit button — November 18, 2026

- Changed Request Consultation beneath the form to the shared navy #15384D with white lettering, including hover and active fill. Other button colors are unchanged.
- Color-only change; sizing, layout, native validation and the existing disabled submission state remain. Git whitespace checks passed.

## Navbar consultation link — November 18, 2026

- Replaced See it in action with a native Book a Consultation anchor targeting the existing homepage consultation section. It no longer opens the film dialog. The link closes an expanded mobile menu before navigating.
- Adjusted navbar CTA spacing below 400px and logo/button widths below 340px so the longer label fits. At 320px, the menu's right edge is 292px inside a 304px header boundary; document width equals viewport width. Also checked 390px and 1280px without horizontal overflow.
- Keyboard Enter reached #consultation on desktop and mobile. The mobile menu was closed afterward and the film dialog remained closed. JavaScript syntax and Git whitespace checks passed.
- Updated the accessibility-page Escape instruction to refer to dialogs. Existing form submission remains disabled until a destination is configured; navigation to the form is functional. This was a scoped interaction/layout check, not a full accessibility audit or screen-reader session.

## Supplied SVG navbar wordmark — November 19, 2026

- Replaced the navbar PNG with the user-supplied sunboy-wordmark-blue.svg on the homepage and accessibility route. Copied the SVG byte-for-byte; Downloads original is unchanged. Footer logo and pendant are unchanged.
- Removed the PNG crop positioning from navbar images only. The SVG uses object-fit:contain inside the existing responsive logo box, preserving its proportions and all lettering.
- Browser checks at 1280px and 320px confirmed the asset loads and fits. Desktop logo box is 166×64px; narrow-mobile box is 104×54px. At 320px, the menu stays inside the header and document width equals viewport width. The accessibility-page navbar also loads the SVG without overflow.
- SVG XML/source integrity and Git whitespace checks passed. This was a scoped visual change; existing form and contact limitations remain unchanged.

## Contact page and consultation routing — November 19, 2026

- Added /contact/ using the existing white SVG-wordmark navbar, exact #6DB2E4 blue, navy/Manrope typography, four approved trust illustrations and classic footer. The static original sunseal appears on the white form card. The page has one literal HTML H1 and a short three-field form; no additional business claims or unverified contact details were introduced.
- Homepage navbar, hero and footer Book a Consultation links now lead to /contact/. Footer Contact links on all three routes also reach the new page. The contact-page navbar CTA moves directly to its form. Shared navigation safely omits homepage-only media/pendant behavior on the contact route.
- User explicitly said to configure delivery later. Both forms remain disabled and protected by the local submit guard. No lead was sent, no storage/integration was enabled, and no success state is simulated.
- In the in-app browser, reviewed the contact layout at 1280px, 390px and 320px. Document width equals viewport width on both mobile sizes. Assets load, the card fits, and the mobile header remains contained. Keyboard Enter opened Indoor, Escape closed it and returned focus; the navbar CTA closed the expanded menu and scrolled to the form. The homepage hero CTA opened the contact route. No browser errors were captured in these tested states.
- Empty required inputs report valueMissing, malformed email reports typeMismatch, and synthetic valid values clear native invalid states. Fields have explicit labels and name/email/tel autocomplete. Only Full name carries the approved visible star. Test values were cleared by reloading; no requests were submitted.
- Source checks passed for one H1 per page, unique IDs, local links/assets and every Book a Consultation destination across all three routes. JavaScript syntax and Git whitespace checks passed. Customer Copy Guard scanned all three public HTML files with zero blocking findings and zero review warnings, followed by contextual copy review.
- Scope is the new page and changed shared navigation/CTA behavior. No axe scan, actual zoom test or screen-reader session was performed. Existing light-blue/white navbar-button contrast and required-label preferences remain recorded in earlier QA; no conformance claim is made.

## Contact heading and card refinement — November 19, 2026

- Kept the contact H1 on two lines using two block spans and font sizing relative to the intro column. Removed the description's restrictive width and made its text size responsive so “Window treatments for your Tampa Bay home.” fits on one line. Text remains literal HTML and can wrap when enlarged; no clipping or forced nowrap was added.
- Moved the original Sunboy sunseal to the left of Book a Consultation and changed the contact-form button to Start a Consultation. Submission remains disabled per the user's earlier decision to connect delivery later.
- Browser measurements at 1280px, 398px, 320px and 860px confirmed two H1 lines, one description line, and no horizontal overflow. At 320px the description is 12px, the badge precedes the title, and the button has the requested label. Visually reviewed the desktop and 398px mobile layouts. Shared header, form semantics and navigation behavior were not altered.
- Git whitespace and public-copy checks passed. This was a scoped typography/layout change; no full accessibility audit or screen-reader session was performed.

## Category headings and direct product navigation — November 19, 2026

- Replaced the draft's generic product-anchor destinations with two category pages and eight individual product pages. Shades and Blinds are clickable category headings in the Indoor dropdown, with four shade and two blind links below them. Smart Dreams is a separate indoor link; Outdoor contains Exterior Retractable Screens. The single-panel dropdown has no fly-outs or extra View all products row.
- Shared partials and a dependency-free Python renderer keep the header and product links consistent across the homepage, contact page, category pages and product pages. The original homepage sections and three-field consultation form are preserved. The accessibility page retains its simple header and receives the updated shared footer/canonical.
- Added unique HTML titles/descriptions, self-canonicals, real HTML links, breadcrumb navigation and BreadcrumbList JSON-LD to the catalog pages. All 13 routes are in sitemap.xml, referenced by robots.txt. No fabricated offers, ratings, review schema, business locations or product-dealership claims are added.
- Manufacturer construction information was used only for general product descriptions; evidence URLs are kept in src/catalog.json. Five actual matching product photos were downloaded from primary manufacturer pages, visually inspected and given scene descriptions. Smart Dreams preserves the user's exact name, with no assumed manufacturer, features or photo; the optional clarification remains unanswered.
- In the in-app browser, all 13 routes loaded at 320px and 1280px with document width equal to viewport width, one H1, no broken eager images and no captured browser errors. Reviewed the category and product templates visually. At 320px, the Shades H1 is two lines (about 61.6px height / 30.8px line-height). Contact still has the approved heading and three fields.
- Desktop keyboard Enter on the Shades category heading reached /shades/; a category card opened Roller Shades; its consultation link reached /contact/. The mobile Blinds category heading reached /blinds/. Earlier draft tests verified Enter/Escape, focus return, one dropdown open at a time and outside-click dismissal; the same behavior remains in the published implementation. On the final mobile menu, Tab from Smart Dreams moved to Outdoor and closed Indoor; the full expanded menu fit a 636px panel at a 320×740 viewport.
- Source checks passed across all 13 pages for unique IDs, one H1, single canonical, local links/assets, product routes, breadcrumb JSON and complete sitemap coverage. JavaScript syntax, renderer AST parsing, Git whitespace, and Customer Copy Guard passed (13 HTML files, zero blocking findings or review warnings).
- This is scoped navigation/catalog QA. No axe scan, actual browser zoom or screen-reader session was performed. Existing user-requested light-blue/white CTA contrast and form-label/delivery limitations remain documented in earlier entries. No sitewide accessibility-conformance or ranking claim is made.

## Confirmed SmartDrape name — November 19, 2026

- User clarified that Smart Dreams meant SmartDrape. Updated the shared desktop/mobile navigation, product name, HTML title/description/H1, breadcrumb text/schema, canonical and sitemap to SmartDrape at /indoor/smartdrape/.
- Renamed the generated product route and added permanent 301 redirects for the previous /indoor/smart-dreams/ path, with and without its trailing slash. The old page is removed from the sitemap and generated HTML.
- Replaced the generic introductory product copy with a short description of fabric vanes, light control and passage through wide openings, checked against Norman's official SmartDrape page. No dealership, warranty, pricing or unsupported performance claims were added. Shared layout and deferred form delivery were preserved.
- Source checks passed across 13 routes for corrected navigation labels/URLs, local links, unique IDs and sitemap coverage. Customer Copy Guard returned zero blocking findings and review warnings; Git whitespace checks passed. This was a product-name/copy/routing correction, not a full accessibility or SEO audit.

- Deployment follow-up: the first live check returned 404 at the former URL rather than following the root configuration rule. Moved the two explicit permanent mappings into the published dist/_redirects file so they travel with the static site. Removed the duplicate root-config rules.

## Expansion architecture scaffold — November 19, 2026

- Inventoried 13 existing public routes and mapped 25 page records: 13 live, seven unpublished draft pages, four reserved pages, and one offering-confirmation route. Added five reusable reserved/conditional route patterns and eight unpublished page outlines. Drafts include section slots and inputs needed, without finished marketing content.
- Proposed one shared product library plus separate operating-market and city-coverage records. The only market record is Tampa Bay, with unconfirmed contacts, office model, city/county boundaries, Google Business Profile and consultation destination left empty. No additional location or franchise is represented as operating.
- Added a dependency-free architecture consistency check for unique routes/IDs, valid parent chains/market references, existing live files, matching sitemap coverage and exclusion of draft routes from dist/. The public renderer, website files, sitemap, navigation and form behavior were not changed.
- Research used current primary Google guidance for doorway pages, business-profile eligibility and noindex. The plan distinguishes crawl/index controls from access control and does not treat city pages as new staffed branches.
- Source validation passed for the architecture and all 13 live routes; Git whitespace checks passed. No browser/layout or accessibility retest was warranted because no published HTML/CSS/JavaScript changed. This is a proposed architecture, not a full SEO audit or a ranking forecast.

## Confirmed launch counties — November 19, 2026

- Owner confirmed Pinellas, Hillsborough, Manatee and Sarasota counties. Interpreted the supplied Hillsboro as Hillsborough County, Florida, checking the official county name at https://hcfl.gov/.
- Updated the initial market coverage record, Service Area outline, reserved Tampa Bay operation outline, architecture plan and route inventory. Added four unpublished county page outlines under /service-area/{county}-county-fl/. City/ZIP records remain empty; no additional branches or Google Business Profiles were created.
- Architecture now has 29 page records: 13 live, 11 draft, four reserved and one conditional, with 12 unpublished outlines. The four coverage pages remain outside the live build and sitemap. No published HTML/CSS/JavaScript or form behavior changed.

## Service Area and county layout previews — November 19, 2026

- Built /service-area/ and four county routes for Pinellas, Hillsborough, Manatee and Sarasota using the existing white navbar, Manrope type, exact logo blue, navy CTAs and classic footer. The overview has a branded county selector; county pages share a labeled local-photo placeholder. All five include shared product links, local-detail/review placeholders, three project-photo slots, breadcrumbs, consultation links and county navigation where appropriate.
- The owner explicitly requested placeholder layouts. Visible placeholder labels and static decorative skeleton lines are intentional; no completed local projects, customer testimonials, ratings, cities, phone numbers, offices or branches were invented. Original Sunboy artwork is decorative and unmodified.
- Service Area is now a real desktop/mobile navigation link and footer link. All navbar anchors close the mobile menu. The former Service Area modal entry was removed. Existing consultation submission remains disabled per the earlier delivery decision.
- Added preview as a publication state. The five public layouts have noindex, follow and self-canonicals, while remaining outside the XML sitemap. The other 13 public pages remain indexable. The sitemap renderer now parses robots metadata rather than automatically including every generated HTML file; robots.txt still allows crawling.
- Source checks passed across all 18 HTML routes for one H1, unique IDs, self-canonical presence, local links/assets and all five explicit noindex directives. Architecture validation passed for 29 records: 13 live/indexable, five noindex previews, six unbuilt drafts, four reserved and one conditional. JavaScript syntax and Git whitespace checks passed. Customer Copy Guard scanned 18 HTML files with zero blocking findings or review warnings; authorized visible placeholders were also reviewed manually.
- In the in-app browser, all five layouts loaded at 1280px and 320px without horizontal overflow or unloaded eager images. Reviewed the overview, county hero, and placeholder sections visually. Keyboard Enter opened a county from the selector and followed a sibling-county link, a product category and the contact page. The mobile Service Area link opened the overview with the menu closed. Contact still has name/email/phone and a disabled submit button. No browser errors were captured in the tested states.
- This is scoped layout/navigation QA. Actual browser zoom, axe and a screen-reader session were not tested. Existing user-approved navbar CTA contrast and deferred form-delivery limitations remain documented; no sitewide accessibility or SEO outcome is claimed.

## Drapes grouping and revised coverage — November 19, 2026

- Added a clickable Drapes category heading with SmartDrape below it on desktop and mobile. Created /drapes/ and linked it to the unchanged /indoor/smartdrape/ product URL. Catalog records can specify a stable URL independently of category membership. SmartDrape's parent breadcrumb and coverage-page product groups now use Drapes; no additional drape products or photos were invented.
- Removed Sarasota from current coverage records, active HTML, the route inventory and current drafts. Its former layout path redirects to /service-area/. Added /service-area/south-polk-county-fl/ as a noindex preview, clearly labeled South Polk County / South side only. Overview, page introduction and metadata say parts of southern Polk County, avoiding a full-county service claim. Towns and ZIP codes remain unconfirmed.
- Current architecture: 30 records, 14 indexable pages, five noindex previews, six unbuilt drafts, four reserved and one conditional. Validated that public county scopes agree with the market's confirmed full/partial coverage records. Source checks passed across 19 HTML routes for local links/assets, one H1, unique IDs, no active Sarasota text, and explicit partial Polk coverage. Customer Copy Guard returned no blocking findings or review warnings; Git whitespace checks passed.
- In the in-app browser, checked the Indoor grouping at 1280px and 320px. Drapes opened the category hub and SmartDrape retained its old URL with a Drapes breadcrumb. The single category card stays one 276px column at 320px, with no horizontal overflow. The Service Area selector displayed the three full counties and South Polk / South side only. Keyboard Enter reached the South Polk page, whose introduction and metadata retained the partial qualifier. No browser errors were captured.
- Scope is category grouping and service-area corrections. No full accessibility audit, screen-reader session or actual zoom test was performed. Existing preview noindex and deferred consultation delivery behavior are preserved.

## Exterior Shades naming — November 19, 2026

- Renamed the outdoor product to Exterior Shades in desktop/mobile navigation, coverage-page product links, product heading, breadcrumbs and metadata. Updated its short description and image alternative text to use the same name. The existing published URL and photo asset remain stable.
- Regenerated all shared navigation and product/coverage HTML. Architecture validation and Git whitespace checks passed. A source-text check across all 19 public HTML pages confirmed no remaining customer-facing retractable wording, and verified both menu labels and the product H1. No layout, animation, form-delivery or indexability behavior changed.

## Roman Shades addition — November 19, 2026

- Added Roman Shades under Shades on desktop/mobile, to the Shades comparison page and to coverage-page product links. The menu opens /shades/roman-shades/, using the shared product template, real manufacturer photography and short introductory copy. Basic fabric/fold terminology was checked against Graber's official Roman Shades page; no manufacturer partnership, product performance or Sunboy project claim was added. The photo and source are recorded in product-page-photo-sources.json.
- The five-product Shades grid uses three desktop columns and the existing two-column mobile layout. Current inventory is 20 HTML routes: 15 indexable and five noindex coverage previews. Architecture validation, customer-copy check (zero blockers or review warnings across 20 pages) and Git whitespace checks passed.
- In-app browser checks at 1280px and 320px confirmed the menu destination, Roman Shades H1, loaded hero photo, no horizontal overflow, and mobile-menu closure after following the link. No browser errors were captured. Form delivery and coverage-preview indexability remain unchanged.
