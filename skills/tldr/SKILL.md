---
name: tldr
description: >
  Use when the user has a long-form article (their own draft, typically 2,500–3,000 words)
  and wants a single-paragraph abstract for the top of the piece. Triggers: "tldr",
  "abstract this", "write an abstract for", "synopsis of this draft", "summarize this
  article". Produces ~100–150 words, neutral synthesis register, in the user's voice and
  the source's register — functions as a hybrid academic abstract / synopsis that lets
  a reader decide whether to commit to the full piece. Not for: distilling into multiple
  shorter posts (see distill), rating quality (see rate), generating headlines (see
  headlines), structural diagnostics (see diagnose), or marketing teasers / meta
  descriptions / SEO blurbs (different register, out of scope).
---

# TLDR

You produce a single-paragraph abstract of a long-form article — the kind of upfront block that sits between the title and the intro and gives a reader enough to decide whether to commit to the full piece. The abstract is neutral synthesis, not a hook. It compresses the article's thesis, main beats, and payoff without flatlining it. It sits *inside* the user's voice and the source's register — not in third-person academic-paper voice and not in clickbait teaser voice.

This skill outputs the abstract as a copyable block. It does not modify the article file.

---

## Setup

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`tonality.md`** and **`references/tonality-guide.md`** — the abstract is written in the user's voice, in the source article's register.

Skipped on purpose: `purpose.md`, `buckets.md`, `expertise.md`. The abstract describes the article, not the user's strategic positioning. The article's register beats the user's typical register: a descriptive case study gets a descriptive abstract regardless of how the user usually writes.

If `tonality.md` is unpopulated, fall back to `references/tonality-guide.md` plus voice cues from the source article itself. Do not fail and do not ask the user to run `discover-tonality` first.

---

## Step 1 — Read and Map

Read the full article. Identify three things:

1. **Thesis or central frame** — one sentence answering "what is this piece really about?" For descriptive pieces (case study, build log, story), this is the central observation, not an argued claim. For Opinion pieces, it is the line the author defends.
2. **Main beats** — the 3–5 substantive moves the article makes. Not every section header. The load-bearing ones that drive the piece. A 3,000-word article typically has 3–5 of these; if you find 8, you are listing too many.
3. **Payoff** — what the reader walks away with: a decision they can make, a lens they can apply, a verdict, a shift, a takeaway.

Hold these as state. The abstract is built from them.

---

## Step 2 — Determine Source Register

Identify the article's register using `references/tonality-guide.md`. Read that file before drafting if you are unsure.

- **Descriptive** — Credible Talking Head, case study, build log, Story. Specifics-first, observations woven in, lands on what the setup produced.
- **Argumentative** — Opinion. Thesis-led, defended, lands on the line being made.
- **Instructional** — Actionable Guide. Steps and frameworks, lands on what the reader can now do.
- **Referential** — Curated List. Entries with framing, lands on the recommendation pattern.

The abstract preserves the source's register. **Do not drill a thesis on a piece that describes. Do not impose argumentative framing on instructional content. Do not turn a curated list into an opinion piece.** Source register wins over LLM defaults and over the user's typical register.

If the source register is mixed (e.g., a case study that argues a point), pick the dominant one — the one the article spends most of its words on — and let the abstract follow that.

---

## Step 3 — Draft the Abstract

One paragraph, 100–150 words. Prose only — no bullet structure, no numbered list, no sub-headers, no inline emphasis on every other phrase.

- **Lead** with the thesis or framing (what the piece is really about). Not with "This article…" or "In this piece…".
- **Move through** the main beats compactly. The reader should grasp the shape of the argument or narrative — not every twist.
- **Close** on the payoff. What the reader walks away with.
- **Voice.** Match the user's tonality at long-form length. The abstract sits inside the article in the user's voice — not as a third-person external description of it.

Density matters. Every sentence should advance the abstract. If a sentence could be cut without losing substance, cut it.

---

## Step 4 — Voice and Register Pass

Re-read the draft against three sources, in this order:

1. The named failure modes below.
2. `tonality.md` agent-specific failure modes (when populated).
3. `references/tonality-guide.md` register defaults and LLM register failures.

If any pattern matches, revise.

### Failure modes (named, so you have anti-patterns to match against)

- **Academic drone.** *"This article explores…", "The author argues that…", "In this piece, the writer examines…", "The piece presents…".* Third-person research-paper voice. The abstract sits inside the user's article in the user's voice. It does not refer to the article as an external object.
- **Marketing hook drift.** *"Discover how…", "Find out why…", "What if I told you…", "Imagine a world where…".* Clickbait teaser register. The abstract is neutral synthesis, not a hook.
- **Spoiler flatlining.** Listing every beat in sequence so the reader has no reason to keep reading. Convey what the piece does and where it lands — the destination, not every step. The abstract should make a reader more likely to commit, not less.
- **Engagement-bait close.** *"Read on to find out…", "Keep reading for…", "The full piece reveals…".* Same family as hook drift, at the closing line. Cut.
- **Register imposition.** Forcing argumentative thesis-and-defense onto a descriptive case study, or instructional how-to onto an Opinion piece, or argumentative framing onto a curated list. Source register wins.
- **Padding.** Hitting 150 with *"importantly", "ultimately", "fundamentally", "crucially"* and other filler. The abstract is as long as it needs to be inside the range — not longer.
- **Voice drift to LLM mean.** Generic synthesis tone that could have been written by anyone. The user's tonality is the calibration. If your draft could appear under any author's byline without raising suspicion, it has drifted.

---

## Step 5 — Word Count

Hard range: **100–150 words.** Count every word. Adjust as needed.

- **Under 100:** the abstract is too thin. Fold in another beat or expand the payoff. Don't pad with filler.
- **Over 150:** trim filler and connective tissue, not substance. Replace "in order to" with "to", "the reason why" with "why", drop "actually / really / just / very". Restructure to front-load the substance.
- **Lands cleanly at 110:** that is the abstract. Do not pad to fill the range.

---

## Output Format

Produce a single block. No preamble, no caveats, no commentary outside the block.

```
# Abstract — [article title]

**Word count:** [n]
**Source register:** [descriptive / argumentative / instructional / referential]

---

[abstract paragraph, 100–150 words]
```

---

## After Delivery — Soft Prompt

After producing the output above, offer one optional next step. Keep it brief and non-blocking — the user decides.

- **Save to file?** Ask whether to write the abstract to disk. If yes, ask the user where and what to name it — defer to whatever conventions apply in their environment, do not assume a specific layout or naming scheme.

Do not auto-save. Do not modify the article file. If the user asks you to insert the abstract into the article, that is a separate action and you should confirm the insertion point before writing.

---

## Important Reminders

- Word count is hard-bounded: 100–150. Count it. The header in the output reports it so the user can verify at a glance.
- The abstract sits inside the article in the user's voice. Not third-person ("the author argues"), not marketing-hook ("discover how"), not academic-paper register.
- Source register beats user register beats LLM default. Descriptive pieces get descriptive abstracts. Don't drill a thesis on a piece that describes.
- Neutral synthesis, not a hook. The abstract is for the reader who is deciding whether to commit — it gives them enough to decide. It is not a teaser whose job is to generate clicks.
- Spoil the destination, not every step. The reader should know where the article lands and roughly how it gets there — not every twist along the way.
- One abstract per run. No variants, no length modes, no companion bullet list. If the user wants those, they will ask — and that is a different request.
- Output only. The skill does not modify the article file unless the user explicitly asks for insertion.
