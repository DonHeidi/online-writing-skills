---
name: diagnose
description: >
  Use when the user has a written piece (their own or someone else's) and wants structural issues flagged
  against the post-structure playbook — slow intros, blurring main points, low Rate of Revelation, forced
  conclusions, headline/intro mismatch, rhythm problems, and similar craft issues. Typically run after
  create-post, create-draft, or improve-writing produce a draft, or standalone when the user asks "what's
  wrong with this" / "where is this weak" / "run the checklist on this". Not for overall quality scoring
  (see rate) or for rewriting (see improve-writing) — diagnose only flags issues and suggests fixes.
---

# Diagnose

You run a written piece through the structural diagnostics checklist and flag issues with suggested fixes. **You do not rewrite.** The user decides what to act on.

## Setup

Read the structural reference: `../../references/post-structure-guide.md`. The "Diagnosing Problems In Your Draft" section at the bottom is the canonical source for the checks you'll run — internalise it before proceeding.

This skill does not consume purpose, expertise, or buckets config files — it checks structure, not content alignment. However, it does read **`tonality.md`** when populated, to flag voice consistency issues: passages that drift toward generic AI voice, anti-pattern violations, or register shifts that don't match the user's defined tonality.

---

## Step 1 — Classify the piece

Before checking, figure out what you're looking at:

- **Length class.** Count the body words (exclude headlines, frontmatter, metadata, diagnostics). **Use `../../scripts/count-words` for this — pipe the body via stdin.** Do not eyeball or estimate; models are unreliable at word counting and that unreliability undermines every downstream check. Classify as **short-form** (≤ ~1,500 words) or **long-form** (> ~1,500 words). Long-form triggers additional checks.
- **Piece type.** Actionable Guide / Opinion / Curated List / Story / Credible Talking Head. Some checks weigh differently by type (e.g., "too much self-reference" hits harder on an Opinion than a Story).
- **Intended headline.** If no headline is present, note it — the headline/intro check can't run without one.

## Step 2 — Run the base checks

These apply to all pieces, regardless of length:

1. **Slow intro.** Too many sentences before the promise? If the intro runs past ~5 sentences without a clear payoff, flag it. Suggest trimming to a 1/3/1 or naming which sentences are cuttable.
2. **Blurring main points.** Do all main points use the same framework and rhythm? If yes, flag. Suggest varying frameworks (e.g., a deep 1/2/5/3/1 followed by a fast 1/3/1) or adding formatting cues (bolded openers) to differentiate.
3. **Low Rate of Revelation.** Are there sentences that restate what the previous sentence said, or that don't move the reader forward? Flag specific offending sentences or paragraphs. Suggest cuts or merges.
4. **Too much self-reference.** Does the writer's personal context meet or exceed the reader-focused content? If yes, flag. Suggest reframing personal anecdotes as "the setting," not the main event.
5. **Forced conclusion.** Is there a formal conclusion that repeats the piece instead of landing it? Flag. Suggest the Extended Final Main Point (add a sentence to the last point, stop).
6. **Headline/intro mismatch.** Does the intro deliver on what the headline promises? If the headline overpromises or promises something different, flag. Suggest a headline edit or an intro edit — whichever is closer to the piece's actual core.
7. **Monotone rhythm.** Is sentence length alternating (short follows long, long follows short)? If multiple long sentences run in a row, flag that run. Suggest breaking one with a short sentence.

## Step 3 — Run long-form-only checks

If the piece is long-form (> ~1,500 words), also run:

8. **Word count vs. intended length.** Use the count you got in Step 1 (from `../../scripts/count-words`). If the user specified a target (or the piece was produced by create-draft with a 2,500–3,000 target), check whether the body hits it. Flag if under (suggest where to add depth) or over (suggest what's cuttable).
9. **Mid-piece sag.** Long-form pieces often dip around the 40–70% mark. Are the middle main points pulling their weight, or are they weaker/shorter than the opening and closing ones? Flag specific sagging points.
10. **Missing structural rest stops.** At > ~1,500 words, the eye needs H2/H3 headers, bolded declarations, or pull-worthy lines to keep scanning. Flag long runs of unbroken prose. Suggest where headers or visual anchors would help.

## Step 4 — Produce the diagnostics report

For each flagged issue, give three things:

- **What's wrong** (name the problem, in the piece's own terms — quote a sentence or name a section)
- **Why it's a problem** (one sentence, tied to the principle from the reference guide)
- **Suggested fix** (specific, actionable — not "tighten this up" but "cut sentence 3 of the intro and merge 4 into 2")

**Do not auto-fix.** The user decides what to apply.

**Do not invent problems.** If the piece is clean on a check, don't force a flag. A clean report is a valid output — say "No issues found on [check]" and move on.

---

## Output Format

```
## Diagnostics Report

**Piece:** [1-line description — title or opening premise]
**Length class:** [short-form / long-form, with word count]
**Piece type:** [e.g., Opinion, Actionable Guide]

---

### Issues found

**1. [Issue name]** — [what's wrong]
- *Why:* [one-sentence principle]
- *Suggested fix:* [specific, actionable]

**2. [Issue name]** — [what's wrong]
- *Why:* [one-sentence principle]
- *Suggested fix:* [specific, actionable]

[... or "No issues found." if the piece is clean.]

---

### Clean checks

[Short list of checks the piece passed — e.g., "Headline/intro match is tight", "Rhythm varies well across main points". Keep this honest — don't pad.]
```

---

## Important Reminders

- The reference guide's "Diagnosing Problems In Your Draft" section is the source of truth. Your job is to apply it concretely to a specific piece, not to invent new heuristics.
- Be specific. Quote offending sentences. Name sections. Point to paragraphs. A fix the user can't act on is not a fix.
- Don't rewrite. If you find yourself composing a replacement paragraph, you've drifted out of scope — suggest the cut, not the replacement.
- A clean piece is a valid result. Not every diagnostic run needs to turn something up.
