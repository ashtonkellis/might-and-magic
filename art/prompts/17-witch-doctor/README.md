# Witch Doctor — art prompts

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
each orientation. The landscape face is Mire at rest among the jars; the portrait face is the thing they are famous for, a cure nobody consented to working anyway, with the vertical format carrying the bloom going up the body.

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
| [`poultice-bearer.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/poultice-bearer.txt) | Poultice Bearer | Unit | 1 |
| [`unpleasant-remedy.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/unpleasant-remedy.txt) | Unpleasant Remedy | Spell | 1 |
| [`fever-nurse.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/fever-nurse.txt) | Fever Nurse | Unit | 2 |
| [`salve-of-poor-provenance.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/salve-of-poor-provenance.txt) | Salve of Poor Provenance | Upgrade | 2 |
| [`ward-of-many-wounds.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/ward-of-many-wounds.txt) | Ward of Many Wounds | Spell | 2 |
| [`confident-diagnosis.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/confident-diagnosis.txt) | Confident Diagnosis | Unit | 3 |
| [`mender-of-bad-cases.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/mender-of-bad-cases.txt) | Mender of Bad Cases | Unit | 3 |
| [`spore-physician.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/spore-physician.txt) | Spore Physician | Unit | 3 |
| [`rot-fed-healer.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/rot-fed-healer.txt) | Rot-Fed Healer | Unit | 4 |
| [`mire-no-bedside-manner.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/mire-no-bedside-manner.txt) | Mire, No Bedside Manner | Leader | 5 |
| [`everything-thrives-here.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/everything-thrives-here.txt) | Everything Thrives Here | Unit | 7 |
| [`spotless-success-rate.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/spotless-success-rate.txt) | Spotless Success Rate | Unit | 8 |

## The hero

| File | Face |
|---|---|
| [`mire-hero-front.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/mire-hero-front.txt) | Landscape — full art, Mire at rest among the jars |
| [`mire-hero-back.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/mire-hero-back.txt) | Portrait — full art, a cure nobody consented to, working |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

Straight from the class bible, so the cards and the bible cannot drift apart:
actual growth patterns — mold colonies, bacterial culture, spreading rings and
fractal branching — laid over hand-dyed wax-resist cloth with the crackle where
the wax broke and the dye got in. The light is damp and ambient like a cellar, and
**nothing casts a clean shadow because nothing has a clean edge**.

Two things carry it. The first is that composition here is colonization: growth
radiates from a single point of infection somewhere in the frame, and everything
else is arranged by how far it has got. The spread is the composition, not the
subject sitting in it. The second is a prohibition that every prompt repeats —
**not one straight line anywhere in this class.** No ruled edge, no architectural
line, no square corner. Where every other style in the game has an edge, this one
has a bloom.

The register is in every file, and it is the reason the class isn't a horror deck:
rot is growth pointed the other way, and Mire has never understood why that upsets
people. Whatever is being done in these pictures is working. The patient was not
consulted.
