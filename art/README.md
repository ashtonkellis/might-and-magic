# Card art

Drop card images here, named by the card id shown on each empty card's
placeholder — e.g. `SOR-059.webp`. Then list the filenames in `manifest.json`:

```json
["SOR-059.webp", "TWI-011.png"]
```

The manifest exists because a static host has no directory listing: without it
the page would have to guess, firing a failed request for every card. Cards
whose id is not in the manifest simply show the class glyph instead.

Cards print at 2.5in x 3.5in, so the art slot is roughly 2.5in x 1.6in.
At 300dpi that is about 750 x 480px — supply a little larger and let it crop.
