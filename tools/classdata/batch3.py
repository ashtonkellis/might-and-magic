# -*- coding: utf-8 -*-
CLASSES = {}

CLASSES["12-windrunner"] = dict(
    display="Windrunner",
    label="WINDRUNNER",
    hero_who="the same woman",
    hero_summary="The landscape face is Gale at rest above her own chart; the portrait face is "
                 "the thing she is famous for, putting herself between people and what is "
                 "coming, with the vertical format carrying the drop she is standing under.",
    front_desc="Gale at rest above the chart",
    back_desc="between them and what is coming",
    style="""
Medium: a meteorological chart. Isobars, wind barbs, pressure gradients and
storm-track projections drawn in fine survey ink on aged chart paper, with fold
creases, coordinate ticks along the margins and the soft foxing of a document
that has been carried folded for years.

Light: the chart itself is flat and completely unlit -- it is a document, not a
scene. The figure is the only luminous thing on it, glowing from within and
leaking bright vapor at the shoulders and heels.

Composition: the ground is drawn entirely in the language of the map -- contour,
isobar, projection, coordinate grid -- and the subject sits above the chart plane,
outside its coordinate system, casting no shadow onto it. She is the one thing on
the page the survey could not fix a position for.

Signature: one flight path traced across every card, entering at one edge and
leaving at another, drawn as a survey line with direction arrows -- and wherever
that path passes an ally, that figure is drawn glowing too. This is the only
class whose art shows its power landing on somebody else. Every card needs the
path, and every card needs somebody other than the hero lit by it.

Annotation: coordinates, pressure values and margin notation are present in the
chart's own hand but never legible as actual letters or numerals -- only the
convincing impression of survey data.

Ground: chart buff #E8DFC8 for the paper, survey green #2C8C4E and ink brown
#6B5333 for the drawn map, storm grey #6E7684 for weather, and Stormlight
white-gold #F5E6B0 for everything that glows. Nothing saturated. The paper stays
paper.

Register: a protector, and the flying is incidental to that. The oaths are spoken
out loud, they bind, and each one costs something to mean. Nobody in this class
is showing off.
""",
    hero_front="""Gale at rest, the class portrait. Full figure standing above the
chart plane in three-quarter view, feet just clear of the paper, casting no
shadow onto it -- she is not in the map's coordinate system. She glows from
within and leaks bright white-gold vapor from the shoulders and heels. Beneath
her the whole frame is drawn as a survey chart: isobars, contour, a storm track
curving through, coordinate ticks at the margins, a fold crease across one
corner. Her flight path enters at the left edge and leaves at the right, drawn as
a ruled survey line with direction arrows -- and standing on the chart where it
passes are three ordinary figures, drawn flat and small in survey ink, each one
glowing white-gold because she went by. She is looking at them, not at the
viewer.""",
    hero_back="""An action shot, and for this class an action shot is interposition
rather than attack. A tall vertical chart: filling the upper two-thirds, a storm
system drawn as dense survey work coming down -- packed isobars, converging wind
barbs, a projection cone narrowing straight toward the bottom of the frame. At
the base of it, small and lit and entirely alone, Gale standing with her back to
the viewer, arms out wide, between the storm and the handful of flat ink-drawn
figures behind her. She glows; they glow too, because she is standing there. Her
flight path enters at the top edge, comes all the way down the frame and stops
at her heels -- it does not leave the other side. Bright white-gold vapor pouring
off her shoulders. The chart records everything about the storm and has no
position for her at all.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
the ground of every card is a meteorological chart — isobars, wind barbs,
pressure gradients and storm-track projections in survey ink on aged folded chart
paper — and the chart itself is **flat and completely unlit**, because it is a
document rather than a scene. The figure is the only luminous thing on it,
glowing from within and leaking bright vapor at the shoulders and heels.

Two things carry it. The first is that the subject sits *above* the chart plane,
outside its coordinate system, casting no shadow onto it — she is the one thing on
the page the survey could not fix a position for. The second is the rule that
makes this class unlike every other one in the game: one flight path crosses every
card, entering at one edge and leaving at another, and **wherever it passes an
ally, that figure is drawn glowing too**. Every prompt requires the path, and
every prompt requires somebody other than the hero lit by it. This is the only
class whose art shows its power landing on someone else.

Coordinates and pressure values appear everywhere and never resolve into readable
letters or numerals. And the register is in every file: Gale is a protector, the
flying is incidental, and nobody here is showing off.""",
    subjects={
        "oathbearer-squire": """A young figure standing flat on the chart in survey ink, holding up a folded
cloak toward the flight path that is passing overhead. Where the ruled path
crosses above them they have begun to glow white-gold at the hands and shoulders,
though the rest of them is still drawn in plain ink. Isobars run behind. The path
enters bottom-left and leaves top-right with direction arrows.""",
        "two-sworn-together": """Two figures on the chart moving in the same direction along parallel survey
lines, both glowing white-gold, with the flight path running between them and
touching each in turn -- the arrows show it crossing from one to the other and
back. Beneath, the map's isobars are drawn tightly to show the pressure they are
moving against. Fold crease through the lower margin.""",
        "lift-them-higher": """A figure being carried upward off the chart plane by another: the lower one
still drawn flat in survey ink with contour lines running across the feet, the
upper one glowing and already clear of the paper, both hands locked. The flight
path enters low, hooks up through both of them and exits at the top edge. The
figure being lifted glows brighter than the one lifting.""",
        "shared-ascent": """A length of luminous cord drawn between two figures on the chart, one glowing and
airborne just above the plane and one still standing on it -- and the cord is
transferring the glow visibly along its length, brightest at the middle. The
flight path runs alongside the cord and exits at the right margin. Coordinate
ticks along both edges.""",
        "bound-in-purpose": """Two figures standing back to back at the exact center of a coordinate grid, one
glowing and one not, joined at the wrists by a drawn survey line rather than by
anything physical -- the map's own notation used as a bond. Along that line the
unlit figure is filling with white-gold from the wrist inward. The flight path
circles them once and leaves at the bottom edge.""",
        "three-oaths-spoken": """Three ordinary flat ink figures standing in a row on the chart, each drawn at a
different brightness -- the first fully white-gold, the second half lit, the third
just beginning at the hands -- with the flight path passing over all three in one
unbroken ruled line, entering left and leaving right. Above each, the impression
of an annotation in the chart's hand that never resolves into words.""",
        "cover-their-retreat": """A single glowing figure holding position at the right edge of the chart, facing
into converging wind barbs, while behind her a line of small flat ink figures
moves away toward the left margin and off the page. The flight path comes in
behind them, sweeps past each one -- lighting them as it goes -- and terminates at
her heels rather than leaving the frame.""",
        "skyward-vanguard": """A wedge of figures ascending off the chart plane together, the leader highest and
brightest, the rest lit progressively less toward the back, all clear of the
paper and casting no shadow on it. The flight path is the wedge's own spine,
ruled with direction arrows, entering at the lower-left margin and leaving at the
top. Storm-track projection curving beneath them.""",
        "between-you-and-it": """A single glowing figure standing square in the middle of the chart with arms out,
facing a dense mass of storm survey work drawn coming in from the right -- packed
isobars, converging barbs, a projection cone whose narrow end is exactly where
she is standing. Directly behind her, two small flat ink figures, glowing. The
flight path enters at the left edge and stops at her back.""",
        "gale-who-lifts-others": """Gale herself, the class leader, drawn above the chart plane in three-quarter
view with one arm extended down toward the paper, glowing from within and
trailing white-gold vapor from the shoulders and heels. She casts no shadow on
the map. Beneath her outstretched hand the chart is crowded with small flat
survey-ink figures, and the four nearest her are lit white-gold while the rest are
not. Her flight path enters at one edge, passes over every lit figure in turn and
leaves at the other. She is watching them rise, not the viewer.""",
        "windsworn-marshal": """A commanding figure just above the chart plane with one arm swept forward, and
along the line of that arm the flight path drawn ruled and arrowed, running the
full width of the frame and passing over five flat ink figures on the ground --
each one glowing white-gold, each one facing the same direction as the arm.
Isobars beneath run parallel to the path. Fold crease down the middle of the
sheet.""",
        "the-whole-flight-rises": """The chart nearly buried under its own subject: dozens of small figures leaving
the paper together across the full width of the frame, every one of them glowing
white-gold, the survey ink of the map visible only in the gaps between them. A
single flight path threads the entire mass, entering at the bottom-left margin,
touching every figure in a long continuous ruled line and leaving at the top-right.
Coordinate ticks and fold creases still legible at the edges. Gale is not
identifiable in it.""",
    },
)

