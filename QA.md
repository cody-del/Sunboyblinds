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
