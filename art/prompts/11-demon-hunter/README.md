# Demon Hunter — art prompts

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
each orientation. The landscape face is Kell at rest, which is as still as this class ever gets; the portrait face is the thing they are famous for, spending the borrowed power all at once, with the vertical format carrying the drop.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`fury-vent.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/fury-vent.txt) | Fury Vent | Upgrade | 1 |
| [`goading-scout.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/goading-scout.txt) | Goading Scout | Unit | 1 |
| [`no-time-to-wait.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/no-time-to-wait.txt) | No Time to Wait | Spell | 1 |
| [`impossible-choice.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/impossible-choice.txt) | Impossible Choice | Spell | 2 |
| [`leaping-stalker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/leaping-stalker.txt) | Leaping Stalker | Unit | 2 |
| [`vanguard-doctrine.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/vanguard-doctrine.txt) | Vanguard Doctrine | Unit | 2 |
| [`kell-on-a-clock.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/kell-on-a-clock.txt) | Kell, On a Clock | Leader | 4 |
| [`pouncing-reaver.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/pouncing-reaver.txt) | Pouncing Reaver | Unit | 4 |
| [`kell-borrowed-power.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/kell-borrowed-power.txt) | Kell, Borrowed Power | Leader | 5 |
| [`twinned-assault.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/twinned-assault.txt) | Twinned Assault | Unit | 7 |
| [`unspent-momentum.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/unspent-momentum.txt) | Unspent Momentum | Unit | 7 |
| [`nothing-left-standing.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/nothing-left-standing.txt) | Nothing Left Standing | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`kell-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/kell-hero-front.txt) | Landscape — full art, Kell at rest, as still as this class gets |
| [`kell-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/kell-hero-back.txt) | Portrait — full art, spending the borrowed power all at once |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
woodblock print — flat color fills with visible grain, hard spot-blacks, keyblock
outlines, slightly imperfect registration — with dense parallel hatching borrowed
from horror manga wherever the shadow gets bad. **No gradients anywhere.** Light
here is a shape you cut, not a falloff you render, and every prompt says it in
those words.

Two things carry it. The first is instability: every composition is aggressively
diagonal, entered from a corner, on a tilted ground plane, with speed-lines and
impact bursts breaking the frame edge and running off it. No card in this class
shows a figure at rest on both feet on level ground — this is the class that never
has its feet under it. The second is restraint in the palette: three or four
flats per image, indigo and bone doing the work, block black used only as cut
spot-blacks and never as shading, and **one** vermilion note.

The register is in every file: the deal is already done and the clock is already
running, and none of that is drawn as sorrow. It is drawn as speed.
