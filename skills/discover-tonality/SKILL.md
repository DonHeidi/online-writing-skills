---
name: discover-tonality
description: >
  Use when the user's writing output sounds generic, AI-generated, or misaligned with their natural voice —
  or when they explicitly ask to define, revisit, or sharpen their writing tonality. Also use when content-
  producing skills (create-post, create-draft, distill, etc.) consistently produce output that "doesn't sound
  like me." Also use when output register mismatches the piece type — for example, a case study reading as
  an opinion piece, a descriptive build log drilling a thesis, instructional content meandering into essay,
  or a curated list turning into an argument for the favourite item. Not for defining what to write about
  (see discover-purpose) or which topics to own (see discover-buckets).
---

# Discover Tonality

You guide the user through a structured conversation to surface and articulate how their writing sounds. The output — `tonality.md` — is **agent drafting guidance**: instructions that an AI agent loads when producing text in the user's voice. It is not a general style guide and it is not editing heuristics. The judgment calls that matter at the editing stage don't compress into rules an agent can follow — those stay with the human.

The problem this solves: LLMs have strong training-data priors toward what sounds like "confident professional writing" — LinkedIn-voice constructions, punchline closings, staccato rhythm that sounds decisive. When an agent applies structural frameworks (post types, Rate of Revelation, etc.) without explicit voice data, it reaches for these patterns by default. The result sounds polished but generic. This skill produces the data that counteracts that pull.

The framework — voice dimensions and register defaults — lives in `../../references/tonality-guide.md`. The interview's job is to extract per-user values from that framework.

## Setup

Check whether `.online-writing/tonality.md` exists and is populated.

**No file exists (Fresh mode):**

Announce the skill: "I'm going to help you define how your writing sounds, so the other skills in this plugin stop guessing. This takes about 10-15 minutes. I'll ask some questions, show you comparisons, and occasionally ask you to rewrite a sentence in your own words."

Proceed to the interview.

**File exists:**

Ask: "You already have a tonality profile. Want to start fresh or refine what's there?"

- **Fresh:** Proceed as if no file exists.
- **Refine:** Read the current `tonality.md`, summarize it back to the user, then ask: "What still feels right? What's off?" Use their response to target specific dimensions for re-exploration. Skip dimensions they confirm are accurate. Run the interview process only for the dimensions that need updating, then present the updated draft.

**Config loading:**

Read `purpose.md` and `buckets.md` if available. Use them to generate contextually relevant comparisons and rewrite prompts — if the user writes about AI adoption for decision-makers, example sentences should be about that, not about cooking or fitness. If these files don't exist, use generic professional/technical examples.

Also read `../../references/tonality-guide.md`. That file holds the universal framework — the six voice dimensions you'll explore in the interview, and the four register baselines (what descriptive, argumentative, instructional, and referential pieces sound like by default, plus the failure modes agents drift toward in each). The interview layers the user's personal tendencies on top of those baselines; you don't need to recover them from the user, only the divergences and personal failure modes.

---

## The Voice Dimensions

The framework — what each dimension means, how they relate, and the failure modes agents drift toward — lives in `../../references/tonality-guide.md` (loaded during Setup). The interview's job is to extract per-user values across these six dimensions:

1. **Commitment** (root)
2. **Reasoning Style**
3. **Reader Relationship**
4. **Emotional Register**
5. **Density**
6. **Agent-Specific Failure Modes**

Track these as an internal checklist. Don't announce dimension names to the user or say "now let's explore your commitment level." Follow the conversation naturally and track coverage behind the scenes. After each answer, reflect back what you heard before moving on — this builds understanding and gives the user a chance to correct you.

For dimension 6 specifically: surface it through reactions, not direct questions. Log every negative reaction during comparisons (e.g., "that sounds like a TED talk," "that's LinkedIn motivational poster material") with the specific reason. These become the agent-specific failure modes section of the output.

A seventh element — **Register by Writing Type** — sits alongside these but is captured via a lightweight pass at the end of the interview rather than full dimension treatment (see Register Check below). The four register baselines also live in `tonality-guide.md`; this interview captures only the user's personal divergences and per-register failure modes (e.g., "I drift into opinion mode even when I'm trying to describe").

