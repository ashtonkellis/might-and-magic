# Art prompts

One complete, self-contained prompt per image. Every file is the whole thing —
subject, style block and format — so it can be handed to an image model as a URL
with no other context.

## The twenty-one classes

Each class folder holds fourteen prompts: one for each of its twelve cards, plus
one for each face of its hero. Within a folder the house-style block is
byte-identical across all fourteen and only the SUBJECT line differs, so the art
cannot drift from the class bible. All twenty-one classes are written.

| Folder | Class | Hero | Art tradition |
|---|---|---|---|
| [`01-pyromancer/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/01-pyromancer/README.md) | Pyromancer | Caine | Polished digital illustration, fire-lit and mid-key |
| [`02-chronomancer/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/02-chronomancer/README.md) | Chronomancer | Vesper | Copperplate etching with chromatic ghosting |
| [`03-druid/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/03-druid/README.md) | Druid | Briar | Art Nouveau botanical plate |
| [`04-sorceress/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/04-sorceress/README.md) | Sorceress | Crystal | Silverpoint on prepared blue-grey paper |
| [`05-necromancer/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/05-necromancer/README.md) | Necromancer | Viol | Dutch vanitas in charcoal and bone black |
| [`06-warrior/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/06-warrior/README.md) | Warrior | Hale | Carved stone relief |
| [`07-wizard/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/07-wizard/README.md) | Wizard | Arc | Long-exposure light painting on a lab plate |
| [`08-shaman/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/08-shaman/README.md) | Shaman | Ash | Ochre-and-charcoal cave painting |
| [`09-trinket-mage/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/09-trinket-mage/README.md) | Trinket-mage | Quench | Exploded-view patent plate, brass and blueprint |
| [`10-warlock/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/10-warlock/README.md) | Warlock | Brand | Scorched illuminated manuscript |
| [`11-demon-hunter/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/11-demon-hunter/README.md) | Demon Hunter | Kell | Ukiyo-e woodblock with horror hatching |
| [`12-windrunner/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/12-windrunner/README.md) | Windrunner | Gale | Storm chart with a luminous figure |
| [`13-edgedancer/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/13-edgedancer/README.md) | Edgedancer | Prism | Faceted crystalline geometry |
| [`14-soulcaster/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/14-soulcaster/README.md) | Soulcaster | Mirren | Dark stained glass, mid-transmutation |
| [`15-runeblade/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/15-runeblade/README.md) | Runeblade | Stave | Damascened metal inlay |
| [`16-shapeshifter/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/16-shapeshifter/README.md) | Shapeshifter | Pelt | Sumi-e ink wash, single-breath brushwork |
| [`17-witch-doctor/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/17-witch-doctor/README.md) | Witch Doctor | Mire | Bio-culture bloom on batik |
| [`18-ranger/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/18-ranger/README.md) | Ranger | Fletch | Naturalist field-journal gouache |
| [`19-lich/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/19-lich/README.md) | Lich | Rime | Frost-fogged daguerreotype |
| [`20-death-knight/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/20-death-knight/README.md) | Death Knight | Pall | Funerary brass rubbing over frozen steel |
| [`21-assassin/`](https://ashtonkellis.github.io/might-and-magic/art/prompts/21-assassin/README.md) | Assassin | Hush | Shadow-puppet silhouette |

## Resource cards

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
