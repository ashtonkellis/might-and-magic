/* Builds the two print-and-play PDFs: one of card fronts, one of backs.
 *
 * The page's own print sheet relies on the browser fragmenting a single long
 * grid across pages. That works, but it wastes paper and it is not duplex-safe:
 * a landscape card spans two of the three 2.5in columns and leaves the third
 * empty, and the number of cards on a page is whatever happens to fit. Here the
 * cards are instead chunked into explicit pages of eight, each its own 4x2 grid
 * with a hard break after it, so every sheet holds exactly eight whole cards and
 * back page N lines up with front page N. Eight to a landscape sheet rather than
 * nine to a portrait one because each card carries a ring of bleed that three
 * rows of 3.5in no longer leave room for.
 *
 * Landscape faces (resources, hero fronts) are rotated a quarter turn into a
 * portrait slot rather than given a wider one: the physical card is 2.5x3.5 and
 * those faces are landscape because the card is turned to read them.
 *
 *   node tools/make-print-pdf.mjs [outDir]     (needs the site on :8099)
 */
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { basename } from 'node:path';

const OUT = process.argv[2] || 'print';
const SITE = process.env.SITE || 'http://127.0.0.1:8099/index.html';
const PER_PAGE = 8;

const BLEED = '2mm';                      // colour past the cut line, per side
const SHEET_CSS = `
  @page{size:letter landscape;margin:.1in}
  body{background:#fff}
  header.top,.bar,.empty,.noprint{display:none!important}
  #grid{display:block!important;padding:0!important;gap:0!important}
  /* Eight to a landscape sheet rather than nine to a portrait one: a bleed ring
     round every card does not fit three rows of 3.5in down a letter page. */
  .print-page{display:grid;grid-template-columns:repeat(4,calc(2.5in + 2*${BLEED}));
    grid-auto-rows:calc(3.5in + 2*${BLEED});justify-content:center;align-content:start;
    break-after:page;page-break-after:always}
  .print-page:last-child{break-after:auto;page-break-after:auto}
  /* The ring carries the card's own two frame colours, so a punch that lands a
     millimetre or two out still comes up coloured to the edge instead of white. */
  .slot{display:block;width:calc(2.5in + 2*${BLEED});height:calc(3.5in + 2*${BLEED});
    padding:${BLEED};overflow:hidden;
    background-size:cover;background-position:center}
  .slot .card{margin:0}
  /* A turned card, rotated in flow. Taking it out of flow to centre it is the
     obvious fix and it renders on screen, but an absolutely positioned element
     does not survive Chromium's pagination: every hero front silently vanished
     from the PDF while the portrait cards beside it printed fine. Rotating about
     the top-left corner and translating back down needs no centring at all. */
  .slot .card.wide{transform-origin:0 0;transform:translate(0,3.5in) rotate(-90deg)}
  .backimg{width:2.5in;height:3.5in;object-fit:cover;display:block}
`;

const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1500,height:1100} });
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto(SITE, { waitUntil:'networkidle' });

