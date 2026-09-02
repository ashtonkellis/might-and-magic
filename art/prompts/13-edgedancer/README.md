# Edgedancer — art prompts

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
each orientation. The landscape face is Prism at rest mid-glide, which is as close to rest as this class gets; the portrait face is the thing she is famous for, going past everything that was built to stop her, with the vertical format carrying the length of the slide.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`slipped-away.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/slipped-away.txt) | Slipped Away | Spell | 1 |
| [`unnoticed-runner.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/unnoticed-runner.txt) | Unnoticed Runner | Unit | 1 |
| [`quiet-introduction.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/quiet-introduction.txt) | Quiet Introduction | Unit | 2 |
| [`remembered-later.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/remembered-later.txt) | Remembered Later | Upgrade | 2 |
| [`sent-home-gently.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/sent-home-gently.txt) | Sent Home Gently | Spell | 2 |
| [`found-underfoot.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/found-underfoot.txt) | Found Underfoot | Spell | 3 |
| [`never-quite-still.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/never-quite-still.txt) | Never Quite Still | Unit | 3 |
| [`the-overlooked-arrive.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/the-overlooked-arrive.txt) | The Overlooked Arrive | Unit | 4 |
| [`prism-who-remembers.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/prism-who-remembers.txt) | Prism, Who Remembers | Leader | 5 |
| [`between-two-breaths.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/between-two-breaths.txt) | Between Two Breaths | Unit | 6 |
| [`glide-past.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/glide-past.txt) | Glide Past | Unit | 6 |
| [`nothing-holds-them.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/nothing-holds-them.txt) | Nothing Holds Them | Spell | 12 |

## The hero

| File | Face |
|---|---|
| [`prism-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/prism-hero-front.txt) | Landscape — full art, Prism at rest, mid-glide |
| [`prism-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/prism-hero-back.txt) | Portrait — full art, past everything built to stop her |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
every form is constructed from flat planes and hard vector edges — low-poly form
language — but rendered with **real refraction**, so each facet carries a shifted
copy of whatever sits behind it and prismatic dispersion fringes every edge. Light
is refracted, never cast. There is not one soft edge in the class.

Two things carry it. The first is motion: a strict geometric armature, faintly
visible, cut by one long unbroken glide path — and every figure is mid-slide,
never mid-step. **No card in this class shows a planted foot**, and the prompts
say it in those words. The second is the rule that makes the class what it is:
somewhere in every frame, one ordinary overlooked person is rendered at exactly
the same fidelity as the hero. The servant, the bystander, the name left off the
list. Nobody in an Edgedancer card is background.

The register follows from that. Prism is frictionless and kind about it; the
precision reads as grace rather than calculation, and her attention — not her
speed — is the actual subject.
