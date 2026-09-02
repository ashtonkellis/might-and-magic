# Pyromancer — art prompts

Fourteen prompts: one per card in the class, plus both faces of the hero. Each
file is complete on its own — subject, then the house style — so it can be
handed to an image model as a URL with nothing else.

## Sizing

These are **art**, not finished cards. A Star Wars: Unlimited card image is
1120 × 1560 because it is the whole printed face with the frame and rules text
baked in; this project draws its frames in HTML and only needs the picture that
goes inside them. Measured in the browser, that slot is:

| Slot | Shape |
|---|---|
| Unit / spell / upgrade / leader art panel | **3:2 landscape**, 47% of card height |
| Hero front, full art | 1.82:1 — 3:2 crops in cleanly |
| Hero flipped, art panel | 3.29:1 letterbox band |

So every prompt asks for landscape 3:2. If you would rather generate whole card
faces at 1120 × 1560 with the frame drawn into the image, the format paragraph
is the only thing that changes.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`ashfall-runner.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/ashfall-runner.txt) | Ashfall Runner | Unit | 1 |
| [`cinder-flick.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/cinder-flick.txt) | Cinder Flick | Spell | 1 |
| [`kindling-scholar.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/kindling-scholar.txt) | Kindling Scholar | Unit | 2 |
| [`emberbrand-zealot.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/emberbrand-zealot.txt) | Emberbrand Zealot | Unit | 2 |
| [`scattershot-torch.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/scattershot-torch.txt) | Scattershot Torch | Upgrade | 3 |
| [`sweeping-flame.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/sweeping-flame.txt) | Sweeping Flame | Spell | 3 |
| [`caine-gleeful-arsonist.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/caine-gleeful-arsonist.txt) | Caine, Gleeful Arsonist | Leader | 4 |
| [`bonfire-chorus.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/bonfire-chorus.txt) | Bonfire Chorus | Unit | 4 |
| [`conflagration-titan.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/conflagration-titan.txt) | Conflagration Titan | Unit | 6 |
| [`pyre-colossus.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/pyre-colossus.txt) | Pyre Colossus | Unit | 6 |
| [`last-spark-martyr.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/last-spark-martyr.txt) | Last Spark Martyr | Unit | 6 |
| [`firestorm-incarnate.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/firestorm-incarnate.txt) | Firestorm Incarnate | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`caine-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/caine-hero-front.txt) | Front — full-art landscape |
| [`caine-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/caine-hero-back.txt) | Flipped — wide letterbox band |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
fire is the only light source and it sits inside the frame; the figure is a dark
shape in a hot field rather than a lit shape in darkness; there is no
environment at all, only flame and smoke; edges are lost-and-found; no pure
black and no saturated cadmium red. And on every single card, a phoenix head
resolving out of the fire behind the subject's shoulder — low contrast, visible
only on a second look.
