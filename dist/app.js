const background = document.querySelector('#hero-video');
const motionButton = document.querySelector('#motion-control');
const motionLabel = document.querySelector('#motion-label');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const mobile = matchMedia('(max-width: 700px)');
const dialog = document.querySelector('#film-dialog');
const film = document.querySelector('#full-film');
let wantsPlayback = !reducedMotion.matches && !navigator.connection?.saveData;
let heroVisible = true;
let dialogTrigger;

function updateMotionLabel() {
  const playing = !background.paused;
  motionButton.setAttribute('aria-pressed', String(playing));
  motionButton.setAttribute('aria-label', playing ? 'Pause background video' : 'Play background video');
  motionLabel.textContent = playing ? 'Pause video' : 'Play video';
}
function ensureSource() {
  const path = mobile.matches ? '/assets/hero-mobile.mp4' : '/assets/hero-desktop.mp4';
  if (background.getAttribute('src') !== path) {
    background.src = path;
    background.load();
  }
}
function syncPlayback() {
  if (wantsPlayback && heroVisible && !document.hidden && !dialog.open) {
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
    wantsPlayback = background.paused;
    syncPlayback();
  });
  reducedMotion.addEventListener('change', () => {
    wantsPlayback = !reducedMotion.matches && !navigator.connection?.saveData;
    syncPlayback();
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
