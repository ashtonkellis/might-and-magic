#!/usr/bin/env node
// Bump the deploy version in the two places that must agree: the cache name in
// sw.js and the badge in index.html. Run before every push to the public page.
//
//   node bump-version.mjs          -> next version
//   node bump-version.mjs --check  -> verify the two agree, change nothing
import { readFileSync, writeFileSync } from 'node:fs';

const read = f => readFileSync(f, 'utf8');
const swV   = f => Number(/^const VERSION = (\d+);/m.exec(f)?.[1]);
const htmlV = f => Number(/id="version">V(\d+)</.exec(f)?.[1]);

let sw = read('sw.js'), html = read('index.html');
const a = swV(sw), b = htmlV(html);
if (!Number.isInteger(a) || !Number.isInteger(b)) {
  console.error('Could not read the version from sw.js and/or index.html.'); process.exit(1);
}
if (process.argv.includes('--check')) {
  if (a !== b) { console.error(`MISMATCH: sw.js is v${a}, index.html shows V${b}`); process.exit(1); }
  console.log(`v${a} — sw.js and index.html agree`); process.exit(0);
}
if (a !== b) { console.error(`Refusing to bump: sw.js is v${a} but index.html shows V${b}.`); process.exit(1); }

const next = a + 1;
writeFileSync('sw.js', sw.replace(/^const VERSION = \d+;/m, `const VERSION = ${next};`));
writeFileSync('index.html', html.replace(/id="version">V\d+</, `id="version">V${next}<`));
console.log(String(next));
