# Pyromancer — art prompts

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
each orientation. The landscape face is Caine at rest inside his own fire; the
portrait face is the thing he is famous for, burning the book, with the vertical
format carrying the rising column of flame.

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
| [`caine-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/caine-hero-front.txt) | Landscape — full art, Caine at rest in his fire |
| [`caine-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/caine-hero-back.txt) | Portrait — full art, burning the book |

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
