# -*- coding: utf-8 -*-
CLASSES = {}

CLASSES["07-wizard"] = dict(
    display="Wizard",
    label="WIZARD",
    hero_who="the same man",
    hero_summary="The landscape face is Arc at rest, which for him means an exposure still "
                 "running; the portrait face is the thing he is famous for, standing inside the "
                 "reaction rather than behind glass, with the vertical format carrying the "
                 "column of discharge.",
    front_desc="Arc at rest, the exposure still running",
    back_desc="standing inside the reaction",
    style="""
Medium: photographic, not painted. A long-exposure light-painting frame with
genuine lens artifacts -- bloom around the highlights, veiling flare across the
frame, magenta fringing at the edges of the brightest passages, and grain in the
dark. It should look like a plate that came out of a camera in a laboratory,
not like an illustration of one.

Light: the subject IS the light source and it is overexposed. A blown-out
blue-white core with all detail lost inside it, falling off fast into a very dark
plate. Nothing else in the frame is lit by anything else.

Composition: centered and radial, set against a gridded scientific plate --
ruled reference squares, fiducial marks and margin annotation in a technical
hand. The annotation is never legible as words or numbers, only the impression
of exposure data in a margin.

Signature: motion trails that record where the subject was a second ago. Every
figure and every object drags a bright continuous streak behind it through the
frame. Nothing in this class is ever still, and nothing in it is ever
photographed cleanly.

Ground: plate black #0D0F16, electric blue-white #D8ECFF at the overexposed
core, magenta fringe #D14CA8 at the highlight edges and arc orange #CE7A16 in
the warmer discharge. Very dark overall except where it is completely blown out
-- there is almost no midtone in this class.

Register: manic and unfinished. Every image is a record of an experiment already
in progress, run by someone who is not waiting for the result before starting
the next one. Nothing has been made safe. Nobody is standing behind glass.
""",
    hero_front="""Arc at rest, the class portrait, which for this man means an
exposure that is still running. Full figure, seated sideways on the edge of a
laboratory bench in a very dark room, one boot up, holding something small and
overexposed in his bare fingers and looking at it with total delight. He has
moved during the exposure: his own outline is doubled and trailing, one arm
drawn as a bright streak across the frame from where it was to where it is. He
is missing an eyebrow. The whole frame sits on a gridded plate with ruled
reference marks and illegible margin annotation. Bloom, veiling flare, magenta
fringing at every highlight edge. He is the only light in the room.""",
    hero_back="""An action shot, and for this class that means the moment the
experiment stops being contained. Arc standing at the base of a tall vertical
frame with both arms up and open, inside -- not beside -- a column of discharge
that goes from his hands to the top edge of the picture and is completely blown
out at its core. The overexposure is so total that his hands and forearms are
being eaten by it and the outline of his head is a bright smear. Enormous
magenta fringing down both edges of the column, veiling flare across the whole
plate, motion trails recording three previous positions of his arms. Low camera
looking up the column. His face, what survives of it in the exposure, is
laughing. Nobody is standing behind glass and there is no glass.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
this class is **photographic, not painted** — a long-exposure light-painting plate
with real lens artifacts, bloom, veiling flare, magenta fringing at the highlight
edges and grain in the dark. Every prompt says so in those words, because an
image model's default is to illustrate a wizard rather than photograph one.

Two things carry it. The first is the exposure: the subject *is* the light source
and it is blown out, a blue-white core with all detail lost inside it falling off
fast into a nearly black plate. There is almost no midtone anywhere in the class.
The second is the trails — every figure and object drags a bright streak from
where it was a second ago. Nothing in this class is ever still and nothing in it
is ever photographed cleanly.

Underneath sits the gridded laboratory plate with its ruled reference marks and
margin annotation, which is never legible as words or numbers — only the
impression of exposure data. And the register, in every file: this is an
experiment already in progress, run by a man who does not wait for the result
before starting the next one, and who does not delegate any of it.""",
    subjects={
        "spellsure-novice": """A student in a dark laboratory holding a small charged object at arm's length,
overexposed at the point of contact so the fingers holding it are being eaten by
the highlight. A single thin bright trail leaves the object and terminates
somewhere off to the side. The student's other arm has trailed during the
exposure and is drawn twice. Gridded plate, illegible margin annotation.""",
        "unmake-the-working": """A structure of light coming apart on the plate -- a coherent radial figure of
bright trails that has lost its center, its lines going slack and dissipating
outward, magenta fringing heavy where they fray. In the dark below, a figure
stands with one hand still raised, having just taken the thing apart. Motion
trails on the hand from three previous positions.""",
        "focused-detonation": """A single overexposed point at the exact center of the plate, so blown out that
the core is featureless white, with a hard radial burst of bright trails leaving
it in every direction and heavy veiling flare washing the whole frame. Very
dark everywhere the burst is not. One small trailing figure at the frame's edge
has been thrown backward and is drawn twice.""",
        "volatile-coil": """A tight helix of overexposed wire clamped to something in the dark, photographed
during a long exposure so the coil reads as a continuous bright spiral trail
rather than as an object. It is running hotter than its own mounting: the metal
around it glows arc orange, and magenta fringing crawls the full length of the
highlight. Grain heavy in the surrounding black.""",
        "warded-theorist": """A figure at a bench inside a spherical shell of bright trails -- a ward
photographed as a long-exposure sphere of light drawn by something that circled
him many times during the frame. He is not looking at it; he is reading. The
sphere is overexposed where the trails cross, blown white at the intersections
with magenta fringe at every edge.""",
        "wild-discharge": """A discharge that went somewhere nobody chose: a bright trail leaving frame center
in one direction, kinking hard twice, and terminating on something at the plate's
edge that is not the subject. Overexposed at both ends, fringing along its whole
length. The dark middle of the plate is full of grain and gridded reference
marks. Nothing here was aimed.""",
        "arc-who-does-not-delegate": """Arc himself, the class leader, centered and radial in the frame, both hands
apart and holding a working between them that is completely blown out -- the core
is featureless white and it is consuming the detail of his fingers. He has moved
during the exposure and his head is drawn one and a half times. Missing an
eyebrow, grinning, wholly absorbed. Behind him the laboratory is black and empty:
nobody else is in the room, because he has never once handed one of these to
anybody. Ruled plate grid, illegible exposure data in the margin.""",
        "recovered-formula": """A page of working recovered from somewhere it should not have survived, lying
on a gridded plate and lit only by the overexposed thing it describes hovering
above it. The writing on the page is never legible as letters or numbers -- only
the impression of dense notation. Bright trails loop from the page to the object
and back, recording something that has been read more than once.""",
        "second-detonation": """The same burst twice: two overexposed radial cores on one plate, offset from each
other, their trails overlapping into a lattice of blown-white intersections. The
first is already dissipating into flare; the second is at full brightness. Very
dark elsewhere, heavy grain, magenta fringing wherever the two fields cross.""",
        "sudden-postulate": """Something arriving faster than the exposure could follow: one enormously long
bright trail entering at the top left edge of the plate and terminating in an
overexposed figure at bottom right that is only half resolved, still smearing.
The trail is the subject; the figure is where it stopped. Veiling flare across
the lower third. Nothing else in frame.""",
        "costly-proof": """A demonstration that worked, photographed from behind the bench: an enormous
overexposed core at the center, and in the dark foreground the silhouettes of
two pieces of apparatus that have been spent doing it -- one collapsed, one
still trailing sparks as bright streaks toward the floor. The proof is legible
and the price is in the foreground. Heavy fringing, heavy grain.""",
        "the-unnamed-reaction": """The largest plate in the class and the least contained: an overexposed field
occupying most of the frame with no discernible center, its trails going out
past all four edges rather than terminating, magenta fringing along every one of
them and veiling flare washing the gridded plate almost blank. At the very bottom
of the frame, tiny and dark, the silhouette of one man with his arms still up.
It has no shape a diagram could hold and it is not slowing down.""",
    },
)

