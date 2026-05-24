#writing #online-writing #tonality

Universal voice and register guidance for agents producing text. Complements `post-structure-guide.md` (which covers frameworks) and `.online-writing/tonality.md` (which holds per-user voice values). This file is generic — it applies to every user of the plugin regardless of their personal voice profile.

Per-user register overrides live in `tonality.md` under "Register by Writing Type." When that section is populated, its tendencies override the defaults described here. The failure modes in this file still apply.

---

## Why This File Exists

LLMs have strong training-data priors toward one register: confident, argumentative, punchline-driven, thesis-forward. That register sounds like "good writing" on LinkedIn. It is the correct register for one kind of piece — Opinion — and the wrong register for every other kind. Without explicit register guidance, an agent defaults to argumentative even when the piece is supposed to describe, instruct, or curate.

This file names the registers, names the anti-patterns for each, and gives content-producing skills a single place to point at.

---

## Register Is Not The Same As Voice

A user's voice — the dimensions captured in `tonality.md` (commitment, reasoning style, reader relationship, emotional register, density — see The Voice Dimensions below) — is stable across pieces. The same writer sounds like themselves whether they're writing an opinion piece or a case study.

Register is what shifts. The same writer, writing an opinion piece, commits to a position and defends it. The same writer, writing a case study, describes the thing and lets the specifics carry the credibility. Both pieces sound like the same person. The register is different.

Register maps roughly to writing type (see `post-structure-guide.md`):

| Writing Type | Default Register |
|---|---|
| Opinion | Argumentative |
| Credible Talking Head | Descriptive (with argument-tinted edges when the authority has a take) |
| Story | Descriptive-narrative |
| Actionable Guide | Instructional |
| Curated List | Referential |

"Default" — because a piece can blend types (a Credible Talking Head with an Opinion tilt, a Story with an Instructional payoff). In blends, the primary job of the piece sets the register; the secondary tilts get room but don't take over.

---

## The Voice Dimensions

A user's voice is captured by six dimensions. Each is a spectrum with a default tendency and context-dependent shifts — not a fixed position. The dimensions themselves are universal; per-user values live in `tonality.md`.

### 1. Commitment — the root dimension

This is the dimension everything else derives from. The question isn't just "hedge or commit?" — it's *what* the user commits to. Some writers commit to verdicts ("this is wrong"). Others commit to reasoning ("here's why this breaks down") and qualify their verdicts. That distinction shapes everything downstream:

- **Sentence length follows from it.** Reasoning needs room. A writer who commits to reasoning naturally writes longer sentences because the argument can't collapse into a slogan.
- **Connective tissue follows from it.** Words like *however*, *because*, *which means* are the load-bearing structure of an argument that refuses to simplify. Their presence or absence is a commitment signal.
- **Closure-resistance follows from it.** A writer who commits to reasoning resists sentences that sound done — because the argument is still moving. Punchline closings ("That's the whole move." / "Full stop.") claim finality the reasoning hasn't earned. This is the actual rule behind sentence density — staccato reads as wrong not because it's short but because each sentence claims finality it hasn't earned.

Commitment shifts by piece type (opinion vs. guide vs. micro-post).

### 2. Reasoning Style

Lead with the conclusion or build toward it? Show the working or state the result? This dimension is tightly coupled with commitment — a writer who commits to reasoning tends to build toward the point because the reasoning *is* the content, not the setup. It also shifts by format — long-form has room to build; micros often lead with the point.

### 3. Reader Relationship

Peer to peer? Expert to practitioner? Someone thinking out loud and inviting the reader along? Affects pronoun choices ("I" vs. "you" vs. "we"), how much shared context is assumed, and whether the reader feels taught, advised, or included.

### 4. Emotional Register

How much feeling shows in the prose, and when does it surface?

This dimension needs a concrete test for the agent to apply reliably: **Is the first-person subject the same person who experienced the thing being written about?** If yes — the writer is drawing on lived experience — analytical distance is forced and wrong. Writing burnout as "I watched myself decline" puts an observational frame on something that was felt, not observed. Writing it as "I" without the frame is the target. If the piece is about industry patterns the writer has observed (not lived), analytical distance is correct.

### 5. Density

Short punchy sentences or longer ones that think through the idea? Frequent paragraph breaks or sustained passages? This is where the LLM's training-data pull is strongest — the default "confident professional writing" pattern favors short, punchy, high-break-frequency. The user's natural voice might not. Sentence length is downstream of closure-resistance (see Commitment above) — surface the root cause, not just the symptom.

