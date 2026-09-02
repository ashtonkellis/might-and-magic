/* Rebuild the art manifests from what is actually on disk.
 *
 * A static host has no directory listing, so the page cannot discover art by
 * looking -- it has to be told. These two manifests are that telling:
 *
 *   art/index.json         card art, named by card id (SOR-059.webp)
 *   art/heroes/index.json  hero art, named <hero>-hero-front|back.webp
 *
 * Hand-maintaining them means the page silently misses art that was pushed
 * without a manifest edit, so run this after adding images:  node tools/build-art-index.mjs
 * --check reports drift without writing, for use before a release.
 */
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = dirname(dirname(fileURLToPath(import.meta.url)));
const IMAGE = /\.(webp|png|jpe?g|avif)$/i;
const check = process.argv.includes('--check');

// Only files with real bytes: a 0-byte image is a failed upload, and listing it
// would render a broken <img> instead of the placeholder the page falls back to.
const scan = dir => readdirSync(join(ROOT, dir), { withFileTypes: true })
  .filter(e => e.isFile() && IMAGE.test(e.name))
  .filter(e => readFileSync(join(ROOT, dir, e.name)).length > 0)
  .map(e => e.name).sort();

let drift = 0;
for (const dir of ['art', 'art/heroes']) {
  const path = join(ROOT, dir, 'index.json');
  const found = scan(dir);
  let had = [];
  try { had = JSON.parse(readFileSync(path, 'utf8')); } catch {}
  const added = found.filter(f => !had.includes(f));
  const gone = had.filter(f => !found.includes(f));
  if (added.length || gone.length) {
    drift++;
    console.log(`${dir}/index.json: ${found.length} images` +
      (added.length ? `, +${added.length} (${added.slice(0, 4).join(', ')}${added.length > 4 ? ', …' : ''})` : '') +
      (gone.length ? `, -${gone.length} (${gone.slice(0, 4).join(', ')}${gone.length > 4 ? ', …' : ''})` : ''));
    if (!check) writeFileSync(path, JSON.stringify(found, null, 2) + '\n');
  } else {
    console.log(`${dir}/index.json: ${found.length} images, up to date`);
  }
}
if (check && drift) { console.error('manifests are stale — run node tools/build-art-index.mjs'); process.exit(1); }