CLASSES["13-edgedancer"] = dict(
    display="Edgedancer",
    label="EDGEDANCER",
    hero_who="the same woman",
    hero_summary="The landscape face is Prism at rest mid-glide, which is as close to rest as "
                 "this class gets; the portrait face is the thing she is famous for, going "
                 "past everything that was built to stop her, with the vertical format "
                 "carrying the length of the slide.",
    front_desc="Prism at rest, mid-glide",
    back_desc="past everything built to stop her",
    style="""
Medium: faceted crystalline geometry. Every form in the image is constructed from
flat planes and hard vector edges -- low-poly form language -- but rendered with
real refraction, so the planes behave like cut glass rather than like shading.

Light: each facet carries a shifted, displaced copy of whatever sits behind it,
and prismatic dispersion fringes every edge in the frame. Light is refracted
rather than cast; there are no soft shadows anywhere.

Composition: a strict geometric armature -- golden-section or radial grid, faintly
visible if you look for it -- cut across by one long unbroken glide path. Every
figure is mid-slide, never mid-step. No card in this class shows a planted foot.

Signature: the cleanest, most machined-looking cards in the game, with not one
soft edge anywhere -- and somewhere in every frame, one ordinary overlooked
person rendered at exactly the same fidelity as the hero. The servant, the
bystander, the one left off the list. Nobody in an Edgedancer card is background.

Ground: glacier white #EAF2F8 as the field, cobalt #3256C6 and aurora teal
#3FA8A0 in the planes, and spectral fringe #C06BD6 in the dispersion at the
edges. Cool, bright and clean throughout, with no muddy passages and no black.

Register: frictionless, and kind about it. Nothing holds her, nothing slows her,
nothing has ever cornered her -- and the precision reads as grace rather than as
calculation. Her attention is the point: she is looking at whoever nobody else
looked at.
""",
    hero_front="""Prism at rest, the class portrait, which for this class means the
middle of a glide. Full figure crossing the frame low and level with both feet
sliding and neither planted, body constructed from flat faceted planes with real
refraction and spectral fringing at every edge. The armature is faintly visible
behind her -- a radial grid the composition obeys -- and her glide path cuts across
it as one long unbroken line, entering one edge and leaving the other. Standing
still in that path, rendered at exactly her fidelity and not one facet less, an
ordinary person: an old servant with a broom, watching her go by. Prism is
looking back at them. Glacier-white field, cobalt and teal in the planes, not one
soft edge in the picture.""",
    hero_back="""An action shot, and for this class an action shot is a single
uninterrupted line through everything that was built to stop it. A tall vertical
frame: the glide path enters at the bottom edge and runs the whole height of the
picture without one break, and Prism is on it -- body low, fully extended, both
feet sliding, mid-slide at the top of the frame. Around and behind the path,
constructed from the same faceted planes, everything that failed to catch her:
closing gates, a raised barricade, spears converging, all of it exact and
machined and all of it aimed at where she was. Refraction displaces the whole
barricade a few degrees behind each facet. Spectral fringing runs the length of
the path. And halfway up, standing in a doorway nobody else in the picture has
noticed, one ordinary person rendered at full fidelity -- and Prism has turned her
head to look at them, in the middle of all this, at speed.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
every form is constructed from flat planes and hard vector edges — low-poly form
language — but rendered with **real refraction**, so each facet carries a shifted
copy of whatever sits behind it and prismatic dispersion fringes every edge. Light
is refracted, never cast. There is not one soft edge in the class.

Two things carry it. The first is motion: a strict geometric armature, faintly
visible, cut by one long unbroken glide path — and every figure is mid-slide,
never mid-step. **No card in this class shows a planted foot**, and the prompts
say it in those words. The second is the rule that makes the class what it is:
somewhere in every frame, one ordinary overlooked person is rendered at exactly
the same fidelity as the hero. The servant, the bystander, the name left off the
list. Nobody in an Edgedancer card is background.

The register follows from that. Prism is frictionless and kind about it; the
precision reads as grace rather than calculation, and her attention — not her
speed — is the actual subject.""",
    subjects={
        "slipped-away": """A figure in the act of not being where it was: the glide path runs unbroken
through the frame, and along it the body is drawn as two faceted positions
overlapping, the earlier one already dispersing into spectral fringe at its
edges. A closing grip in the foreground has hold of nothing. In the corner, at
full fidelity, a child watching.""",
        "unnoticed-runner": """A slight figure crossing the frame low and fast on the glide path, faceted and
refracting, whom none of the four larger constructed figures in the picture are
looking at -- their attention is all on each other. Radial armature faintly
visible. The runner is rendered more finely than any of them. Spectral fringe
along the path.""",
        "quiet-introduction": """A hand extended into the frame, faceted and refracting, offering a
handhold -- and taking it, at exactly the same fidelity as the hand, a person in
plain working clothes who is clearly not anybody's idea of a combatant. The
glide path passes through both wrists. Glacier-white field, cobalt planes,
dispersion at every edge.""",
        "remembered-later": """An empty place at a long faceted table, rendered with as much care as any figure
in the class -- the chair, the setting, the space where somebody sat. The glide
path enters, curves once around that empty place, and leaves. Standing behind
the chair at full fidelity, holding a cloth, the person who used to be given that
seat and no longer is.""",
        "sent-home-gently": """A figure being returned rather than removed: constructed from faceted planes and
already halfway dispersed into spectral fringe along the glide path, both feet
off the ground, face entirely calm. Nothing is broken anywhere in the frame. A
doorkeeper in plain clothes stands at the edge, rendered at full fidelity,
holding the door.""",
        "found-underfoot": """A low view along a faceted floor, the glide path running away into the distance
along the strict armature, and near the front of the frame something small and
overlooked lying on the ground being picked up by a sliding hand at speed. What
is being picked up is rendered as precisely as the hero. Two servants further
back, also at full fidelity, have stopped to watch.""",
        "never-quite-still": """A figure that has not stopped and is not going to: drawn as one continuous
faceted form smeared along the glide path with three overlapping positions
refracting through each other, each displaced a few degrees. The armature behind
is dead straight and dead still by contrast. In a doorway at the frame's edge,
one ordinary person, exact, watching it go past for the third time.""",
        "the-overlooked-arrive": """A group entering the frame together along a single glide path -- six or seven
plain, unremarkable people, all faceted and refracting, all rendered at the
identical fidelity, none of them foregrounded over the others. There is no hero
in this picture. The armature is radial and centered on the group rather than on
any one figure. Spectral fringe along every edge.""",
        "prism-who-remembers": """Prism herself, the class leader, crossing the frame low and level on one
unbroken glide path, both feet sliding and neither planted, body constructed from
flat faceted planes with real refraction and heavy spectral fringing. The
armature is faintly visible and she is exactly on it. She is not looking ahead:
her head is turned to the side, toward an ordinary man in servant's clothes
standing at the frame's edge, and he is rendered at precisely her fidelity, every
facet. He looks surprised to be seen. She does not look surprised to have seen
him.""",
        "between-two-breaths": """A figure arriving in the exact middle of the frame with no approach shown -- the
glide path enters at one edge, is absent across the center, and resumes at the
other side, and she is in the gap. Faceted, refracting, both feet off the floor.
A guard mid-turn, too late, rendered at full fidelity. So is the man he was
guarding.""",
        "glide-past": """A long low slide down the full width of the frame through a corridor of
constructed faceted forms, all of them angled inward to close it and none of them
touching her. Every facet of the corridor carries a displaced copy of the figure
sliding through it, so she appears dozens of times in the walls. One kitchen
worker flattened against the wall at the far end, rendered exactly, entirely
unharmed.""",
        "nothing-holds-them": """The longest line in the class: a single unbroken glide path entering at one corner
and leaving at the opposite one, and strung along it three faceted figures all
mid-slide, all fully extended, none with a planted foot. Everything built to stop
them -- chains, a gate, a closing wall -- is rendered in the same machined facets
and is already behind. Refraction displaces the whole barrier a few degrees.
Standing clear at the side, watching, one ordinary person at full fidelity.""",
    },
)

