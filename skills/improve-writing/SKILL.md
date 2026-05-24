---
name: improve-writing
description: >
  Use when the user has an existing draft with some structure already in place — headers, partial sections,
  framework annotations, or a clear direction — and wants it refined, tightened, restructured, or finished.
  Signals include: draft feels flat or rough, sections trail off mid-thought, the writer can't name what's wrong
  but knows it's not ready. Not for raw unstructured input (see create-post / create-draft) or for rating a
  finished piece (see rate).
---

# Improve Writing

You take existing drafts and refine them into well-structured, publishable online posts. The input will be text that already has some structure — section headers, partially written paragraphs, framework annotations, or at least a clear direction. Your job is to respect the choices the writer already made, improve where things aren't working, fill gaps, and produce a polished result.

## Setup

Read the structural reference: `../../references/post-structure-guide.md` — every framework you'll use, with example skeletons and a diagnostics checklist. Internalise it before proceeding.

Read the tonality reference: `../../references/tonality-guide.md` — universal register guidance by writing type (descriptive, argumentative, instructional, referential), the cross-cutting LLM register failure modes the agent will drift toward, and self-check questions for catching drift before delivery. Apply this on every refinement pass, not just when `tonality.md` is populated. Register drift is the refinement-specific risk: each rewrite pass is a fresh chance to regress a descriptive piece toward argumentative register (drilling the thesis, adding counterfactuals, sharpening the close into a pitch).

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`expertise.md`**, **`buckets.md`**, **`tonality.md`** — with the rewrite emphasis on **preserving** the existing alignment, not redirecting it. Don't drift the draft away from the user's stated purpose, zones, or buckets during refinement. When `tonality.md` is populated, use it as the voice target — move the draft toward the user's defined tonality while preserving content and structure. **Reload both `tonality.md` and `tonality-guide.md` on every refinement pass.** Voice drift and register drift in multi-turn rewriting are the main risks — each pass regresses toward LLM training-data defaults unless both the voice profile and the register guide are actively applied. Treat both as load-bearing for every iteration, not just the first.

---

## Step 1 — Assess the existing draft

Read the draft carefully and take stock:

- **What structure exists?** Does it have headers, sections, an introduction, main points, a conclusion? Are there explicit framework annotations (1/3/1, 1/2/5/3/1, etc.)?
- **What's working?** Which sections already read well? Which arguments are clear and compelling? Don't rewrite what doesn't need rewriting.
- **What's incomplete?** Look for sections that trail off mid-thought, placeholder headers with no content, ideas that are stated but not developed.
- **What's the writing type?** Refer to the five types in the reference guide (Actionable Guide, Opinion, Curated List, Story, Credible Talking Head). The existing structure will usually make this obvious.
- **What's the intended scope?** If the draft has many sections with shallow content, the user may be aiming for breadth. If it has few sections with deep arguments, they're aiming for depth. Respect this.

## Step 2 — Plan the rewrite

Before rewriting, plan what you'll change and what you'll keep:

1. **Respect intentional choices.** If the user chose a 1/3/1 + 1/3/1 introduction, don't switch it to a 1/3/1 unless it's clearly not working. If they organised their main points in a specific order, keep that order unless the flow is broken.
2. **Identify framework fit.** For sections without explicit framework annotations, determine which framework best fits the existing content and apply it. For sections with annotations, check whether the content actually follows the framework — if not, reshape it to match.
3. **Complete incomplete sections.** Where the draft trails off, continue the thought in the direction the user was heading. Use the surrounding context and the user's voice to infer what they intended. Flag anything you're unsure about in the Diagnostics.
4. **Cut or merge redundant sections.** If multiple sections make the same argument in different words, merge them. Move the leftover material to Discarded Ideas.
5. **Don't invent new arguments.** Everything in the final post should trace back to something in the draft. You can develop, clarify, and restructure — but don't add ideas the user didn't express.

## Step 3 — Write the refined post

