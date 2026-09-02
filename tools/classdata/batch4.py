# -*- coding: utf-8 -*-
CLASSES = {}

CLASSES["17-witch-doctor"] = dict(
    display="Witch Doctor",
    label="WITCH DOCTOR",
    hero_who="the same person",
    hero_summary="The landscape face is Mire at rest among the jars; the portrait face is the "
                 "thing they are famous for, a cure nobody consented to working anyway, with "
                 "the vertical format carrying the bloom going up the body.",
    front_desc="Mire at rest among the jars",
    back_desc="a cure nobody consented to, working",
    style="""
Medium: bio-culture bloom over batik. Actual growth patterns -- mold colonies,
bacterial culture, spreading rings and fractal branching, irregular and never
repeating -- laid over hand-dyed wax-resist cloth with the characteristic crackle
where the wax broke and the dye got in.

Light: damp and ambient, like a cellar. Nothing casts a clean shadow because
nothing in this image has a clean edge. No highlight, no direction, no sun.

Composition: colonization. Growth radiates outward from a single point of
infection somewhere in the frame and everything else in the picture is arranged by
how far it has got. The composition is the spread, not the subject.

Signature: not one straight line anywhere in this class. No ruled edge, no
architectural line, no straight tool, no square corner. Where every other style
in the game has an edge, this one has a bloom. Check the whole frame for straight
lines and remove them.

Ground: swamp green #3E5B2E and bruise purple #6B3A72 in the colonies, mud ochre
#8A6A38 in the cloth, bone #D8CFB8 where the culture has not reached. Damp,
desaturated, with the wax crackle visible through everything.

Register: rot is growth pointed the other way, and nobody here understands why
that upsets people. No bedside manner and a spotless success rate. Whatever is
being done in this picture is working, and the patient was not consulted.
""",
    hero_front="""Mire at rest, the class portrait. A single seated figure at the
center of a batik field, surrounded by jars -- dozens of them, on shelves and on
the floor, each holding something, each labelled with a mark that never resolves
into readable letters. The figure is drawn in the same bio-culture logic as
everything else: their outline is a colony boundary rather than a line, blooming
outward at the shoulders into the cloth. They are looking directly out at the
viewer with total professional calm and no warmth at all. Wax crackle runs
through the whole picture. Growth radiates from the jar in their lap. Not one
straight line anywhere -- not in the shelves, not in the jars, not in the room.""",
    hero_back="""An action shot, and for this class an action shot is a cure taking
hold in somebody who did not agree to it. A tall vertical batik: at the bottom, a
figure laid out, and at the point where Mire's hand rests on their chest, the
infection begins -- and from there it goes up the whole height of the frame, a
bloom of swamp green and bruise purple colonizing the body, the cloth and the
picture together, radiating in irregular fractal rings that get thinner and paler
toward the top edge. The wound at the center is already closed and clean. Mire is
crouched beside them, one hand down, watching the spread the way a person watches
water boil. Nothing here has a clean edge and nothing casts a clean shadow. Not
one straight line in the frame. It is going to work.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
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
consulted.""",
    subjects={
        "poultice-bearer": """A figure carrying a wide shallow bowl of grey-green culture in both hands, moving
across a batik field, the bowl's contents already spilling over the rim and
blooming down the front of their clothing in irregular rings. The bowl's own
outline is a colony edge rather than a drawn curve. Wax crackle throughout.""",
        "unpleasant-remedy": """A cup being held to a mouth that is not opening willingly. What is in the cup is
alive: a dense fractal colony pressing up against the rim. Around the point where
cup meets lip, the bloom is already spreading outward across the face and into the
cloth. Nobody in the frame is being cruel and nobody is being gentle either.""",
        "fever-nurse": """A figure standing over another and drawing something out of them: the colony that
was radiating across the patient is visibly reversed, its rings contracting toward
the nurse's hands, and where it arrives on the nurse's forearms it is beginning to
grow instead. Both faces are calm. Damp ambient light, no shadow with an edge.""",
        "salve-of-poor-provenance": """A jar with no label the viewer can read, opened, its contents blooming up out of
the neck in a slow irregular column and colonizing the cloth around it in rings.
Beside it, an arm already treated with it and visibly better. Where the jar came
from is not in the picture and the ochre batik gives nothing away.""",
        "ward-of-many-wounds": """Several bodies laid in a rough ring on a batik ground, all of them treated, all
of them blooming the same colony from different points -- and the colonies have
grown into each other in the middle of the ring, joining into one organism. The
wounds are closed. The ring's shape is irregular; nothing here is arranged
squarely.""",
        "confident-diagnosis": """A single hand pressed flat against a chest, and radiating out from beneath it in
perfect fractal rings, the spread of something that has been identified correctly.
The face above the hand -- the physician's -- shows no doubt whatsoever. The patient's
face is out of frame. Wax crackle running through the whole cloth.""",
        "mender-of-bad-cases": """A crowded field of small figures on batik, most of them in poor condition, and
one upright figure moving among them with a jar under one arm -- and the colony
spreading outward through the group from wherever they have already been, so the
picture reads as a map of the rounds they have made. Bone-colored where they have
not reached yet.""",
        "spore-physician": """A figure whose exhalation is a visible cloud of spores drifting across the frame
in an irregular plume, and where the plume has settled on other figures they have
stopped doing whatever they were doing. Nothing is straight, including the plume.
Bruise purple in the densest part of the cloud, swamp green at its edges.""",
        "rot-fed-healer": """A figure kneeling on rotted ground and drawing the rot up through their own hands
and into a patient beside them, the colony running visibly from the earth through
one body and into the other in one continuous irregular channel. The patient is
improving. The healer is not. Damp cellar light. No clean edges anywhere.""",
        "mire-no-bedside-manner": """Mire themself, the class leader, standing over a seated patient on a batik ground
with one hand pressed flat to the patient's shoulder -- and the point of infection
under that hand is radiating outward in irregular fractal rings across the arm,
the chest and on into the cloth of the picture itself. The patient's expression is
not good. Mire's is entirely neutral, absorbed and professional, and they are not
looking at the patient's face. Jars at their feet, labelled with marks that never
become letters. Wax crackle throughout, not one straight line in the frame.""",
        "everything-thrives-here": """A whole field where the colony has won: every figure in the picture is blooming
with the same growth from a different point, the ground itself is a culture plate,
and the batik's ochre survives only in the narrow channels between colonies. All
of them are healthier than they were. None of them chose it. Rings on rings on
rings, no straight line anywhere.""",
        "spotless-success-rate": """A row of patients on a batik ground, all recovered, all standing, all blooming --
each one carrying the visible colony that fixed them, and each colony a different
irregular fractal at a different stage. At the near end of the row, a shelf of
jars, empty now. Nothing in the picture has a clean edge and every single case
worked. Damp ambient light throughout.""",
    },
)

