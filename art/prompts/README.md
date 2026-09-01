# Resource-card prompts

One complete, self-contained prompt per ink. Each file is the whole thing —
object, palette and style block — so it can be handed to an image model as a
URL with no other context.

| File | Ink | Hex |
|---|---|---|
| [`red.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/red.txt) | Red · Fire | `#D3082F` |
| [`amber.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/amber.txt) | Amber · Arcane | `#F5B202` |
| [`green.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/green.txt) | Green · Nature | `#2A8934` |
| [`blue.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/blue.txt) | Blue · Frost | `#0189C4` |
| [`purple.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/purple.txt) | Purple · Shadow | `#81377B` |
| [`steel.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/steel.txt) | Steel · Physical | `#9FA8B4` |

[`all.txt`](https://ashtonkellis.github.io/might-and-magic/art/prompts/all.txt) holds all six in one file.

## Running them

Each prompt goes in a **fresh chat**. Running the second in the same thread as
the first makes the image tool treat it as an edit of the previous image, and
it will ask for a target image instead of generating one.

Every prompt points at the two seed images in `../seeds/` as its style
reference. That shared reference is what holds the set together — do not edit
the style block, only the object line.

## Why these objects

Six distinct silhouettes: loose stone, pendulum, staff, ring, locket, hammer.
Both existing seeds are staves, which would have spent two of six slots on the
same outline, so only Green keeps that form. The amethyst seed still serves as
a style reference for all six; it simply no longer matches the purple object.
