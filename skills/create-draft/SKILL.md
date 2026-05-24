---
name: create-draft
description: >
  Use when the user has raw material (brain dump, notes, research, bullet points) and wants it shaped into a
  publishable long-form piece in the 2,500–3,000 word range — full blog post, article, essay, deep dive, or
  feature. For short-form posts (800–1,200 words, social/LinkedIn-length), use create-post. For platform-specific
  micro-posts, use distill. For existing long-form drafts that already have structure and need refinement, use
  improve-writing.
---

# Create Draft

You transform raw, unstructured input into a well-structured, ready-to-publish **long-form draft** of **2,500–3,000 words**. Long-form gives you room for depth, layered arguments, extended stories, and thorough evidence — but it also raises the bar on Rate of Revelation. Every sentence still has to earn its place; there is just more room for each one to contribute.

## Setup

Read the structural reference: `../../references/post-structure-guide.md` — every framework you'll use, with example skeletons and a diagnostics checklist. Internalise it before proceeding. The guide does not prescribe a word count; that target is set here (2,500–3,000 words).

Read the tonality reference: `../../references/tonality-guide.md` — universal register guidance by writing type (descriptive, argumentative, instructional, referential), the cross-cutting LLM register failure modes the agent will drift toward, and self-check questions for catching drift before delivery. Apply this on every draft, not just when `tonality.md` is populated. Long-form amplifies register drift — a 3,000-word descriptive piece that slips into argumentative register reads like 3,000 words of pitching.

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`expertise.md`**, **`buckets.md`**, **`tonality.md`** — with one override: **ignore any channel-specific length targets in `purpose.md`**. This skill always produces long-form. If the user wants something shorter, route them to `create-post` or `distill`. When `tonality.md` is populated, apply the voice profile: match dimension tendencies for long-form, match register tendencies from the Register by Writing Type section when present, check output against anti-patterns, and use reference samples as calibration.

---

## Step 1 — Understand the raw input

Read the user's input carefully. Don't start structuring yet. First, answer these questions for yourself:

- **What is the core argument or insight?** Strip away the tangents and repetition. What is the user actually trying to say? There's usually one central idea buried in the stream of consciousness — find it. Long-form can support one or two secondary threads too, but there must still be a single spine.
- **Who is this for?** Look for cues about the intended audience. If the user doesn't specify, infer from the topic and vocabulary.
- **What writing type is this?** Refer to the five types in the reference guide (Actionable Guide, Opinion, Curated List, Story, Credible Talking Head). Long-form favours types that reward depth — Actionable Guide, Opinion, Story, and Credible Talking Head all work well at this length. Curated Lists can stretch to long-form, but need more per-item substance.

**Separating raw material from scaffolding.** The user's input may be a file that contains metadata, frontmatter, section headers, material brief scaffolding, headline lists, or other non-content elements. Only the user's actual ideas, arguments, stories, and opinions count as raw input. Ignore structural scaffolding when assessing the material — and when counting words later, count only the words of the draft you write, not the input file or the surrounding output sections (headlines, diagnostics, discarded ideas).

## Step 2 — Extract and skeleton

Pull out the distinct ideas from the raw input:

1. **Identify the main points.** Group related ideas. Merge overlapping ones. Discard tangents that don't serve the core argument (but keep them in a note at the end — the user may want them later).
2. **Order them.** What's the strongest opening? What builds naturally on what? What's the strongest closer? The skeleton should have a logical or emotional arc — not just a random sequence.
3. **Decide how many main points.** Target length is **2,500–3,000 words** for the draft body only (not headlines, diagnostics, or discarded ideas). At this length, **3–6 main points** usually works best: fewer than 3 and each point has to carry too much weight and risks sprawling; more than 6 and the piece feels shallow or list-like at long-form length. Let the content decide — depth per point matters more than hitting a point count.

**After you finish drafting, verify the body word count with `../../scripts/count-words` — pipe the post body via stdin.** Don't eyeball or estimate; models are unreliable at word counting and that unreliability leads to pieces that are silently 30% under or over target. If the count is outside 2,500–3,000, note it in the output and flag to the user whether to expand (add depth to thin points) or trim (cut fat from the longest points).

## Step 3 — Choose frameworks

With the skeleton in hand, select frameworks for each section. The reference guide describes what each framework *favours* — match those qualities to what your piece needs.

**Introduction:** Long-form earns more intro room than short-form. A 1/3/2/1 or 1/5/1 works well when the piece makes a bold claim or tackles a complex topic — you have budget to set it up properly. A 1/3/1 still works if the headline already implies the promise clearly. Don't over-extend the intro just because you have the word budget; every sentence still has to move the reader forward.

**Main Points:** Vary the framework across points to create rhythm. Don't use 1/2/5/3/1 for every point — the piece will feel exhausting even at long-form length. Follow a deep point with a fast one. Layer formatting techniques (bolded statements, repetition, Short/Long/Long/Short) on top of the base frameworks. Long-form is where 1/2/5/3/1 shines — use it for the 1–2 most important points.