CLASSES["08-shaman"] = dict(
    display="Shaman",
    label="SHAMAN",
    hero_who="the same person",
    hero_summary="The landscape face is Ash at rest on the mountain's flank; the portrait face is "
                 "the thing they are famous for, standing in the eruption because it is a "
                 "season, with the vertical format carrying the column of ash.",
    front_desc="Ash at rest on the mountain's flank",
    back_desc="standing in the eruption",
    style="""
Medium: ochre-and-charcoal cave painting on rough rock. Ritual pigment -- red
ochre, charcoal, white clay -- blown through a tube, hand-pressed and finger-drawn
rather than brushed. Marks are simple, confident and slightly irregular, made by
someone who was not trying to draw well.

Light: flickering and warm, as if a torch were being held at arm's length just
outside the frame. Deep natural pitting in the stone catches real shadow, so the
lighting belongs to the rock rather than to the picture painted on it.

Composition: simplified, powerful animal and figure forms, overlapping each
other without perspective, at different scales and orientations because they were
added at different times. Hand stencils in the margins.

Signature: deliberately the most primitive-looking cards in the game. The rock's
grain, cracks and irregular surface show through every mark and interrupt the
forms -- the surface is half the image. Never smooth, never rendered, never
digital.

Ground: red ochre #A8442A and charcoal #2A2420 for the marks, white clay #DCD3BE
for the stencils and highlights, basalt #4E4A46 for the rock itself. No
saturated color, no black beyond the charcoal, no rendering of any kind.

Register: fire and growth are one cycle seen at two points, and nobody here is
alarmed by either. The eruption and the orchard are the same process with a gap
in the middle. Ritual-minded, unhurried, treating catastrophe as a season that
will pass.
""",
    hero_front="""Ash at rest, the class portrait. A single standing figure painted
large on a rough rock face in red ochre and charcoal, arms slightly out and
palms forward, facing the viewer -- the posture of someone presiding rather than
fighting. Painted around and overlapping them at other scales and other angles,
plainly added at other times: a mountain in outline, animals moving downhill, a
row of young trees, and the same mountain again with the trees on it. Hand
stencils in white clay along the margins, one of them smaller than the rest. The
stone's cracks run straight through the figure and are not worked around. Torch
light from outside the frame catching the pitting.""",
    hero_back="""An action shot, and for this class an action shot is a season
arriving. A tall vertical rock face: at the top, the mountain opened, painted as
a huge charcoal-and-ochre column of ash going up past the frame edge and spreading
where it meets the top; below it, the flank painted in falling ochre with animals
in flight; and at the bottom, painted small and dead center and absolutely
unhurried, Ash standing with both arms raised, facing into it. The column is not
painted as an attack. It is painted the way the seasonal marks around it are
painted. Handprints in white clay across the base of the column, one of them
fresh. The rock is deeply pitted here and the torch light throws real shadow into
the pits, breaking the ash column into fragments.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
ritual pigment on rough rock — red ochre, charcoal and white clay, blown and
hand-pressed rather than brushed — lit by a torch held at arm's length outside the
frame, so the deep pitting in the stone catches real shadow. The lighting belongs
to the rock, not to the picture on it.

Two things carry it. The first is that this is **deliberately the most primitive
work in the game**: simplified forms overlapping without perspective, at different
scales and orientations because they were added at different times, with hand
stencils in the margins. Nothing is rendered and nothing is smooth. The second is
the surface — the rock's grain and cracks run straight through every mark and
interrupt the forms rather than being worked around. The surface is half the
image, and every prompt says so.

The register is the class's whole argument and it is in every file: the eruption
and the orchard are one process with a gap in the middle. Nobody in a Shaman card
is alarmed by fire or by growth, because they are the same season observed at two
different points.""",
    subjects={
        "ash-fed-salve": """A cupped pair of hands holding a smear of grey paste, painted large in charcoal
outline with the paste itself in white clay, and beneath the hands a small figure
painted with new marks over old worn ones -- visibly repainted, visibly stronger
for it. Hand stencils in the margin. A crack in the rock runs through the wrist
and is left alone.""",
        "fallow-offering": """A field left deliberately unpainted: a large bare patch of raw pitted rock in
the middle of the frame with ochre marks crowding all around its edge and none
inside it. At the patch's rim, a small figure setting something down and walking
away. What was given up here is what makes the surrounding marks so dense.""",
        "seedbearer": """A single small figure in red ochre carrying a bulging pouch at the hip, walking
across the frame in profile, and trailing behind it in white clay a scatter of
dots that become, further back, three simple upright tree shapes. It is drawn
smaller than the trees it left. The dots run over a fissure in the rock.""",
        "ashling-herald": """A running figure in charcoal, arms out, mouth open in a simple painted O,
overlapping a much larger and much older painted animal that it is running away
from -- or toward, the marks do not say. Grey handprints in white clay follow it
across the rock, getting fainter. Deep pitting takes a bite out of its legs.""",
        "cinder-rite": """A ring of small ochre figures painted around a central charcoal blot, all facing
inward, none of them detailed beyond a head and two arms. The blot at the middle
is thick, finger-smeared and still spreading into the rock's grain. Above the
ring, painted at a different scale and clearly at a different time, the same ring
again with a tree in the middle instead.""",
        "everything-feeds": """A dense overlapping tangle of animal forms in ochre and charcoal at several
scales, some upright and some sideways, drawn over each other until it is not
clear where one ends -- and running through them all, painted last and in white
clay, a single continuous line that connects every mouth to every body. Hand
stencils crowded into every margin.""",
        "magma-tender": """A crouching figure in profile, close to the ground, one hand down flat on a
charcoal seam that runs across the rock and glows red ochre where the hand
touches it. The figure's posture is entirely relaxed. Behind it, painted small,
three young trees in white clay standing on the same seam further along.""",
        "eruption-warden": """A large heavy figure painted frontal and squared with arms wide, standing across
a painted fissure that runs the width of the frame and is filled with thick red
ochre. It is not blocking the fissure. It is standing over it the way a person
stands over a fire they are responsible for. The rock's own crack runs into the
painted one and continues it.""",
        "orchard-of-cinders": """A row of simple upright tree shapes in white clay and ochre painted directly on
top of an older, darker charcoal layer of burned stumps -- the earlier marks still
visible through the newer ones, not scraped away. The new trees are painted
larger than the old stumps were. Torch light rakes across the pitting.""",
        "ash-who-tends-the-mountain": """Ash themself, the class leader, painted large and frontal on the rock in red
ochre with charcoal outline, one hand raised palm out and the other resting on
the painted line of the mountain beside them -- the gesture of an owner rather
than a supplicant. Around and overlapping them at other scales and other angles:
the mountain smoking, animals coming downhill, a stand of young trees on the same
slope. They are entirely unhurried. White clay hand stencils in the margins, and
the rock's cracks run straight through the figure.""",
        "twin-eruption": """Two charcoal columns going up from two points on a painted ridge, drawn at
different scales because they were painted at different times, their ash spreading
into one another at the top of the frame. Beneath each, in ochre, the same small
row of trees. Deep pitting in the rock breaks both columns into fragments and
neither has been worked around.""",
        "the-mountain-is-fertile": """The whole rock face given to one image: an enormous painted mountain in charcoal
occupying the full frame, its flanks in red ochre, opened at the summit with ash
going out past the top edge -- and painted directly over the whole of it in white
clay, at the same scale and with the same weight, an orchard in full leaf. The
two images are not layered as before-and-after; they are the same painting. Hand
stencils across the base. The stone's grain runs through everything.""",
    },
)

