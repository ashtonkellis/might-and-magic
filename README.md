# Might & Magic

Design reference for the Might & Magic card game.

## `index.html`

A browser for the card list, served as the site's home page. Every card renders
in the colors of the class it was chosen for, filterable by class, type, cost
and rules text, with a **Print these cards** button that lays the current
selection out at true card size — 2.5in x 3.5in, nine to a Letter page, with
dashed cut guides.

The card face reads top to bottom: **name**, **art**, **type bar**, **rules
box**. The mana cost sits top-left as a vertical column — one coloured pip per
aspect in the class's own two colours, then a single generic pip for the rest
of the cost, so an 8-cost two-aspect card reads as two colours over a 6. Power
and HP sit at the left and right ends of the type bar, which also carries the
card's flank.

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
Cards naming another specific card were excluded. The card a player defends is a
**Hero**, not a base — renamed throughout, in card types and rules text alike, so
damage is dealt to heroes.

The board is split into a **left flank** and a **right flank**, replacing the
source game's ground and space arenas. Units are played into one flank and act
within it; `flanks` on each entry says which one, and the rules text follows —
"a left flank unit", "units in this flank". The card a player defends is a
**Hero**, and the round's reset is the **rest phase**.

Each entry carries an opaque `id`, `type`, `cost`, `power`, `hp`, `unique`,
`aspects`, `flanks`, `keywords`, `traitCount`, and rules text.

### Class assignments

Every entry also carries a `class` field: the Might & Magic class that card was
chosen to represent, or `null` if unassigned. A card belongs to at most one
class. Twelve cards are assigned to each of the twenty-one classes — 252 of the
755 — drawn from units, events, upgrades and leaders. **Heroes are never
assigned**: a hero is a starting card rather than something drawn and played, so
it does not belong in a class's twelve.

Each class's twelve reach across the whole curve — every one of them covers all
five cost bands (0-1, 2-3, 4-5, 6-7, 8+) and carries at least three of the four
card types. The top-level `classes` object lists the twelve card ids per class.
