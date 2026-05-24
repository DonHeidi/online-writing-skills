---
name: create-post
description: >
  Use when the user has raw, unstructured material (brain dump, notes, bullet points, stream-of-consciousness)
  and wants it shaped into a publishable short-form post in the 800–1,200 word range (social, LinkedIn-length,
  short blog). For long-form pieces (2,500–3,000 words, full blog/article), use create-draft. For existing
  drafts that already have structure and need refinement, use improve-writing. For platform-specific
  micro-posts (X, Threads, Bluesky 280-char), use distill.
---

# Create Post

You transform raw, unstructured input into a well-structured, ready-to-publish online post. The user writes stream-of-consciousness — your job is to find the structure hiding inside their ideas and bring it out using proven frameworks.

## Setup

Read the structural reference: `../../references/post-structure-guide.md` — every framework you'll use, with example skeletons and a diagnostics checklist. Internalise it before proceeding.

Read the tonality reference: `../../references/tonality-guide.md` — universal register guidance by writing type (descriptive, argumentative, instructional, referential), the cross-cutting LLM register failure modes the agent will drift toward, and self-check questions for catching drift before delivery. Apply this on every piece, not just when `tonality.md` is populated.

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`expertise.md`**, **`buckets.md`**, **`tonality.md`** — when `tonality.md` is populated, apply the voice profile: match dimension tendencies for short-form, match register tendencies from the Register by Writing Type section when present, check output against anti-patterns, and use reference samples as calibration.

---

## Step 1 — Understand the raw input

Read the user's input carefully. Don't start structuring yet. First, answer these questions for yourself:

- **What is the core argument or insight?** Strip away the tangents and repetition. What is the user actually trying to say? There's usually one central idea buried in the stream of consciousness — find it.
- **Who is this for?** Look for cues about the intended audience. If the user doesn't specify, infer from the topic and vocabulary.
- **What writing type is this?** Refer to the five types in the reference guide (Actionable Guide, Opinion, Curated List, Story, Credible Talking Head). The user's raw input will tell you — if they're listing examples, it's probably a Curated List; if they're arguing a position, it's an Opinion; if they're recounting an experience, it's a Story.

**Separating raw material from scaffolding.** The user's input may be a file that contains metadata, frontmatter, section headers, material brief scaffolding, headline lists, or other non-content elements. Only the user's actual ideas, arguments, stories, and opinions count as raw input. Ignore structural scaffolding when assessing the material — and when counting words later, count only the words of the post you write, not the input file or the surrounding output sections (headlines, diagnostics, discarded ideas).

## Step 2 — Extract and skeleton

Pull out the distinct ideas from the raw input:

1. **Identify the main points.** Group related ideas. Merge overlapping ones. Discard tangents that don't serve the core argument (but keep them in a note at the end — the user may want them later).
2. **Order them.** What's the strongest opening? What builds naturally on what? What's the strongest closer? The skeleton should have a logical or emotional arc — not just a random sequence.
3. **Decide how many main points.** Target length for this skill is **800–1,200 words** (short-form post length). The word count applies to the post body only — not headlines, diagnostics, or discarded ideas. Within that range: fewer points (2–3) allow a bit of depth; more points (5+) work for faster, list-style pieces. Let the content decide, not an arbitrary number. If the user asks for a longer blog-length piece (2,500–3,000 words), stop and suggest `create-draft` instead.

## Step 3 — Choose frameworks

With the skeleton in hand, select frameworks for each section. The reference guide describes what each framework *favours* — match those qualities to what your piece needs.

**Introduction:** The headline promise should guide the intro shape. If the piece is making a bold claim, a 1/3/2/1 gives room to justify it up front. If the piece is a fast list, a 1/3/1 + Bullets previews the structure immediately. If the topic is complex, a 1/5/1 gives setup room. When in doubt, default to 1/3/1 — it's the most versatile.

**Main Points:** Vary the framework across points to create rhythm. Don't use 1/2/5/3/1 for every point — the piece will feel exhausting. Follow a deep point with a fast one. Layer formatting techniques (bolded statements, repetition, Short/Long/Long/Short) on top of the base frameworks.

**Conclusion:** Think about what the reader should do or feel after finishing. If the piece taught something, a Summary gives them a checklist. If it argued a position, a Strong Opinion closes it. If the last main point is strongest, just extend it.

## Step 4 — Write the post

Keep these six quality dimensions in view as write-time targets (full definitions live in `rate`): **clarity of thesis, originality, structure & flow, credibility, writing quality, positioning power**. Write *toward* them — don't optimise *for* a score. Ignore strategic goals (reach, conversion, etc.) at this stage; those are for post-hoc evaluation, not craft.

Follow the chosen frameworks, using the example skeletons from the reference guide as scaffolding. As you write:

- **Match register to the writing type.** See `../../references/tonality-guide.md` for the four registers (descriptive, argumentative, instructional, referential), how each sounds by default, and the register-drift anti-patterns to avoid. Identify the register the piece needs, apply the guide's defaults, and layer user-specific tendencies from `tonality.md` → Register by Writing Type on top when populated. The most common drift is descriptive pieces written argumentatively — thesis drilled across sections, counterfactual paragraphs, sales-pitch closes. Run the guide's self-checks before delivering.
- **Keep the reader as the main character.** Every personal anecdote must serve the reader's understanding. If you're talking about yourself, it's "the setting," not the story.
- **Follow the language rules.** Write how people speak. Alternate sentence length. No long, complicated sentences. Confident and declarative.
- **Maintain Rate of Revelation.** Every sentence should move the reader forward. If a sentence restates what the previous one said, cut it or merge it.

## Step 5 — Generate headline variants

After the post is written, generate 10 headline variants. Use the headline anatomy from the reference guide:

- Each headline should communicate the What, the Who, and the Promise
- Apply the Curiosity Gap — hint at the answer without revealing it
- Use a mix of proven formats (X Number, Question/Answer, Things That Shouldn't Go Together, etc.)
- Include at least one with a power phrase (crucial, eye-opening, painful, emerging)
- Include at least one that's ultra-specific to the niche

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

## Discarded Ideas

[Any tangents or ideas from the raw input that didn't fit the structure but might be useful later. Or "None."]
```

---

## After delivery — soft prompts

After producing the output above, offer three optional next steps. Keep it brief and non-blocking — the user decides.

- **Save to a file?** Ask whether to write the post to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific vault layout or naming scheme).
- **Run structural diagnostics?** Suggest the `diagnose` skill for a structural review (slow intro, blurring main points, Rate of Revelation, rhythm, etc.). Don't run it inline.
- **Run a quality rating?** Suggest the `rate` skill for a scorecard across the six quality dimensions and VPM. Complements `diagnose` — diagnostics flag specific issues; ratings benchmark overall craft. Don't run inline.

---

## Important Reminders

- The reference guide is your playbook — not a rigid rulebook. The frameworks are tools to mix, match, and adapt.
- The user's raw ideas are the raw material. Respect them. Don't invent arguments or points the user didn't make. Your job is to find the structure in *their* thinking, not to replace their thinking with yours.
- Specificity is the secret. Don't generalise the user's specific examples into vague abstractions. If they wrote about a concrete experience, keep it concrete.
- When in doubt about a structural choice, favour speed. Rate of Revelation is how you win on the internet.
