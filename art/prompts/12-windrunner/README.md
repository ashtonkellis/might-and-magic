# Windrunner — art prompts

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
each orientation. The landscape face is Gale at rest above her own chart; the portrait face is the thing she is famous for, putting herself between people and what is coming, with the vertical format carrying the drop she is standing under.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`oathbearer-squire.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/oathbearer-squire.txt) | Oathbearer Squire | Unit | 1 |
| [`two-sworn-together.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/two-sworn-together.txt) | Two Sworn Together | Spell | 1 |
| [`lift-them-higher.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/lift-them-higher.txt) | Lift Them Higher | Unit | 2 |
| [`shared-ascent.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/shared-ascent.txt) | Shared Ascent | Upgrade | 2 |
| [`bound-in-purpose.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/bound-in-purpose.txt) | Bound in Purpose | Unit | 3 |
| [`three-oaths-spoken.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/three-oaths-spoken.txt) | Three Oaths Spoken | Spell | 3 |
| [`cover-their-retreat.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/cover-their-retreat.txt) | Cover Their Retreat | Unit | 4 |
| [`skyward-vanguard.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/skyward-vanguard.txt) | Skyward Vanguard | Unit | 5 |
| [`between-you-and-it.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/between-you-and-it.txt) | Between You and It | Unit | 6 |
| [`gale-who-lifts-others.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/gale-who-lifts-others.txt) | Gale, Who Lifts Others | Leader | 6 |
| [`windsworn-marshal.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/windsworn-marshal.txt) | Windsworn Marshal | Leader | 6 |
| [`the-whole-flight-rises.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/the-whole-flight-rises.txt) | The Whole Flight Rises | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`gale-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/gale-hero-front.txt) | Landscape — full art, Gale at rest above the chart |
| [`gale-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/gale-hero-back.txt) | Portrait — full art, between them and what is coming |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
the ground of every card is a meteorological chart — isobars, wind barbs,
pressure gradients and storm-track projections in survey ink on aged folded chart
paper — and the chart itself is **flat and completely unlit**, because it is a
document rather than a scene. The figure is the only luminous thing on it,
glowing from within and leaking bright vapor at the shoulders and heels.

Two things carry it. The first is that the subject sits *above* the chart plane,
outside its coordinate system, casting no shadow onto it — she is the one thing on
the page the survey could not fix a position for. The second is the rule that
makes this class unlike every other one in the game: one flight path crosses every
card, entering at one edge and leaving at another, and **wherever it passes an
ally, that figure is drawn glowing too**. Every prompt requires the path, and
every prompt requires somebody other than the hero lit by it. This is the only
class whose art shows its power landing on someone else.

Coordinates and pressure values appear everywhere and never resolve into readable
letters or numerals. And the register is in every file: Gale is a protector, the
flying is incidental, and nobody here is showing off.
