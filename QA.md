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