const info = await p.evaluate(PER_PAGE => {
  const cards = [...document.querySelectorAll('#grid .card')];
  const total = cards.length;
  const pages = Math.ceil(total / PER_PAGE);
  const grid = document.getElementById('grid');
  const frag = document.createDocumentFragment();
  for (let i = 0; i < pages; i++) {
    const page = document.createElement('section');
    page.className = 'print-page';
    for (const c of cards.slice(i*PER_PAGE, (i+1)*PER_PAGE)) {
      const slot = document.createElement('div');
      slot.className = 'slot';
      /* Every card frames itself with the same gradient -- the --split angle and
         the two --split-a/--split-b stops -- so the ring is that same gradient
         again on a slightly larger box, and the colour carries across the cut
         line instead of meeting it. Three things have to be read rather than
         assumed:

         The colours. A hero carries --c1/--c2 inline, a class card an inline
         background, a resource a border colour. Reading the computed background
         covers none of them: on a hero it resolves to the dark ground the art
         sits on, which is why every ring came out black. Copying the class
         card's inline gradient string is no better -- it is written in terms of
         var(--split), which is defined on .card and so resolves to nothing out
         here on the slot, leaving 252 class cards with a silently white ring.

         The stops. 90deg/50% is right for a portrait card and wrong for a
         landscape one, which splits on a diagonal. And a percentage cannot just
         be carried over: it measures along the gradient line, the slot's line is
         longer than the card's, so the same 48.5% puts the colour change about
         2mm off where the card puts it. Anchoring the stops to the middle of the
         line and offsetting by a length off the CARD's line makes the two meet
         exactly. CSS gradient-line length for angle t on a WxH box is
         |W sin t| + |H cos t|, and rotation preserves it, so a turned card can
         be measured on the box it actually had.

         The turn. A card rotated into its slot takes its frame round with it, so
         the ring has to turn by the same quarter to stay aligned with it. */
      const cs = getComputedStyle(c);
      const wide = c.classList.contains('wide');
      let angle = parseFloat(cs.getPropertyValue('--split')) || 90;
      const pct = v => (parseFloat(v) || 0) / 100;
      const pa = pct(cs.getPropertyValue('--split-a')) || .485;
      const pb = pct(cs.getPropertyValue('--split-b')) || .515;
      let c1 = c.style.getPropertyValue('--c1').trim();
      let c2 = c.style.getPropertyValue('--c2').trim();
      if (!c1) {                              // class card, token, or resource
        const hex = (c.getAttribute('style') || '').match(/#[0-9a-fA-F]{6}\b/g) || [];
        c1 = hex[0]; c2 = hex[1];
      }
      if (!c1) c1 = cs.borderTopColor;
      if (!c1) c1 = '#2A2536';
      if (!c2) c2 = c1;
      const t = angle * Math.PI / 180;        // on the card's own, unturned box
      const [cw, ch] = wide ? [3.5, 2.5] : [2.5, 3.5];
      const line = Math.abs(cw * Math.sin(t)) + Math.abs(ch * Math.cos(t));
      const at = p => `calc(50% + ${((p - .5) * line).toFixed(4)}in)`;
      if (wide) angle -= 90;
      slot.style.background =
        `linear-gradient(${angle}deg, ${c1} 0 ${at(pa)}, ${c2} ${at(pb)} 100%)`;
      slot.appendChild(c);                    // move, keeping its fitted --fit
      page.appendChild(slot);
    }
    frag.appendChild(page);
  }
  grid.replaceChildren(frag);
  return { total, pages, lastPage: total - (pages-1)*PER_PAGE };
}, PER_PAGE);

await p.addStyleTag({ content: SHEET_CSS });

/* Re-encode the art as JPEG at print resolution and serve it from disk.
   Chromium cannot pass a webp through into a PDF -- it decodes and re-embeds it
   Flate-compressed, which took the fronts to 126MB from 29MB of source art.
   Re-encoding to JPEG lets it embed the bytes directly. The files go to disk
   rather than into data: URLs, which is what the obvious version does and which
   wedges the page: 321 base64 strings in the DOM at once never finished. */
const CACHE = `${OUT}/.art-cache`;
mkdirSync(CACHE, {recursive:true});
/* Every card's art has to be decoded before any of it can be re-encoded, and
   most of it is lazy: sampling straight away finds only what happens to be on
   screen, which silently left two thirds of the art at full weight. */
await p.evaluate(async () => {
  for (const im of document.images) im.loading = 'eager';
  await Promise.all([...document.images].map(im => im.complete
    ? Promise.resolve()
    : new Promise(r => { im.onload = im.onerror = r; })));
});
await p.waitForTimeout(1500);
const urls = await p.evaluate(() =>
  [...new Set([...document.images].filter(i => i.naturalWidth).map(i => i.currentSrc || i.src))]);
let written = 0;
for (let i = 0; i < urls.length; i += 20) {
  const batch = urls.slice(i, i + 20);
  const out = await p.evaluate(async ({batch, CAP, Q}) => batch.map(u => {
    const im = [...document.images].find(x => (x.currentSrc || x.src) === u);
    const sc = Math.min(1, CAP / Math.max(im.naturalWidth, im.naturalHeight));
    const cv = document.createElement('canvas');
    cv.width = Math.round(im.naturalWidth * sc);
    cv.height = Math.round(im.naturalHeight * sc);
    cv.getContext('2d').drawImage(im, 0, 0, cv.width, cv.height);
    return cv.toDataURL('image/jpeg', Q).split(',')[1];
  }), {batch, CAP:800, Q:0.75});
  batch.forEach((u, k) => {
    writeFileSync(`${CACHE}/${basename(new URL(u).pathname)}.jpg`, Buffer.from(out[k], 'base64'));
    written++;
  });
}
await p.evaluate(CACHE => {
  for (const im of document.images) {
    const u = im.currentSrc || im.src;
    if (!u) continue;
    im.src = `${CACHE}/${u.split('/').pop()}.jpg`;
  }
}, `${OUT}/.art-cache`);
await p.waitForTimeout(1500);
console.log(`art re-encoded: ${written} images to ${CACHE}`);

await p.emulateMedia({ media:'print' });
await p.waitForTimeout(2500);
/* Split in half. The whole front sheet is around 50MB, which is past what
   most places will accept as one attachment; two halves at full quality beat
   one file with the art crushed to fit. */
const half = Math.ceil(info.pages / 2);
for (const [n, range] of [[1, `1-${half}`], [2, `${half+1}-${info.pages}`]]) {
  await p.pdf({ path:`${OUT}/might-and-magic-fronts-${n}.pdf`, format:'Letter',
                printBackground:true, pageRanges:range });
}
console.log(`fronts: ${info.total} cards over ${info.pages} pages `
          + `(last page ${info.lastPage}), split 1-${half} and ${half+1}-${info.pages}`);

// Backs: one shared image, same page count, same number of slots per page, so a
// duplex run lands a back behind every front. A uniform back needs no mirroring.
const BACK = 'art/might-and-magic-card-back.webp';
await p.evaluate(({pages, total, PER_PAGE, BACK}) => {
  const grid = document.getElementById('grid');
  const frag = document.createDocumentFragment();
  for (let i = 0; i < pages; i++) {
    const n = Math.min(PER_PAGE, total - i*PER_PAGE);
    const page = document.createElement('section');
    page.className = 'print-page';
    for (let k = 0; k < n; k++) {
      const slot = document.createElement('div');
      slot.className = 'slot';
      const im = document.createElement('img');
      im.className = 'backimg'; im.src = BACK;
      slot.appendChild(im); page.appendChild(slot);
    }
    frag.appendChild(page);
  }
  grid.replaceChildren(frag);
}, {pages:info.pages, total:info.total, PER_PAGE, BACK});
await p.waitForTimeout(2000);
await p.pdf({ path:`${OUT}/might-and-magic-backs.pdf`, format:'Letter', printBackground:true });
console.log(`backs : ${info.total} backs over ${info.pages} pages`);
rmSync(`${OUT}/.art-cache`, {recursive:true, force:true});
console.log('page errors:', errs.length ? errs : 'none');
await b.close();
