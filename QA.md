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
