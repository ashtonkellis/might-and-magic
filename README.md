# Might & Magic

Design reference for the Might & Magic card game.

## `index.html`

A browser for the card list, served as the site's home page. Every card renders
in the colors of the class it was chosen for, filterable by class, type, cost
and rules text, with a **Print these cards** button that lays the current
selection out at true card size — 2.5in x 3.5in, nine to a Letter page, with
dashed cut guides. The cards on screen hold those same proportions, so the grid
is a preview of the sheet rather than a different shape from it.

The card face reads top to bottom: a **title banner** carrying the class's two
colours — solid for a pure class, split down the middle for a blend — then the
**art panel**, a **stat line** where power and HP flank the card type, and the
**rules box**. Those panels are inset on all four sides from the card's own
gradient, so the class colour frames the card rather than only banding its
title. The frame is **3mm** — a Magic card's border width on a 63mm card, stated
exactly in the print sheet and matched on screen — and every card kind carries
the same one, whether it draws it as padding over the gradient (class cards) or
as a real border (resources in their ink, heroes in their two-colour gradient). Keywords appear in the rules box and nowhere else: the stat line names
the card type and nothing more. Power is drawn as a blade point and HP as a shield, so the two
numbers are told apart by shape as well as colour — a red blade and a green
shield. An upgrade puts those two
numbers in the bottom corners of the card instead of the stat line, since they
modify the unit it attaches to rather than describing the card itself. A credit band appears under
the rules once the card has art.

The mana cost sits top-left as a vertical column — one coloured pip per aspect
in the class's own two colours, then a single generic pip for the rest of the
cost, so an 8-cost two-aspect card reads as two colours over a 6. A pure class
shows two pips of one colour and a blend one of each, which makes colour
identity readable without reading anything.

### Resource cards

Six cards, one per ink, and the only ones that are ours rather than adapted
from the imported corpus — so they are defined in `index.html` beside the class
table rather than added to `card-list.json`, which stays what it claims to be.

They are the exception to every rule the other cards follow. Landscape rather
than portrait, 3.5in by 2.5in. No name, no cost, no stat line, no rules box —
nothing printed on them at all. A resource is identified by its art and by the
ink of its border, which is why that border is heavier than it would be
anywhere else: it is the only chrome the card has.

Their art lives in `art/resources/<ink>.png` and is found by deriving the path
from the ink, so it bypasses `art/index.json` — that manifest exists to map
corpus ids to filenames, and a resource has neither. Filtering keeps them out
of every class-shaped view; they appear under their own option and under
Everything. A print sheet of nothing but resources retracks to two landscape
cards across, eight to a page.

Card art for the other 252 is not in place yet; each shows its class glyph and
card id until images land. See `art/README.md` for how to add them.

The browser shows only cards that are in the game — 21 heroes as 42 faces, 6
resources, and 12 cards for each of the 21 classes, 300 in all. The 503
unassigned corpus cards were raw material for choosing the twelves and are not
listed; the file still holds them.

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

## `hero-cards.json`

The twenty-one hero cards, one per class — canonical, and the only two-sided
cards in the game. A hero is the card an opponent damages to win, which is what
Star Wars: Unlimited calls a base; the name changed when this project renamed
bases to heroes.

They are deliberately not in `card-list.json`. That file is the imported
corpus: one flat card shape, a single cost, a single body. A hero has no cost,
two sides, and two different meanings for HP — forcing it into that schema
would break both files.

`front` is the hero at rest: a starting HP and one ability. The HP is the whole
design. Twenty is the notional blank baseline, so below it the ability was
bought with health and above it health was paid for a drawback, which is why
the Lich sits at 25 for starting a card down.

`back` is the hero flipped. It enters play as an ordinary unit and can attack,
so its power and HP are a real body — the front's HP and the back's HP are
unrelated numbers that happen to share a name. Ported from the deployed sides
of SWU leaders, mechanics only, no card names, the same rule `card-list.json`
was built under.

Power has a floor of 1. Since a flipped hero attacks, a 0-power body would be
one that can never do anything on the attack — a dead card rather than a
design.

Class slugs, hero names and ordering are read from the `CLASSES` table in
`index.html` rather than retyped; the generator fails if any has drifted.

`join` is the cost to **Join the Fight** — the hero turns over and enters play,
paid by defeating resources. It is the game term for the action; "flipped" below
still describes the physical card, which does turn over. The notation is the
class's two ink letters plus any generic, so the Lich pays `BP1` — a Blue, a
Purple, and one of any colour. The coloured half is always the class's own
identity; the total is priced off the body being bought, because that is what
joining the fight buys. Power+HP of 8 or less costs 2, 9–10 costs 3, 11 or more
costs 4.

That bracketing was checked against the deploy costs of the SWU leaders these
bodies came from, and it reproduces them: every hero paying 2 came from a
4-cost leader, every 3 from a 5-cost, and the 4s from 6s and 7s.

