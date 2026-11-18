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