CLASSES["18-ranger"] = dict(
    display="Ranger",
    label="RANGER",
    hero_who="the same woman",
    hero_summary="The landscape face is Fletch at rest in camp; the portrait face is the thing "
                 "she is famous for, the shot she prepared for weeks ago, with the vertical "
                 "format carrying the whole length of the range.",
    front_desc="Fletch at rest in camp",
    back_desc="the shot prepared for weeks ago",
    style="""
Medium: naturalist field-journal gouache. Quick, confident opaque studies on
tea-stained sketchbook paper, with the pencil underdrawing left visible through
and around the paint. Brushwork is economical and unfussy -- these were painted
outdoors, fast, by somebody recording rather than composing.

Light: plain daylight, observed rather than arranged. Nothing is dramatized,
nothing is spotlit, no golden hour. The light is whatever the light was.

Composition: several small studies per card rather than one hero image -- three
views of the same subject, a detail at larger scale, a measurement, a thumbnail
of the whole scene in a corner. The page, not the picture, is the unit.

Signature: handwritten annotation and specimen labels in the margins and beside
the studies, in the hero's own hand, with leader lines to what they describe.
This is the only class whose cards contain her notes as well as her images. The
writing must always read convincingly as a naturalist's cursive and must never
resolve into actual letters, words or numerals -- the impression of a hand only.

Ground: paper tan #DCCFB0 for the sheet, moss #5C7A3E and umber #7C5433 in the
studies, sky wash #9FBCCB for the thin washes, and red ink #B03A2E for
corrections and the occasional underline. Muted throughout, with the paper
showing in every unpainted area.

Register: the most competent ordinary person alive. No pact, no curse, no tragic
backstory -- she simply out-prepared everybody, and finds the rest of the roster's
suffering somewhat self-inflicted. Dry, self-sufficient, quietly amused.
""",
    hero_front="""Fletch at rest, the class portrait, laid out as a page from her own
journal. The largest study, centered, is her sitting on a pack beside a small
fire with her boots off and a mug in one hand, painted quickly in gouache with
the pencil underdrawing showing through -- entirely at ease, faintly amused,
looking at something off the page. Around it on the tea-stained sheet, smaller
studies of what that ease is built on: her bow unstrung and laid flat, three
views of a boot sole, a food cache diagrammed, the same fire drawn again from
above. Handwritten annotation in her own hand beside each, with leader lines,
never legible as words. One red-ink underline. Plain daylight, nothing
dramatized.""",
    hero_back="""An action shot, and for this class the action happened weeks ago --
what the picture shows is the last two seconds of a long preparation. A tall
journal page: the main study runs the full height of it, Fletch at the bottom of
the frame at full draw, and the whole vertical distance above her painted as the
range itself -- the slope, the wind she noted, the mark she set out three days
ago, the target at the top of the sheet. It is a single continuous study rather
than a composition. Around its edges, smaller studies on the same page, made
earlier: the wind noted twice, the ground measured, the mark drawn from below.
Her annotation in her own hand runs the length of the margin with leader lines
into the main study, never resolving into words. One red-ink correction, where
she revised her own earlier estimate. Her expression is entirely unbothered.
Plain daylight. It is going to work because it was always going to work.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
quick confident gouache studies on tea-stained sketchbook paper with the pencil
underdrawing left visible, lit by plain observed daylight — nothing dramatized,
nothing spotlit, no golden hour. The light is whatever the light was.

Two things carry it. The first is that **the page, not the picture, is the unit**:
every card is several small studies rather than one hero image — three views of a
subject, a detail at larger scale, a measurement, a thumbnail of the whole scene
in a corner. The second is the annotation, which makes this the only class whose
cards contain the hero's *notes* as well as her images: handwritten labels in her
own hand, with leader lines to what they describe. It must read convincingly as a
naturalist's cursive and must never resolve into actual letters, words or
numerals — the impression of a hand only. Every prompt states that limit, because
this is the class most likely to produce readable gibberish.

The register is in every file: no pact, no curse, no tragic backstory. Fletch
out-prepared everybody, and she finds the rest of the roster's suffering somewhat
self-inflicted.""",
    subjects={
        "cached-supplies": """A journal page of a supply cache: the main study a hollow under a rock with
oilcloth-wrapped bundles inside it, painted quickly in gouache; around it, three
smaller studies of the same site from other angles, a cross-section showing how
deep it sits, and a thumbnail of the surrounding country for finding it again.
Annotation with leader lines beside each, never legible.""",
        "provisioned-scout": """A page given to one figure studied three times -- front, back and in profile with
the pack on -- painted economically with the pencil showing, plus a larger detail
study of how the straps are run and a smaller one of the contents laid out in a
row. Plain daylight. Red-ink underline beside one item in the row.""",
        "read-the-ground": """A page of ground sign: a large study of a single print in soft earth at close
range with a measure laid beside it, and around it five smaller studies of the
same track at intervals across a slope, each annotated in her hand with leader
lines. A thumbnail of the whole hillside in the corner shows where they lead.""",
        "forward-marker": """A page recording a mark left deliberately: the main study a cairn or a notched
branch, painted plainly, with two smaller studies showing how it reads from either
approach and one showing how it reads from the wrong direction and does not.
Annotation throughout, a red-ink correction on the third study.""",
        "packed-for-both": """A journal page of a pack laid out fully unpacked: every item painted separately
in gouache in loose rows on the tea-stained sheet, with the pack itself drawn
small in one corner and a second small study showing all of it back inside. The
list is annotated in her hand and none of the writing is legible.""",
        "practised-hand": """A page of the same action studied over and over: eight small gouache studies of
one pair of hands doing one thing -- nocking, drawing, loosing -- in sequence
across the sheet, plus one larger detail of the grip at the moment it matters.
Pencil underdrawing visible in all of them. Plain daylight, no drama.""",
        "trail-reader": """A page of a figure crouched over ground sign, painted as the main study, with
three separate smaller studies around it of what she is looking at: a bent stem,
a scuff, a hair caught on bark, each at larger scale than life and each with a
leader line to its position in the main study. Annotation beside every one.""",
        "recruiting-trip": """A page of faces: six quick gouache portrait studies of very ordinary people
arranged in two rows on the tea-stained sheet, each annotated in her hand with
something short, plus a larger study of two of them shaking hands. Nobody is
heroic-looking. Red ink beside two of the six.""",
        "three-days-foresight": """A journal page laid out as three days: three horizontal bands of study across the
sheet, each with its own weather thumbnail, its own ground detail and its own
short annotation, all painted at the same time and clearly in advance of any of
them happening. Plain daylight in all three. Leader lines run between the bands.""",
        "fletch-simply-prepared": """Fletch herself, the class leader, as the main study on a journal page: standing
three-quarter view with the bow held loose at her side and a pack at her feet,
painted quickly in gouache with the pencil underdrawing showing through, plain
daylight, entirely unbothered and faintly amused. Around her on the tea-stained
sheet, smaller studies of everything that makes her the largest study on the
page -- the pack's contents in rows, two views of a knot, a slope profiled, a
water source marked. Annotation in her own hand throughout with leader lines into
the main figure, never resolving into words. One red-ink correction.""",
        "weathered-tracker": """A page of a much-used figure: the main study a lean weathered tracker standing in
plain daylight, painted economically, with smaller studies of the specific damage
around it -- a scarred hand at large scale, a repaired boot, a bow with a spliced
limb. Each annotated with a leader line. Nothing about the damage is
dramatized.""",
        "everything-already-packed": """The fullest page in the class: an entire expedition's worth of gear painted in
small individual gouache studies covering the whole tea-stained sheet edge to
edge, in rows, each one labelled in her hand with a leader line, none of the
writing legible. In the one clear corner, a small study of a single closed pack,
and beside it a figure walking away from the viewer carrying it. It all fits. It
was always going to fit.""",
    },
)

