# Seeds

Reference images for the six resource cards — the objects a hero draws on to
cast. These are *inputs* to art generation, not shipping art: nothing here is
listed in `art/index.json`, so the card browser never loads them.

## Naming

One file per ink, named for the ink rather than the object, so the mapping
survives someone renaming the object later:

    red.png      Fire      #D3082F
    amber.png    Arcane    #F5B202
    green.png    Nature    #2A8934
    blue.png     Frost     #0189C4
    purple.png   Shadow    #81377B
    steel.png    Physical  #9FA8B4

Where more than one seed exists for an ink, suffix it: `red-2.png`. Any
extension is fine, but make it match the file's real contents — the recovered
art in `art/recovered/` has `.webp` files that are secretly JPEG and vice
versa, which breaks anything reading by extension.
