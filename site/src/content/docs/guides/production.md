---
title: Production
description: Turn a topic or a pile of notes into a structured, publishable draft — ideation through drafting.
---

Production is where the foundation pays off. With `purpose.md`, `buckets.md`, and `tonality.md` in
place (see **[Discovery](/online-writing-skills/guides/discovery/)**), the production skills align
ideas to your purpose, draw examples from your buckets, and match your voice — instead of guessing.

Production has two parts: **find the idea**, then **shape the draft**.

## Find the idea

### `ideate` — when you have a topic but no posts

Hand it a topic, or raw material (notes, transcripts, articles), and it mines publishable post concepts
and sharp, differentiated angles. Use it when you're staring at a blank page or stuck on what to write
next.

```text
I want to create ideas for posts about <topic>.
```

Or invoke the skill directly — `/online-writing:ideate` in Claude Code, `$ideate` in Codex.

### `explore-idea` — when you have one idea to deepen

Once you've picked a concept (often from `ideate`), this thinks it through *before* drafting — angles,
claims, evidence, examples, audience stakes, stories, contradictions, business relevance. It's the step
that turns a thin idea into something with enough substance to draft well.

```text
Let's explore this idea before I draft it: <idea>.
```

## Shape the draft

Start with **`create-draft`** — it's currently the main entry point for long-form content. The others
cover Medium and short-form:

| Skill | Output | Use it for |
| --- | --- | --- |
| `create-draft` | **2,500–3,000 words** | Long-form — full blog post, article, essay, deep dive, feature. **The main entry point for long-form content.** |
| `create-medium-post` | **800–1,200 words** | Medium-ready article — stronger opening hook, compact sectioned flow, title/subtitle treatment, saved as Markdown. |
| `create-post` *(deprecated)* | **800–1,200 words** | Short-form post. Being reworked and likely renamed — see its [page](/online-writing-skills/skills/create-post/). |

They read your discovery context and apply the structural frameworks and register guidance built into
the collection. Hand them your raw material — they find the structure in *your* thinking rather than
inventing arguments for you.

```text
Turn these notes into a long-form draft (use create-draft): <raw material>.
```

### Headlines

Run [`headlines`](/online-writing-skills/skills/headlines/) any time you want options — for a
finished draft, a topic brief with no draft yet, or a published piece whose title is underperforming.
Each variant aims to communicate the What, the Who, and the Promise, with a curiosity gap.

:::note[Writing in German? (experimental)]
The German pipeline is **experimental**, not a full-fledged feature. It has its own production path:
extract a brief with `analysiere-quelle`, then draft with `schreibe-entwurf`; or transfer an existing
English article with `rewrite-de`. See the
[German workflow](/online-writing-skills/skills/overview/#german-workflow).
:::

## Next

A finished draft is ready for **[Review](/online-writing-skills/guides/review/)** — diagnose its
structure, rate its quality, tighten it, and repurpose it. For the per-skill reference, see the
[skills index](/online-writing-skills/skills/overview/).
