# -*- coding: utf-8 -*-
CLASSES = {}

CLASSES["03-druid"] = dict(
    display="Druid",
    label="DRUID",
    hero_who="the same woman",
    hero_summary="The landscape face is Briar at rest in her own overgrowth; the portrait face is "
                 "the thing she is famous for, standing still long enough that the forest does the "
                 "fighting, with the vertical format carrying the canopy closing overhead.",
    front_desc="Briar at rest in the mandorla",
    back_desc="the forest closing while she waits",
    style="""
Medium: Art Nouveau botanical plate. Flat decorative color under a heavy,
confident contour line of even weight -- the line does all the drawing. Gold-leaf
ornament crowds inward from the frame edge. No painterly texture, no
rendering, no visible brushwork.

Light: none. This style is decorative, not illuminated -- there is no light
source, no cast shadow and no modelling. Depth is layering and line weight only.

Composition: symmetrical and mandorla-framed. The subject is centered, static
and facing forward, held inside an almond of foliage. These are deliberately the
stillest cards in the game -- nothing is caught mid-motion, nothing is falling,
nothing is in a hurry.

Signature: ornament density scales with the card's cost, which is printed at the
top of this file. At 1 the frame is nearly bare and the field is open paper
cream; at 8 it is overgrown, the border eating well into the picture and the
subject half-swallowed by it. Read the cost and set the density accordingly.

Ground: warm paper cream #EFE9D8, flat, with the botanical forms drawn on it
rather than in a space. Sap green #3A7D44 and ochre #7E8B3C carry the plant
matter, dusty rose #C08A7E the flesh and the wounds, leaf gold #C9A227 the
ornament. Nothing saturated, no black, no shadow mass.

Register: patience to the point of cruelty. Injuries are not tended here, they
are allowed to sit and feed something downstream, and nobody in frame is
troubled by that. Urgency is vulgar. If a figure is bleeding, the plants are
doing well.
""",
    hero_front="""Briar at rest, the class portrait. Full figure, standing centered and
motionless in a mandorla of bramble that has clearly grown around her over
years rather than been arranged. Bark scarring up both forearms, seed pouches
at the belt, one hand open and empty. She is looking at the viewer and is in no
hurry about it. Maximum ornament density -- this is the most overgrown frame in
the class, gold ornament crowding all the way in from the edges until the
picture is a hole in the foliage.""",
    hero_back="""An action shot, and for this class an action shot is not motion --
it is a season going by while she declines to move. Briar standing absolutely
still at the bottom of a tall vertical frame with her arms at her sides, and
above and around her a whole engagement being resolved by the forest: roots
coming up through armored feet, bramble closing over a raised weapon, a charging
line already half-swallowed and going green. Low camera looking up the trunks so
the closing canopy owns the upper two thirds and Briar is small and unmoved at
the base of it. Her expression has not changed. Everything in the frame is
losing except the plants and the woman who waited.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
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
someone is bleeding, the plants are doing well.""",
    subjects={
        "let-it-fester": """A wound deliberately left open. A gash across a forearm, held apart by two
fingers, and inside it a bramble runner already rooted and thickening -- feeding
on it rather than closing it. The arm belongs to someone who is watching this
happen with mild interest. In the mandorla behind, the same vine drawn healthy
and enormous, showing what the wound is paying for.""",
        "slow-poultice": """A dressing of packed moss, bark fiber and crushed seed bound to a shoulder with
waxed cord. The moss has grown down into the wound instead of over it, and where
the cord crosses the skin, small leaves have started. A pair of hands finishing
the knot without haste. The bandage is more alive than the patient.""",
        "thornbacked-yearling": """A young hoofed beast, still leggy and out of proportion, with a ridge of woody
thorns coming up through the hide along its spine. Two of them are broken off
short. It is standing square and facing forward, unbothered, and the thorns are
visibly longer near the older scars.""",
        "bramblehide-elk": """A full-grown elk whose hide has gone entirely to bramble -- the coat is a mat of
woody stems and the antlers are the same growth continued upward and flowering
at the tips. It is standing in profile-to-frontal in the mandorla, absolutely
still. Old damage in the bramble coat has healed thicker and darker than the
rest.""",
        "rootbound-sentry": """A standing figure rooted where it stands -- legs gone to trunk below the knee
and fused to the ground, arms out and branching. It has clearly been here long
enough that the position was a decision once and is not one now. Frontal,
symmetrical, absolutely centered. Small fresh green at the fingertips.""",
        "season-of-scars": """A cross-cut trunk section shown flat to the viewer like a specimen plate, its
growth rings visible, and in the rings the record of every bad year: char, an
embedded arrowhead the wood has grown around and closed over, a split that
healed off-center. The scars are the widest rings. Ornamental foliage frames the
section in an almond.""",
        "deepwood-steward": """A tall figure in layered bark and moss carrying a shallow wooden bowl of clear
water in both hands, walking forward out of the mandorla -- the one nearly-moving
card in the class, and even here the stride is a single unhurried step. Where
water has slopped over the rim it has already sprouted on the ground behind.""",
        "wound-fed-bull": """A heavy bull, chest-on and filling the frame, with old gores across the
shoulders that have healed as knots of hardwood rather than scar tissue. The
hardwood is the strongest part of it. Head lowered but not charging -- weight
set, patient, waiting to be given a reason. Ornament thickening at the corners.""",
        "briar-patient-as-rot": """Briar herself, the class leader, centered and frontal in a mandorla of
overgrowth, bark-scarred forearms crossed, seed pouches at her belt. She is
looking directly out at the viewer with an expression of enormous, unhurried
patience -- the look of someone who has already decided to outlast you and does
not need you to know it. Around her feet the ornament is going brown and going
back into the ground, and it is thriving there.""",
        "old-growth-warden": """An immense figure of old wood, mostly trunk, so long-standing that a whole small
ecology lives on it -- lichen, ferns in the joints, a bird's nest in the crook of
one shoulder. A split runs down the length of its chest and has closed over
thicker than the surrounding wood. It stands centered and takes the whole
height of the frame. Heavy ornament, near the top of the range.""",
        "the-grove-remembers": """Not one figure but a stand of them -- five or six rooted forms of very different
ages in a semicircle, drawn overlapping and flat with no perspective, all facing
the viewer. The youngest is a sapling with a face barely indicated; the oldest is
almost entirely trunk. They are clearly one thing with several bodies. Ornament
dense, gold crowding well into the picture from every edge.""",
        "blight-of-slow-years": """A vast slow rot, drawn as decoratively as everything else in this class: a
canopy in the upper frame going gold and brown and thin, and beneath it a field
of standing figures already half unmade -- hollowed, leaning, quietly diminished.
Nothing is violent and nothing is bleeding. It simply reached them, the way a
season does. Maximum ornament, the border eating deep into the art.""",
    },
)