**Conclusion:** Long-form deserves a real conclusion more often than short-form does. Think about what the reader should do or feel after finishing. If the piece taught something, a Summary gives them a checklist. If it argued a position, a Strong Opinion closes it. If the last main point is the strongest, extending it can be cleaner than bolting on a formal close.

## Step 4 — Write the draft

Keep these six quality dimensions in view as write-time targets (full definitions live in `rate`): **clarity of thesis, originality, structure & flow, credibility, writing quality, positioning power**. Long-form rewards each of these more, not less — a 3,000-word piece that's weak on credibility or originality fails harder than a 1,000-word one. Write *toward* them — don't optimise *for* a score. Ignore strategic goals (reach, conversion, etc.) at this stage.

Follow the chosen frameworks, using the example skeletons from the reference guide as scaffolding. As you write:

- **Match register to the writing type.** See `../../references/tonality-guide.md` for the four registers (descriptive, argumentative, instructional, referential), how each sounds by default, and the register-drift anti-patterns to avoid. Identify the register the piece needs, apply the guide's defaults, and layer user-specific tendencies from `tonality.md` → Register by Writing Type on top when populated. At long-form length the most common drift is descriptive pieces written argumentatively — thesis drilled across sections, counterfactual paragraphs, sales-pitch closes. Run the guide's self-checks before delivering; drift compounds across 2,500+ words.
- **Use the length for depth, not padding.** Long-form invites longer stories, extended examples, layered evidence, caveats, and counterarguments. It does NOT invite restating the same point three ways, unnecessary throat-clearing, or filler transitions. If a paragraph would survive deletion, it should be deleted.
- **Keep the reader as the main character.** Every personal anecdote must serve the reader's understanding. If you're talking about yourself, it's "the setting," not the story.
- **Follow the language rules.** Write how people speak. Alternate sentence length. No long, complicated sentences. Confident and declarative.
- **Maintain Rate of Revelation.** Every sentence should move the reader forward. The bar is actually higher at long-form, because monotony is deadlier over 3,000 words than over 1,000.
- **Use headers and structure generously.** Long-form needs visual rest stops. Use `## H2` for main points and `### H3` for sub-beats where useful. Pull-quote-worthy lines and bolded declarations help the eye keep moving.

## Step 5 — Generate headline variants

After the draft is written, generate 10 headline variants. Use the headline anatomy from the reference guide:

- Each headline should communicate the What, the Who, and the Promise
- Apply the Curiosity Gap — hint at the answer without revealing it
- Use a mix of proven formats (X Number, Question/Answer, Things That Shouldn't Go Together, etc.)
- Include at least one with a power phrase (crucial, eye-opening, painful, emerging)
- Include at least one that's ultra-specific to the niche
- Lean slightly toward headlines that signal depth and substance — long-form readers click differently than feed-scrollers

## Output Format

```
## Headlines

1. [headline variant]
2. [headline variant]
...
10. [headline variant]

---

[The full long-form draft, structured and ready to publish, with H2/H3 headers]

---

## Discarded Ideas

[Any tangents or ideas from the raw input that didn't fit the structure but might be useful later. Or "None."]
```

---

## After delivery — soft prompts

After producing the output above, offer three optional next steps. Keep it brief and non-blocking — the user decides.

- **Save to a file?** Ask whether to write the draft to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific vault layout or naming scheme).
- **Run structural diagnostics?** Suggest the `diagnose` skill for a structural review — at long-form length this is especially valuable (word count against target, mid-piece sag, missing structural headers, plus the base checks). Don't run it inline.
- **Run a quality rating?** Suggest the `rate` skill for a scorecard across the six quality dimensions and VPM. Long-form especially benefits from a rating pass — VPM is unforgiving over 3,000 words. Complements `diagnose`. Don't run inline.

---

## Important Reminders

- **Length is a feature, not a target.** 2,500–3,000 words is the zone this skill is designed for, but don't pad to hit the number. If the raw material is too thin to carry long-form without padding, **stop and surface that to the user** — don't silently pad or silently shrink the piece. Then let them choose: run `explore-idea` to draw out more material (stories, opinions, contradictions, evidence) and come back to `create-draft` with richer input, or write it at its natural length with `create-post` now. Their call, not yours.
- The reference guide is your playbook — not a rigid rulebook. The frameworks are tools to mix, match, and adapt.
- The user's raw ideas are the raw material. Respect them. Don't invent arguments or points the user didn't make. Your job is to find the structure in *their* thinking, not to replace their thinking with yours.
- Specificity is the secret. Don't generalise the user's specific examples into vague abstractions. If they wrote about a concrete experience, keep it concrete.
- When in doubt about a structural choice, favour speed. Rate of Revelation is how you win on the internet — even at 3,000 words.
