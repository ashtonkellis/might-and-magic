# Might & Magic

Design reference for the Might & Magic card game.

## `index.html`

A browser for the card list, served as the site's home page. Every card renders
in the colors of the class it was chosen for, filterable by class, type, cost
and rules text, with a **Print these cards** button that lays the current
selection out at true card size — 2.5in x 3.5in, nine to a Letter page, with
dashed cut guides.

Card art is not in place yet; each card shows its class glyph and card id until
images land. See `art/README.md` for how to add them.

The page fetches `card-list.json`, which browsers block on `file://`. To preview
locally, serve the folder — `python3 -m http.server` — rather than opening the
file directly. On the deployed site it just works.

### Installable and offline

The site is a PWA: it can be installed to a phone or tablet home screen and
works with no network, which is the point at a playtest table. Card data is
served **network-first**, so an online visit always shows the latest deploy and
the cache is only a fallback; art is cache-first, since it never changes once
added.

The version badge beside the title changes on every deploy. It is the staleness
check — if it does not show the version you were told to expect, you are looking
at a cached copy. Run `node bump-version.mjs` before every push to increment it;
see `CLAUDE.md` for the full release workflow.

## `class-bible.html`

The class, character and art-direction bible. Six colors — Fire, Arcane, Nature,
Frost, Shadow, Physical — yielding six pure classes and fifteen blends, for a
closed roster of twenty-one. For each class: hero, character, color identity,
counter, and a locked art tradition with medium, light, composition, signature
and palette.

Open it in a browser.

## `card-list.json`

A card list drawn from the first three Star Wars: Unlimited sets, kept as a
source of mechanics to design against. 755 cards, stripped to
mechanics only — no names, no art, no artist, no rarity, no pricing — with
faction and species traits abstracted to `[TRAIT A]` / `[TRAIT B]` placeholders.
Cards naming another specific card were excluded.

Arena (ground/space) is also stripped, since the game this feeds has no
equivalent. Two cards whose targeting *was* the arena choice now read as
unconditional board sweeps.

Each entry carries an opaque `id`, `type`, `cost`, `power`, `hp`, `unique`,
`aspects`, `keywords`, `traitCount`, and rules text.

### Class assignments

Every entry also carries a `class` field: the Might & Magic class that card was
chosen to represent, or `null` if unassigned. A card belongs to at most one
class. Twelve cards are assigned to each of the twenty-one classes — 252 of the
755 — picked so that each class's twelve span the cost curve from its cheapest
rung to its most expensive and cover at least four of the five card types. The
top-level `classes` object lists the twelve card ids per class.