CLASSES["04-sorceress"] = dict(
    display="Sorceress",
    label="SORCERESS",
    hero_who="the same woman",
    hero_summary="The landscape face is Crystal at rest in an empty pale field; the portrait "
                 "face is the thing she is famous for, stopping a room without touching it, "
                 "with the vertical format carrying the ice going up the walls.",
    front_desc="Crystal at rest in the empty field",
    back_desc="stopping a room without touching it",
    style="""
Medium: silverpoint on prepared blue-grey paper, with drybrush white gouache
highlights. Almost no color anywhere -- this is the most restrained hand in the
set. Fine metal-point line, faint and grey, that cannot be erased and was
therefore drawn slowly.

Light: cold, diffuse and directionless, like an overcast snowfield. No shadow
in this image has an edge. Nothing is dramatized and nothing is spotlit.

Composition: extreme negative space. The subject occupies roughly a third of the
frame and the rest is empty pale field -- not background, not scenery, just
prepared paper. Small figure, enormous silence.

Structure: hard crystalline geometry is the one thing in the image drawn with
conviction. Faceted ice grows in straight runs with sharp terminations, cutting
across all that soft grey. Everything organic is barely indicated; everything
frozen is exact. That contrast is the class.

Ground: paper blue-grey #B9C2D2, graphite #5A6478 for the line, lead white
#F4F6FA for the drybrush highlights, and exactly one saturated glacial blue
#8FD3F0 -- used once, at the point of casting, and nowhere else. Everything else
is almost not there. Where the Pyromancer is a dark figure in a hot bright
field, this class inverts it exactly: a pale figure in a pale field with a
single blue note.

Register: preservation offered as love and received as something else. Nothing
here is killed; it is stopped, and kept, and will be kept. Aristocratic bearing,
surgical precision, profound loneliness. Whatever she has held still in this
picture is going to stay that way.
""",
    hero_front="""Crystal at rest, the class portrait. Full figure, standing in
three-quarter view in an enormous empty pale field, occupying no more than a
third of the frame and set well off-center so the emptiness is the subject as
much as she is. Aristocratic posture, hands loose, court dress rendered in the
faintest possible silverpoint. Around her, at some distance, small ordinary
things she has preserved and kept -- a bird mid-flight, a cup mid-fall, a
flower -- each one held perfectly still in exact faceted ice while she herself is
barely drawn. She is not looking at any of them. The single saturated glacial
blue note sits at her fingertips.""",
    hero_back="""An action shot, and for this class an action shot is not a blow --
it is a room ceasing to be able to act. Crystal walking forward down the
vertical of a long hall with one hand slightly raised, and the freeze going up
the walls ahead of her: exact faceted ice climbing columns, spreading across the
floor in straight runs with sharp terminations, catching a dozen figures mid-step
and mid-shout on either side. Every frozen thing is drawn hard and precise; she
is the softest, faintest thing in her own picture. Low camera looking up the
hall so the ice owns the height of the frame. Nobody is hurt. Nobody is going to
move again either. The one saturated glacial blue is at her raised hand and
nowhere else in the image.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
silverpoint on prepared blue-grey paper with drybrush white gouache, almost no
color, and cold directionless light in which **no shadow has an edge**. This is
the most restrained hand in the set and the prompts say so in those words.

Two things carry it. The first is emptiness: the subject takes about a third of
the frame and the rest is bare prepared paper — small figure, enormous silence.
The second is the contrast between what is drawn faintly and what is drawn
exactly. Everything organic is barely indicated; everything *frozen* is hard
faceted geometry with straight runs and sharp terminations. The ice is the only
thing in a Sorceress card drawn with conviction.

And exactly one saturated glacial blue per image, at the point of casting, used
once. Where the Pyromancer is a dark figure in a hot bright field, the Sorceress
inverts it exactly: a pale figure in a pale field with a single blue note. The
register underneath is in every file — nothing in this class is killed, it is
stopped and kept, and it is going to stay that way.""",
    subjects={
        "frostbound-acolyte": """A young student in plain robes, small in an enormous empty pale field, kneeling
to press one bare palm flat against the ground. Where the palm meets it, a
small exact disc of faceted ice has formed and a wound in the ground -- a scorch,
a split -- has been closed under it. The figure is barely drawn. The disc is
drawn precisely. The single glacial blue note is under the palm.""",
        "held-still": """A running figure stopped mid-stride, both feet off the ground, held there. No
ice touches the body: the ice is in a hard faceted lattice through the air
around it, sharp straight runs terminating in points, and the runner is simply
not permitted through. The face is barely indicated and is only beginning to
understand. Vast empty pale field on all sides.""",
        "winter-without-end": """A figure already stopped some time ago -- long enough that the exact faceted ice
has grown a second generation on top of the first, straight runs off straight
runs, and the shape underneath is now only a suggestion inside it. Nothing is
breaking. Nothing is going to thaw. Small in an enormous empty field, off-center,
with the one blue note deep inside the ice where the body is.""",
        "glacier-custodian": """A tall attendant figure standing watch at the foot of a wall of glacier ice, so
faintly drawn as to be almost paper, while the ice behind is exact -- a hard
faceted face with straight fracture runs and sharp terminations. Set inside the
ice at a distance, barely legible, something being kept. The custodian's hands
are folded. Enormous negative space above.""",
        "perfect-preservation": """A single object held in exact faceted ice at the center of an empty field: a
flower, complete, at its absolute best, every petal open. The ice around it is
drawn hard and precise and the flower inside is drawn perfectly. It will never
be better than this and it will never be anything else again. The one saturated
glacial blue note sits at the flower's heart.""",
        "rimeguard-sentinel": """A single armored figure standing directly frontal and dead still, feet planted,
occupying a third of the frame in an otherwise empty pale field -- the flank is
closed and this is why. A shield of exact faceted ice, drawn hard where the
figure is drawn faintly, has grown across the forearm in straight runs. Nothing
approaches. Nothing has needed to be struck.""",
        "crystal-who-preserves": """Crystal herself, the class leader, standing three-quarter view and small in an
enormous empty pale field, drawn in the faintest silverpoint the class allows.
Aristocratic bearing, chin level, one hand extended palm-down. Beneath the palm,
exact faceted ice is running outward across the ground in straight lines with
sharp terminations. She is not watching it work. She has done this before and it
always works. The one blue note is at her palm.""",
        "icebound-paragon": """A figure in full ceremonial armor made entirely of exact faceted ice -- straight
runs, sharp terminations, hard clean planes -- standing frontal and still. The
person inside is barely indicated through it, a faint silverpoint suggestion at
best. The armor is the only thing here drawn with conviction, and it is
magnificent, and it does not come off.""",
        "hoarfrost-colossus": """An enormous crystalline figure, entirely faceted ice, standing at the far side
of a vast empty pale field so that even at its size it occupies about a third of
the frame. Every plane hard and exact, every termination sharp; the scale reads
from the tiny faintly-drawn figures at its feet, each of whom carries a small
exact plate of the same ice on one arm. Cold flat light, no cast shadow.""",
        "keeper-of-kept-things": """An interior rendered almost entirely as empty pale field, with a long shelf
receding through it holding kept things: a bird, a cup, a letter, a hand -- each
sealed in its own exact block of faceted ice, each perfect, each labelled by
nothing. A single faint figure stands at the shelf's end, having just set
another one down. The one blue note is inside the newest block.""",
        "warden-of-the-still-halls": """A vast pale hall drawn as almost nothing -- two faint suggestions of columns and
otherwise open paper -- with one small figure standing at the center of the floor,
facing away, perfectly composed. The hall is full of exact faceted ice growing
along the floor in straight runs, and it is completely empty of people. Whatever
was here has already been stopped and taken away. Enormous silence.""",
        "the-long-freeze": """The widest emptiness in the class: a pale field taking nearly the entire frame,
and across the lower third a whole army -- both armies -- held motionless in exact
faceted ice, drawn small and precise and going all the way to the edges. Every
figure caught in the position it was in. No violence, no wreckage, nothing
broken. Just a battle that has been stopped and will now be kept. One saturated
glacial blue note somewhere in the ice, used once.""",
    },
)

