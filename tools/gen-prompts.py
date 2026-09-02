#!/usr/bin/env python3
"""Generate a class's fourteen art prompts and its README.

One prompt per card plus one per hero face. Each file is self-contained: the
subject, then the class house-style block byte-identical across the class, then
the format. Card data comes from card-list.json and hero-cards.json so a prompt
cannot describe a card the game does not have.

Usage: python3 tools/gen-prompts.py tools/classdata/03-druid.py [...]
"""
import json, os, re, sys, runpy

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://ashtonkellis.github.io/might-and-magic/art/prompts"

CARDS = json.load(open(os.path.join(ROOT, "card-list.json")))["data"]
HEROES = {h["class"]: h for h in json.load(open(os.path.join(ROOT, "hero-cards.json")))["data"]}


def slugify(name):
    s = name.lower().replace("'", "").replace("’", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


CARD_FORMAT = """FORMAT: landscape 3:2. Full bleed to all four edges. No text, lettering,
numerals, signatures, watermarks, borders, frames or card templates -- the card
frame is drawn separately and this image sits inside it. Keep nothing essential
within the outer 4% of the left and right edges."""

HERO_FORMAT = """FORMAT: full art, {shape}. The image is the entire card face -- nothing
will be printed over it and no frame will crop it, so it must carry the card by
itself. Bleed to all four edges. No text, lettering, numerals, signatures,
watermarks, borders or frames. Keep nothing essential within the outer 4% of any
edge."""


def build(slug, D):
    outdir = os.path.join(ROOT, "art", "prompts", slug)
    os.makedirs(outdir, exist_ok=True)
    cards = sorted([c for c in CARDS if c.get("class") == slug],
                   key=lambda c: (c.get("cost", 0), c["name"]))
    assert len(cards) == 12, f"{slug}: expected 12 cards, found {len(cards)}"
    hero = HEROES[slug]
    name, display = hero["hero"], D["display"]
    label = D["label"] + " HOUSE STYLE -- identical on every card in this class, do not vary it."
    style = D["style"].strip("\n")

    subjects = dict(D["subjects"])
    written = []
    for c in cards:
        key = slugify(c["name"])
        assert key in subjects, f"{slug}: no subject written for {c['name']} ({key})"
        body = "\n".join([
            c["name"],
            f"{c['type']} · {c.get('cost', 0)} cost",
            f"{display} · Might & Magic card art",
            "Paste this whole file into a fresh chat. It is complete on its own.",
            "",
            "SUBJECT: " + subjects.pop(key).strip(),
            "",
            label,
            "",
            style,
            "",
            CARD_FORMAT,
            "",
        ])
        open(os.path.join(outdir, key + ".txt"), "w").write(body)
        written.append((key, c))

    for face, shape, desc in (("front", "landscape 3:2", "landscape"),
                              ("back", "portrait 2:3", "portrait")):
        key = f"{slugify(name)}-hero-{face}"
        body = "\n".join([
            f"{name} — hero card, {desc} face (full art)",
            f"{display} · Might & Magic hero art",
            "Paste this whole file into a fresh chat. It is complete on its own.",
            "",
            "SUBJECT: " + D["hero_" + face].strip(),
            "",
            HERO_FORMAT.format(shape=shape),
            "",
            label,
            "",
            style,
            "",
        ])
        open(os.path.join(outdir, key + ".txt"), "w").write(body)

    assert not subjects, f"{slug}: subjects written for cards that do not exist: {list(subjects)}"

    rows = "\n".join(
        f"| [`{k}.txt`]({BASE}/{slug}/{k}.txt) | {c['name']} | {c['type']} | {c.get('cost', 0)} |"
        for k, c in written)
    hslug = slugify(name)
    readme = f"""# {display} — art prompts

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
face, nothing printed over it — and they are two scenes of {D['hero_who']}, one in
each orientation. {D['hero_summary']}

## The cards

| File | Card | Type | Cost |
|---|---|---|---|
{rows}

## The hero

| File | Face |
|---|---|
| [`{hslug}-hero-front.txt`]({BASE}/{slug}/{hslug}-hero-front.txt) | Landscape — full art, {D['front_desc']} |
| [`{hslug}-hero-back.txt`]({BASE}/{slug}/{hslug}-hero-back.txt) | Portrait — full art, {D['back_desc']} |

## Running them

Each prompt goes in a **fresh chat**. Running a second in the same thread makes
the image tool treat it as an edit of the previous image and it will ask for a
target instead of generating one.

The house-style block is byte-identical in all fourteen and is what holds the
class together. Edit the SUBJECT line only.

## What the style enforces

{D['enforces'].strip()}
"""
    open(os.path.join(outdir, "README.md"), "w").write(readme)
    print(f"{slug}: 14 prompts + README")


for path in sys.argv[1:]:
    mod = runpy.run_path(path)
    for slug, D in mod["CLASSES"].items():
        build(slug, D)
