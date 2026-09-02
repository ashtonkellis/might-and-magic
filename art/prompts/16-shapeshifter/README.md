# Shapeshifter — art prompts

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
face, nothing printed over it — and they are two scenes of the same person, one in
each orientation. The landscape face is Pelt at rest, or as close to a person as they get; the portrait face is the thing they are famous for, the winter's worth of waiting spent in one stroke, with the vertical format carrying the drop.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`borrowed-shape.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/borrowed-shape.txt) | Borrowed Shape | Upgrade | 1 |
| [`packmate.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/packmate.txt) | Packmate | Unit | 1 |
| [`sizing-up.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/sizing-up.txt) | Sizing Up | Spell | 1 |
| [`lick-the-wound.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/lick-the-wound.txt) | Lick the Wound | Spell | 2 |
| [`pack-ambush.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/pack-ambush.txt) | Pack Ambush | Unit | 2 |
| [`outnumbered-hunter.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/outnumbered-hunter.txt) | Outnumbered Hunter | Unit | 3 |
| [`winter-patient-stalker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/winter-patient-stalker.txt) | Winter-Patient Stalker | Unit | 3 |
| [`answering-the-call.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/answering-the-call.txt) | Answering the Call | Unit | 4 |
| [`shape-of-the-season.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/shape-of-the-season.txt) | Shape of the Season | Unit | 4 |
| [`long-wait-ended.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/long-wait-ended.txt) | Long Wait Ended | Unit | 6 |
| [`pelt-who-waits-out-winter.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/pelt-who-waits-out-winter.txt) | Pelt, Who Waits Out Winter | Leader | 7 |
| [`everything-becomes-teeth.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/everything-becomes-teeth.txt) | Everything Becomes Teeth | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`pelt-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/pelt-hero-front.txt) | Landscape — full art, Pelt at rest, or nearly a person |
| [`pelt-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/pelt-hero-back.txt) | Portrait — full art, a winter of waiting spent in one stroke |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
sumi-e ink wash on unbleached paper, **one continuous loaded stroke per form** —
no correction, no second pass, no outline-then-fill — with the brush visibly
loaded at the start and visibly dry and splitting at the end. And no light at all:
value is ink dilution and nothing else, so there is not one highlight or cast
shadow in the class.

Two things carry it. The first is emptiness — the subject sits hard off-center
with the weight in one corner and two-thirds or more of the paper left completely
untouched. The emptiness is the larger half of the composition, not the
background. The second is the signature every card must contain: a form that never
fully resolves, where a human shoulder becomes an elk foreleg *within the same
stroke* and there is no point you can put a finger on where the change happens,
because the brush never lifted.

The palette is three inks and one color: exactly one small vermilion seal mark per
image, never more. And the register is in every file — nothing here is explained,
decorated or performed.