CLASSES["19-lich"] = dict(
    display="Lich",
    label="LICH",
    hero_who="the same person",
    hero_summary="The landscape face is Rime at rest, sitting for a portrait; the portrait face "
                 "is the thing they are famous for, the plate failing around them while they "
                 "hold the pose, with the vertical format carrying the cracks to the top edge.",
    front_desc="Rime at rest, sitting for a portrait",
    back_desc="the plate failing, the pose held",
    style="""
Medium: a frost-fogged tintype. Wet-plate photography with silver-halide bloom in
the highlights, heavy vignetting into the corners, chemical staining and
tide-lines at the plate edges, and dust and pinholes in the emulsion. This is a
photographic object with damage of its own, not a picture of a scene.

Light: long-exposure studio light, harsh and frontal, from a single large source
close in. Eyes are never quite in focus, because the sitter moved during the
exposure -- everything else is sharp and the eyes are not.

Composition: formal portrait staging. Everyone is posed, centered and symmetrical,
hands placed, holding still for far too long. Studio furniture -- a chair, a
column, a plain backdrop -- appears where a portrait would have it. Nobody in this
class is caught doing anything.

Signature: spiderweb cracks in the emulsion radiating outward from the subject.
The plate is failing where the figure touches it, and the cracks are always
centered on the sitter rather than on any damage to the plate's edge.

Ground: silver #B8BCC4 in the highlights, plate grey #5A6068 through the
midtones, tarnish violet #6B4A82 in the chemical staining and black #16141C in
the vignette. Monochrome with the violet coming only from the tarnish.

Register: unfailingly polite and completely without appetite. Curious about the
living the way one is curious about weather, with no stake in the outcome. Has all
the time there is and no particular plan for it. Nothing here is menacing; it is
courteous, and it is not going to leave.
""",
    hero_front="""Rime at rest, the class portrait, and in this class that is literal.
A formal wet-plate sitting: Rime centered and symmetrical in a studio chair,
hands placed on the arms, shoulders square, holding the pose. Harsh frontal
studio light, silver bloom in the highlights along the collar and the hands,
heavy vignetting into all four corners, chemical tide-lines at the plate's edges.
The face is composed and courteous and entirely without appetite. The eyes are
the one soft passage in an otherwise sharp plate -- they moved. Spiderweb cracks
in the emulsion radiate outward from where their hands rest on the chair arms.
Frost has fogged the plate's lower corner. They are being extremely polite about
sitting this long, and they could sit very much longer.""",
    hero_back="""An action shot, and for this class an action shot is a plate
failing while the sitter declines to move. A tall vertical tintype: Rime standing
full-length and dead center at the bottom of the frame, hands folded, pose
perfect, harsh frontal studio light -- and from their feet and shoulders the
emulsion is failing upward, spiderweb cracks radiating out and running the full
height of the plate, splitting, branching, taking the backdrop apart. Silver
bloom floods the upper half where the emulsion has lifted; chemical staining in
tarnish violet runs down through the cracks; frost fogs the whole top third. They
have not moved. The eyes are still soft. Everything in the picture is coming
apart except the person it is a picture of, and they are being very courteous
about it.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
these are wet-plate tintypes, not illustrations — silver-halide bloom in the
highlights, heavy vignetting, chemical staining and tide-lines at the plate edges,
dust and pinholes in the emulsion. The plate is a physical object with damage of
its own.

Two things carry it. The first is the exposure: harsh frontal studio light, formal
staging, everyone posed and centered and symmetrical and holding still far too
long — **nobody in this class is caught doing anything** — and the eyes never
quite in focus, because the sitter moved. Everything else on the plate is sharp
and the eyes are not. The second is the signature failure: spiderweb cracks in the
emulsion radiating outward from the subject, always centered on the sitter rather
than on any edge damage. The plate is failing where the figure touches it.

The register is in every file and it is what keeps the class from reading as a
monster: Rime is unfailingly polite and completely without appetite, curious about
the living the way one is curious about weather. Nothing here is menacing. It is
courteous, and it is not going to leave.""",
    subjects={
        "attending-revenant": """A formal standing portrait of an attendant figure, centered and symmetrical, one
hand resting on the back of an empty chair as a servant is posed in a household
photograph. Harsh frontal light, silver bloom on the cuff. The eyes are soft; the
rest of the plate is sharp. Emulsion cracks radiate from the hand on the chair.""",
        "polite-insistence": """A seated sitter and, standing behind the chair, a second figure with one hand
placed lightly on their shoulder -- the pressure of it is the only thing happening
in the picture. Both are posed correctly. Neither expression is unfriendly. The
cracks in the emulsion radiate from the hand on the shoulder and from nowhere
else.""",
        "courtesy-of-the-pause": """A portrait in which the sitter is held very slightly too still: an entirely
conventional posed figure, hands folded, with a thin frost bloom fogging the plate
in a clean shell around them and nowhere else. Heavy vignetting. Chemical
tide-lines at the plate edge. The eyes are soft. Nothing is wrong and everything
is.""",
        "frostbitten-clerk": """A formal seated portrait of a clerkish figure with a ledger closed on their lap,
hands placed on it, posed and symmetrical. Silver bloom along the ledger's edge.
Frost has fogged the plate across the lower third, taking the feet. The cracks
radiate from the ledger. Long exposure: the eyes moved.""",
        "recalled-from-rest": """A double-exposed plate: the same chair photographed twice, once empty and once
occupied, both images present at the same strength so the sitter is transparent
over the furniture. Formal staging, harsh frontal light. The cracks radiate from
where the two exposures overlap. Heavy vignette, chemical staining down one
side.""",
        "warded-sleeper": """A recumbent figure posed on a studio couch as for a memorial portrait, hands
crossed, absolutely still and lit hard and frontally, with a clean unfogged shell
of plate around the body and dense frost fogging everywhere outside it. Silver
bloom on the crossed hands. The cracks radiate from beneath the couch.""",
        "preserved-attendant": """A standing attendant in formal pose beside a plain studio column, one hand at the
side and one behind the back, immaculately turned out and photographed at close
frontal light. The plate around them is in excellent condition; the plate around
everything else has stained and lifted. The eyes are soft. Cracks radiate from
their feet.""",
        "rime-without-appetite": """Rime themself, the class leader, in a formal seated wet-plate portrait: centered,
symmetrical, hands placed on the chair arms, shoulders square, holding a pose
they could hold indefinitely. Harsh frontal studio light, silver bloom on the
collar and knuckles, heavy vignetting into all four corners, chemical tide-lines
at the plate edges. The expression is courteous, attentive and entirely without
hunger -- the look of someone politely interested in you as weather. The eyes are
the only soft passage on a sharp plate. Spiderweb cracks radiate outward from
both hands.""",
        "two-slow-certainties": """A double portrait: two sitters posed side by side in identical chairs, identically
composed, hands identically placed, photographed in one exposure. Harsh frontal
light on both. One of them is slightly more faded into the plate than the other
and it is not clear which was there first. Cracks radiate from between the two
chairs.""",
        "guest-who-never-leaves": """A formal group portrait -- a household posed on and around a settee, everyone
correct, everyone holding still -- with one additional figure standing at the back
who is lit differently from the rest and casts no shadow onto the backdrop. Nobody
is looking at them. The emulsion cracks radiate from where that figure stands.""",
        "host-of-the-long-pause": """A wide formal interior plate: a long table set for many, every place laid, every
chair occupied by a posed and motionless sitter, and one figure standing at the
head of it with hands folded. Harsh frontal light down the whole table. Silver
bloom on the glassware. Frost fogs the far end. Cracks radiate from the head of
the table outward past every guest.""",
        "all-the-time-there-is": """The most damaged plate in the class and the most composed sitter on it: a single
full-length figure centered in a formal standing pose, hands folded, perfectly
still, while the emulsion around them has failed almost completely -- spiderweb
cracks radiating out to all four edges, silver bloom flooding the corners,
chemical staining in tarnish violet running the height of the plate, frost fog
across the top. The sitter is untouched, sharp except for the eyes, and waiting
with total patience for the exposure to finish.""",
    },
)

