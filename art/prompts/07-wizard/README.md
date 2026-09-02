# Wizard — art prompts

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
each orientation. The landscape face is Arc at rest, which for him means an exposure still running; the portrait face is the thing he is famous for, standing inside the reaction rather than behind glass, with the vertical format carrying the column of discharge.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`spellsure-novice.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/spellsure-novice.txt) | Spellsure Novice | Unit | 1 |
| [`unmake-the-working.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/unmake-the-working.txt) | Unmake the Working | Spell | 1 |
| [`focused-detonation.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/focused-detonation.txt) | Focused Detonation | Spell | 2 |
| [`volatile-coil.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/volatile-coil.txt) | Volatile Coil | Upgrade | 2 |
| [`warded-theorist.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/warded-theorist.txt) | Warded Theorist | Unit | 2 |
| [`wild-discharge.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/wild-discharge.txt) | Wild Discharge | Unit | 2 |
| [`arc-who-does-not-delegate.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/arc-who-does-not-delegate.txt) | Arc, Who Does Not Delegate | Leader | 5 |
| [`recovered-formula.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/recovered-formula.txt) | Recovered Formula | Unit | 5 |
| [`second-detonation.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/second-detonation.txt) | Second Detonation | Spell | 5 |
| [`sudden-postulate.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/sudden-postulate.txt) | Sudden Postulate | Unit | 5 |
| [`costly-proof.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/costly-proof.txt) | Costly Proof | Unit | 7 |
| [`the-unnamed-reaction.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/the-unnamed-reaction.txt) | The Unnamed Reaction | Unit | 10 |

## The hero

| File | Face |
|---|---|
| [`arc-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/arc-hero-front.txt) | Landscape — full art, Arc at rest, the exposure still running |
| [`arc-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/arc-hero-back.txt) | Portrait — full art, standing inside the reaction |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
this class is **photographic, not painted** — a long-exposure light-painting plate
with real lens artifacts, bloom, veiling flare, magenta fringing at the highlight
edges and grain in the dark. Every prompt says so in those words, because an
image model's default is to illustrate a wizard rather than photograph one.

Two things carry it. The first is the exposure: the subject *is* the light source
and it is blown out, a blue-white core with all detail lost inside it falling off
fast into a nearly black plate. There is almost no midtone anywhere in the class.
The second is the trails — every figure and object drags a bright streak from
where it was a second ago. Nothing in this class is ever still and nothing in it
is ever photographed cleanly.

Underneath sits the gridded laboratory plate with its ruled reference marks and
margin annotation, which is never legible as words or numbers — only the
impression of exposure data. And the register, in every file: this is an
experiment already in progress, run by a man who does not wait for the result
before starting the next one, and who does not delegate any of it.
