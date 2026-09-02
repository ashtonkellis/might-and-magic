# Necromancer — art prompts

Fourteen prompts: one per card in the class, plus both faces of the hero. Each
file is complete on its own — subject, then the house style — so it can be
handed to an image model as a URL with nothing else.

## Sizing

These are **art**, not finished cards. A Star Wars: Unlimited card image is
1120 × 1560 because it is the whole printed face with the frame and rules text
baked in; this project draws its frames in HTML and only needs the picture that
goes inside them. Measured in the browser, that slot is:

| Image | Shape | Kind |
|---|---|---|
| Unit / spell / upgrade / leader | **3:2 landscape**, 47% of card height | art slot |
| Hero, landscape face | **3:2 landscape** | **full art** |
| Hero, portrait face | **2:3 portrait** | **full art** |

The twelve class cards are art slots: the frame is drawn in HTML and the picture
sits inside it, so those prompts forbid frames and borders because the frame
already exists elsewhere.

The two hero images are different. They are full art — the picture *is* the card
face, nothing printed over it — and they are two scenes of the same man, one in
each orientation. The landscape face is Viol at rest with his ledger; the portrait face is the thing he is famous for, calling someone back and paying for it, with the vertical format carrying the rise out of the dark.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`grave-salvage.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/grave-salvage.txt) | Grave Salvage | Spell | 0 |
| [`unwanted-gift.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/unwanted-gift.txt) | Unwanted Gift | Unit | 1 |
| [`buried-again.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/buried-again.txt) | Buried Again | Unit | 2 |
| [`called-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/called-back.txt) | Called Back | Spell | 2 |
| [`reclaimed-reliquary.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/reclaimed-reliquary.txt) | Reclaimed Reliquary | Upgrade | 2 |
| [`the-ledger-reopened.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/the-ledger-reopened.txt) | The Ledger Reopened | Spell | 2 |
| [`successor-sought.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/successor-sought.txt) | Successor Sought | Unit | 3 |
| [`paid-in-kind.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/paid-in-kind.txt) | Paid in Kind | Unit | 4 |
| [`viol-keeper-of-the-ledger.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/viol-keeper-of-the-ledger.txt) | Viol, Keeper of the Ledger | Leader | 5 |
| [`toll-of-three.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/toll-of-three.txt) | Toll of Three | Unit | 6 |
| [`mass-exhumation.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/mass-exhumation.txt) | Mass Exhumation | Unit | 7 |
| [`the-unwilling-return.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/the-unwilling-return.txt) | The Unwilling Return | Unit | 9 |

## The hero

| File | Face |
|---|---|
| [`viol-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/viol-hero-front.txt) | Landscape — full art, Viol at rest with the ledger |
| [`viol-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/viol-hero-back.txt) | Portrait — full art, calling one back, and paying |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
dry media only — charcoal, bone black and chalk, smudged with the hand, with the
**fingerprints left in** — and hard chiaroscuro from a single candle just outside
the frame, swallowing two-thirds of every image in shadow.

Two things carry it. The first is still-life logic: even the action cards are
*arranged* rather than caught. Objects are placed, weighted and considered, and
everything looks posed for a portrait nobody survived. The second is the memento
mori — a guttering candle, a fly, a tipped glass, a stopped watch — tucked into
every single frame, never the focus and never centered, but never absent either.

The register is what keeps this class from being a villain deck, and it is in
every file: Viol is a grief-worker. Nobody in a Necromancer card is enjoying
this, nobody is going to stop, and the cost is being written down.