CLASSES["14-soulcaster"] = dict(
    display="Soulcaster",
    label="SOULCASTER",
    hero_who="the same woman",
    hero_summary="The landscape face is Mirren at rest, further along than she was; the portrait "
                 "face is the thing she is famous for, arguing a wall out of existence, with "
                 "the vertical format carrying the panel dissolving upward.",
    front_desc="Mirren at rest, further along than before",
    back_desc="arguing a wall out of existence",
    style="""
Medium: dark stained glass. Leaded came divides every form into flat colored
panes -- no modelling inside a pane, no gradient, no brushwork -- and the glass is
darker and more saturated than church glass. The medium is the class's argument:
glass is sand that was persuaded, by fire, to become light.

Light: from behind the image, always. The subject is a silhouette made of colored
light and is never lit from the viewer's side. Nothing in this class casts a
shadow forward.

Composition: each card catches one substance partway into becoming another --
half the panel still stone, half already smoke -- with the boundary between them
irregular, unfinished and mid-negotiation. Not an explosion. A conversation being
won.

Signature: the came does not merely divide the image, it spreads. Lead lines creep
across the figures themselves like the crystal growing up Mirren's arm, and in
every card she is a little further along than she was in the last one.

Ground: cobalt #1F3A8C and amethyst #81377B carry the panes, amber #F5B202 is the
warm note, lead grey #4A4A52 is the came and void black #120E1A is what sits
between the lit panels. Saturated but dark -- this is a night window, not a noon
one.

Register: unhurried certainty. Nothing here is destroyed; it is persuaded, and it
agrees, because she is more certain of what it ought to be than it is. The cost
runs the other way and she has already done the arithmetic and found the trade
acceptable.
""",
    hero_front="""Mirren at rest, the class portrait, rendered as a single dark
stained-glass panel lit from behind. Full figure, standing three-quarter view,
composed and unhurried, one hand resting on a stone ledge that is smoke by the
time it reaches her fingers -- the boundary irregular, mid-negotiation, neither
half finished. She is a silhouette of colored light: cobalt in the robe, amethyst
in the shadow, one amber pane at the heart. The leaded came dividing the panel
has spread onto her: lines of lead run up her left forearm and under the jaw
where the crystal has grown, and her left eye is a pane of smoke-grey glass
rather than glass of the same color as the right. She is a little further along
than she was. She is entirely calm about it.""",
    hero_back="""An action shot, and for this class an action shot is an argument
being won. A tall vertical stained-glass panel: at the bottom, Mirren standing
with one palm flat against a wall, and running the full height of the frame above
her, the wall in the act of agreeing -- the lower courses still cut stone in
heavy dark panes, the middle irregular and mid-negotiation, the top already smoke
rendered as thin pale glass with the light coming straight through it. The came
between the stone panes is dense and structural; where the smoke begins it opens
out and lets go. Backlight only: she is a silhouette of cobalt and amethyst
against the brightening upper panel, casting nothing forward. The lead has spread
further up her arm than on her other card, and further under the jaw. She is not
straining. She is just more certain than the wall is.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
dark stained glass, with leaded came dividing every form into flat colored panes —
no modelling inside a pane, no gradient, no brushwork — and the light coming
**from behind the image, always**. The subject is a silhouette made of colored
light and is never lit from the viewer's side. Nothing in this class casts a
shadow forward.

The medium is chosen as the class's own argument, and the prompts say so: glass is
sand that was persuaded, by fire, to become light. Every card catches one
substance partway into becoming another — half the panel still stone, half already
smoke — with the boundary irregular and mid-negotiation. Not an explosion. A
conversation being won.

The signature is the cost, and it accumulates: the came doesn't only divide the
image, it *spreads*, creeping across the figures themselves like the crystal
growing up Mirren's arm. In every card she is a little further along than in the
last one — the hero's two faces are written to be read in that order. And the
register is in every file: nothing here is destroyed, it agrees, because she is
more certain of what it ought to be than it is.""",
    subjects={
        "argued-into-wholeness": """A wound closing because it has been persuaded to: a forearm in flat cobalt panes
with a break across it, and the break's panes visibly changing color from the
outside in until the boundary is only a line of came. Backlit throughout. A pair
of hands holds the arm without gripping it. The lead has begun to spread from the
mend onto the healer's own wrist.""",
        "persuading-hand": """A hand laid flat against a shoulder plate, and under the hand the plate is no
longer metal: three panes of it have gone thin and pale and the light is coming
straight through where it used to be stopped. The wearer has not moved. The
boundary between armor and air is irregular and unfinished. Came spreading from
the contact point up the hand's own fingers.""",
        "terms-of-exchange": """Two objects on a dark ledge, lit from behind, each one halfway into being the
other -- a stone becoming a lantern flame and a lantern flame becoming a stone,
meeting at an irregular came boundary in the middle of the panel. Neither is
finished. Nothing is broken. Amber pane at the flame end, cobalt at the stone
end.""",
        "it-agrees-to-be-useful": """A blank piece of matter -- a lump of rough stone in heavy dark panes -- caught in
the middle of resolving into a tool, the handle already clear and thin-glassed and
the head still stone. The came has reorganized itself around the new shape. A hand
waits, open, not yet reaching. Backlight strongest through the finished end.""",
        "rendered-to-stock": """A figure being un-made downward: standing full length in the panel, intact from
the chest up in cobalt and amethyst panes, and from the waist down already a
column of plain undifferentiated glass the color of raw material. The boundary
is irregular and it is not distressing anyone. Came spreads up from it toward the
shoulders.""",
        "spent-as-substance": """A shape on a dark ground that was a person a moment ago and is now mostly
material, drawn as a panel where the figurative came-work at one end gives way to
plain rectangular glazing at the other -- the leading itself losing its subject.
Lit from behind so the plain end is the brightest part of the picture. Nothing
violent has happened.""",
        "traded-back": """Two hands passing a single object across the panel in opposite directions, and
the object is different in each hand -- stone leaving one, smoke arriving in the
other, the transition happening exactly at the came line between them. Both
figures are silhouettes of colored light. Neither is hurrying. Lead spreading
across both wrists.""",
        "two-concessions": """A panel split by a single vertical came line into two halves that are the same
scene resolved two different ways: on the left, a standing figure in cobalt; on
the right, the same figure as amber smoke. Both are backlit at the same
intensity, so neither reads as the correct one. The line between them is straight
and structural -- this one was agreed cleanly.""",
        "reclaimed-essence": """Something recovered out of what it had become: a figure kneeling over a spread of
plain glazing on the ground, drawing one recognizable form back up out of it, the
came reassembling around the shape as it rises. Backlit hard from below so the
recovered form is the brightest passage. Lead creeping up the kneeling figure's
forearm.""",
        "mirren-who-persuades-stone": """Mirren herself, the class leader, standing three-quarter view in a dark backlit
panel with one hand raised, palm out, toward a mass of cut stone that occupies the
right half of the picture -- and the stone is halfway through agreeing. Its lower
panes are heavy and dark; its upper panes are thin, pale and already letting light
through, and the boundary between the two is irregular and unfinished. She is a
silhouette of cobalt and amethyst with one amber pane at the heart. The came has
spread up her left forearm and under her jaw, and her left eye is a pane of
smoke-grey glass. She is entirely unhurried.""",
        "the-wider-argument": """The same persuasion made to several things at once: a panel in which four
separate objects at four corners are each partway into becoming something else,
and the came lines connecting them run across the whole picture as one continuous
network rather than four local ones. Backlit evenly. A single figure at the
center with both arms out, barely more than lead and shadow.""",
        "mirren-half-turned-to-smoke": """Mirren much further along, and it is the same panel logic doing it to her.
Standing full length, backlit, the right side of her still figurative in cobalt
and amethyst panes -- and the left side, from the shoulder down, already smoke:
thin pale glass with the light coming straight through and the came opening out
and letting go of the outline. Her left eye is gone entirely to grey. She is
standing perfectly upright and her expression has not changed. She has done the
arithmetic and finds the trade acceptable.""",
    },
)

