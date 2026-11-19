# Sunboy Blinds website

Buildless HTML, CSS and JavaScript. Serve `dist/` with a static HTTP server.

The navbar uses the user-supplied sunboy-wordmark-blue.svg, displayed in a contained box without cropping or stretching. The footer retains the original user-supplied PNG, with its surrounding white space cropped in CSS and its white styling preserved. Original supplied files are unchanged.

The desktop/mobile videos and posters were copied from the retired John Crawford hero in `owner-copy-work/dist/assets`. That project was only read. Source edit: `20261017_120924.mp4` and `20261017_120958.mp4`, kitchen/living/dining montage. The November 4 replacement video was not used.

The site includes a homepage, a dedicated /contact/ consultation page, and an accessibility page. The navigation has Indoor, Outdoor, Services, About and Service Area detail panels, plus a flat logo-blue Book a Consultation link. Homepage and footer consultation links lead to /contact/; on the contact page, the navbar link moves to the form. The consultation form is a local front-end preview; no submission destination is configured. The centered, two-line H1 and Tampa Bay service area are supplied by the user. The accessibility route provides practical controls information. Public assistance contact details have not been supplied.

The Book a Consultation CTAs link to the contact page. Call Sunboy remains disabled until a phone number is supplied. The requested five-star Google and Facebook badges are design treatments; no profile URLs, verified ratings or review counts are supplied. The badges are not linked. The site is published on Netlify from GitHub main.

Page typography uses the self-hosted Manrope variable font, sourced from Google Fonts, for the hero, navigation, trust section, form and interface copy. Its OFL license is included in dist/assets/fonts/. The hero uses weight 800, the consultation heading uses 700, and trust points, labels and navigation use 600. The navbar collapses at 960px. The hero headline remains centered on two lines.

The section pendant is the supplied sunboy-badge-blue SVG with a white circle inserted under the existing blue path, inside the same viewBox. The circle is slightly inset and scales with the entire SVG. No independent CSS white background is used. The original Downloads file is unchanged.

Trust points: Professional installation, Quick turnaround times, and No subcontractors were supplied by the user. The tentative satisfaction guarantee was rendered as “Your satisfaction comes first”; no warranty terms or turnaround duration were invented.

The homepage and contact-page forms each have exactly three labeled fields: full name, email and phone, with autocomplete attributes and native validation. Its button reads “Request Consultation.” The submit control is disabled and a submit handler prevents navigation until a real destination is supplied. The user explicitly deferred form delivery on November 19, 2026. Neither form stores, sends, or claims to submit requests.

The entire consultation section and form panel now use the exact logo blue (#6DB2E4), with dark ink labels and white fields. Its submit button is navy #15384D with white text.

The pendant now uses the supplied sunboy-sunseal-blue SVG. The ray and face artwork are separated into matched 700×700 SVG layers. Rays rotate around the shared viewBox center on a 90-second loop; the face and blue circular frame never transform. The white circle has radius 247, inside the fixed blue frame outer radius 252. One subtle keyboard-operable “Pause motion” control in the hero stops/resumes both the background video and rays. There is no separate control beneath the sun. Reduced-motion preferences start the sun paused; offscreen/hidden pages also pause it. The SVG in outputs is a static, white-backed editable version with named ray/face groups.

The shared section heading is “Schedule a free in-home consultation.” as supplied by the user on November 18, 2026. A single centered heading replaces the competing left/form headings. The section uses equal-width, vertically balanced columns in a 1000px content area with an 88px desktop gap. Four custom SVG icons identify the trust points: a sunlit blind, a clock in the supplied sunburst, the supplied Sunboy mascot, and a smiling sunburst. Navy outlines and white accents match the section typography and pendant; the icons are 48px on desktop and 40px on mobile, without cards or list dividers. Dark ink is #15384D; the Sunboy blue is unchanged.

The current trust illustrations are white SVG paths with transparent cutouts, converted from the approved illustrated drill/clock concepts, revised construction helmet, and plain geometric sun. They map respectively to Professional installation, Quick turnaround times, No subcontractors, and Your satisfaction comes first. Each SVG has only a white even-odd path, with no painted blue/black background and no embedded raster image. Icon boxes are 56px on desktop and 44px on mobile.

The form now marks Full name with a visible asterisk, replacing the all-fields-required introduction; Email and Phone have plain labels. Native required attributes and validation remain; decorative asterisks are hidden from assistive technology to avoid duplicate required announcements.

The section heading displays the supplied lettering in navy #15384D via sunboy-cta-schedule-navy.svg. A mobile derivative uses the same paths on two centered lines; the original file remains unchanged. The H2 retains the exact heading words in a visually hidden HTML span and the artwork is decorative.

The homepage product section contains Shades, Blinds, Shutters and Exterior Shades in a four-column desktop row and a two-column mobile grid. Real product photographs from the Graber manufacturer galleries replace the original SVG illustrations, with category names in HTML. Photo sources are recorded in product-photo-sources.json; the photos are category examples, not Sunboy installation claims. The section is informational; no product destinations are implied. Netlify publishes dist automatically from GitHub main.

A shared classic navy footer appears on the homepage, contact page and accessibility page. It includes the supplied logo rendered white with CSS, product anchors, existing-page navigation, a consultation CTA and a copyright/accessibility row. Phone, email, street address, social profiles and policy links are omitted because no verified destinations have been supplied.

The navbar is white with the original blue logo and navy text, including the mobile menu and accessibility-page header. The blue buttons in the navbar, hero and footer all use the same flat logo blue #6DB2E4 through the shared --sky variable, including hover/active states. The form submit button uses navy #15384D with white text.

The contact page uses the same exact logo blue, navy, white navbar, Manrope typography, illustrated trust icons and classic footer. A navy HTML H1 and concise trust list sit beside a white form card. The original Sunboy sunseal is static within the card, where its blue artwork remains visible on white. The responsive layout becomes one column on mobile. Only Full name has a visible asterisk, matching the approved homepage labels. All heading and form text is HTML. No unverified phone, email, address, response time or appointment confirmation is added. Shared navigation JavaScript safely skips homepage-only video and pendant behavior on /contact/.