CLASSES["05-necromancer"] = dict(
    display="Necromancer",
    label="NECROMANCER",
    hero_who="the same man",
    hero_summary="The landscape face is Viol at rest with his ledger; the portrait face is the "
                 "thing he is famous for, calling someone back and paying for it, with the "
                 "vertical format carrying the rise out of the dark.",
    front_desc="Viol at rest with the ledger",
    back_desc="calling one back, and paying",
    style="""
Medium: Dutch vanitas in dry media -- charcoal, bone black and chalk, smudged
with the hand. Leave the fingerprints in. The surface should look worked and
reworked, with the heel of the hand visible in the darks.

Light: hard chiaroscuro from a single candle just outside the frame. Deep
swallowing shadow across roughly two-thirds of the image, and what is lit is lit
warmly and from one side only.

Composition: still-life logic even in an action shot. Objects and figures are
arranged, not caught -- placed on a surface, weighted, considered. Everything
looks posed for a portrait nobody survived.

Signature: a memento mori tucked into every single frame -- a guttering candle, a
fly on a pale surface, a tipped glass, a stopped watch, a flower already turning.
Never the focus. Always present. Put one in and do not center it.

Ground: bone white #E3DCCB for the lit passages, bitumen brown #4A3626 through
the mid-tones, violet-black #1E1526 in the shadow mass and muted gold #9A7B3A
for the one or two warm glints. No saturated color anywhere.

Register: grief-work, not villainy. Nobody in this class is enjoying this and
nobody is going to stop. Whoever is doing the work looks tired, apologetic and
entirely unstoppable, and the arithmetic of what it costs is being kept
somewhere in writing.
""",
    hero_front="""Viol at rest, the class portrait. Seated three-quarter view at a
worked wooden table in deep vanitas shadow, a heavy open ledger in front of him
and a pen still in his hand. He has stopped writing mid-column and is looking
out of the frame at nothing, with the expression of a man who has been doing
this for a very long time and has slept badly the entire time. One candle just
outside frame lights the page, his hands and one side of his face; the rest of
the room is swallowing shadow. Arranged on the table with still-life
deliberateness: a stopped watch, a tipped glass, a fly on the ledger's open page.
Fingerprints visible in the charcoal.""",
    hero_back="""An action shot, and for this class an action shot is still a
still life -- it is arranged, it is quiet, and it is enormously expensive.
Viol standing at the bottom of a tall vertical frame with both hands open and
lowered, and rising up the height of the picture out of the dark behind him, one
figure coming back: not lunging, not screaming, simply standing up out of the
shadow with a bewildered ordinary face, lit by the same single candle. Viol is
not looking at it. He is looking down at his own hands, and he is paying for
this right now. His face is grey, his shoulders are down, and he is apologizing.
The memento mori here is his own: the candle is at his elbow and it is guttering.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
dry media only — charcoal, bone black and chalk, smudged with the hand, with the
**fingerprints left in** — and hard chiaroscuro from a single candle just outside
the frame, swallowing two-thirds of every image in shadow.

Two things carry it. The first is still-life logic: even the action cards are
*arranged* rather than caught. Objects are placed, weighted and considered, and
everything looks posed for a portrait nobody survived. The second is the memento
mori — a guttering candle, a fly, a tipped glass, a stopped watch — tucked into
every single frame, never the focus and never centered, but never absent either.

The register is what keeps this class from being a villain deck, and it is in
every file: Viol is a grief-worker. Nobody in a Necromancer card is enjoying
this, nobody is going to stop, and the cost is being written down.""",
    subjects={
        "grave-salvage": """A table laid out with the effects of the recently defeated, arranged as a still
life: a dented pauldron, a bent ring, a knife with its grip worn to the shape of
a hand. A pair of tired hands is picking one item up and turning it to the
candlelight, deciding whether it can be used again. It can. A fly has settled on
the pauldron.""",
        "unwanted-gift": """A wrapped parcel being handed across a table from one pair of hands, in the
light, to another pair reaching in from the dark. It has been wrapped carefully
and tied. The giver's hands are apologetic; the receiver's are eager. What is
inside is not quite the right shape for the wrapping. A guttering candle at the
table's edge lights the exchange and nothing else.""",
        "buried-again": """A grave being closed for the second time, seen as still life rather than labor:
a spade set down and leaning, a mound of turned earth, a ledger open on the earth
with the page held flat by a stone. The entry has been ruled through. A single
figure stands at the edge of the light with his hat in his hands. A stopped watch
lies on the ledger.""",
        "called-back": """A hand rising out of dark earth into candlelight, palm open, not clawing --
asking. Another hand, living and tired, is coming down to take it. Between them,
arranged on the ground with still-life deliberateness, a spent coin, a tipped
glass and a candle burned nearly to the holder. Two-thirds of the frame is
swallowing shadow.""",
        "reclaimed-reliquary": """A small hinged reliquary casket, dented and re-soldered more than once, open on
a dark table in a pool of candlelight, with the relic inside it warmly lit in
muted gold. Somebody has repaired this thing repeatedly with visible, unhidden
work. Arranged beside it: a stopped watch, a flower already turning at the
petals.""",
        "the-ledger-reopened": """A heavy ledger opened flat and filling the frame, its columns of names dense in
the candlelight, and a tired hand drawing a line under everything spent today.
The names above the line are legible only as the shape of writing -- never
actual letters or words, only the impression of a great many entries. A fly on
the open page. Fingerprints in the charcoal all over the paper's dark edges.""",
        "successor-sought": """An old figure in the last of the candlelight holding out a pen, handle first,
toward a much younger one standing at the edge of the shadow. The younger one has
not taken it yet. Between them on the table sits the ledger, closed, and a
guttering candle with maybe a minute left in it. Still-life staging: everyone is
posed, nobody is moving.""",
        "paid-in-kind": """A settled account, arranged as vanitas: a scale on a dark table with a small
heap of coin on one pan and, on the other, something plainly worth more and no
longer of use to its owner. A tired hand rests on the table beside it, not
touching either pan. The candle is behind the scale so both pans are rim-lit and
the middle is dark. A fly on the coin.""",
        "viol-keeper-of-the-ledger": """Viol himself, the class leader, seated at his table in a three-quarter portrait
with the ledger open before him and the pen down. He is looking straight out of
the frame -- soft-spoken, apologetic, grey with tiredness and entirely
unstoppable. A single candle just outside the frame lights his hands and half his
face; behind him the room is swallowing violet-black shadow with faint standing
shapes in it that are waiting for him and are in no hurry. The memento mori sits
by his elbow: a stopped watch, and beside it one page torn out.""",
        "toll-of-three": """Three shrouded forms laid out side by side on a stone table, arranged with
absolute still-life symmetry, feet toward the viewer, lit from one side. At the
near end a fourth place is cleared and empty. A tired hand is drawing the sheet
up over the third face. Nothing is violent. Everything has been counted. A tipped
glass on the floor at the table's foot.""",
        "mass-exhumation": """A wide field of turned earth receding into the dark, dozens of shallow openings
in it, and a single small figure standing among them with a lamp -- the only warm
light in a vast violet-black frame. Where the lamplight reaches, hands and
shoulders are coming up out of the ground in unhurried numbers. It looks less
like an army rising than like a harvest being brought in, and the figure with
the lamp looks exhausted.""",
        "the-unwilling-return": """The largest and worst of the class: something coming back that did not want to,
arranged as a monstrous still life -- a huge draped form on a bier, half risen,
the sheet sliding, one enormous hand already on the stone taking weight. It has
been assembled out of more than one contributor and the joins are not hidden.
The single candle is guttering hard in the draft it is making. Below it, small,
Viol has taken his hat off.""",
    },
)

