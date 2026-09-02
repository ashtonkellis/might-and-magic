# Ranger — art prompts

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
each orientation. The landscape face is Fletch at rest in camp; the portrait face is the thing she is famous for, the shot she prepared for weeks ago, with the vertical format carrying the whole length of the range.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`cached-supplies.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/cached-supplies.txt) | Cached Supplies | Upgrade | 1 |
| [`provisioned-scout.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/provisioned-scout.txt) | Provisioned Scout | Unit | 1 |
| [`read-the-ground.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/read-the-ground.txt) | Read the Ground | Spell | 1 |
| [`forward-marker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/forward-marker.txt) | Forward Marker | Unit | 2 |
| [`packed-for-both.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/packed-for-both.txt) | Packed for Both | Spell | 2 |
| [`practised-hand.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/practised-hand.txt) | Practised Hand | Unit | 2 |
| [`trail-reader.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/trail-reader.txt) | Trail Reader | Unit | 2 |
| [`recruiting-trip.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/recruiting-trip.txt) | Recruiting Trip | Unit | 4 |
| [`three-days-foresight.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/three-days-foresight.txt) | Three Days' Foresight | Spell | 4 |
| [`fletch-simply-prepared.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/fletch-simply-prepared.txt) | Fletch, Simply Prepared | Leader | 5 |
| [`weathered-tracker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/weathered-tracker.txt) | Weathered Tracker | Unit | 6 |
| [`everything-already-packed.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/everything-already-packed.txt) | Everything Already Packed | Spell | 14 |

## The hero

| File | Face |
|---|---|
| [`fletch-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/fletch-hero-front.txt) | Landscape — full art, Fletch at rest in camp |
| [`fletch-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/fletch-hero-back.txt) | Portrait — full art, the shot prepared for weeks ago |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
quick confident gouache studies on tea-stained sketchbook paper with the pencil
underdrawing left visible, lit by plain observed daylight — nothing dramatized,
nothing spotlit, no golden hour. The light is whatever the light was.

Two things carry it. The first is that **the page, not the picture, is the unit**:
every card is several small studies rather than one hero image — three views of a
subject, a detail at larger scale, a measurement, a thumbnail of the whole scene
in a corner. The second is the annotation, which makes this the only class whose
cards contain the hero's *notes* as well as her images: handwritten labels in her
own hand, with leader lines to what they describe. It must read convincingly as a
naturalist's cursive and must never resolve into actual letters, words or
numerals — the impression of a hand only. Every prompt states that limit, because
this is the class most likely to produce readable gibberish.

The register is in every file: no pact, no curse, no tragic backstory. Fletch
out-prepared everybody, and she finds the rest of the roster's suffering somewhat
self-inflicted.