CLASSES["15-runeblade"] = dict(
    display="Runeblade",
    label="RUNEBLADE",
    hero_who="the same man",
    hero_summary="The landscape face is Stave at rest at his own anvil; the portrait face is the "
                 "thing he is famous for, standing still while work he finished days ago goes "
                 "off, with the vertical format carrying the channels lighting up the blade.",
    front_desc="Stave at rest at the anvil",
    back_desc="work finished days ago, going off",
    style="""
Medium: damascened metal inlay. The ground of every image is real pattern-welded
steel -- watered-damascus swirl, the layered grain of folded metal -- and the
imagery is inlaid into it in gold and silver wire, cut in and hammered flush.
This is a photograph of a worked metal object, not a drawing.

Light: specular and anisotropic. Highlights streak along the grain of the steel
rather than pooling into round hot spots, and they move with the direction of the
pattern. The metal is polished but not mirror-bright.

Composition: knotwork borders that interlace with the subject, so that figure and
frame are one continuous line entering and leaving the picture. There is no
separate background -- the steel is the background and the subject is cut into it.

Signature: rune channels cut into the metal and glowing from within -- the only
light in this class that is not reflected. They are always already lit, and they
are the work of somebody who set this up earlier and has since moved on.

Ground: watered steel #6E7178 for the damascus, gold inlay #C9A227 and silver
#D6D9DE for the wire, ember channel #CE7A16 for the light inside the cut. Cool
metal, two warm notes, nothing else.

Register: a smith first and a caster second, and the distinction is meaningless
posturing. Methodical, literal-minded, quietly and enormously proud of work
nobody will ever notice. Nothing here wins the exchange it is in; it wins the one
three turns out, which was set up while you were watching something else.
""",
    hero_front="""Stave at rest, the class portrait, inlaid into a broad panel of
watered damascus steel. Full figure in three-quarter view at his anvil, hammer
down and resting on the face of it, one hand flat on the work -- not striking,
checking. The figure is cut in gold and silver wire and hammered flush with the
steel ground; the anvil, the tools and the knotwork border are the same
continuous inlaid line, so frame and man are one drawing. Anisotropic highlights
streak along the damascus grain behind him. Cut into the blade on the anvil, and
glowing ember-orange from inside the cut, a channel of runes that he finished
some time ago and is no longer thinking about. He looks quietly, enormously
pleased with a joint nobody will ever see.""",
    hero_back="""An action shot, and this class's action shot is deferred: the thing
going off is work he finished days ago and has already stopped thinking about. A
tall vertical panel of watered steel: at the bottom, Stave standing square and
entirely still, arms at his sides, not casting anything -- and running the full
height of the frame above him, a blade held point-up with every rune channel in
it lit at once, ember-orange light pouring out of the cuts and running up the
grain. The knotwork border has caught fire along its whole interlaced length, so
frame and blade are the same burning line. He is not looking at it. He is looking
out of the frame at whoever is about to find out. The steel's anisotropic
highlights streak the full height of the picture.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
the ground of every image is **real pattern-welded steel** — watered-damascus
swirl, the layered grain of folded metal — with the imagery inlaid into it in gold
and silver wire, cut in and hammered flush. These are photographs of a worked
object, not drawings of a scene, and there is no separate background: the steel is
the background and the subject is cut into it.

Two things carry it. The first is the light on the metal — specular and
anisotropic, streaking along the grain rather than pooling into round hot spots.
The second is the one light in the class that isn't reflected: rune channels cut
into the steel and glowing from within, ember-orange, **always already lit**,
because they are the work of somebody who set this up earlier and has since moved
on. Knotwork borders interlace with the subject throughout, so figure and frame
are one continuous line.

The register is in every file, and it is also the mechanic: nothing here wins the
exchange it is in. It wins the one three turns out, which was set up while you
were watching something else — and the smith is quietly, enormously proud of work
nobody will ever notice.""",
    subjects={
        "forge-sworn-ally": """Two figures inlaid side by side in gold wire on the damascus ground, one handing
the other a finished weapon across the knotwork border that links them. The
receiver's grip is already correct. A rune channel runs from the giver's hand
along the weapon's length and is lit ember-orange the whole way. Anisotropic
streak along the steel behind.""",
        "unmade-inscription": """A rune channel being closed: a cut in the steel that was glowing and is now being
hammered shut, silver wire driven into the groove and flushed off, the ember light
surviving only at the last few unclosed millimetres. A punch and hammer inlaid in
gold above it. The knotwork border stops dead where the channel ends.""",
        "binding-rune": """A single closed loop of rune channel inlaid around a wrist -- one continuous cut,
no beginning and no end, glowing ember-orange from inside. The hand below it is
open and still. The knotwork border repeats the same loop at four corners of the
panel, unlit. Watered grain running vertically behind.""",
        "cutting-rune": """A channel cut along a blade's edge in a line that does not follow the edge --
it crosses it twice -- glowing ember from within, with fine gold wire inlaid on
either side to fence it. The blade is inlaid into damascus that is itself
patterned, so two grains disagree across the panel. Knotwork border interlacing
through the guard.""",
        "journeyman-striker": """A young smith inlaid mid-strike in gold and silver, hammer at the top of the
swing, feet correct, on a ground of coarser damascus than the rest of the class
uses. Two rune channels on the anvil face below the work are already lit -- somebody
better than him prepared this piece earlier. Knotwork border joins his back foot
to the frame.""",
        "reforged-claim": """An inlay being lifted out of one panel and set into another: a length of gold
wire drawn up out of a groove in the steel at the left of the picture and laid
into a waiting groove at the right, still warm, the channel behind it going dark
and the channel ahead of it lighting up. Two knotwork borders, one closing and one
opening.""",
        "scarred-anvilhand": """A heavy figure inlaid full-length in silver wire whose old damage is worked as
gold: every scar on him is an inlaid line, and the deepest of them are cut through
as rune channels and lit ember-orange from inside. He is standing square. The
damascus grain runs straight through him. Knotwork border interlacing with both
forearms.""",
        "master-inlay": """A close panel of the finest work in the class: an intricate figure inlaid in gold
and silver wire at a density that could only have been done slowly, every line
flush, the seams invisible. One rune channel runs beneath the whole design and
lights it from underneath at the joins. Anisotropic highlight streaking hard
along the grain. Nobody is in the picture but the work.""",
        "stave-smith-first": """Stave himself, the class leader, inlaid three-quarter view in gold and silver
wire on a broad damascus panel, standing at the anvil with the hammer resting head
down on its face and one hand flat on the finished piece. He is not casting
anything and there is nothing magical in his posture. The knotwork border runs
into his shoulders and out through the anvil so the frame and the man are one
line. On the piece under his hand, four rune channels are cut and all four are
already lit ember-orange -- finished some time ago, and no longer his concern. He
looks quietly, enormously satisfied.""",
        "rune-transfer": """One lit channel moving from one object to another across the panel: the groove in
the first object closing and going dark behind, the groove in the second opening
and lighting ahead, the ember running between them along a thread of silver wire.
Two hands, one at each end, doing something delicate. Knotwork border passing
through both objects.""",
        "anvil-guard": """A broad standing figure inlaid frontal on the damascus ground with an anvil held
across the body like a shield, feet planted, the knotwork border thickened into
a barrier along the panel's whole lower edge. Rune channels run along the anvil's
horn and underside, lit, facing away from him. Anisotropic highlight across the
anvil's polished face.""",
        "three-turns-ahead": """The class's whole argument in one panel: a broad field of watered steel with an
inlaid figure standing calmly at one edge, hands empty, having plainly finished
his work -- and running away from him across the entire rest of the picture, a
network of rune channels cut into the steel and lit ember-orange at every
junction, arriving at three separate inlaid figures on the far side who have only
just noticed. The knotwork border carries the network out past the frame. He set
this up while they were watching something else.""",
    },
)