CLASSES["09-trinket-mage"] = dict(
    display="Trinket-mage",
    label="TRINKET-MAGE",
    hero_who="the same man",
    hero_summary="The landscape face is Quench at rest among his own inventory; the portrait face "
                 "is the thing he is famous for, standing inside a rig that is running past its "
                 "tolerances, with the vertical format carrying the pressure column.",
    front_desc="Quench at rest among his inventory",
    back_desc="inside a rig running past tolerance",
    style="""
Medium: an exploded-view patent plate on aged drafting paper. Isometric technical
illustration -- parts floating apart along thin straight leader lines with
numbered callout bubbles -- but the metal itself is rendered as real material:
brass with genuine specular hits, copper going warm, cold-sweating steel with
beads of condensation on it.

Light: schematic flatness for the linework, real speculars on the metal. The
drawing is a document; the machine described in it is an object. Both readings
have to hold at once.

Composition: blueprint ground with white line, plus a second annotation layer in
heat orange marking every point where fire meets frost. Condensation, escaping
steam and dripping meltwater are drawn with exactly the same technical precision
as the parts -- ruled, sectioned and called out, not atmospheric.

Signature: dream-punk, not steampunk. Every diagram is plausible right up until
it isn't. The tolerances are believable, the callouts are numbered, the fasteners
are correct -- and the machine as drawn could not possibly work. Precise, warm,
and slightly absurd given what these things do.

Annotation: callout numbers, dimension arrows and margin notes are present
everywhere, but they are never legible as actual letters or numerals -- only the
convincing impression of a numbered technical document.

Ground: drafting blue #1B3A6B for the plate, white line #EFF4FA for the drawing,
brass #C9A227 and copper #B87333 for the rendered metal, heat orange #E8811C for
the second annotation layer. Restrained -- the plate reads cool and the metal
reads warm.

Register: a tinkerer's optimism. Everything here was built by someone with singed
fingertips and full pockets who is genuinely pleased with how it came out. His
power is inventory, not talent, and that does not bother him nearly as much as it
should.
""",
    hero_front="""Quench at rest, the class portrait, drawn as the assembly page of
his own patent. He sits three-quarter view on a crate at the center of the
plate, entirely relaxed, one boot up, holding a small brass device in both hands
and looking at it fondly. Everything he owns is exploded around him along thin
leader lines with numbered callouts -- gauges, valves, a coil, three unmatched
gauntlets, a kettle, spare glass, a great deal of copper pipe -- floating in
isometric order against the drafting-blue ground. The devices are rendered as
real brass and cold-sweating steel while he himself is drawn in white line like
a component. Heat-orange annotation marks every joint where hot meets cold. He
is a part in his own exploded view, and the callout for him is not larger than
the others.""",
    hero_back="""An action shot, and for this class an action shot is a pressure
event with the tolerances still called out. A tall vertical plate: at the bottom,
Quench braced with both hands on the control yoke of a rig that runs the full
height of the frame above him -- a column of brass, copper and cold-sweating steel
venting hard at three points. The steam and the frost plume are drawn with the
same ruled technical precision as the metal, sectioned and numbered. Dimension
arrows across a joint that is visibly opening. The heat-orange annotation layer
is everywhere at once because hot is meeting cold along the entire column.
Leader lines still point neatly to parts that are in the act of leaving the
assembly. He is grinning. The document is immaculate and the machine is not going
to hold.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
an exploded-view patent plate on aged drafting paper — isometric, parts floating
apart along thin leader lines with numbered callouts — with the metal rendered as
real material. Brass takes genuine specular hits, steel sweats, copper goes warm.
The drawing is a document and the machine in it is an object, and both readings
have to hold at once.

Two things carry it. The first is that steam, condensation and meltwater are
drawn with **the same technical precision as the parts** — ruled, sectioned and
called out rather than painted in as atmosphere. The second is the class's own
phrase for itself: dream-punk, not steampunk. Every diagram is plausible right up
until it isn't. The tolerances are believable, the fasteners are correct, and the
machine as drawn could not possibly work.

Annotation appears on every card and is never legible — callout numbers,
dimension arrows and margin notes give the convincing impression of a numbered
technical document without resolving into letters or numerals. Underneath is the
register: this is inventory, not talent, built by a man with singed fingertips
who is genuinely pleased with how it came out.""",
    subjects={
        "overpressure-fitter": """A pressure fitting exploded along its axis -- cap, spring, seat, body -- with the
spring drawn compressed well past where the dimension arrows say it should sit.
Heat-orange annotation rings the seat. A gloved hand at the plate's edge is
tightening it further. Condensation beading on the body, drawn as ruled droplets
with their own callout.""",
        "parts-requisition": """A storage rack drawn in isometric section, its pigeonholes each containing a
different fitting rendered in brass and copper, every one with a numbered callout
bubble on a leader line. One hole is empty, and a hand is reaching in for the
part that belongs in it -- which is drawn separately, floating, at the plate's
edge, already found.""",
        "pressure-tap": """A tap clamped onto a much larger pipe, exploded to show the piercing valve
inside it, with a thin copper line leading away off the plate. The main pipe is
cold-sweating steel; the tap body is brass and hot. Heat-orange annotation at the
join, ruled condensation on one side of it and ruled steam on the other, both
called out.""",
        "stripped-for-parts": """A device drawn mid-disassembly and not politely: the exploded view has gone
further than an exploded view should, fasteners floating loose in no order,
one leader line pointing to a part that has already been taken away and is drawn
as an empty numbered bubble. A pair of pliers rendered in real steel lies across
the plate.""",
        "valve-technician": """A figure drawn in white line like a component, standing in isometric at a bank of
four valves rendered in brass, with one hand on the second wheel. Each valve has
its own callout and its own small heat-orange marking. A pressure gauge above the
bank is drawn twice, at two different readings, on the same plate.""",
        "bulk-fitting": """A single oversized coupling drawn large and central, exploded into far more
components than a coupling should have -- eleven numbered parts for a joint that
needs three -- with every one of them rendered in convincing brass and correctly
threaded. The dimension arrows are consistent. The assembly is absurd. Heat-orange
annotation on the inner seat.""",
        "modular-frame": """A wearable frame drawn in full isometric exploded view: a harness with mounting
points along both arms and the spine, and floating away from each point on a
leader line a different attachment -- a clamp, a nozzle, a coil, a shield plate.
Every mount is the same standard fitting, which is the joke and also the point.
Numbered callouts throughout.""",
        "countermeasure-rig": """A shoulder-mounted rig drawn in section as well as exploded, showing a frost
chamber and a fire chamber sharing one wall, with the heat-orange annotation layer
running the length of that wall. Condensation beads down the cold side and is
ruled and called out; scorch discoloration is dimensioned on the hot side. The
shared wall's thickness has an arrow and a tolerance on it that is plainly too
small.""",
        "requisition-clamp": """A heavy brass clamp shown open and shown closed on the same plate, with a leader
line between the two states. What it is closing on is drawn as a dotted outline
only -- the part is somebody else's and is not specified. The clamp is beautifully
made. Numbered callouts, dimension arrows, a small heat-orange note at the jaw.""",
        "quench-all-pockets-full": """Quench himself, the class leader, drawn at the center of his own patent plate in
white line while everything on him is rendered as real material: brass at the
belt, copper coiled over one shoulder, cold-sweating steel canisters in every
pocket, a gauge strapped to the back of one glove. He is exploded outward along
leader lines like his own assembly diagram, every pocket's contents floating in
numbered isometric order around him. Singed fingertips. Entirely pleased with
himself. Heat-orange annotation wherever two of his own devices touch.""",
        "borrowed-apparatus": """A device drawn as belonging to two plates at once: the left half rendered in one
hand's brass and callout style, the right half in another's, the leader lines
from each side meeting in the middle and disagreeing about the numbering. A
gloved hand is unbolting the far side's mounting. Heat-orange annotation along
the seam where the two documents meet.""",
        "total-systems-failure": """The whole plate failing at once: a full assembly drawn in exploded isometric with
every single leader line still neatly ruled to its numbered callout, while the
parts they point to are venting, splitting, frosting over and coming apart
simultaneously. Steam and frost plumes drawn with full technical precision,
sectioned and dimensioned. Heat orange over the entire drawing rather than at
marked points. The document remains immaculate. Nothing in it survives.""",
    },
)

