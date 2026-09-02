# Death Knight — art prompts

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
each orientation. The landscape face is Pall at rest, laid out as an effigy; the portrait face is the thing he is famous for, keeping an oath he cannot remember taking, with the vertical format carrying the full length of the slab.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`given-orders.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/given-orders.txt) | Given Orders | Upgrade | 0 |
| [`conscript.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/conscript.txt) | Conscript | Unit | 1 |
| [`discarded-prisoner.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/discarded-prisoner.txt) | Discarded Prisoner | Spell | 1 |
| [`finisher.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/finisher.txt) | Finisher | Unit | 2 |
| [`paired-compulsion.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/paired-compulsion.txt) | Paired Compulsion | Unit | 2 |
| [`choose-your-loss.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/choose-your-loss.txt) | Choose Your Loss | Spell | 3 |
| [`standing-sentence.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/standing-sentence.txt) | Standing Sentence | Unit | 4 |
| [`cold-vanguard.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/cold-vanguard.txt) | Cold Vanguard | Unit | 5 |
| [`implacable-rider.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/implacable-rider.txt) | Implacable Rider | Unit | 6 |
| [`pall-bound-to-anothers-will.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/pall-bound-to-anothers-will.txt) | Pall, Bound to Another's Will | Leader | 7 |
| [`weight-of-every-oath.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/weight-of-every-oath.txt) | Weight of Every Oath | Unit | 10 |
| [`the-whole-field-conscripted.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/the-whole-field-conscripted.txt) | The Whole Field Conscripted | Unit | 11 |

## The hero

| File | Face |
|---|---|
| [`pall-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/pall-hero-front.txt) | Landscape — full art, Pall at rest, laid out as an effigy |
| [`pall-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/pall-hero-back.txt) | Portrait — full art, keeping an oath he cannot remember |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
every image is a **wax rubbing taken from a memorial brass** — the figure rendered
as black wax dragged over an incised plate, the line surviving only where the
engraving is deep, the paper's tooth showing everywhere else. There is no light in
the rubbing itself, because it is a flat record rather than a lit scene.

Two things carry it. The first is the staging: rigidly symmetrical and
full-length, laid out like a tomb slab with feet together, hands crossed or on a
hilt, heraldry at the feet and an inscription band around the border. **Even
mid-swing the figure is composed as an effigy** — the prompts say it in those
words, because the instinct is to make a death knight dynamic. The second is the
frost, which is the only light in the class: rime crystal blooming *on top of* the
rubbing, above the image rather than inside it, obscuring parts of it. The record
is icing over as you look at it.

No lettering resolves — the inscription band and heraldry carry the texture of an
epitaph without a legible character. And the register is in every file, including
the line that separates this class from the Runeblade: these marks were inflicted,
not authored.