The browser renders both faces — each hero is two cards in the grid, since you
need both to make the physical card, so twenty-one heroes are forty-two
entries, and the two faces are different shapes. A hero is **turned as well as
flipped**: the front is landscape with a banded layout and a Join the Fight
cost, the
flipped face is portrait and full art with only its body and one rules line
printed over the picture. Same rectangle, rotated ninety degrees — the browser
renders the flipped face at exactly the front's height for its width. They sit under their own **Heroes** filter option and under Everything,
and are excluded from every class-shaped filter, so *All assigned* stays 252.

## `art/prompts/`

Image-generation prompts, one file per image, each complete on its own so it can
be handed to a model as a URL with nothing else.

`art/prompts/*.txt` are the six resource cards. `art/prompts/<class-slug>/` is a
class: one prompt for each of its twelve cards plus one for each face of its
hero, fourteen in all. All twenty-one classes are written — 294 prompts, which is
every card in the game plus both faces of every hero.

Each class prompt carries a house-style block lifted from that class's entry in
the bible rather than paraphrased from it, byte-identical across the class. Only
the SUBJECT line differs, so the art cannot drift from the art direction — and
subjects come from the card's own rules text, not just its name.

These are sized to the slot, not to a printed card. A Star Wars: Unlimited card
image is 1120 × 1560 because it is the whole face with frame and rules baked in;
this project draws frames in HTML and needs only the picture inside them. That
slot is 3:2 landscape at 47% of card height. The two hero images are the
exception: both faces are full art, the picture *is* the card, so they are sized
to the face itself -- 3:2 landscape for the front, 2:3 portrait for the flipped
side. Each folder's README records the measurements.

## `card-list.json`

A card list drawn from the first three Star Wars: Unlimited sets, kept as a
source of mechanics to design against. 755 cards, stripped to
mechanics only — no names, no art, no artist, no rarity, no pricing — with
faction and species traits abstracted to `[TRAIT A]` / `[TRAIT B]` placeholders.
Cards naming another specific card were excluded. The card a player defends is a
**Hero**, not a base — renamed throughout, in card types and rules text alike, so
damage is dealt to heroes.

The board is split into a **left flank** and a **right flank**, but no card
dictates which one it enters — that is the player's choice at the moment of
play. Rules text still speaks of flanks relationally ("units in this flank",
"the same flank"); it never names one. Events are **spells**, the card a player
defends is a **Hero**, and the round's reset is the **rest phase**.

Each entry carries an opaque `id`, `type`, `cost`, `power`, `hp`, `unique`,
`aspects`, `keywords`, `traitCount`, and rules text.

### Class assignments

Every entry also carries a `class` field: the Might & Magic class that card was
chosen to represent, or `null` if unassigned. A card belongs to at most one
class. Twelve cards are assigned to each of the twenty-one classes — 252 of the
755 — drawn from units, spells and upgrades. **Heroes are never
assigned**: a hero is a starting card rather than something drawn and played, so
it does not belong in a class's twelve.

Twenty-six of the assigned cards came out of the corpus typed `Leader`, the SWU
mechanic this game replaced with heroes. They are **Unit** here, and their
leader-only machinery — the deployed side and the epic deploy action — is
dropped, since a card with a cost that enters play is a unit. No assigned card
mentions a leader in its rules any more: `non-leader unit` is now just `unit`,
because a hero is never a unit and so every unit in play was always a non-leader
one. The 503 unassigned corpus cards keep their original SWU wording, leaders
included — they are reference material for mechanics, and rewriting them would
cost them that.

**Smuggle costs are written in this game's inks.** The corpus priced them in SWU
aspects — `Smuggle [3 resources Vigilance]` — which are not resources anything
here can pay. All thirteen now use the same notation the hero's Join the Fight
cost uses: the class's two ink letters, then any generic, so the Shaman's
`Ash-Fed Salve` reads `Smuggle [RG1]`. Each card keeps the total SWU gave it, so
the premium over its printed cost is unchanged; only the coloured half was
restated. One card's brackets were unbalanced in the corpus and are now closed.

**Sentinel is called Bodyguard here**, after the equivalent keyword in Disney
Lorcana, on all 20 cards that carry it and in every reminder that names it —
including Saboteur's, which ignores it. Only the word changed: it still gates a
flank, where Lorcana's Bodyguard gates the whole board and carries an
enter-play-exerted rider this one does not. The corpus keeps `Sentinel` for the
same reason it keeps `leader`. One card is still *named* Rimeguard Sentinel,
where the word is a noun meaning a guard rather than the keyword.

Each class's twelve reach across the whole curve — every one of them covers all
five cost bands (0-1, 2-3, 4-5, 6-7, 8+) and carries at least three of the four
card types. The top-level `classes` object lists the twelve card ids per class.

Each assigned card also carries a `name`, written for the class that chose it
from that class's character in the bible and the card's own effect — so the
Warlock's twelve read as instalments and collateral, and the Chronomancer's as
rehearsals and foreseen arrivals. Unassigned cards have no name.