CLASSES["10-warlock"] = dict(
    display="Warlock",
    label="WARLOCK",
    hero_who="the same man",
    hero_summary="The landscape face is Brand at rest, mid-negotiation and charming about it; "
                 "the portrait face is the thing he is famous for, the page burning through "
                 "while he keeps talking, with the vertical format carrying the fire going up "
                 "the margin.",
    front_desc="Brand at rest, mid-negotiation",
    back_desc="the page burning through mid-sentence",
    style="""
Medium: a scorched illuminated manuscript. Blackletter marginalia and gold
rubrication on vellum -- and then burned. Charred edges, holes eaten right
through the page, and the illustration continuing around the damage as though the
damage had always been part of the design.

Light: flat medieval illumination with no modelling and no cast shadow, undercut
by real scorch shadow where the page has curled and lifted away from the plane.
The only three-dimensional thing in the image is the burning.

Composition: text-block logic. The figure occupies a historiated initial capital
or lives in the margin, with grotesques and small demons crawling the border and
climbing the ascenders. Register lines and a ruled text block are visible
underneath everything.

Signature: annotations in a second, later hand -- red ink corrections and marginal
marks made by somebody who read this page after Brand did and was alarmed by it.
The two hands should be distinguishable at a glance.

Lettering: text blocks, marginal notes and the initial's own body carry the
convincing texture of blackletter and of a later annotating hand, but no
character is ever legible as an actual letter or word. Impression of writing
only.

Ground: vellum cream #E4D9BE, iron-gall black #241E1A for the main hand, minium
red #C8342B for the rubrication and the alarmed later hand, gold #C9A227 for the
leaf, and char #2A211C at every burned edge.

Register: charm that is visibly load-bearing. Everybody in this class is being
generous with something that is not theirs yet, and doing arithmetic behind their
eyes the entire time. Fire and shadow both take payment in advance.
""",
    hero_front="""Brand at rest, the class portrait. He fills a large historiated
initial at the left of a ruled text block, seated, leaning back, one ankle over
the other, with both hands open in the universal posture of a man explaining
that this is a very good deal. Flat medieval illumination, gold leaf on the
initial's ground, no modelling anywhere. Grotesques and small well-dressed demons
crawl the border and climb the initial's ascender; two of them are holding a
scroll he has already signed. The lower right corner of the page is charred and
a hole is eaten through it, and the illumination simply continues around the
hole. In the margin, in a second and later hand, minium-red marks by somebody
who has read this and is alarmed. Brand is charming. The charm is load-bearing.""",
    hero_back="""An action shot, and for this class an action shot is a bill coming
due mid-sentence. A tall vertical page: Brand stands in the lower third still
mid-gesture, still talking, still generous -- and above him the page itself is
burning, the fire eating up the margin and through the text block toward the top
edge, holes opening in the vellum, the illumination continuing gamely around each
one. Grotesques flee up the ascenders ahead of the burn. The gold leaf blisters.
Where the char reaches the ruled lines, the second later hand's red annotations
are the last thing legible before the page goes. He has not stopped explaining.
The scorch shadow where the vellum curls is the only three-dimensional thing in
the picture.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
blackletter marginalia and gold rubrication on vellum, **then burned** — charred
edges, holes eaten through the page, and the illumination continuing around the
damage as though the damage had always been part of the design. Flat medieval
illumination with no modelling anywhere, undercut by real scorch shadow where the
page has curled. The burning is the only three-dimensional thing in the image.

Two things carry it. The first is text-block logic: the figure lives inside a
historiated initial or out in the margin, with grotesques and small demons
crawling the border and climbing the ascenders, and ruled register lines visible
under everything. The second is the second hand — red-ink corrections and marginal
marks made by somebody who read the page after Brand did and was alarmed by it.
The two hands are distinguishable at a glance, and one of them is worried.

No lettering ever resolves. The blackletter and the annotating hand carry the
texture of writing without a single legible character. And the register is in
every file: everyone here is being generous with something that is not theirs
yet, and doing arithmetic behind their eyes the whole time.""",
    subjects={
        "first-instalment": """A small demon in the margin holding out a purse with one hand and, with the
other, already taking something from a figure who has not noticed. Flat gold
ground, no modelling. The first payment is drawn as coins going one way and the
figure's shadow -- the only shadow on the page -- going the other. Char along the
margin's outer edge. Red marks in the later hand beside the purse.""",
        "small-mercy-larger-debt": """A historiated initial in which one figure lifts another out of water, drawn with
genuine tenderness in flat illumination and gold leaf -- while in the border
directly beneath, a small demon is neatly entering the transaction in a book. The
rescue is the picture; the accounting is the ornament. A burn hole through the
border eats the book's lower corner.""",
        "creditors-draw": """A hand reaching across a ruled text block to draw a card from a fanned deck held
by a figure in the opposite margin, who is smiling and letting it happen. Gold
leaf on the deck. In the border, three grotesques are drawing cards from each
other in a chain that goes round the whole page. Alarmed red marks in the later
hand at the point the chain closes.""",
        "read-the-terms": """A very long unrolled scroll drawn winding down the entire margin and around the
foot of the page, covered in the texture of dense blackletter that never resolves
into words, with one small clause near the bottom marked in minium red by the
later hand and circled twice. A figure at the top of the page is reading from
the wrong end. Char eating the scroll's tail.""",
        "recalled-from-default": """A figure being pulled back into a historiated initial that it had clearly left --
half in the letter, half in the margin, with a chain from the initial's ground
around one ankle. Flat illumination, gold leaf, no modelling. The margin around
it is heavily charred and a hole is eaten through where the figure had been
standing.""",
        "collateral-clause": """A small, beautifully illuminated pledge scene in a bottom-margin roundel: a
figure handing over something precious with both hands, held with genuine care by
the receiver, and gold leaf on the object itself. The roundel's border is
grotesques. Directly through the roundel's lower edge, a burn hole -- and the
illumination continues around it as though it had always been designed that
way.""",
        "interest-on-every-spell": """A page where the marginal demons have got into the working: a ruled text block of
illegible blackletter with a small red-inked figure sitting on every line's end,
each one taking a small toll from the words as they pass. Gold rubrication at the
line starts. The later hand has written alarmed marks the whole length of the
outer margin.""",
        "settled-in-blood": """A settlement scene in flat medieval illumination: two figures shaking hands
across a ruled block, one of them bleeding freely into a bowl held by a grotesque
below, the blood drawn in minium red as ornament rather than as gore. Neither
face registers distress. Char and a burn hole directly beneath the bowl, the
illumination continuing around it.""",
        "brand-several-deals-deep": """Brand himself, the class leader, standing in the margin rather than in the
initial -- he has come out of the text block -- with one hand out in a warm
persuasive gesture and the other behind his back holding three separate signed
scrolls he is not mentioning. Flat illumination, heavy gold leaf, no modelling.
Grotesques and small demons swarm the border around him, several of them holding
documents that name him. The page is charred along its whole right edge and two
holes are eaten through it. Alarmed red annotations in the later hand crowd the
margin beside his head.""",
        "three-sold-at-once": """A bottom-margin scene of three separate transactions being conducted
simultaneously by the same pair of hands, drawn as three roundels chained
together with the chain passing through all three. Gold on each roundel's ground.
The chain's last link goes off the page's charred edge. The later hand has ruled
a red line through the middle roundel.""",
        "nothing-down": """A magnificent illuminated gift being handed over free: gold leaf laid thick, a
grand figure receiving with both hands, flat and joyful and entirely
unshadowed -- and directly below the gift, in the border, the burn has already
started, a ring of char eating outward through the vellum toward the scene. The
illumination continues around it. Red marks in the later hand: two strokes, hard.""",
        "the-balance-comes-due": """The whole page against the reader: a full-page illumination in which the border
grotesques have left the border and come inward across the text block, dozens of
them, each carrying a document, all converging on one figure at the center who
still has one hand raised as though about to make a further offer. Gold leaf
blistering. Char eating in from all four edges at once and holes through the
page in three places. The later hand's red annotation covers what margin is
left.""",
    },
)