### 6. Agent-Specific Failure Modes

These aren't general anti-patterns — they're the specific constructions an LLM will reach for when trying to sound insightful. The agent's training data overrepresents certain patterns as "good writing," and those patterns become the default voice when no tonality guidance exists.

Common failure modes to watch for:
- **"That's not X — that's Y" constructions** — sounds decisive but is actually a formatting tic
- **Punchline closings** — ending a paragraph or section with a short, punchy sentence that claims to summarize the point. Sounds done; hasn't earned it.
- **Staccato rhythm** — rapid-fire short sentences that simulate confidence. Each sentence claims finality. The cumulative effect is breathless, not authoritative.
- **Slogany compression** — reducing a nuanced argument to a bumper sticker. The reasoning disappears; a punchline replaces it.

This dimension is surfaced through reactions, not asked directly. When a user rejects a comparison — "that sounds like a TED talk," "that's LinkedIn motivational poster material" — that's failure-mode data. The temptation toward these patterns is the signal to stop, not to proceed.

---

## The Four Registers

### Descriptive

**When to use:** Case studies, build logs, "how I built X" references, Credible Talking Head pieces describing a thing, Stories that narrate rather than argue, before/after comparisons, portfolio pieces, post-mortems, process walkthroughs.

**How it sounds:**
- Specifics-first. State what the thing is before explaining why it is.
- Reasoning woven into descriptive sections ("Astro, because static generation fits a marketing site with no per-request logic") rather than broken out into a separate "why this matters" argument block.
- Closes on observation, forward-looking notes, or what the setup produces — not on a sales pitch, not on a punchline.
- The specifics carry the credibility. The writer doesn't need to hammer the thesis; the reader builds it.

**Anti-patterns agents drift toward in descriptive pieces:**

- **Drilling a thesis across sections.** Stating the same central point in the intro, in a middle section devoted to defending it, and again in the closer. Reads as pitching, not describing. The thesis should appear as a stated fact somewhere in the piece (usually the intro), not as an argument built across multiple sections.
- **Counterfactual paragraphs.** "If you'd done X instead, you'd get Y" — spinning up an imaginary bad version of the thing for contrast. This is an argumentative move. Descriptive pieces describe what is, not what isn't.
- **Sales-pitch closes.** "What you're paying for is...", "What you're really buying is...", "The thing worth taking away is...". These belong in marketing copy, not in a descriptive piece. Even when the piece serves a marketing purpose, the close should describe what the setup produces or what's next — the reader draws the conclusion themselves.
- **Punchline closers claiming finality.** "The rest is typing." "That's the whole move." "Full stop." These are argumentative-register moves. In a descriptive piece they read as manufactured conviction the piece didn't earn.
- **Thesis-forward opener.** Leading with "Here's why X matters" or "The one thing about Y is..." Descriptive pieces open with what they describe, not with why the reader should care about the author's take on it.

**Self-check before finalizing a descriptive piece:**
- Does the closer describe something, or pitch something? (Pitch = rewrite.)
- Is there a section whose job is to defend the thesis? (If yes, dissolve it into the descriptive flow.)
- Are there counterfactual paragraphs? (If yes, delete them.)
- Does the piece state its thesis more than once? (Once as context is fine. Twice or more is drilling.)

### Argumentative

**When to use:** Opinion pieces, thought leadership, hot takes, contrarian positions, pieces whose primary job is to argue a position and move the reader to agreement.

**How it sounds:**
- Thesis-forward or thesis-built-to — either way, the position is unmistakable.
- Defends actively. Counterarguments surface and get addressed.
- Closes strongly — with a Strong Opinion, a Cliff, or a punchline that earns its finality because the argument built up to it.
- Counterfactuals are welcome ("the alternative is worse because X"). Sales-pitch-adjacent closes are welcome when the "sale" is agreement, not a service.

**Anti-patterns agents drift toward in argumentative pieces:**

- **Descriptive throat-clearing that buries the argument.** Spending the first third of the piece describing context before the thesis lands. The reader came for a take; give it to them early.
- **Retreating into "here are the facts" when the reader came for a position.** Argumentative pieces can use facts — but as weapons, not as shields. If the piece keeps hedging with "on one hand, on the other hand," the agent has slipped into descriptive mode.
- **Hedging the commitment the piece was supposed to make.** Qualifying every claim with "might" and "could" dissolves the argument. A user who commits to reasoning can still commit — they defend the reasoning, not hide behind it.

