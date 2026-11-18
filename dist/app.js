const background = document.querySelector('#hero-video');
const motionButton = document.querySelector('#motion-control');
const motionLabel = document.querySelector('#motion-label');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const mobile = matchMedia('(max-width: 700px)');
const dialog = document.querySelector('#film-dialog');
const film = document.querySelector('#full-film');
const infoDialog = document.querySelector('#info-dialog');
const menuToggle = document.querySelector('#menu-toggle');
const mobileNav = document.querySelector('#mobile-nav');
let wantsMotion = !reducedMotion.matches && !navigator.connection?.saveData;
let heroVisible = true;
let dialogTrigger;

function updateMotionLabel() {
  motionButton.setAttribute('aria-pressed', String(wantsMotion));
  motionButton.setAttribute('aria-label', wantsMotion ? 'Pause motion' : 'Play motion');
  motionLabel.textContent = wantsMotion ? 'Pause motion' : 'Play motion';
}
function ensureSource() {
  const path = mobile.matches ? '/assets/hero-mobile.mp4' : '/assets/hero-desktop.mp4';
  if (background.getAttribute('src') !== path) {
    background.src = path;
    background.load();
  }
}
function syncPlayback() {
  if (wantsMotion && heroVisible && !document.hidden && !dialog.open && !infoDialog.open) {
    ensureSource();
    background.play().catch(updateMotionLabel);
  } else background.pause();
  updateMotionLabel();
}
if (background) {
  background.addEventListener('play', updateMotionLabel);
  background.addEventListener('pause', updateMotionLabel);
  background.addEventListener('error', updateMotionLabel);
  motionButton.addEventListener('click', () => {
    wantsMotion = !wantsMotion;
    syncPlayback();
    syncSunMotion();
  });
  reducedMotion.addEventListener('change', () => {
    wantsMotion = !reducedMotion.matches && !navigator.connection?.saveData;
    syncPlayback();
    syncSunMotion();
  });
  mobile.addEventListener('change', () => {
    if (background.hasAttribute('src')) ensureSource();
    syncPlayback();
  });
  document.addEventListener('visibilitychange', syncPlayback);
  new IntersectionObserver(([entry]) => {heroVisible = entry.isIntersecting; syncPlayback();}, {threshold:0.05}).observe(background);
  syncPlayback();
}
document.querySelectorAll('[data-open-film]').forEach(button => button.addEventListener('click', () => {
  closeMenu();
  dialogTrigger = button;
  if (!film.hasAttribute('src')) film.src = '/assets/hero-desktop.mp4';
  dialog.showModal();
  background.pause();
  film.play().catch(() => {});
}));
document.querySelector('#close-film')?.addEventListener('click', () => dialog.close());
dialog?.addEventListener('click', event => {
  if (event.target === dialog) {
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  }
});
dialog?.addEventListener('close', () => {
  film.pause();
  syncPlayback();
  dialogTrigger?.focus();
});

function closeMenu() {
  mobileNav.hidden = true;
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Open navigation menu');
}
document.querySelector('#nav-consultation-button')?.addEventListener('click', closeMenu);
menuToggle.addEventListener('click', () => {
  const opening = mobileNav.hidden;
  mobileNav.hidden = !opening;
  menuToggle.setAttribute('aria-expanded', String(opening));
  menuToggle.setAttribute('aria-label', opening ? 'Close navigation menu' : 'Open navigation menu');
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !mobileNav.hidden) {
    closeMenu();
    menuToggle.focus();
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.navbar')) closeMenu();
});
const navigationContent = {
  indoor: {title:'Indoor', html:'<p>Window treatments for your home.</p>'},
  outdoor: {title:'Outdoor', html:'<p>Shade for your outdoor space.</p>'},
  services: {title:'Services', html:'<p>Indoor window treatments and outdoor shade in the Tampa Bay area.</p>'},
  about: {title:'Sunboy Blinds', html:'<p>Professional window treatment experts for the Tampa Bay Area.</p>'},
  'service-area': {title:'Service Area', html:'<p>Serving the Tampa Bay Area.</p>'}
};
let infoTrigger;
document.querySelectorAll('[data-open-info]').forEach(button => button.addEventListener('click', () => {
  const content = navigationContent[button.dataset.openInfo];
  infoTrigger = mobileNav.contains(button) ? menuToggle : button;
  closeMenu();
  document.querySelector('#info-title').textContent = content.title;
  document.querySelector('#info-content').innerHTML = content.html;
  infoDialog.showModal();
  background.pause();
}));
document.querySelector('#close-info').addEventListener('click', () => infoDialog.close());
infoDialog.addEventListener('close', () => {
  syncPlayback();
  infoTrigger?.focus();
});

// Until the consultation destination is supplied, keep the visual form local.
// The disabled submit control and submit guard prevent sending personal data.
document.querySelector('#consultation-form').addEventListener('submit', event => {
  event.preventDefault();
});

const sunPendant = document.querySelector('.section-pendant');
let sunIsVisible = false;

function syncSunMotion() {
  sunPendant.dataset.sunPlaying = String(wantsMotion && sunIsVisible && !document.hidden);
}
document.addEventListener('visibilitychange', syncSunMotion);
new IntersectionObserver(([entry]) => {
  sunIsVisible = entry.isIntersecting;
  syncSunMotion();
}, {threshold:0.1}).observe(sunPendant);
syncSunMotion();
