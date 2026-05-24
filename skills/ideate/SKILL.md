---
name: ideate
description: >
  Use when the user has a topic but no specific posts to write about it, or hands over raw material (notes,
  transcripts, articles) and wants publishable post concepts mined out. Also use when the user is stuck on
  what to write next and needs sharp, differentiated angles. Not for expanding a single idea into drafting
  material (see explore-idea) or for writing the post itself (see create-post / create-draft).
---

# Ideate

You generate specific, publishable post ideas for online writing. The user either gives you a topic to explore or hands you existing text to mine for ideas. Your job is to produce a set of sharp, differentiated post concepts — not vague themes, but ideas specific enough that someone could sit down and start writing immediately.

## Setup

Read the ideation reference: `../../references/ideation-guide.md` — the Endless Idea Generator system, differentiation strategies, and content bucket logic. Internalise it before proceeding.

For headline seeds, also consult the "The Headline" section of `../../references/post-structure-guide.md` — headline anatomy (What / Who / Promise), Curiosity Gap, and proven formats.

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`**, **`expertise.md`**, **`buckets.md`**. When `buckets.md` is populated, tag each generated idea with the bucket it serves (General / Niche / Industry).

---

## Step 0 — Determine the Mode

**Mode A — From Prompt.** The user gives you a topic, theme, or question. Could be as vague as "AI" or as specific as "why junior developers should write documentation." Your job is to fan the idea out into multiple distinct post concepts.

**Mode B — From Text.** The user gives you existing text — notes, a draft, a transcript, a brain dump, an article, or points to a file. Your job is to extract the distinct ideas buried in that text and expand each one into a standalone post concept.

How to tell: if the user provides or points to a body of text and asks for ideas, it's Mode B. Everything else is Mode A.

**A note on input length in Mode B:** A short input (a few sentences, a tweet, a single observation) will yield fewer but more tightly focused ideas — mine every sentence for angles. A long input (a full draft, transcript, or multi-page document) will have many extractable ideas — be selective, prioritise the sharpest and most distinct ones, and group related threads rather than listing every possible angle.

---

## Mode A — From Prompt

### Step 1 — Understand the seed

Before generating, understand what you're working with:

- **What's the topic?** Name it as given. Don't narrow a broad topic prematurely — the Endless Idea Generator will produce specific angles. If the user says "AI," keep "AI" as the seed and let specificity emerge through the type × angle combinations in Step 2.
- **Who might this be for?** If the user hasn't specified an audience, consider multiple possible audiences — different audiences produce different ideas. Note the most likely ones.
- **Which content buckets could this touch?** General Audience (universal), Niche Audience (expertise-specific), or Company/Industry? A broad seed might span all three — that's fine. A narrow seed tells you which bucket you're in.

### Step 2 — Run the Endless Idea Generator

For the topic, systematically combine writing types × idea types to produce distinct angles:

1. Go through each **writing type** (Actionable Guide, Opinion, Curated List, Story, Credible Talking Head) and ask: what would a [type] about this topic look like?
2. For each promising type, layer on **idea types** (Explanation, Habits, Mistakes, Lessons, Tips, Stories, Timely Events) to find the specific angle.
3. For each angle, consider the **credibility frame**: expert, curator of experts, or most-articulate opinion?

Not every combination will be interesting. Discard weak ones. Keep the ones where the combination produces something a reader would actually click.

### Step 3 — Sharpen with differentiation

For each idea, ask: what makes this *better* than what already exists? Apply the differentiation strategies from the reference guide:

- Could this use a different perspective (better positioned)?
- Could this use unconventional examples (better examples)?
- Could this start at a moment of conflict (better opener)?
- Could this use niche topics to answer universal questions?

### Step 4 — Generate headline seeds

For each idea, write 2–3 headline variants using the headline anatomy from the post structure guide: every headline must communicate the **What** (topic), the **Who** (audience), and the **Promise** (problem solved or solution offered) — without revealing the answer (the Curiosity Gap). These aren't final headlines — they're sharpening tools. If you can't write a clear headline, the idea isn't specific enough yet.

---

## Mode B — From Text

### Step 1 — Read and mine

Read the full text carefully. Look for:

- **Distinct arguments or insights** — things the author is claiming or explaining that could stand alone as a post.
- **Buried specifics** — concrete examples, stories, data points, or experiences mentioned in passing that deserve their own piece.
- **Tensions or contrasts** — places where the text argues against conventional wisdom, or where two ideas create an interesting friction.
- **Questions the text raises but doesn't answer** — implicit follow-ups that a reader might want explored.
- **Repeating themes** — ideas the author keeps coming back to, which signal what they care most about.

### Step 2 — Extract and expand

For each extracted idea:

1. **Name it** — give it a clear, specific label. Not "something about AI" but "why AI makes first drafts worse but final drafts better."
2. **Assign a writing type** — what type of post would this idea best become?
3. **Identify the angle** — which idea type (Explanation, Habits, Mistakes, Lessons, Tips, Stories, Timely Events) fits?
4. **Expand it** — what would this idea look like if developed into a full post? What main points would it need? What audience would care?

### Step 3 — Generate headline seeds

Same as Mode A: 2–3 headline variants per idea to sharpen it.

---

## Output Format

```
## Topic: [the seed topic or source text summary]

### Idea 1: [specific, descriptive name]

**Type:** [Actionable Guide / Opinion / Curated List / Story / Credible Talking Head]
**Angle:** [Explanation / Habits / Mistakes / Lessons / Tips / Stories / Timely Events]
**Bucket:** [General / Niche / Industry]
**Shelf life:** [Timely / Timeless / Timely hook + timeless core]
**Audience:** [who this is for]
**Core argument:** [1–2 sentences — what this post would say]
**Headlines:**
- [headline variant 1]
- [headline variant 2]

### Idea 2: [specific, descriptive name]
...

---

## Expansion opportunities

[Note any ideas that could become Pillar Pieces, series, or that connect to each other in a content web.]
```

---

## Important Reminders

- Specificity is everything. "How to use AI" is not an idea. "3 AI prompts that replaced my morning research routine" is an idea. Every idea should be specific enough to start writing immediately.
- In Mode B, stay faithful to the source material. Extract what's there — don't invent ideas the author didn't express. You can expand and sharpen, but the seed must come from the text.
- Aim for 5–10 ideas. Fewer than 5 doesn't give enough variety. More than 10 gets diluted. Quality over quantity.
- Include at least one idea that uses niche topics to answer universal questions — these tend to have the widest reach with the strongest specificity.
- Aim for a mix of timely and timeless ideas, and a spread across content buckets where possible.
- Don't write the posts. This skill generates the ideas. The user will take them to create-post or improve-writing when they're ready.
