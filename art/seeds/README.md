# Seeds

Reference images for the six resource cards — the objects a hero draws on to
cast. These are *inputs* to art generation, not shipping art: nothing here is
listed in `art/index.json`, so the card browser never loads them.

They live on `main` so they are publicly fetchable, which is the point — an
image model can be pointed straight at the URL:

    https://ashtonkellis.github.io/might-and-magic/art/seeds/<file>

## What is here

| File | Ink | Hex | Object |
|---|---|---|---|
| `amethyst-gemstone.jpg` | Purple · Shadow | `#81377B` | gem set into a staff |
| `emerald-gemstone.jpg`  | Green · Nature  | `#2A8934` | orb set into a staff |

Still missing: Red (Fire), Amber (Arcane), Blue (Frost), Steel (Physical).

Name new files for the ink they belong to, not the object — the object may be
redrawn later, the ink will not. Match the extension to the file's real
contents; the recovered art on the `claude/might-magic-card-design-t4qy7x`
branch has `.webp` files that are secretly JPEG, which breaks anything reading
by extension.

## Both of these are staves

That is a coincidence of what was to hand, not the intended direction. The six
should not all be wands with a stone in the end — a set that varies the object
while holding one ink each reads better than six of the same silhouette.