CLASSES["20-death-knight"] = dict(
    display="Death Knight",
    label="DEATH KNIGHT",
    hero_who="the same man",
    hero_summary="The landscape face is Pall at rest, laid out as an effigy; the portrait face is "
                 "the thing he is famous for, keeping an oath he cannot remember taking, with "
                 "the vertical format carrying the full length of the slab.",
    front_desc="Pall at rest, laid out as an effigy",
    back_desc="keeping an oath he cannot remember",
    style="""
Medium: a wax rubbing taken from a memorial brass. Flat, formal, full-length
effigy work -- the figure rendered entirely as the texture of black wax dragged
over an incised plate, with the line surviving only where the engraving is deep,
and the paper's tooth showing everywhere else.

Light: none in the rubbing itself. It is a flat record, not a lit scene. All
light in the image comes from rime crystal blooming across the surface of the
rubbing afterward, catching cold and pale on top of the black wax.

Composition: rigidly symmetrical and full-length. Every figure is laid out like a
tomb slab -- feet together at the bottom of the frame, hands crossed or on a hilt,
heraldry at the feet, an inscription band running the border. Even mid-swing, the
figure is composed as an effigy.

Signature: frost growing on top of the image and obscuring parts of it. The
rubbing is a record of someone already gone, and it is icing over as you look at
it. The frost must sit above the rubbing, not inside it.

Lettering: the inscription band and the heraldry carry the convincing texture of
memorial lettering but never resolve into actual letters, words or numerals --
the impression of an epitaph only.

Ground: rubbing black #1E1C1A for the wax, brass #9A7B3A where the plate shows
through, frost white #E8EEF4 for the rime and steel blue #5A7A96 in the cold
shadow of it. Flat, cold and funerary.

Register: raised by somebody else's will and freed of it later, which was the
harder half. Slow, implacable, unbothered by damage, keeping an oath he cannot
remember taking. Set against the Runeblade deliberately: these marks were
inflicted, not authored.
""",
    hero_front="""Pall at rest, the class portrait, and in this class rest is the
default state: a full-length memorial effigy taken as a wax rubbing. He is laid
out rigidly symmetrical along the length of the frame, in armor, hands crossed on
the hilt of a sword that runs the full height of the figure, feet together at
one end with heraldry beneath them and an inscription band running the whole
border -- never legible as letters. The rubbing is black wax over paper tooth,
with brass showing through where the engraving cut deepest. Two points of cold
blue light where the eyes were. Rime crystal has begun to bloom on top of the
rubbing, growing across the chest and one hand, obscuring part of the crossed
fingers. It is icing over as you look at it.""",
    hero_back="""An action shot, and for this class an action shot is still an
effigy -- he is composed exactly as a tomb slab even in the middle of the blow. A
tall vertical rubbing: Pall full-length and dead center, feet together at the
bottom on his heraldry, the sword raised straight up the vertical axis of the
frame and taking its whole height, both hands on the grip. The symmetry is
absolute; nothing is off-balance, nothing is dynamic, the swing is laid out
rather than caught. Black wax over paper tooth, brass showing in the deepest
cuts, inscription band running the border and never resolving into words. Cold
blue where the eyes were. And rime is growing across the top of the whole
rubbing, heaviest on the raised blade and the shoulders, taking the upper third
of the record away as you look at it. He is keeping an oath he cannot remember
taking, and he is going to finish the sentence.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
every image is a **wax rubbing taken from a memorial brass** — the figure rendered
as black wax dragged over an incised plate, the line surviving only where the
engraving is deep, the paper's tooth showing everywhere else. There is no light in
the rubbing itself, because it is a flat record rather than a lit scene.

Two things carry it. The first is the staging: rigidly symmetrical and
full-length, laid out like a tomb slab with feet together, hands crossed or on a
hilt, heraldry at the feet and an inscription band around the border. **Even
mid-swing the figure is composed as an effigy** — the prompts say it in those
words, because the instinct is to make a death knight dynamic. The second is the
frost, which is the only light in the class: rime crystal blooming *on top of* the
rubbing, above the image rather than inside it, obscuring parts of it. The record
is icing over as you look at it.

No lettering resolves — the inscription band and heraldry carry the texture of an
epitaph without a legible character. And the register is in every file, including
the line that separates this class from the Runeblade: these marks were inflicted,
not authored.""",
    subjects={
        "given-orders": """A memorial brass of a hand receiving a folded document from another hand that
enters from the border and is not attached to any figure. Rigidly symmetrical
composition, inscription band around the whole edge, heraldry beneath. Rime has
grown across the giving hand, obscuring most of it, and not at all across the
receiving one.""",
        "conscript": """A full-length effigy of a very ordinary person in ill-fitting armor, laid out
symmetrically with hands crossed and feet together, heraldry at the feet that is
clearly not theirs. Black wax over paper tooth. Frost blooming from the heraldry
upward across the legs. Two points of cold blue where the eyes were.""",
        "discarded-prisoner": """A tomb-slab composition of two figures laid out side by side, identical in
posture, one of them rubbed clean off the plate from the waist up so only the
paper tooth remains there. The inscription band continues unbroken around both.
Rime has grown thickest exactly over the missing half.""",
        "finisher": """An effigy laid out full-length in the act of a downward blow, and composed
exactly as a recumbent figure would be -- symmetrical, feet together, the weapon
along the body's axis. Beneath the feet, in the heraldic panel, a second smaller
figure already laid out the same way. Rime across both.""",
        "paired-compulsion": """Two full-length effigies laid out head to foot along the frame, mirror-symmetric,
their hands crossed in exactly the same way -- the same rubbing taken twice from
the same plate. A single chain, incised deeply enough to survive the rubbing,
runs from one to the other. Rime grows along the chain and nowhere else.""",
        "choose-your-loss": """A memorial brass showing three identical effigies in a row, and one of them
rubbed out entirely -- not damaged, simply not taken, the paper left blank in a
figure-shaped absence between the other two. The inscription band runs around all
three positions. Frost blooms heaviest over the blank one.""",
        "standing-sentence": """A full-length effigy standing rather than recumbent -- vertical, rigidly
symmetrical, hands crossed on a grounded sword, feet together on a heraldic
panel -- of a figure who has plainly been standing there through the entire
making of the rubbing. The wax is heavier at the shoulders where the plate is
worn. Rime up to the knees.""",
        "cold-vanguard": """A frieze-like rubbing of a rank of effigies laid out shoulder to shoulder across
the full width of the frame, all identical, all symmetrical, all with hands
crossed the same way, one continuous inscription band running above and below
them. Rime has grown across the whole rank in one sheet, thickest at the
center.""",
        "implacable-rider": """A memorial brass of a mounted figure, laid out with the same slab symmetry as a
recumbent one -- horse and rider flat, frontal, motionless, feet and hooves in a
row along the bottom edge, heraldry beneath. Nothing about it is dynamic. Rime
grows up the horse's legs and across the rider's shield.""",
        "pall-bound-to-anothers-will": """Pall himself, the class leader, taken as a full-length memorial rubbing:
standing, rigidly symmetrical, in old armor, both hands crossed on the hilt of a
grounded sword, feet together on a heraldic panel, an inscription band running
the whole border and never resolving into letters. Black wax over paper tooth,
brass showing where the engraving cut deepest. Two points of cold blue where the
eyes were. Rime crystal blooms on top of the rubbing across his chest and both
forearms -- exactly where a set of marks is incised into the armor that he did not
put there. He is not resisting any of it.""",
        "weight-of-every-oath": """An effigy laid out under everything it agreed to: a full-length symmetrical
figure with the inscription band not confined to the border but repeated inward
in ring after ring across the whole plate until the figure is almost buried in
bands of illegible epitaph. Hands still crossed. Rime growing over the outermost
rings.""",
        "the-whole-field-conscripted": """The largest rubbing in the class: a single enormous plate covered edge to edge
with full-length effigies in ordered rows, every one laid out identically, hands
crossed, feet together, dozens of them, one continuous inscription band running
the entire border. At the center, one figure slightly larger than the rest with a
hand raised. Rime is growing across the whole plate at once and has already taken
the outer rows.""",
    },
)

