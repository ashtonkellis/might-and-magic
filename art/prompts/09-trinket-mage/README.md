# Trinket-mage — art prompts

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
each orientation. The landscape face is Quench at rest among his own inventory; the portrait face is the thing he is famous for, standing inside a rig that is running past its tolerances, with the vertical format carrying the pressure column.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`overpressure-fitter.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/overpressure-fitter.txt) | Overpressure Fitter | Unit | 1 |
| [`parts-requisition.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/parts-requisition.txt) | Parts Requisition | Spell | 1 |
| [`pressure-tap.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/pressure-tap.txt) | Pressure Tap | Upgrade | 1 |
| [`stripped-for-parts.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/stripped-for-parts.txt) | Stripped for Parts | Spell | 2 |
| [`valve-technician.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/valve-technician.txt) | Valve Technician | Unit | 2 |
| [`bulk-fitting.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/bulk-fitting.txt) | Bulk Fitting | Upgrade | 3 |
| [`modular-frame.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/modular-frame.txt) | Modular Frame | Unit | 3 |
| [`countermeasure-rig.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/countermeasure-rig.txt) | Countermeasure Rig | Unit | 4 |
| [`requisition-clamp.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/requisition-clamp.txt) | Requisition Clamp | Upgrade | 5 |
| [`quench-all-pockets-full.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/quench-all-pockets-full.txt) | Quench, All Pockets Full | Leader | 6 |
| [`borrowed-apparatus.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/borrowed-apparatus.txt) | Borrowed Apparatus | Unit | 7 |
| [`total-systems-failure.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/total-systems-failure.txt) | Total Systems Failure | Spell | 8 |

## The hero

| File | Face |
|---|---|
| [`quench-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/quench-hero-front.txt) | Landscape — full art, Quench at rest among his inventory |
| [`quench-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/quench-hero-back.txt) | Portrait — full art, inside a rig running past tolerance |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
an exploded-view patent plate on aged drafting paper — isometric, parts floating
apart along thin leader lines with numbered callouts — with the metal rendered as
real material. Brass takes genuine specular hits, steel sweats, copper goes warm.
The drawing is a document and the machine in it is an object, and both readings
have to hold at once.

Two things carry it. The first is that steam, condensation and meltwater are
drawn with **the same technical precision as the parts** — ruled, sectioned and
called out rather than painted in as atmosphere. The second is the class's own
phrase for itself: dream-punk, not steampunk. Every diagram is plausible right up
until it isn't. The tolerances are believable, the fasteners are correct, and the
machine as drawn could not possibly work.

Annotation appears on every card and is never legible — callout numbers,
dimension arrows and margin notes give the convincing impression of a numbered
technical document without resolving into letters or numerals. Underneath is the
register: this is inventory, not talent, built by a man with singed fingertips
who is genuinely pleased with how it came out.
