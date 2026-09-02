# Warrior — art prompts

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
each orientation. The landscape face is Hale at rest between engagements; the portrait face is the thing they are famous for, still standing when the line has gone, with the vertical format carrying the full height of the slab.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`break-the-line.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/break-the-line.txt) | Break the Line | Unit | 1 |
| [`opening-guard.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/opening-guard.txt) | Opening Guard | Spell | 1 |
| [`standing-order.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/standing-order.txt) | Standing Order | Upgrade | 1 |
| [`hold-this-ground.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/hold-this-ground.txt) | Hold This Ground | Spell | 2 |
| [`paired-bulwark.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/paired-bulwark.txt) | Paired Bulwark | Unit | 2 |
| [`shieldwall-recruit.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/shieldwall-recruit.txt) | Shieldwall Recruit | Unit | 2 |
| [`dented-veteran.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/dented-veteran.txt) | Dented Veteran | Unit | 3 |
| [`bulwark-of-the-pass.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/bulwark-of-the-pass.txt) | Bulwark of the Pass | Unit | 4 |
| [`unmarked-champion.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/unmarked-champion.txt) | Unmarked Champion | Unit | 5 |
| [`hale-who-does-not-fall.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/hale-who-does-not-fall.txt) | Hale, Who Does Not Fall | Leader | 6 |
| [`rampart-captain.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/rampart-captain.txt) | Rampart Captain | Unit | 6 |
| [`the-last-wall.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/the-last-wall.txt) | The Last Wall | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`hale-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/hale-hero-front.txt) | Landscape — full art, Hale at rest between engagements |
| [`hale-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/hale-hero-back.txt) | Portrait — full art, still standing when the line has gone |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
shallow bas-relief chiseled into weathered limestone, with tool marks, chip
damage and lichen; hard raking sidelight where the only thing making form is the
shadow cast by real physical depth; and friezelike frontal staging along a single
baseline with no perspective and no recession.

The rule that does the most work is a prohibition, and every prompt states it in
those words: **zero luminous effects anywhere in this class.** No glow, no
particles, no magic, no light source in frame, nothing radiant at all. In a game
where every other class emits something, the Warrior is the one thing that is
just an object — and that absence is the whole read. It is also the thing an
image model will try hardest to undo, so it is repeated as an instruction rather
than a description.

The register is in every file too: nothing here is dramatized. The armor is old,
it has been repaired many times, and not one repair has been hidden — the seams
and mismatched plates are carved in.
