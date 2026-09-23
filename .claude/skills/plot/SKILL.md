---
name: plot
description: Builds and diagnoses plot - what happens, in what order, and when and through whom the audience finds out - using the owner's Gap theory of narrative, with the Anticipation theory for suspense and fear. Use this whenever someone is turning an idea into a plot, outlining, ordering events or scenes, planning a twist, reveal, mystery or ending, choosing a narrator or point of view, or says a story "sags", "drags", "has no tension", "isn't scary", "the twist doesn't land", "I saw it coming", "the ending falls flat", "too much exposition", "is my narrator cheating", "should I tell it backwards", "where should it start", "what should I hold back" or "what is it about", even if they never say the word plot. Also for premise, theme, symbols and scene order. Not for building a world's rules or places (story-world), making readers care about a person (character), wording lines of talk (dialogue), a genre's promised beats (genre), or critiquing a whole work (story-critique leads).
---

# Plot

A story is what happens. A plot is the order, selection and emphasis in which the audience finds it out. This skill builds plots and diagnoses them with the owner's Gap theory: a narrative is a stack of gaps that open and close over time, and the plot's job is to schedule them. It covers the breach and how it escalates, reveals, twists, mysteries and wonders, suspense and fear, narrators and point of view, endings, premise, theme, symbols, and the order and making of scenes.

**Built on.** The primary source is `sources/gap-theory-of-narrative.md`. This skill derives from it and does not change it; read the full text once per conversation before a first full run. `sources/anticipation-theory.md` is this skill's second source, registered in `sources/README.md` as the source of its suspense module: it is the frame of `references/suspense-and-fear.md`, and should be read in full before that module's first full use. The skill also draws on the Implied World theory (`sources/implied-world-theory.md`): plot schedules facts about the world as well as the story, and the world's main departure should embody the story's question (its *thematic fit*). And on the Bond theory (`sources/bond-theory.md`): care is the first term of the suspense equation and has to be built before the threat. Three craft books fill in method in the modules, always in the workshop's own words: Truby, *The Anatomy of Story*; Egri, *The Art of Dramatic Writing*; McKee, *Dialogue*. Where a book disagrees with a theory, the module follows the theory and records the book's view as a rival.

