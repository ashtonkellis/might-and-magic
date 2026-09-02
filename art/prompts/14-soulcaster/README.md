# Soulcaster — art prompts

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
face, nothing printed over it — and they are two scenes of the same woman, one in
each orientation. The landscape face is Mirren at rest, further along than she was; the portrait face is the thing she is famous for, arguing a wall out of existence, with the vertical format carrying the panel dissolving upward.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`argued-into-wholeness.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/argued-into-wholeness.txt) | Argued into Wholeness | Spell | 1 |
| [`persuading-hand.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/persuading-hand.txt) | Persuading Hand | Unit | 1 |
| [`terms-of-exchange.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/terms-of-exchange.txt) | Terms of Exchange | Upgrade | 1 |
| [`it-agrees-to-be-useful.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/it-agrees-to-be-useful.txt) | It Agrees to Be Useful | Spell | 3 |
| [`rendered-to-stock.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/rendered-to-stock.txt) | Rendered to Stock | Unit | 3 |
| [`spent-as-substance.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/spent-as-substance.txt) | Spent as Substance | Unit | 3 |
| [`traded-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/traded-back.txt) | Traded Back | Unit | 3 |
| [`two-concessions.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/two-concessions.txt) | Two Concessions | Spell | 4 |
| [`reclaimed-essence.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/reclaimed-essence.txt) | Reclaimed Essence | Unit | 5 |
| [`mirren-who-persuades-stone.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/mirren-who-persuades-stone.txt) | Mirren, Who Persuades Stone | Leader | 6 |
| [`the-wider-argument.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/the-wider-argument.txt) | The Wider Argument | Unit | 6 |
| [`mirren-half-turned-to-smoke.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/mirren-half-turned-to-smoke.txt) | Mirren, Half Turned to Smoke | Leader | 8 |

## The hero

| File | Face |
|---|---|
| [`mirren-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/mirren-hero-front.txt) | Landscape — full art, Mirren at rest, further along than before |
| [`mirren-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/mirren-hero-back.txt) | Portrait — full art, arguing a wall out of existence |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
dark stained glass, with leaded came dividing every form into flat colored panes —
no modelling inside a pane, no gradient, no brushwork — and the light coming
**from behind the image, always**. The subject is a silhouette made of colored
light and is never lit from the viewer's side. Nothing in this class casts a
shadow forward.

The medium is chosen as the class's own argument, and the prompts say so: glass is
sand that was persuaded, by fire, to become light. Every card catches one
substance partway into becoming another — half the panel still stone, half already
smoke — with the boundary irregular and mid-negotiation. Not an explosion. A
conversation being won.

The signature is the cost, and it accumulates: the came doesn't only divide the
image, it *spreads*, creeping across the figures themselves like the crystal
growing up Mirren's arm. In every card she is a little further along than in the
last one — the hero's two faces are written to be read in that order. And the
register is in every file: nothing here is destroyed, it agrees, because she is
more certain of what it ought to be than it is.
