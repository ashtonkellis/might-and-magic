# Lich — art prompts

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
each orientation. The landscape face is Rime at rest, sitting for a portrait; the portrait face is the thing they are famous for, the plate failing around them while they hold the pose, with the vertical format carrying the cracks to the top edge.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`attending-revenant.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/attending-revenant.txt) | Attending Revenant | Unit | 1 |
| [`polite-insistence.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/polite-insistence.txt) | Polite Insistence | Spell | 1 |
| [`courtesy-of-the-pause.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/courtesy-of-the-pause.txt) | Courtesy of the Pause | Upgrade | 2 |
| [`frostbitten-clerk.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/frostbitten-clerk.txt) | Frostbitten Clerk | Unit | 3 |
| [`recalled-from-rest.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/recalled-from-rest.txt) | Recalled from Rest | Spell | 3 |
| [`warded-sleeper.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/warded-sleeper.txt) | Warded Sleeper | Unit | 3 |
| [`preserved-attendant.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/preserved-attendant.txt) | Preserved Attendant | Unit | 4 |
| [`rime-without-appetite.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/rime-without-appetite.txt) | Rime, Without Appetite | Leader | 4 |
| [`two-slow-certainties.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/two-slow-certainties.txt) | Two Slow Certainties | Spell | 4 |
| [`guest-who-never-leaves.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/guest-who-never-leaves.txt) | Guest Who Never Leaves | Unit | 6 |
| [`host-of-the-long-pause.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/host-of-the-long-pause.txt) | Host of the Long Pause | Unit | 6 |
| [`all-the-time-there-is.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/all-the-time-there-is.txt) | All the Time There Is | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`rime-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/rime-hero-front.txt) | Landscape — full art, Rime at rest, sitting for a portrait |
| [`rime-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/rime-hero-back.txt) | Portrait — full art, the plate failing, the pose held |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
these are wet-plate tintypes, not illustrations — silver-halide bloom in the
highlights, heavy vignetting, chemical staining and tide-lines at the plate edges,
dust and pinholes in the emulsion. The plate is a physical object with damage of
its own.

Two things carry it. The first is the exposure: harsh frontal studio light, formal
staging, everyone posed and centered and symmetrical and holding still far too
long — **nobody in this class is caught doing anything** — and the eyes never
quite in focus, because the sitter moved. Everything else on the plate is sharp
and the eyes are not. The second is the signature failure: spiderweb cracks in the
emulsion radiating outward from the subject, always centered on the sitter rather
than on any edge damage. The plate is failing where the figure touches it.

The register is in every file and it is what keeps the class from reading as a
monster: Rime is unfailingly polite and completely without appetite, curious about
the living the way one is curious about weather. Nothing here is menacing. It is
courteous, and it is not going to leave.