Keep these six quality dimensions in view as targets for the rewrite (full definitions live in `rate`): **clarity of thesis, originality, structure & flow, credibility, writing quality, positioning power**. The rewrite should leave each dimension at least as strong as the original, ideally stronger. Write *toward* them — don't optimise *for* a score. Ignore strategic goals (reach, conversion, etc.) at this stage.

Follow the chosen frameworks, using the example skeletons from the reference guide as scaffolding. As you write:

- **Preserve the user's voice.** Pay attention to the vocabulary, sentence patterns, and tone of the existing draft. The rewrite should sound like a better version of the same writer, not a different writer.
- **Match register to the writing type.** See `../../references/tonality-guide.md` for the four registers (descriptive, argumentative, instructional, referential), how each sounds by default, and the register-drift anti-patterns to avoid. Identify the register the piece was written in, and hold it through the refinement. If the original draft is descriptive, refinement passes should not introduce argumentative moves — thesis-drilling, counterfactuals, sales-pitch closes — even when those moves would "tighten" the prose by LLM defaults. Layer user-specific tendencies from `tonality.md` → Register by Writing Type on top when populated.
- **Keep the reader as the main character.** Every personal anecdote must serve the reader's understanding. If you're talking about yourself, it's "the setting," not the story.
- **Follow the language rules.** Write how people speak. Alternate sentence length. No long, complicated sentences. Confident and declarative.
- **Maintain Rate of Revelation.** Every sentence should move the reader forward.

## Step 4 — Generate headline variants

After the post is written, generate 10 headline variants. Use the headline anatomy from the reference guide:

- Each headline should communicate the What, the Who, and the Promise
- Apply the Curiosity Gap — hint at the answer without revealing it
- Use a mix of proven formats
- If the draft already has a headline, include it (or a refined version) as one of the 10

## Step 5 — Note what you changed

This skill rewrites — so the user needs transparency on what moved. Capture two things as you go (for the Rewrite Notes section of the output):

- **Inferred sections.** Anywhere the draft trailed off and you continued the thought — flag it so the user can verify you guessed right about their intent.
- **Structural changes.** Any framework or ordering choice the user made that you overrode — name what you changed and why.

This is about transparency of the rewrite, not structural quality review. For structural diagnostics (slow intro, blurring points, Rate of Revelation, rhythm, etc.), the user should run the `diagnose` skill on the output — that's a separate concern with its own checklist.

---

## Output Format

```
## Headlines

1. [headline variant]
2. [headline variant]
...
10. [headline variant]

---

[The full post, structured and ready to publish]

---

## Rewrite Notes

[Inferred sections (flag what you guessed at) and structural changes (explain what you overrode and why). Or "No inferences made; original structure preserved."]

## Discarded Ideas

[Ideas from the original that didn't fit the refined structure but might be useful later. Or "None."]
```

---

## After delivery — soft prompts

After producing the output above, offer three optional next steps. Keep it brief and non-blocking — the user decides.

- **Save to a file?** Ask whether to write the refined post to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific vault layout or naming scheme).
- **Run structural diagnostics?** Suggest the `diagnose` skill for a structural review (slow intro, blurring main points, Rate of Revelation, rhythm, etc.). Don't run it inline — the Rewrite Notes above cover rewrite transparency, not structure.
- **Run a quality rating?** Suggest the `rate` skill for a scorecard across the six quality dimensions and VPM. Especially useful after a rewrite — comparing pre- and post-rating tells the user whether the revision actually moved the piece, or just shuffled it. Don't run inline.

---

## Important Reminders

- The reference guide is your playbook — not a rigid rulebook. The frameworks are tools to mix, match, and adapt.
- Err on the side of preserving the user's choices. Only change structure when there's a clear reason — and flag it in Diagnostics when you do.
- The user's ideas are the raw material. Don't invent arguments they didn't make.
- Specificity is the secret. Don't generalise specific examples into vague abstractions.
- When in doubt about a structural choice, favour speed. Rate of Revelation is how you win on the internet.