**Words.** The theory's terms are used exactly as it defines them. *World*: what is possible, normal and valued. *Story*: what happens, in the order it happened, inner change included. *Plot*: the order, selection and emphasis in which the audience learns the story and the world. *Telling*: who or what delivers the plot (a narrator, a point-of-view character, a camera), with what knowledge and what bias; this skill calls that deliverer the *teller*. *Narrative*: the whole. The five gaps are *departure* (reality against the world), *breach* (the world's normal against what happens), *withholding* (story order against plot order), *perspective* (what happened against what the teller says) and *knowledge* (what the audience knows against what the characters know). Named with its layer (*the knowledge gap*), a gap is one of these five. The theories also say *gap* for any single open question inside a layer (Sternberg's suspense is "a gap about the future"; each rung of the fear ladder closes one), and this skill follows them in that looser use. (The Implied World theory also says *gap* for something left unfilled on purpose; at the level of plot the Gap theory calls such an open question a *wonder*.) Three plain words are added: a *fact* is anything about the story or world the audience can learn; a *reveal* is the moment a withheld fact reaches the audience, a character, or both; a *turn* is a point where the story changes direction.

## The idea in one example

*Romeo and Juliet*. The story: two teenagers from feuding houses marry in secret. A street fight kills her cousin and gets him banished. She takes a drug that makes her seem dead, so she can slip away to him. The message explaining the plan never reaches him. He finds her in the tomb and kills himself; she wakes and does the same. The feud ends over their bodies.

Shakespeare's plot opens by telling the audience how it ends. That throws away one question (will they live?) and buys two things. Uncertainty moves from *whether* to *how*, so every hopeful moment is watched from above. And in the tomb the audience knows what Romeo does not: she is asleep. That is the knowledge gap with the audience ahead, which the Anticipation theory calls the suspense of helplessness. We fear *for* him and cannot warn him.

Now keep the story and change the plot. Withhold the ending and the sleeping-drug plan. The tomb becomes a surprise: a few seconds of it when she wakes, instead of a whole last act of helpless suspense. The events are the same; the narrative is not. The plot chose which gap the audience would live in.

Then test the choices with `hard-to-vary`. *Remove* the lost message: Romeo learns the plan, and the deaths do not happen, so the turn is held in place by it. *Swap* why it is lost (the play's quarantine for, say, a lame horse): the turn still happens. What is held is that it fails by chance, not by anyone's will; a villain who intercepted it would make a different story. *Flip* the settlement: the lovers live and the feud goes on. Now the ending gives the opposite answer to the question the world poses (can love live inside a feud?), so the play would mean something else.

## Where to look, and when

This file holds the method. The modules hold detail; open one only when its row applies.

| You are... | Open | To get |
|---|---|---|
| turning an idea into a plot, or adding a part | "The procedure" below, building | the order of decisions, from normal to settlement |
| looking at a draft where something feels wrong | "The procedure" below, diagnosing | symptom first, then which gap |
| working on a small story, or wanting a quick check | "The quick version" below | four questions |
| making a scene tense or frightening, or finding out why it is not | `references/suspense-and-fear.md` | the four terms, the fear ladder, knowledge positions, the ratchet, residue, prose against film |
| deciding when a fact comes out: a twist, a mystery, a clue, backstory, exposition, a set-up and its payoff | `references/reveals-and-withholding.md` | suspense, curiosity and surprise; mystery against wonder; reveals in sequence; exposition as ammunition; fair and unfair withholding |
| choosing who tells it: a narrator, a point of view, a frame, an unreliable teller | `references/telling-and-perspective.md` | kinds of teller and their settings, the character-narrator, fair play, what each medium makes cheap |
| making the breach escalate: the opening, the middle, crisis, climax, the jobs a plot must get done | `references/structure-and-conflict.md` | the core jobs of a plot, kinds of conflict, where to start, crisis, climax and resolution |
| working out what the story means, or stating a premise | `references/premise-and-theme.md` | premise, moral argument, and theme as settlement |
| ordering scenes, or building one | `references/scenes.md` | scene order and weave, scene construction, beats and turns |
| using an image or object that keeps coming back | `references/symbols.md` | how a symbol gathers meaning, and how it ties to theme |
| testing one plot choice (a reveal's timing, a turn's cause), or whether it does any work | Building step 8 below; `.claude/skills/hard-to-vary/SKILL.md`, section 5 of its `references/by-domain.md` | remove, move, swap, flip, two routes |

```mermaid
flowchart TD
  S["What is in front of you?"] --> Q{"A new plot, a draft, a small case, or one choice?"}
  Q -->|new, or adding a part| B["Building, in this file"]
  Q -->|a draft, something feels wrong| D["Diagnosing, in this file"]
  Q -->|a small story or quick check| K["The quick version, in this file"]
  Q -->|one choice to test| H["8 hard-to-vary skill: test each choice"]
  B --> I["1 place the idea"]
  I --> N["2-3 normal, breach, story"]
  N --> SC["4 schedule of knowledge"]
  SC --> T["5 teller"]
  T -.->|may send you back| SC
  T --> KP["6 knowledge position"]
  KP --> SE["7 settlement"]
  N -.-> SCC["structure-and-conflict.md"]
  SC -.-> RW["reveals-and-withholding.md"]
  T -.-> TP["telling-and-perspective.md"]
  KP -.-> SF["suspense-and-fear.md"]
  KP -.-> SN["scenes.md"]
  SE -.-> PT["premise-and-theme.md"]
  PT -.-> SY["symbols.md"]
  D --> G{"Which gap, or the settlement?"}
  G -->|departure| SW["story-world skill"]
  G -->|breach| SCC
  G -->|withholding| RW
  G -->|perspective| TP
  G -->|knowledge| SF
  G -->|settlement| PT
  SE --> H
  G --> H
```

**Keeping the map true.** When a module is added, split or changed, update the table and the graph in the same edit. A module with no row is unreachable: give it a row or remove it.

**What belongs in this skill.** One test for any addition: does it help decide what happens, in what order, or when and through whom the audience learns it? How a world works goes to `story-world`, why the audience cares about a person to `character`, how a line is worded to `dialogue`, what a genre promises to `genre`. When in doubt, leave it out and say why.

## The stance

- **The audience rebuilds; it is never handed anything.** It infers the world from what is shown and the story from the plot (the theory's *nested inference*). Plan both inferences.
- **One story, many plots.** Before changing what happens, ask whether changing when the audience learns it would fix the problem.
- **Emphasis is a promise.** A question the telling lingers on, that characters chase and that keeps coming back, is a *mystery* and must be answered. One mentioned in passing and never pressed is a *wonder* and must be left open.
- **The teller sets the fair limits.** Hold back only what this teller could not know or would not say, or a wonder that was never promised an answer.
- **Show the normal before breaking it.** The world sets the price of the breach, and the audience has to see what could be lost before the threat arrives.
- **Books fill in; the theories decide.** Most book rules are fitted from past plays and films. Use them as patterns to question, and record where one rivals a theory.
- **Every load-bearing choice should be held in place.** A reveal that could come anywhere, or a turn whose cause could be cut without loss, is loose.

## The procedure

Read `sources/gap-theory-of-narrative.md` before a first full run in a conversation.

### Building

Work in this order of logic, not necessarily the order of writing. Each step names the module with the detail.

1. **Place the idea.** An idea usually arrives as one piece of the stack: a strange world (the departure gap), a situation (the breach), a person who wants something (the story), a secret or twist (withholding), a voice (perspective), a scene where the audience knows more than the characters (knowledge), or an ending (the settlement). Name which piece it is, then build outwards through the steps below.
2. **The world's normal, and what breaks it.** Write the normal in two or three lines: what is possible, normal and valued here, and what things cost. Then the breach: what happens that breaks the world's *own* normal. In *The Hunger Games* a child's name drawn for the arena is routine, the normal; a girl volunteering in her sister's place is the breach, because in her district nobody volunteers. A breach that could happen in any world has arbitrary stakes. Building the world itself: `story-world`. Where to open, and how the breach escalates: `references/structure-and-conflict.md`.
3. **The story, in the order it happened.** Who wants what, what resists, what changes, inner change included. Write it in time order, starting before page one: the events that make waiting impossible when the plot opens belong to the story even if the plot never shows them. Want, need and care: `character`. The jobs a plot must get done: `references/structure-and-conflict.md`.
4. **The plot: a schedule of knowledge.** List the key facts of story *and* world. For each, write when the audience learns it, from whom, and with what emphasis. Draft this with a working teller in mind; step 5 may send you back. Choose its interest on purpose: *suspense* (they know what is at stake but not how it ends: show it early), *curiosity* (something happened that they have not been told: withhold a past fact) or *surprise* (they did not know there was a question: plant, hide, reveal). Then mark every open question as a mystery or a wonder and check that the emphasis matches. Detail: `references/reveals-and-withholding.md`.
5. **The teller.** Who or what delivers the plot, what they know and when they know it, and their bias. From that, write down what may fairly be held back. Then check step 4 both ways. Everything it holds back needs a fair ground: this teller could not know it, would not say it because of who they are, or it is a wonder. Everything it puts the audience ahead on must be something this teller can deliver, or use one of the three routes in `references/telling-and-perspective.md`, section 5. Where either check fails, change the schedule or the teller. Detail: `references/telling-and-perspective.md`.
6. **The knowledge position, scene by scene.** For each major scene: does the audience know more than, the same as, or less than the characters, and about what? Choose on purpose, and plan where, or whether, it shifts. Detail: `references/suspense-and-fear.md`; scene order and construction: `references/scenes.md`.
7. **The settlement.** Which mysteries close, which wonders stay open, how the normal at the end differs from the normal at the start, and what that cost. The theme is the story's answer to the question its world poses: write the question in one line and check that the ending answers it. Detail: `references/premise-and-theme.md`; images that carry it: `references/symbols.md`.
8. **Test each load-bearing choice** with `hard-to-vary` (section 5 of its `references/by-domain.md`). For every turn, *remove* its cause: would the turn happen anyway? Then it is placed, not caused. For every reveal, *move* it earlier and later: if nothing changes, its timing is loose. *Flip* the ending, two ways. If the story would mean the same, the settlement is doing no work. If the same set-up could lead just as convincingly to the opposite ending, the ending is not yet earned. *Two routes*: if two reveals or scenes do one job, keep both only if each has a second job.

### Diagnosing

1. **Pin down the symptom before explaining it.** To whom (which reader, which kind of reader), where (the page, scene or minute it starts), compared with what (what they expected, an earlier draft, a work that does it). "It drags" is not yet a symptom. "Two of three readers stopped in chapter six, where the earlier draft had the letter scene" is.
2. **Find which gap is mismanaged, or whether the settlement is.** First guesses, each to be tested:

| Symptom | Check first | Then open |
|---|---|---|
| "generic", "could be anywhere" | departure | `story-world` |
| "nothing is at stake", "why does this matter" | breach: the normal not shown, or its price not set by the world; or care | `references/structure-and-conflict.md`; `character` |
| "confusing", "info-dump", "I saw it coming", "the twist is cheap" | withholding | `references/reveals-and-withholding.md` |
| "the narrator cheated", "flat voice", "whose story is this" | perspective | `references/telling-and-perspective.md` |
| "no tension", "not scary", "I never worried" | knowledge, and the four terms of suspense | `references/suspense-and-fear.md` |
| "sags in the middle", "episodic" | the breach not escalating; or no new facts arriving | `references/structure-and-conflict.md`; `references/scenes.md` |
| "the ending falls flat", "so what" | settlement | `references/premise-and-theme.md` |

3. **Ask the theory's five questions** of the draft. What is the normal, and what breaks it? Which open questions are mysteries and which wonders, and does the emphasis match? In each major scene, what does the audience know that the characters do not, and the other way round? Is anything held back "only because I want a twist, rather than because the teller couldn't or wouldn't say"? What has changed from the opening normal, and what did it cost?
4. **Build the rival diagnosis and tell the two apart.** Most symptoms have two plausible gaps. "No tension" may be the knowledge position, or no care. Name a change that would fix one and not the other: if letting the audience see the threat a scene earlier would help, the knowledge position was wrong; if more of the normal before the threat would help, care was. (If worse odds would help, a third candidate, uncertainty, was low.) Try the cheaper change first, on paper.
5. **Fix the smallest thing that answers the symptom,** then check the fix against the symptom as pinned in step 1, and against the nearby scenes it must leave alone.
6. **Hand off** where the question crosses over: a world's rules to `story-world`, caring about a person to `character`, the wording of a line to `dialogue`, a genre's promised beats to `genre`. For a critique of a whole work, `story-critique` leads if it is available, and this skill is consulted on its own area.

## The quick version

For a small case, four questions are enough. For a single choice (a reveal's timing, a turn's cause), use Building step 8 instead.

1. What is the world's normal, and what breaks it?
2. Take the fact that matters most. When does the audience learn it, and is that suspense, curiosity or surprise on purpose?
3. Is each open question a mystery or a wonder, and does the emphasis match?
4. By the end, what has changed from the opening normal, and what did it cost?

## Traps

- **Calling a list of events a plot.** Events in time order are the story. The plot is the schedule of what the audience learns; until that exists, nothing has been plotted.
- **Holding back only for a twist.** If the teller could know it and would say it, and it is not a wonder left open, hiding it is cheating, and a second reading shows it.
- **Emphasis that promises what the ending will not pay.** Pressing a question you mean to leave open is betrayal; explaining a wonder is deflation.
- **Surprise by default.** A hidden threat buys seconds; a shown one buys minutes. Truby's method hides the opponent's attacks; check each against the suspense it could have bought instead.
- **A breach with no normal.** Opening on the explosion before the audience knows what could be lost. See the rival with Egri in `references/suspense-and-fear.md`.
- **Explaining before the symptom is pinned.** An account of "it drags" that does not say where and for whom cannot be wrong, so it cannot help.
- **Adding conflict to every flat stretch.** Egri puts boredom down to missing conflict. The workshop reads the owner theories as naming other causes: no care, no uncertainty, no time (the threat not shown early enough), too many new things to learn at once (the Implied World theory's attention budget).
- **Letting a checklist decide.** Truby's steps and Egri's build order are fitted from past plays and films. A missing step is a question to ask, not a fault to fix.
- **Cutting the world to serve the hero.** A filter that removes every scene not moving the hero can strip out the world's own business, which the Implied World theory says makes it feel real. Keep that texture inside the scenes that stay.
- **Settling everything, or nothing.** Close every gap and nothing stays with the audience; close none and the events never become a shape.
