# Runeblade — art prompts

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
each orientation. The landscape face is Stave at rest at his own anvil; the portrait face is the thing he is famous for, standing still while work he finished days ago goes off, with the vertical format carrying the channels lighting up the blade.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`forge-sworn-ally.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/forge-sworn-ally.txt) | Forge-Sworn Ally | Unit | 1 |
| [`unmade-inscription.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/unmade-inscription.txt) | Unmade Inscription | Spell | 1 |
| [`binding-rune.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/binding-rune.txt) | Binding Rune | Upgrade | 2 |
| [`cutting-rune.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/cutting-rune.txt) | Cutting Rune | Upgrade | 2 |
| [`journeyman-striker.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/journeyman-striker.txt) | Journeyman Striker | Unit | 2 |
| [`reforged-claim.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/reforged-claim.txt) | Reforged Claim | Spell | 3 |
| [`scarred-anvilhand.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/scarred-anvilhand.txt) | Scarred Anvilhand | Unit | 3 |
| [`master-inlay.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/master-inlay.txt) | Master Inlay | Upgrade | 4 |
| [`rune-transfer.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/rune-transfer.txt) | Rune Transfer | Unit | 5 |
| [`stave-smith-first.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/stave-smith-first.txt) | Stave, Smith First | Leader | 5 |
| [`anvil-guard.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/anvil-guard.txt) | Anvil Guard | Unit | 6 |
| [`three-turns-ahead.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/three-turns-ahead.txt) | Three Turns Ahead | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`stave-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/stave-hero-front.txt) | Landscape — full art, Stave at rest at the anvil |
| [`stave-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/stave-hero-back.txt) | Portrait — full art, work finished days ago, going off |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
the ground of every image is **real pattern-welded steel** — watered-damascus
swirl, the layered grain of folded metal — with the imagery inlaid into it in gold
and silver wire, cut in and hammered flush. These are photographs of a worked
object, not drawings of a scene, and there is no separate background: the steel is
the background and the subject is cut into it.

Two things carry it. The first is the light on the metal — specular and
anisotropic, streaking along the grain rather than pooling into round hot spots.
The second is the one light in the class that isn't reflected: rune channels cut
into the steel and glowing from within, ember-orange, **always already lit**,
because they are the work of somebody who set this up earlier and has since moved
on. Knotwork borders interlace with the subject throughout, so figure and frame
are one continuous line.

The register is in every file, and it is also the mechanic: nothing here wins the
exchange it is in. It wins the one three turns out, which was set up while you
were watching something else — and the smith is quietly, enormously proud of work
nobody will ever notice.
