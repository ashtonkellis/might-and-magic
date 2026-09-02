# Sorceress — art prompts

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
each orientation. The landscape face is Crystal at rest in an empty pale field; the portrait face is the thing she is famous for, stopping a room without touching it, with the vertical format carrying the ice going up the walls.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`frostbound-acolyte.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/frostbound-acolyte.txt) | Frostbound Acolyte | Unit | 1 |
| [`held-still.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/held-still.txt) | Held Still | Spell | 1 |
| [`winter-without-end.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/winter-without-end.txt) | Winter Without End | Spell | 2 |
| [`glacier-custodian.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/glacier-custodian.txt) | Glacier Custodian | Unit | 3 |
| [`perfect-preservation.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/perfect-preservation.txt) | Perfect Preservation | Upgrade | 3 |
| [`rimeguard-sentinel.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/rimeguard-sentinel.txt) | Rimeguard Sentinel | Unit | 3 |
| [`crystal-who-preserves.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/crystal-who-preserves.txt) | Crystal, Who Preserves | Leader | 4 |
| [`icebound-paragon.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/icebound-paragon.txt) | Icebound Paragon | Unit | 5 |
| [`hoarfrost-colossus.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/hoarfrost-colossus.txt) | Hoarfrost Colossus | Unit | 6 |
| [`keeper-of-kept-things.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/keeper-of-kept-things.txt) | Keeper of Kept Things | Leader | 6 |
| [`warden-of-the-still-halls.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/warden-of-the-still-halls.txt) | Warden of the Still Halls | Leader | 6 |
| [`the-long-freeze.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/the-long-freeze.txt) | The Long Freeze | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`crystal-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/crystal-hero-front.txt) | Landscape — full art, Crystal at rest in the empty field |
| [`crystal-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/crystal-hero-back.txt) | Portrait — full art, stopping a room without touching it |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
silverpoint on prepared blue-grey paper with drybrush white gouache, almost no
color, and cold directionless light in which **no shadow has an edge**. This is
the most restrained hand in the set and the prompts say so in those words.

Two things carry it. The first is emptiness: the subject takes about a third of
the frame and the rest is bare prepared paper — small figure, enormous silence.
The second is the contrast between what is drawn faintly and what is drawn
exactly. Everything organic is barely indicated; everything *frozen* is hard
faceted geometry with straight runs and sharp terminations. The ice is the only
thing in a Sorceress card drawn with conviction.

And exactly one saturated glacial blue per image, at the point of casting, used
once. Where the Pyromancer is a dark figure in a hot bright field, the Sorceress
inverts it exactly: a pale figure in a pale field with a single blue note. The
register underneath is in every file — nothing in this class is killed, it is
stopped and kept, and it is going to stay that way.
