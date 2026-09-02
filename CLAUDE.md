# Working in this repo

## Release workflow — follow this on every push to the public page

The site is a PWA. A service worker caches it, so a viewer can be looking at an
older release than the one just pushed. The version badge at the top of the page
is how that gets caught: it changes on every deploy, so if the user does not see
the number they were told to expect, the cache is stale rather than the work
being wrong.

**Before any push that changes what the site serves:**

0. If you added or removed images under `art/`, `node tools/build-art-index.mjs`
   — the page finds art through `art/index.json` and `art/heroes/index.json`,
   never by looking in the directory, so art pushed without a manifest rebuild
   is invisible on the site. `--check` reports drift without writing.
1. `node bump-version.mjs` — increments the version in the two places that must
   agree: `VERSION` in `sw.js` (which names the cache) and the badge in
   `index.html`. It prints the new number and refuses to run if the two have
   drifted apart.
2. Commit and push as usual.
3. **Tell the user which version they should see**, e.g. "this is V4 — the badge
   at the top of the page should read V4." Do this every single time, in the
   reply that reports the push.

`node bump-version.mjs --check` verifies the two agree without changing them.

Skip the bump only for changes that cannot alter what a visitor sees — editing
`CLAUDE.md`, say. When in doubt, bump; a skipped bump is a silently stale page,
while an extra bump costs nothing but a cache refresh.

## If the user reports seeing the wrong version

The service worker is network-first for everything except art, and calls
`skipWaiting()` and `clients.claim()`, so a new release should take over on the
next load without closing tabs. If a stale version persists, suspect in order:
GitHub Pages not yet finished deploying, then a bump that was skipped, then the
browser holding `sw.js` itself — the registration already passes
`updateViaCache: 'none'` to prevent that last one.

## Repo shape

Four things, no build step, served from the repository root by GitHub Pages:

- `index.html` — the card browser and print sheet, and the site's home page
- `card-list.json` — 755 cards, 252 of them assigned to a class
- `class-bible.html` — the twenty-one classes, their colors and art direction
- `art/` — card images, listed in `art/index.json` (a static host has no
  directory listing, so the page needs that list to know what exists)

The class colors in `index.html` were extracted from `class-bible.html`. If the
bible's palette changes, re-extract them rather than editing by hand.
