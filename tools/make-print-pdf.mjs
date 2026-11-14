/* Builds the two print-and-play PDFs: one of card fronts, one of backs.
 *
 * The sheet layout -- pages of eight, one slot per card, the bleed ring and the
 * quarter turn on landscape faces -- is not here. It lives in index.html's
 * paginate(), which the page runs as it renders, so the site's own Print button
 * and this builder put out the same sheet instead of two layouts that drift.
 * What is left here is the work only a build step can do: re-encoding the art
 * so the fronts are not 126MB, splitting them into two attachable halves, and
 * building the matching sheet of backs, which the site has no reason to show.
 *
 *   node tools/make-print-pdf.mjs [outDir]     (needs the site on :8099)
 */
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { basename } from 'node:path';

const OUT = process.argv[2] || 'print';
const SITE = process.env.SITE || 'http://127.0.0.1:8099/index.html';
const PER_PAGE = 8;

/* The site has no card backs, so this is the one piece of sheet CSS that does
   not belong in index.html. Everything else comes from the page. */
const SHEET_CSS = `.backimg{width:2.5in;height:3.5in;object-fit:cover;display:block}`;

const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:1500,height:1100} });
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto(SITE, { waitUntil:'networkidle' });

/* The page paginates itself as it renders, so there is nothing to restructure
   here -- only to read back how many sheets it made, for the split and the
   matching backs. */
const info = await p.evaluate(() => {
  const pages = document.querySelectorAll('#grid .print-page');
  const total = document.querySelectorAll('#grid .slot').length;
  const last = pages[pages.length - 1];
  return { total, pages: pages.length,
           lastPage: last ? last.querySelectorAll('.slot').length : 0 };
});
if (!info.pages) throw new Error('the page rendered no print sheets');

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