CLASSES["21-assassin"] = dict(
    display="Assassin",
    label="ASSASSIN",
    hero_who="the same person",
    hero_summary="The landscape face is Hush at rest, off the clock; the portrait face is the "
                 "thing they are famous for, the job done exactly as quoted, with the vertical "
                 "format carrying the height of the screen.",
    front_desc="Hush at rest, off the clock",
    back_desc="the job done exactly as quoted",
    style="""
Medium: shadow-puppet theatre. Cut-paper figures held against a lit screen --
wayang logic -- with articulated joints and the control rods visible as part of
the design rather than hidden. The figures are flat cut shapes; the screen is
cloth and shows its weave.

Light: from behind the screen, warm and even, from a single lamp. The figures are
pure negative shapes with no interior modelling at all, and the ground is the only
thing in the image that glows.

Composition: everything is told in outline and gesture. There is no interior
detail anywhere -- the silhouette carries one hundred percent of the read, so the
pose must be legible with no face, no fold and no texture available to help it.

Signature: exactly one accent color per card, used exactly once, on one small
shape. Usually blood; occasionally not. Never a second note.

Ground: lamp amber #D9A441 for the lit screen, pure black #0E0C10 for every
figure, and one red note #B0201C used once. Nothing else. No greys, no
gradients inside a figure, no rim light.

Register: the most professional person in the game. No ideology, no grudge, no
tortured relationship with the work. In a cast of the cursed and the
bargained-away, the one who is simply fine is the most unsettling thing on the
table. Punctual. Reasonable rates.
""",
    hero_front="""Hush at rest, the class portrait, and rest here means off the
clock. A single cut-paper figure against a warm lamp-lit screen, seated on a
low stool in flat profile, one knee up, hands loose -- entirely at ease. The
silhouette does all of it: no face, no interior detail, no modelling anywhere,
and the pose still reads unmistakably as somebody who has finished for the day.
The control rods are visible at the shoulder and wrist and are part of the
design. Beside the stool, cut in the same pure black, the tools of the trade set
down and tidy. The screen's cloth weave shows through the amber. One red note,
used once and small: on a cloth being folded.""",
    hero_back="""An action shot, and for this class an action shot is a job finished
exactly as quoted. A tall vertical screen lit warm from behind: the composition
runs the full height of it, Hush's cut-paper silhouette at the lower third in a
single economical gesture -- one arm extended, the whole body compact and
unhurried -- and above them, occupying the height of the frame, the elaborate
silhouette of the thing that was contracted for: a guarded stair, figures posted
on every landing, all of them cut in the same pure black, none of them turned
around. Not one of them has noticed. The control rods on Hush's figure are
visible and steady. Nothing about the pose is dramatic; it is efficient. And one
red note, used exactly once, small, at the top of the stair.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
cut-paper figures against a lit screen — wayang logic, with the articulated joints
and **control rods visible as part of the design** rather than hidden — lit from
behind by a single warm even lamp, so the figures are pure negative shapes and the
ground is the only thing that glows.

Two things carry it. The first is the hardest constraint in the game: there is no
interior detail anywhere, so **the silhouette carries one hundred percent of the
read**. Every pose has to be legible with no face, no fold and no texture
available to help it, and every prompt says so. The second is the accent: exactly
one color per card, used exactly once, on one small shape. Usually blood;
occasionally not. Never a second note.

The palette is three values and no gradients — lamp amber, pure black, and the one
red. And the register is in every file, because it is what makes the class
unsettling rather than edgy: Hush has no ideology, no grudge and no tortured
relationship with the work. In a cast of the cursed and the bargained-away, the
one who is simply fine is the worst thing on the table.""",
    subjects={
        "contract-opened": """Two cut-paper figures on a warm screen: one seated and offering a folded paper
across a low table, the other standing and taking it. Both pure black, no interior
detail, the whole exchange carried by the angle of two wrists. Control rods
visible. The one red note is a seal on the folded paper, small, used once.""",
        "quiet-professional": """A single flat black figure in profile crossing the screen at an unhurried walk,
carrying nothing visible, posed so ordinarily that only the economy of the outline
suggests anything at all. Two other figures further along the screen, facing the
other way. One red note, small, on the walking figure's cuff.""",
        "working-blade": """A single implement held up in one cut-paper hand against the lit screen, in flat
silhouette, at the exact center of the frame -- plain, well-kept, unremarkable in
shape. The hand's articulated joint and control rod are visible. Nothing else on
the screen. The one red note is a single dot at the tip.""",
        "between-the-guards": """A doorway cut into the screen with a black figure posted on either side, both
alert and both facing outward, and passing between them in the same flat black a
third figure whose silhouette overlaps neither. The read is entirely in the
spacing. Control rods on all three. One red note, on the door's latch.""",
        "clean-entry": """A window shape cut in the lit screen and one flat black figure halfway through
it, body folded into an economical shape that reads instantly as quiet. No frame
is broken, nothing is disturbed, and the silhouette shows that without any
interior detail to help. One red note: a single mark on the sill.""",
        "paid-on-completion": """A hand extended flat against the lit screen with a small purse in it, and another
hand closing on the purse from the opposite side. Both pure black, both with
visible rods. Between them, nothing at all -- the screen's warm weave. The one red
note is a bead on the purse's cord.""",
        "finish-the-job": """A single black figure standing over a shape on the ground, its posture entirely
neutral -- not triumphant, not regretful, simply finished -- rendered with no
interior detail whatsoever so the whole read comes from the angle of the shoulders.
Warm lit screen behind. One red note, small, at the low shape's edge.""",
        "hush-punctual": """Hush themself, the class leader, as a single cut-paper silhouette against the
warm lamp-lit screen: standing in flat profile, weight even, one hand at their
side and the other holding a folded contract, absolutely composed. No face, no
interior detail, no modelling -- the silhouette carries all of it, and what it
carries is a person who is exactly on time and has no feelings about the
appointment. Articulated joints and control rods visible at shoulder, elbow and
wrist. The screen's cloth weave shows through the amber ground. One red note,
small, used once: a seal on the contract.""",
        "no-witnesses": """A wide lit screen with a room's furniture cut in flat black -- table, chairs, a
hanging lamp -- and no figures on it at all except one standing at the very edge,
already leaving. The composition reads as an emptiness that was recently
occupied. Control rod visible on the leaving figure. One red note, small, on the
table.""",
        "reasonable-rates": """A cut-paper figure seated at a small table opposite a client, both flat black
against the warm screen, the client's posture agitated and the figure's entirely
still -- the whole difference carried by two silhouettes and nothing else. A short
list lies between them, cut as a plain shape. One red note, on the list.""",
        "second-contract": """The same figure shown twice on one screen -- once at the left and once at the
right, identical silhouettes with identical posture -- and between them a single
folded paper being handed from one to the other, which makes no sense and is
correct. Control rods on both. One red note, on the paper.""",
        "nothing-personal": """The plainest composition in the class: one flat black figure in the exact center
of a warm lit screen, standing square to the viewer, arms at their sides, entirely
still, with nothing else cut into the picture at all. No interior detail, no face,
no gesture to read -- and it is still unmistakably somebody about to go to work.
One red note, small, used once, on the back of one hand.""",
    },
)