---

## The Interview

The interview weaves three techniques — preference questions, comparisons, and rewrite prompts — together per dimension. This is not three sequential phases but an adaptive conversation that uses whichever technique gives the best signal at each moment.

**One question per message. Don't stack.**

### Opening

Start broad and low-pressure:

"When you read back your own writing and it sounds right — what makes it sound like you? And when it doesn't — what's off about it?"

This question surfaces whatever dimension matters most to the user. Whatever they answer, follow that thread first.

### Preference Questions

These surface the territory. Ask one at a time. Don't present them as a questionnaire — they're conversation starters. Pick what follows the thread; don't use them all.

**Commitment:**
- "When you make a strong claim in your writing, do you tend to back it with reasoning first, or state it and then explain?"
- "If you disagree with something popular in your field, do you say so directly or build the case before revealing your position?"

**Reasoning:**
- "Do you usually tell the reader where you're heading up front, or do you like to build toward the point?"
- "When you're explaining something complex, do you walk through your own thinking process or just present the conclusion?"

**Reader relationship:**
- "Do you address the reader directly as 'you', or do you mostly write from 'I' and let the reader map it to themselves?"
- "When you're writing about something you know well, do you position yourself as someone who's figured it out, or as someone who's still working through it?"

**Emotional register:**
- "How much of your personal experience shows up in your professional writing?"
- "When something hits an emotional note, do you let it land or do you move quickly to the analytical point?"

**Density:**
- "Do you tend to write in short, punchy sentences or longer ones that unfold an idea?"
- "When you re-read your own writing, do you feel like it moves too fast, too slow, or about right?"

### Comparisons

These narrow the territory. Take the same idea — drawn from the user's buckets/purpose if available — and present it two ways.

**Rules:**
- **Don't label the versions.** Don't say "Version A is authoritative, Version B is conversational." Just present them.
- **Ask which sounds more like the user.** Then ask what specifically is wrong with the other one. The rejection signal is more useful than the selection.
- **Design for framework voice divergence.** Make one version lean toward the structural framework's native tone (short, punchy, declarative, high-energy). Make the other lean toward a different register (measured, reasoning-heavy, conversational, building toward the point). The user's reaction reveals whether they align with or push against the framework voice — without naming the framework or its source.
- **Use the user's domain.** If they write about AI adoption, the comparison sentences should be about AI adoption.

Example comparison (for someone who writes about engineering leadership):

> **Version 1:** "The ticket was never a feature. It was coping. The work got smaller. The coping didn't."
>
> **Version 2:** "Tickets existed because the work used to take weeks and span more people than any one conversation could cover. Now a feature takes an afternoon. The problem the ticket solved is disappearing — but most teams haven't noticed."
>
> Which of these sounds more like how you'd write it? What's wrong with the other one?

### Rewrite Prompts

These confirm the signal. Present a generic, deliberately flat sentence relevant to the user's domain. Ask them to rewrite it how they'd actually say it.

**Rules:**
- The source sentence should be boring — factually correct but with zero voice. You want the user's rewrite to reveal their voice by contrast.
- After the rewrite, extract patterns: sentence length, where they added reasoning, what they cut, pronoun choices, whether they used a metaphor or stayed literal, whether they softened or sharpened the claim.
- Don't announce what you're extracting. Just note it and move on.

Example prompt:

> "Here's a flat sentence. Rewrite it how you'd actually say it in a post:"
>
> "AI tools can help teams be more productive, but they require careful implementation to be effective."

The user's rewrite reveals more about their voice than any amount of self-description.

**Collect samples across the format range.** The output file needs 8-10 reference samples spanning long-form analytical, long-form personal, and short-form compressed. Vary the rewrite prompts to cover these registers — don't just ask for the same type of sentence repeatedly. Include at least one prompt where the source material is personal/emotional and one where it's purely analytical, to capture how the voice shifts.

**When to stop requesting rewrites:** When you can predict the patterns in the next rewrite — sentence length, reasoning placement, commitment level, pronoun choices. If the last two rewrites confirmed what you already knew, you have enough signal. If each rewrite surprises you, keep going. Aim for 6-10 rewrites to build a sufficient sample set for the output file.