CLASSES["16-shapeshifter"] = dict(
    display="Shapeshifter",
    label="SHAPESHIFTER",
    hero_who="the same person",
    hero_summary="The landscape face is Pelt at rest, or as close to a person as they get; the "
                 "portrait face is the thing they are famous for, the winter's worth of "
                 "waiting spent in one stroke, with the vertical format carrying the drop.",
    front_desc="Pelt at rest, or nearly a person",
    back_desc="a winter of waiting spent in one stroke",
    style="""
Medium: sumi-e ink wash on unbleached paper. One continuous loaded stroke per
form -- no correction, no second pass, no outline-then-fill. The brush is visibly
loaded at the start of a stroke and visibly dry at its end, splitting into
separate bristle trails where it runs out.

Light: none. Value is ink dilution and nothing else -- there is no light source,
no highlight and no cast shadow anywhere in this class.

Composition: enormous empty ground. The subject is placed hard off-center with
all the weight in one corner, and two-thirds or more of the paper is left
completely untouched. The emptiness is not background; it is the larger half of
the composition.

Signature: the form never fully resolves. A human shoulder becomes an elk foreleg
within the same stroke, and there is no point you can put a finger on where the
change happens -- because the brush never lifted. Every card must contain one such
stroke.

Ground: black ink #1C1A18 at full strength, cold slate wash #5C7488 in the
dilutions, raw paper #E6E0D2 for everything untouched, and exactly one vermilion
#B03A2E seal mark, small, in a corner -- the only color in the image and never
more than one.

Register: forty words total. Nothing here is explained, nothing is decorated and
nothing is performed. Trusts animals immediately and people provisionally, and
has never been given cause to revise either policy.
""",
    hero_front="""Pelt at rest, the class portrait, and as close to a person as they
get. A single figure placed hard into the lower-left of an enormous empty field
of raw paper, crouched on their heels, forearms on knees, absolutely still. Two
or three loaded strokes make the whole body. Within the stroke that runs from the
neck down the near arm, the form stops being a person: it thickens, the wrist
becomes a foreleg and the hand a hoof, and there is no point at which the change
can be said to happen because the brush never lifted. The head is a person's and
the eyes are not quite. Nothing else on the paper. One small vermilion seal in
the far corner.""",
    hero_back="""An action shot, and for this class the action is one winter's worth
of patience spent in a single stroke. A tall vertical sheet, almost entirely
empty: at the very top, small, a suggestion of the branch that has just been left;
and falling the whole height of the paper, one continuous loaded brushstroke that
begins as a crouched human shape and finishes, at the bottom of the frame, as
something with its mouth open and its forelegs out -- the change occurring inside
the stroke, unlocatable, because the brush did not lift once between the top of
the page and the bottom. The stroke is loaded and black where it starts and split
and dry where it lands. Below and around it, nothing at all: raw paper. One
vermilion seal, small, in the lower corner.""",
    enforces="""Straight from the class bible, so the cards and the bible cannot drift apart:
sumi-e ink wash on unbleached paper, **one continuous loaded stroke per form** —
no correction, no second pass, no outline-then-fill — with the brush visibly
loaded at the start and visibly dry and splitting at the end. And no light at all:
value is ink dilution and nothing else, so there is not one highlight or cast
shadow in the class.

Two things carry it. The first is emptiness — the subject sits hard off-center
with the weight in one corner and two-thirds or more of the paper left completely
untouched. The emptiness is the larger half of the composition, not the
background. The second is the signature every card must contain: a form that never
fully resolves, where a human shoulder becomes an elk foreleg *within the same
stroke* and there is no point you can put a finger on where the change happens,
because the brush never lifted.

The palette is three inks and one color: exactly one small vermilion seal mark per
image, never more. And the register is in every file — nothing here is explained,
decorated or performed.""",
    subjects={
        "borrowed-shape": """One stroke that begins at the top as a human forearm and ends at the bottom as
something else's limb entirely -- fur, joint reversed, claw -- with no seam
anywhere along it. The rest of the sheet is untouched. The stroke is loaded and
wet at the top and split dry at the bottom. One vermilion seal, small, far
corner.""",
        "packmate": """Two animal forms placed close together in the lower-right of an empty field, each
made of a single stroke, the second overlapping the first where they touch. One of
them has a shoulder that is not an animal's. Neither is looking at the viewer.
Vast raw paper above and to the left.""",
        "sizing-up": """A single crouched form at the very edge of the sheet, most of the composition
given to the empty ground it is looking across. The form is small, low and
compressed, and one long dry-split stroke leaves it and runs out into the paper --
the measure being taken. Nothing at the other end. One vermilion seal.""",
        "lick-the-wound": """An animal curled hard into one corner of an otherwise empty sheet, head turned
back to its own flank, made of two strokes. Where the head meets the flank the
ink is at full black and slightly pooled -- the only heavy passage on the paper.
The rest runs out dry. The turned head is briefly a person's and then is not.""",
        "pack-ambush": """Three forms arriving from one corner at once, all made of strokes running the
same direction, all still mostly dry-split -- they are not fully there yet. The
opposite two-thirds of the sheet is untouched. One of the three has a hand where
the others have paws, in the middle of a stroke that does not stop.""",
        "outnumbered-hunter": """A single small form at the bottom of a very large empty field, low and turned
side-on, with nothing else drawn -- but the composition weighted so heavily to the
empty side that the absence is what is closing in. One stroke for the body. The
shoulder is a person's for perhaps two centimetres of it. One vermilion seal.""",
        "winter-patient-stalker": """One long horizontal stroke across the lower quarter of the paper -- a body lying
prone and completely still -- loaded at one end and drying out along its entire
length, the split bristle trails reading as fur or as frost. Above it, the whole
sheet is empty. The far end of the stroke has a hand in it. It has been here
longer than anything else in the class.""",
        "answering-the-call": """A form rising out of a crouch at the sheet's edge, drawn in a single upward
stroke that thickens as it goes -- starting animal and finishing standing and
nearly human, with no locatable transition. The rest of the sheet is raw paper.
The brush is at its wettest at the top of the stroke, which is unusual and
deliberate.""",
        "shape-of-the-season": """Four small forms placed along one diagonal in an empty field, each a single
stroke, each a different animal -- and read left to right they are plainly the
same creature four times. Where each one's shoulder sits, the ink is identical.
Nothing else on the paper. One vermilion seal at the lower end of the diagonal.""",
        "long-wait-ended": """A form that has been still so long the paper around it has been left completely
untouched -- and is now, in this instant, uncoiling: one enormous stroke through
the empty field from the corner where it was to the middle of the sheet, wet and
black at the start and split dry where it arrives. The waiting is what the
emptiness records.""",
        "pelt-who-waits-out-winter": """Pelt themself, the class leader, placed hard off-center in an enormous empty
field, crouched low with the weight in one corner and two-thirds of the sheet
untouched. Two or three loaded strokes make the entire figure. The stroke running
from the shoulder down the near arm changes as it goes -- person, then not, then
person again -- without lifting once, and there is no point at which it can be said
to happen. They are looking out of the frame at something the viewer cannot see
and have plainly been looking at it for a very long time. One vermilion seal,
small, in the far corner.""",
        "everything-becomes-teeth": """The heaviest ink in the class: a mass at one corner of the sheet made of a
single enormous stroke that has been overloaded, black and pooling, and which
resolves along its length into nothing but jaws -- several sets, at several
scales, none of them separable from the others because it is one stroke. Where
the brush finally runs out it splits into a dozen dry trails. Two-thirds of the
paper untouched. One vermilion seal.""",
    },
)
