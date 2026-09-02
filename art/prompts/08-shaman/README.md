# Shaman — art prompts

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
each orientation. The landscape face is Ash at rest on the mountain's flank; the portrait face is the thing they are famous for, standing in the eruption because it is a season, with the vertical format carrying the column of ash.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`ash-fed-salve.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/ash-fed-salve.txt) | Ash-Fed Salve | Spell | 1 |
| [`fallow-offering.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/fallow-offering.txt) | Fallow Offering | Upgrade | 1 |
| [`seedbearer.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/seedbearer.txt) | Seedbearer | Unit | 1 |
| [`ashling-herald.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/ashling-herald.txt) | Ashling Herald | Unit | 2 |
| [`cinder-rite.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/cinder-rite.txt) | Cinder Rite | Unit | 2 |
| [`everything-feeds.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/everything-feeds.txt) | Everything Feeds | Spell | 3 |
| [`magma-tender.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/magma-tender.txt) | Magma Tender | Unit | 3 |
| [`eruption-warden.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/eruption-warden.txt) | Eruption Warden | Unit | 4 |
| [`orchard-of-cinders.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/orchard-of-cinders.txt) | Orchard of Cinders | Unit | 4 |
| [`ash-who-tends-the-mountain.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/ash-who-tends-the-mountain.txt) | Ash, Who Tends the Mountain | Leader | 6 |
| [`twin-eruption.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/twin-eruption.txt) | Twin Eruption | Unit | 6 |
| [`the-mountain-is-fertile.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/the-mountain-is-fertile.txt) | The Mountain Is Fertile | Unit | 9 |

## The hero

| File | Face |
|---|---|
| [`ash-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/ash-hero-front.txt) | Landscape — full art, Ash at rest on the mountain's flank |
| [`ash-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/ash-hero-back.txt) | Portrait — full art, standing in the eruption |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
ritual pigment on rough rock — red ochre, charcoal and white clay, blown and
hand-pressed rather than brushed — lit by a torch held at arm's length outside the
frame, so the deep pitting in the stone catches real shadow. The lighting belongs
to the rock, not to the picture on it.

Two things carry it. The first is that this is **deliberately the most primitive
work in the game**: simplified forms overlapping without perspective, at different
scales and orientations because they were added at different times, with hand
stencils in the margins. Nothing is rendered and nothing is smooth. The second is
the surface — the rock's grain and cracks run straight through every mark and
interrupt the forms rather than being worked around. The surface is half the
image, and every prompt says so.

The register is the class's whole argument and it is in every file: the eruption
and the orchard are one process with a gap in the middle. Nobody in a Shaman card
is alarmed by fire or by growth, because they are the same season observed at two
different points.