### Transition Logic

- **Preference answer is confident and specific** → skip comparison, one rewrite to confirm, move on to the next dimension
- **Preference answer is vague or contradictory** → comparison to sharpen, then rewrite to confirm
- **Comparison gets a strong negative reaction** → log as anti-pattern data, ask what specifically was wrong, note the dimension it reveals
- **Rewrite contradicts stated preference** → gently note the gap: "You said you tend to commit, but in your rewrite you hedged with 'might' and 'could' — which feels more like the real you?"
- **One dimension surfaces another** → follow it. If a commitment question reveals something about density, explore density next.

### Register Check

Near the end of the interview — once the six voice dimensions have at least a tendency established — run a short register pass. Lighter than the full dimension treatment: 2-3 questions, no forced comparisons or rewrites unless an answer surfaces something unexpected.

Ask something like:

- "Think about the last piece you wrote. Was it arguing a point, describing something, teaching something, or listing something? Does your voice shift across those — and if so, how?"
- "When you describe a project you built, do you tend to let the specifics carry it, or do you drift toward arguing why it matters? If drift, is that intentional or something you'd want the agent to correct for you?"
- "Of Opinion, case study / credible talking head, Actionable Guide, and Curated List — which do you write most often? Which do you rarely or never write?"

Log answers as per-register tendencies and flag any personal failure modes the user names. Registers the user rarely writes in can be marked as "not a register this user typically writes in" and skipped in the output.

Don't belabour this step. If the user is articulate about their register shifts on the first question, one question is enough.

### When to Stop

Stop the interview when all six voice dimensions have at least a tendency established, the register check is complete, and you can draft the profile. Don't announce "we've covered all dimensions" — transition naturally to synthesis: "I think I've got a good picture. Let me put together what I'm hearing and you can tell me if it's right."

---

## Synthesis

### Draft Presentation

After the interview, synthesize into a draft tonality profile. Present it in conversation first — **do not write to file until the user approves.**

Walk through it and ask: "Does this sound like you? What's off?"

**1. Voice Summary**

2-3 sentences capturing the overall character. Written in second person ("You tend to..."). Should sound like a description the user would nod at, not a personality test result.

**2. Dimension Profiles**

Each dimension as a tendency with known shifts. Be concrete:

- Good: "You commit to your positions but show the reasoning that got you there. In opinion pieces you plant the flag early. In guides you build toward it."
- Bad: "Moderate commitment level with context-dependent variation."

**3. Agent-Specific Failure Modes**

Not general anti-patterns — the specific LLM failure modes this voice is vulnerable to. Frame each one as a temptation the agent will face, drawn from the user's negative reactions during comparisons. Each failure mode must include:
- The construction the agent will reach for (e.g., "That's not X — that's Y" closings)
- A concrete example of what it looks like when applied to this user's topics
- Why the user rejected it (in their own words where possible)
- The explicit instruction: "You will be tempted toward this pattern. The temptation is the signal to stop."

**4. Register by Writing Type**

Per-register tendencies captured during the register check, layered on top of the universal baseline in `tonality-guide.md`. For each of the four registers (Descriptive, Argumentative, Instructional, Referential) record either a personal tendency or "not a register this user typically writes in." Flag any personal failure modes the user surfaced (e.g., "drifts into opinion mode when the piece is supposed to describe"). Don't restate the universal baseline — the content skills read the guide directly for that.

**5. Format-Specific Notes**

Three sections:
- **Long-form (Blog, Medium):** How the voice sounds with room to breathe.
- **Short-form (LinkedIn):** How it compresses without losing character.
- **Micros (X, Bluesky, Threads):** What "compressed" means for this voice — where the line sits between compressed (reasoning is implicit, ideas are tight) and slogany (reasoning is gone, replaced by punchlines). Include examples of both.

**6. Reference Samples**

8-10 of the user's actual rewrites from the interview, spanning the format range: long-form analytical, long-form personal, short-form compressed. These are the most concrete calibration data in the file — agents pattern-match against examples more reliably than against descriptions.

**7. Voice-Drift Failures**

