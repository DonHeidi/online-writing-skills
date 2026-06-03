---
title: Getting Started
description: Set up a writing project and establish the durable foundation the skills build on.
---

The collection is meant to be used inside a **writing project folder**, not only as a global
assistant prompt. A project folder gives the agent one writing context — a personal blog, a
founder-led content system, a newsletter, a client project — with its own purpose, audience, topics,
and voice.

Use separate folders when concerns should stay separate:

```text
~/writing/personal-blog/
~/writing/company-content/
~/writing/client-acme/
```

Each folder gets its own `.online-writing/` configuration, so one installation can support different
voices and strategies without mixing them. See [Configuration](/online-writing-skills/guides/configuration/).

## First-time setup

1. Create or choose a project folder for the writing context.
2. Make the skills available to your agent — see [Installation](/online-writing-skills/guides/installation/).
3. Start your agent from the project folder, or tell it explicitly which folder is the project.
4. Ask the agent to set up the online-writing configuration for this project.
5. Run **[Discovery](/online-writing-skills/guides/discovery/)** to establish the foundation.
6. Use **[Production](/online-writing-skills/guides/production/)** and
   **[Review](/online-writing-skills/guides/review/)** to draft, refine, rate, and repurpose.

A good first prompt:

```text
I want to set up this folder as an online writing project. Please guide me through the
initial setup: purpose, content buckets, and voice/tonality.
```

## The workflow

The skills are organised around three areas of work, each with its own guide. Start with **Discovery**
— it's the foundation everything else reads — but **Production** and **Review** are areas you move
between and revisit as you write, not one-way steps:

- **[Discovery](/online-writing-skills/guides/discovery/)** — establish the durable foundation:
  *why* you write (`purpose.md`), *what* you own (`buckets.md`), and *how* your voice sounds
  (`tonality.md`). This is a prerequisite for good output, not an optional extra.
- **[Production](/online-writing-skills/guides/production/)** — find the idea (`ideate`,
  `explore-idea`) and shape it into a draft (`create-post`, `create-draft`, `create-medium-post`,
  `headlines`).
- **[Review](/online-writing-skills/guides/review/)** — make a draft stronger (`diagnose`,
  `improve-writing`, `rate`) and stretch it further (`tldr`, `distill`, `illustrate`). You can review
  any piece, including one you didn't write here.

:::caution[Start with Discovery]
The production skills work without configuration, but without purpose, content buckets, and especially
voice, they fall back to generic, sales-y defaults. A few discovery interviews up front pay off across
every post you write afterward — so run [Discovery](/online-writing-skills/guides/discovery/) first.
:::

After the foundation exists, prompts can be direct:

```text
Use my online-writing context to explore three angles for a post about AI adoption risk.
Diagnose this draft and tell me why it does not land yet.
Turn this article into five X posts and two LinkedIn shorts.
```

The skills guide both setup and execution — you do not need to fill every configuration file by hand.
The discovery skills interview you, create the initial configuration, and make later writing tasks
more consistent.