CLASSES["06-warrior"] = dict(
    display="Warrior",
    label="WARRIOR",
    hero_who="the same person",
    hero_summary="The landscape face is Hale at rest between engagements; the portrait face is "
                 "the thing they are famous for, still standing when the line has gone, with "
                 "the vertical format carrying the full height of the slab.",
    front_desc="Hale at rest between engagements",
    back_desc="still standing when the line has gone",
    style="""
Medium: shallow carved stone relief -- bas-relief chiseled into weathered
limestone. Visible tool marks, chip damage at the high points, lichen and
staining in the recesses. This is a photograph of a carved object, not a
drawing of a scene.

Light: hard raking sidelight from one side. The only thing creating form is the
shadow cast by actual physical depth in the stone. Where the carving is shallow
the form is faint; where it is deep the shadow is hard.

Composition: friezelike and frontal. Figures in profile or full-face, arranged
along a single baseline like a procession, with the ground line running the width
of the frame. Shallow depth, no perspective, no recession -- everything sits in
one plane and is stacked rather than placed behind.

Signature: zero luminous effects anywhere in this class. No glow, no particles,
no magic, no light source in frame, nothing radiant of any kind. In a game where
every other class emits something, the Warrior is the one thing that is just an
object -- and that absence is the entire read. Do not add light.

Ground: limestone buff #C9BCA4 for the stone, iron-oxide stain #7C5433 where
metal has bled into it, verdigris #5E7A66 in the weathered recesses and shadow
grey #4A443C in the cut. No saturated color, no black.

Register: dry, unimpressed, and startlingly kind to whoever is standing behind.
The repairs in the armor are old and none of them has been hidden. Nothing in
this class is dramatized; it endures, and the carving has endured too.
""",
    hero_front="""Hale at rest, the class portrait. Carved in shallow relief along
a single baseline, full figure, standing frontal with their shield grounded at
their feet and both hands resting on the rim, weight easy. The armor is old and
has been repaired many times and every repair is carved as a visible seam, patch
and mismatched plate -- nothing hidden, nothing prettied. Their face is level and
faintly unimpressed. Behind them along the same baseline, carved shallower and
smaller as a frieze does, the people they are standing in front of: ordinary,
unarmed, going about it. Hard raking sidelight, chip damage across the high
points, lichen in the recesses. No light source anywhere in frame.""",
    hero_back="""An action shot, and for this class an action shot is what is left
standing. A tall vertical slab: at the top, Hale carved full-length, frontal,
shield up and feet planted on the baseline, deeply cut so the raking light throws
hard shadow off them -- the only deep carving on the stone. Below and around,
carved shallow and half worn away, the line that did not hold: shields on the
ground, figures broken off at the ankles, a whole register of the frieze reduced
to tool marks. The slab itself is chipped and stained where the damage is worst.
Hale is not posed heroically. They are simply the part of the carving that
survived. No glow, no radiance, no light source -- just deep cuts, hard sidelight
and a great deal of weathered stone.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
shallow bas-relief chiseled into weathered limestone, with tool marks, chip
damage and lichen; hard raking sidelight where the only thing making form is the
shadow cast by real physical depth; and friezelike frontal staging along a single
baseline with no perspective and no recession.

The rule that does the most work is a prohibition, and every prompt states it in
those words: **zero luminous effects anywhere in this class.** No glow, no
particles, no magic, no light source in frame, nothing radiant at all. In a game
where every other class emits something, the Warrior is the one thing that is
just an object — and that absence is the whole read. It is also the thing an
image model will try hardest to undo, so it is repeated as an instruction rather
than a description.

The register is in every file too: nothing here is dramatized. The armor is old,
it has been repaired many times, and not one repair has been hidden — the seams
and mismatched plates are carved in.""",
    subjects={
        "break-the-line": """A shield wall in shallow relief along the baseline, and one point in it where a
single figure has got a shoulder in and levered two shields apart. The gap is
carved deeper than anything around it so the raking light throws a hard black
wedge into the frieze. Nothing else in the procession has reacted yet.""",
        "opening-guard": """Two figures on the baseline: one in front with a shield held low and to the side,
deliberately opening its own guard, and one behind stepping through the gap it
made with a short blade level. Carved as a single continuous action across one
plane, frontal and shallow, the way a frieze shows a sequence. Chip damage across
the leading shield's rim.""",
        "standing-order": """A single figure carved frontal and dead center, shield squared, feet apart on the
baseline, holding a position it has plainly been told to hold. Cut deeper than
the figures either side of it so the raking light makes it the solid thing in the
frieze. Iron-oxide staining bled down the stone from the shield's fittings.""",
        "hold-this-ground": """A ground line carved emphatically across the full width of the frame, deeper
than a baseline needs to be, and a rank of figures standing on it with shields
locked -- and nothing at all carved on the far side. The stone beyond the line is
blank, weathered and chipped. Whatever was coming is not in the picture and did
not get past.""",
        "paired-bulwark": """Two figures side by side on the baseline, shields overlapped so the two edges
read as one continuous line in the carving. They are carved at exactly the same
depth and scale -- neither is the subject. Between and slightly behind them,
carved shallow, a third much smaller figure they are jointly in front of.""",
        "shieldwall-recruit": """One young figure, alone on the baseline, holding a shield that is plainly a size
too large and holding it correctly anyway. Frontal, still, feet planted. The
armor is not old yet: it has no repairs in it, and in this class that reads as
inexperience rather than as quality.""",
        "dented-veteran": """A single figure frontal on the baseline, shield up, the shield's face carved
covered in the record of everything that has hit it -- dents, punctures, a split
riveted shut with a plate over it. The armor beneath is the same story. Deep
chip damage in the actual limestone across the shield boss, so the stone's
damage and the carved damage read as the same event.""",
        "bulwark-of-the-pass": """A single enormous figure carved frontal and filling the height of the frame,
standing in a narrow gap between two cut stone masses that close in from both
edges. There is no room to go around and the figure entirely fills what is left.
Deep cuts, hard raking shadow down one side, lichen heavy in the recesses.""",
        "unmarked-champion": """A figure carved frontal on the baseline in armor with no damage on it at all --
the cleanest surface in the class -- standing easy with the shield not yet raised.
The stone around it is weathered, chipped and stained, so the undamaged figure
reads as a deliberately preserved passage of carving. It is undamaged because
nothing has reached it yet.""",
        "hale-who-does-not-fall": """Hale themself, the class leader, carved frontal and full-length at the center of
the frieze, shield grounded, one hand out to the side and open -- steadying
someone off-frame rather than striking anyone. The armor is old and every repair
is carved visible: patches, mismatched plates, a seam across the breast where it
was split and closed. Their expression is dry and entirely unimpressed. Hard
raking sidelight, deep cut, no radiance anywhere.""",
        "rampart-captain": """A figure on a carved rampart line, turned three-quarters to speak down the row to
the ranks beside them, one arm raised not in command but in the flat gesture of
someone correcting a grip. The figures being corrected are carved shallower and
are listening. Weathering has taken the captain's face down to the barest
suggestion, which is fine: the posture carries it.""",
        "the-last-wall": """The whole width of the frame is one carved figure seen frontal, arms out, shield
enormous and taking every mark in the picture -- gouges, punctures, splits, the
limestone itself chipped away in the worst places until the relief nearly breaks
through. Behind it, carved very shallow and very small, an entire crowd of
undamaged ordinary people. It has taken everything so that register of the
frieze stayed smooth. No glow. Just stone, damage and raking light.""",
    },
)