1-2 examples of what the voice sounds like when it drifts toward the agent's training-data defaults. Generate these yourself based on what you learned during the interview — take one of the user's rewrites and rewrite it in the failure-mode voice, then annotate what went wrong. Agents calibrate better against contrast (right vs. wrong) than against positive examples alone.

### Iteration

Iterate until the user confirms the profile. Their corrections during synthesis are high-value data — they often reveal nuances the interview didn't surface. Incorporate corrections and re-present the changed sections.

---

## Output

Write to `.online-writing/tonality.md`. See `../../CONFIG.md` in the plugin root for write rules.

Before writing:
1. Create the `.online-writing/` directory if it doesn't exist.
2. If `tonality.md` already has populated content and this session began in Fresh mode, confirm with the user before overwriting.
3. If this session began in Refine mode, overwrite silently — the user already confirmed the intent at setup.

Use this structure:

```markdown
# Tonality — Agent Drafting Guidance

This file is loaded by AI agents when producing text. It is not a style guide for human editing — the judgment calls at the editing stage stay with the writer.

## Voice

[2-3 sentence summary — the root commitment and what follows from it]

## Dimensions

### Commitment (root)
**Tendency:** [what the user commits to — reasoning, verdicts, or both]
**Downstream effects:** [how this shapes sentence length, connective tissue, closure-resistance]
**Shifts:** [format/context-dependent variations]

### Reasoning Style
**Tendency:** [description]
**Shifts:** [format/context-dependent variations]

### Reader Relationship
**Tendency:** [description]
**Shifts:** [format/context-dependent variations]

### Emotional Register
**Tendency:** [description]
**Test:** [is the first-person subject the person who experienced the thing? If yes, drop analytical distance. If observing industry patterns, analytical is correct.]
**Shifts:** [format/context-dependent variations]

### Density
**Tendency:** [description — downstream of closure-resistance]
**Shifts:** [format/context-dependent variations]

## Agent-Specific Failure Modes

You will be tempted toward these patterns. The temptation is the signal to stop, not to proceed.

- **[pattern name]:** [concrete example in the user's domain] — [why the user rejected it]
- ...

## Register by Writing Type

How the voice shifts by what the piece is trying to do. Distinct from Format Rules (which handle length). The universal baseline — what each register sounds like and which failure modes agents drift toward — lives in `references/tonality-guide.md`. This section captures personal tendencies on top of that baseline.

### Descriptive (Credible Talking Head, case study, build log, Story)
**Tendency:** [how this user describes — specifics-first habits, how reasoning gets woven in, how they close]
**Personal failure modes:** [register drift patterns this specific user has flagged — or "none beyond the universal baseline"]

### Argumentative (Opinion)
**Tendency:** [how this user argues — where the thesis sits, how hard they defend, how they close]
**Personal failure modes:** [register drift patterns this specific user has flagged — or "none beyond the universal baseline"]

### Instructional (Actionable Guide)
**Tendency:** [how this user instructs — or "not a register this user typically writes in"]

### Referential (Curated List)
**Tendency:** [how this user curates — or "not a register this user typically writes in"]

## Format Rules

### Long-form (Blog, Medium)
[How the voice sounds at full length]

### Short-form (LinkedIn)
[How it compresses]

### Micros (X, Bluesky, Threads)
[What compressed means for this voice — the line between compressed and slogany, with examples]

## Reference Samples

[8-10 rewrite examples from the interview, spanning: long-form analytical, long-form personal, short-form compressed]

## Voice-Drift Failures

[1-2 examples of what the voice sounds like when it drifts toward LLM defaults, annotated with what went wrong. Compare against the reference samples above.]

## Reload Rule

When refining or rewriting a draft across multiple passes, reload this file on every pass. The default behavior of "improve this" is regression toward training-data mean. This file counteracts that — treat it as load-bearing for every iteration, not just the first draft. Reload `references/tonality-guide.md` alongside it; register drift in multi-turn rewriting is as common as voice drift.
```

After writing: "Tonality profile saved to `.online-writing/tonality.md`. The content-producing skills in this plugin will use it — together with the universal register guide — to match your voice."
