# Might & Magic

Design reference for the Might & Magic card game.

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