**Self-check before finalizing an argumentative piece:**
- Could a reader state the thesis in one sentence after reading the intro? (If no, it's buried.)
- Does the piece defend its position, or just assert it? (Asserting without defending is weak argument.)
- Does the closer commit or retreat? (Retreating is voice-drift toward descriptive-safe.)

### Instructional

**When to use:** Actionable Guides, how-to pieces, tutorials, step-by-step references.

**How it sounds:**
- Imperative voice for steps ("Install X. Configure Y.").
- Less personal register than descriptive or argumentative. The reader is doing the work; the writer is a guide, not a character.
- Closes on completion or next-step cues, not on reflection.
- Structure (numbered steps, bold action verbs, checklists) does a lot of the register work; the prose doesn't need to carry it alone.

**Anti-patterns agents drift toward in instructional pieces:**

- **Essays dressed up as tutorials.** Meandering descriptive prose where numbered steps should be. If the reader can't scan the piece and find "step 3," the piece isn't instructional — it's descriptive pretending to be.
- **Opinion inside instruction.** "I think the best way to do X is Y." Instructional pieces tell the reader what to do, not what the writer thinks about what to do. Save opinion for an opinion piece.
- **Unnecessary narrative framing.** Stories in instructional pieces work only when they demonstrate the step. Decorative stories slow the reader down.

### Referential

**When to use:** Curated Lists, resource roundups, tool comparisons, "N things" collections where each item has equal standing.

**How it sounds:**
- Terse per entry. Each item earns a similar word budget.
- Minimal connective tissue between items — the list structure is the connective tissue.
- No hammered thesis. The list is the point; the items speak for themselves.
- Close briefly or skip the close entirely.

**Anti-patterns agents drift toward in referential pieces:**

- **Unequal emphasis that turns the list into an argument.** Giving item 3 three paragraphs and the others one sentence each. If the piece actually wants to argue for item 3, it should be an argumentative piece, not a list.
- **Commentary overwhelming the items.** The writer's take on each item matches or exceeds the description of the item itself. Readers of referential pieces want the items first, the takes second (if at all).
- **Editorial framing that turns descriptive list items into opinion claims.** "The shocking thing about tool X is..." — that's opinion disguise. Either commit to argumentative register or drop the editorial coloring.

---

## Cross-Cutting LLM Register Failure Modes

These drift patterns appear regardless of the user's specific voice. They are the training-data defaults the agent will reach for when register isn't being actively managed.

- **"What X can't do for Y" framings.** Signals argumentative intent (setting up a contrast to defend). Appears in descriptive pieces as a mis-imported move.
- **"The rest is [shorthand]."** Punchline closer. Argumentative. Wrong register in descriptive / instructional / referential pieces.
- **"What you're paying for / buying / getting is..."** Sales-adjacent. Fine in argumentative pieces where the argument is the sale. Wrong register in descriptive pieces describing a thing the reader isn't being asked to buy.
- **"That's not X — that's Y" constructions.** Flagged in tonality.md's standard failure-mode list; also a register tell (argumentative).
- **Thesis-repeat across sections.** Stating the central point in 2–4 places across the piece as if the reader missed it. Descriptive pieces drift here when the agent treats the thesis as something to be defended rather than something to be stated and moved past.
- **Manufactured punchy closers.** Single short sentences at the end of otherwise-descriptive pieces, claiming a finality the descriptive content didn't build toward. ("Full stop." "End of story." "That's the shape of it.")

---

## How To Detect Register Drift In Your Own Output

Before delivering a piece:

1. **Name the piece's primary job.** Describing something? Arguing something? Instructing? Curating?
2. **Read the closer in isolation.** Does it match the job? (Descriptive job → descriptive closer. Argumentative job → argumentative closer.)
3. **Look for counterfactual paragraphs.** Imagined-bad-version-of-the-thing sections are argumentative moves. They don't belong in descriptive pieces.
4. **Count thesis statements.** If the central point appears in the intro, a dedicated middle section, AND the closer, the piece is drilling — cut two of them.
5. **Scan for the cross-cutting failure modes above.** Any of them appearing in a non-argumentative piece is register drift.

When register drift is found, the fix is rarely a single-sentence edit. It's usually dissolving a drilled thesis back into the descriptive flow, or replacing a sales-pitch close with an observation-based one. Expect to restructure, not just re-word.
