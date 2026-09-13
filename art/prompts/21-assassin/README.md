# Assassin — art prompts

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
each orientation. The landscape face is Hush at rest, off the clock; the portrait face is the thing they are famous for, the job done exactly as quoted, with the vertical format carrying the height of the screen.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`contract-opened.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/contract-opened.txt) | Contract Opened | Spell | 1 |
| [`quiet-professional.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/quiet-professional.txt) | Quiet Professional | Unit | 1 |
| [`working-blade.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/working-blade.txt) | Working Blade | Upgrade | 1 |
| [`clean-entry.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/clean-entry.txt) | Clean Entry | Spell | 2 |
| [`the-one-between.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-one-between.txt) | The One Between | Unit | 2 |
| [`the-paid-hand.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-paid-hand.txt) | The Paid Hand | Unit | 3 |
| [`finish-the-job.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/finish-the-job.txt) | Finish the Job | Spell | 4 |
| [`still-negotiator.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/still-negotiator.txt) | Still Negotiator | Unit | 5 |
| [`the-last-to-leave.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-last-to-leave.txt) | The Last to Leave | Unit | 5 |
| [`the-punctual.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-punctual.txt) | The Punctual | Unit | 5 |
| [`the-twice-hired.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-twice-hired.txt) | The Twice-Hired | Unit | 7 |
| [`the-detached.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/the-detached.txt) | The Detached | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`hush-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/hush-hero-front.txt) | Landscape — full art, Hush at rest, off the clock |
| [`hush-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/hush-hero-back.txt) | Portrait — full art, the job done exactly as quoted |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
cut-paper figures against a lit screen — wayang logic, with the articulated joints
and **control rods visible as part of the design** rather than hidden — lit from
behind by a single warm even lamp, so the figures are pure negative shapes and the
ground is the only thing that glows.

Two things carry it. The first is the hardest constraint in the game: there is no
interior detail anywhere, so **the silhouette carries one hundred percent of the
read**. Every pose has to be legible with no face, no fold and no texture
available to help it, and every prompt says so. The second is the accent: exactly
one color per card, used exactly once, on one small shape. Usually blood;
occasionally not. Never a second note.

The palette is three values and no gradients — lamp amber, pure black, and the one
red. And the register is in every file, because it is what makes the class
unsettling rather than edgy: Hush has no ideology, no grudge and no tortured
relationship with the work. In a cast of the cursed and the bargained-away, the
one who is simply fine is the worst thing on the table.
