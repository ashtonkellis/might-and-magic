# Chronomancer — art prompts

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
each orientation. The landscape face is Vesper at rest among her own apparatus;
the portrait face is her walking forward through a battle that has stopped, with
the vertical format carrying the frozen blast standing over her.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`foreseen-arrival.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/foreseen-arrival.txt) | Foreseen Arrival | Spell | 1 |
| [`hourglass-adept.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/hourglass-adept.txt) | Hourglass Adept | Unit | 1 |
| [`rehearsed-morning.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/rehearsed-morning.txt) | Rehearsed Morning | Upgrade | 1 |
| [`numbered-certainty.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/numbered-certainty.txt) | Numbered Certainty | Unit | 2 |
| [`twice-read-page.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/twice-read-page.txt) | Twice-Read Page | Unit | 2 |
| [`echo-of-the-next-turn.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/echo-of-the-next-turn.txt) | Echo of the Next Turn | Unit | 3 |
| [`four-futures-read.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/four-futures-read.txt) | Four Futures Read | Spell | 3 |
| [`archivist-of-spent-hours.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/archivist-of-spent-hours.txt) | Archivist of Spent Hours | Unit | 4 |
| [`excised-timeline.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/excised-timeline.txt) | Excised Timeline | Spell | 5 |
| [`vesper-bored-of-victory.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/vesper-bored-of-victory.txt) | Vesper, Bored of Victory | Leader | 6 |
| [`warden-of-held-moments.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/warden-of-held-moments.txt) | Warden of Held Moments | Unit | 7 |
| [`the-long-rehearsal.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/the-long-rehearsal.txt) | The Long Rehearsal | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`vesper-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/vesper-hero-front.txt) | Landscape — full art, Vesper at rest among her apparatus |
| [`vesper-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/vesper-hero-back.txt) | Portrait — full art, walking through a stopped battle |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
engraved line and crosshatch only, in the manner of an 18th-century scientific
plate, with no painterly texture and no soft gradients; flat sourceless light,
so form comes from hatch density and there is not one cast shadow in the class;
plate furniture in the corners — ruled margins and tick marks that suggest
annotation but never resolve into readable words.

Two things carry the class. The first is the ground: Chronomancer is the only
class in the game printed on a **pale** field, so a Chronomancer card set beside
any other should read as a page torn out of a different, older book. The second
is registration. Every figure is printed three times slightly out of register —
a cyan copy a few millimetres behind, an amber copy a few millimetres ahead, the
true sepia figure sharp between them. It is misregistration, not motion blur:
crisp line work, just off-plate. The subject is standing in three moments at
once.

The hero's portrait face is the one deliberate inversion. There, everything
frozen prints once and dead sharp and only Vesper carries ghosts — she is the
only thing in the picture occupying more than one moment.
