# Warlock — art prompts

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
each orientation. The landscape face is Brand at rest, mid-negotiation and charming about it; the portrait face is the thing he is famous for, the page burning through while he keeps talking, with the vertical format carrying the fire going up the margin.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`first-instalment.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/first-instalment.txt) | First Instalment | Spell | 1 |
| [`kindly-creditor.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/kindly-creditor.txt) | Kindly Creditor | Unit | 1 |
| [`clause-reader.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/clause-reader.txt) | Clause Reader | Unit | 2 |
| [`creditors-draw.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/creditors-draw.txt) | Creditor's Draw | Spell | 2 |
| [`recalled-debtor.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/recalled-debtor.txt) | Recalled Debtor | Unit | 2 |
| [`collateral-clause.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/collateral-clause.txt) | Collateral Clause | Upgrade | 4 |
| [`marginal-collector.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/marginal-collector.txt) | Marginal Collector | Unit | 4 |
| [`settled-in-blood.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/settled-in-blood.txt) | Settled in Blood | Spell | 4 |
| [`smiling-broker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/smiling-broker.txt) | Smiling Broker | Unit | 6 |
| [`triple-dealer.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/triple-dealer.txt) | Triple Dealer | Unit | 6 |
| [`nothing-down.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/nothing-down.txt) | Nothing Down | Spell | 7 |
| [`the-collectors.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/the-collectors.txt) | The Collectors | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`brand-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/brand-hero-front.txt) | Landscape — full art, Brand at rest, mid-negotiation |
| [`brand-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/brand-hero-back.txt) | Portrait — full art, the page burning through mid-sentence |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
blackletter marginalia and gold rubrication on vellum, **then burned** — charred
edges, holes eaten through the page, and the illumination continuing around the
damage as though the damage had always been part of the design. Flat medieval
illumination with no modelling anywhere, undercut by real scorch shadow where the
page has curled. The burning is the only three-dimensional thing in the image.

Two things carry it. The first is text-block logic: the figure lives inside a
historiated initial or out in the margin, with grotesques and small demons
crawling the border and climbing the ascenders, and ruled register lines visible
under everything. The second is the second hand — red-ink corrections and marginal
marks made by somebody who read the page after Brand did and was alarmed by it.
The two hands are distinguishable at a glance, and one of them is worried.

No lettering ever resolves. The blackletter and the annotating hand carry the
texture of writing without a single legible character. And the register is in
every file: everyone here is being generous with something that is not theirs
yet, and doing arithmetic behind their eyes the whole time.