CLASSES["11-demon-hunter"] = dict(
    display="Demon Hunter",
    label="DEMON HUNTER",
    hero_who="the same person",
    hero_summary="The landscape face is Kell at rest, which is as still as this class ever gets; "
                 "the portrait face is the thing they are famous for, spending the borrowed "
                 "power all at once, with the vertical format carrying the drop.",
    front_desc="Kell at rest, as still as this class gets",
    back_desc="spending the borrowed power all at once",
    style="""
Medium: ukiyo-e woodblock print. Flat color fills with visible woodgrain running
through them, hard spot-blacks, and keyblock outlines of varying weight -- plus
dense parallel hatching borrowed from horror manga wherever the shadow gets bad.
Registration is very slightly off in places, as a real print's is.

Light: no gradients anywhere. Light is a shape you cut, not a falloff you render.
Every value in the image is a flat area with a hard edge.

Composition: aggressively diagonal and off-balance. The frame is entered from a
corner, the horizon is tilted, and kinetic speed-lines and impact bursts break
the frame edge and run off it.

Signature: every composition is mid-motion and slightly unstable -- this is the
class that never has its feet under it. No card in this class shows a figure at
rest on both feet on level ground.

Ground: indigo #26355C and bone #E8DFCB carry the flats, vermilion #C8342B is the
one hot note, and block black #141210 is used only as cut spot-blacks, never as
shading. Restrained -- three or four flats per image at most.

Register: on a clock nobody else can see. The deal is already done, the power is
borrowed and the price is not negotiable, and none of that is drawn as sorrow --
it is drawn as speed. Grim, fast, unexpectedly funny, refusing to plan past the
current month.
""",
    hero_front="""Kell at rest, the class portrait, which for this class means the
one moment they are not already moving. Full figure on a tilted ground plane,
weight hard on the back foot and one shoulder dropped, blade low, caught in the
half-second before going -- not standing. Flat woodblock fills with visible grain,
hard keyblock outline, dense horror-manga hatching packed into the shadow along
one whole side of the body where the borrowed thing lives. Indigo and bone flats,
one vermilion note at the eye. Speed-lines already entering the frame from the
lower corner even though nothing has moved yet. Slightly off-register, so a thin
vermilion ghost sits beside the keyline.""",
    hero_back="""An action shot, and this class's action shot is the whole class:
spending it all at once with no plan for after. A tall vertical print, entered
from the top corner -- Kell coming down through the frame headfirst-diagonal, blade
extended, both feet off the ground and nothing beneath them, the ground plane
visible only as a tilted band at the very bottom. Kinetic speed-lines rake the
full height of the picture and run off all four edges. The horror-manga hatching
has taken the entire lower half of the body into dense black, and where the
borrowed power is working it has been cut away to bone-white flat with a hard
edge. One vermilion note, at the point of the blade. Off-register, grain in every
fill. Nothing in this picture has its feet under it, least of all Kell.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
woodblock print — flat color fills with visible grain, hard spot-blacks, keyblock
outlines, slightly imperfect registration — with dense parallel hatching borrowed
from horror manga wherever the shadow gets bad. **No gradients anywhere.** Light
here is a shape you cut, not a falloff you render, and every prompt says it in
those words.

Two things carry it. The first is instability: every composition is aggressively
diagonal, entered from a corner, on a tilted ground plane, with speed-lines and
impact bursts breaking the frame edge and running off it. No card in this class
shows a figure at rest on both feet on level ground — this is the class that never
has its feet under it. The second is restraint in the palette: three or four
flats per image, indigo and bone doing the work, block black used only as cut
spot-blacks and never as shading, and **one** vermilion note.

The register is in every file: the deal is already done and the clock is already
running, and none of that is drawn as sorrow. It is drawn as speed.""",
    subjects={
        "fury-vent": """A vent opening in armor plate at the shoulder, cut as a hard bone-white shape
against indigo flat, with pressure escaping it in flat cut shapes rather than in
any gradient. The wearer is already turning into the release, off-balance, one
foot leaving the tilted ground. Speed-lines from the vent break the top frame
edge. One vermilion note inside the opening.""",
        "goading-scout": """A small figure sprinting across a steeply tilted ground plane, looking back over
one shoulder and shouting, with one arm flung out pointing behind at whatever it
has just successfully annoyed. Nothing else is in frame. Flat indigo ground,
bone figure, heavy speed-lines running off both side edges. The pointing hand is
vermilion.""",
        "no-time-to-wait": """A figure entering the frame from the top-left corner already at full speed, drawn
so far into the diagonal that the composition has no vertical in it at all. Both
feet off the ground, cloak cut into three hard flat shapes. Impact burst at the
bottom right where it is about to arrive, breaking the frame edge. Dense hatching
under the jaw.""",
        "impossible-choice": """Two hard-edged paths cut into the print as flat shapes diverging from a single
point at the bottom of the frame, one indigo and one bone, with a figure standing
at the fork -- and even here the ground is tilted and the figure's weight is
already committed to one side. Speed-lines only on the side it is falling toward.
A vermilion mark at the fork itself.""",
        "leaping-stalker": """A long low body at the apex of a leap, fully extended across the diagonal of the
frame, no ground visible anywhere in the picture. Flat fills with heavy grain,
keyblock outline breaking where the speed is greatest. Horror-manga hatching packs
the underside of the body into near-black. Impact burst waiting at the far
corner.""",
        "vanguard-doctrine": """Three heavy figures cresting a tilted ridge line together, all in mid-stride and
none with both feet down, arranged along the diagonal so the composition tips
hard to one corner. Flat indigo silhouettes with bone cut into the leading edges.
Speed-lines behind all three, running off the frame. One vermilion note on the
foremost.""",
        "kell-on-a-clock": """Kell themself, the class leader, coming across the frame on the diagonal with
the blade already out and the ground plane tilted well past level -- mid-stride,
weight thrown forward, nothing under the leading foot yet. Flat woodblock fills,
hard keyblock line, dense horror-manga hatching taking one entire side of the
body where the borrowed power sits. Slightly off-register so a vermilion ghost
edge runs beside the keyline. Speed-lines break three of the four frame edges.
One vermilion note at the eye. Grim, fast, and faintly amused.""",
        "pouncing-reaver": """A figure dropping onto its target from above, drawn at the top of the frame with
the target's bone-white flat shape at the bottom, the whole composition a single
falling diagonal. Impact burst already cut into the print where they will meet,
breaking the lower frame edge. Heavy hatching along the falling body's underside.
One vermilion note.""",
        "kell-borrowed-power": """Kell again, later: the same figure with more of the borrowed thing showing.
Mid-motion on a tilted plane, one arm and one whole flank now cut as flat
block-black with hard edges where flesh should be, the hatching around the
boundary at its densest. Their face is unchanged and entirely calm about it.
Speed-lines from the changed side only. Off-register vermilion ghost along the
whole silhouette.""",
        "twinned-assault": """Two figures moving as one along a single steep diagonal, so close their flats
overlap and the keyblock outline between them has been left out -- they read as one
shape with two heads. Neither has a foot down. Speed-lines rake the whole frame.
Hatching where the shapes cross. One vermilion note, shared between them.""",
        "unspent-momentum": """A figure that has already landed a blow and is using the recoil to launch again,
drawn as two overlapping positions on one print, the earlier one slightly
off-register in vermilion behind the later one. The tilted ground appears only in
the bottom corner. Impact burst behind, speed-lines ahead, both breaking the
frame edge.""",
        "nothing-left-standing": """The most unstable print in the class: a full-frame diagonal of destruction with a
single figure at its head, mid-stride and airborne, and behind it a field cut
into flat shapes of what used to be standing -- every one of them broken off the
vertical and falling in the same direction. Speed-lines run off all four edges.
Block-black spot shapes where the hatching gives out entirely. One vermilion note,
far back, small, at the beginning of the line.""",
    },
)
