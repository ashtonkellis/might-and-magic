# Druid — art prompts

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
each orientation. The landscape face is Briar at rest in her own overgrowth; the portrait face is the thing she is famous for, standing still long enough that the forest does the fighting, with the vertical format carrying the canopy closing overhead.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`let-it-fester.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/let-it-fester.txt) | Let It Fester | Spell | 1 |
| [`slow-poultice.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/slow-poultice.txt) | Slow Poultice | Upgrade | 1 |
| [`thornbacked-yearling.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/thornbacked-yearling.txt) | Thornbacked Yearling | Unit | 1 |
| [`bramblehide-elk.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/bramblehide-elk.txt) | Bramblehide Elk | Unit | 2 |
| [`rootbound-sentry.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/rootbound-sentry.txt) | Rootbound Sentry | Unit | 2 |
| [`season-of-scars.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/season-of-scars.txt) | Season of Scars | Spell | 2 |
| [`deepwood-steward.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/deepwood-steward.txt) | Deepwood Steward | Unit | 3 |
| [`wound-fed-bull.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/wound-fed-bull.txt) | Wound-Fed Bull | Unit | 4 |
| [`briar-patient-as-rot.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/briar-patient-as-rot.txt) | Briar, Patient as Rot | Leader | 5 |
| [`old-growth-warden.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/old-growth-warden.txt) | Old Growth Warden | Unit | 6 |
| [`the-grove-remembers.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/the-grove-remembers.txt) | The Grove Remembers | Unit | 7 |
| [`blight-of-slow-years.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/blight-of-slow-years.txt) | Blight of Slow Years | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`briar-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/briar-hero-front.txt) | Landscape — full art, Briar at rest in the mandorla |
| [`briar-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/briar-hero-back.txt) | Portrait — full art, the forest closing while she waits |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
flat decorative color under one heavy contour line, gold ornament crowding in
from the frame edge, and **no light at all** — this style is decorative rather
than illuminated, so there is not one cast shadow or modelled highlight in the
class. Depth comes from layering and line weight alone.

Two things carry it. The first is stillness: every card is symmetrical, centered
and mandorla-framed, and nothing in the class is caught mid-motion. These are the
quietest cards in the game on purpose. The second is that **ornament density
scales with cost**, which is why every prompt prints the card's cost at the top —
a 1-cost card is nearly bare paper cream, an 8-cost card is overgrown with the
border eating into the art and the subject half-swallowed.

The register is the hard part and it is in every file: Briar is patient to the
point of cruelty. Wounds in this class are not tended, they are allowed to sit
and feed something downstream, and no figure in frame is troubled by that. If
someone is bleeding, the plants are doing well.
