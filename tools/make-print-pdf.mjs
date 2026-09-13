/* Builds the two print-and-play PDFs: one of card fronts, one of backs.
 *
 * The page's own print sheet relies on the browser fragmenting a single long
 * grid across pages. That works, but it wastes paper and it is not duplex-safe:
 * a landscape card spans two of the three 2.5in columns and leaves the third
 * empty, and the number of cards on a page is whatever happens to fit. Here the
 * cards are instead chunked into explicit pages of nine, each its own 3x3 grid
 * with a hard break after it, so every sheet holds exactly nine whole cards and
 * back page N lines up with front page N.
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
const PER_PAGE = 9;

const SHEET_CSS = `
  @page{size:letter portrait;margin:.25in}
  body{background:#fff}
  header.top,.bar,.empty,.noprint{display:none!important}
  #grid{display:block!important;padding:0!important;gap:0!important}
  .print-page{display:grid;grid-template-columns:repeat(3,2.5in);
    grid-auto-rows:3.5in;justify-content:center;align-content:start;
    break-after:page;page-break-after:always}
  .print-page:last-child{break-after:auto;page-break-after:auto}
  .slot{position:relative;display:grid;place-items:center;width:2.5in;height:3.5in;overflow:hidden}
  .slot .card{margin:0}
  /* A turned card: 3.5x2.5 rotated a quarter turn fills a 2.5x3.5 slot. It is
     placed absolutely rather than left to the grid -- a grid item wider than its
     track does not centre where you would expect, and the card came out far
     enough right that overflow:hidden sheared the whole banner off, taking the
     hero's name and type line with it. */
  .slot .card.wide{position:absolute;left:50%;top:50%;
    transform:translate(-50%,-50%) rotate(90deg)}
  .backimg{width:2.5in;height:3.5in;object-fit:cover;display:block;
    outline:.5pt dashed rgba(0,0,0,.35);outline-offset:-.5pt}
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
await p.pdf({ path:`${OUT}/might-and-magic-fronts.pdf`, format:'Letter', printBackground:true });
console.log(`fronts: ${info.total} cards over ${info.pages} pages (last page ${info.lastPage})`);

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
