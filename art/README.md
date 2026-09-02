# Card art

Drop card images here, named by the card id shown on each empty card's
placeholder — e.g. `SOR-059.webp`. Hero art goes in `heroes/`, named for the
hero and the face: `caine-hero-front.webp`, `caine-hero-back.webp`.

Then rebuild the manifests:

```
node tools/build-art-index.mjs
```

That writes `index.json` here and in `heroes/`, listing what is actually on
disk. The manifests exist because a static host has no directory listing:
without them the page would have to guess, firing a failed request for every
card. Anything not in a manifest simply shows the class glyph instead — which
is also what happens to a 0-byte file, since the builder skips those rather
than listing a failed upload as art.

`node tools/build-art-index.mjs --check` reports drift without writing.

Cards print at 2.5in x 3.5in, so the art slot is roughly 2.5in x 1.6in.
At 300dpi that is about 750 x 480px — supply a little larger and let it crop.
