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
5. Run the **discovery skills** to establish the foundation (details below).
6. Once the foundation exists, use the **production skills** for ideation, drafting, rewriting,
   diagnosis, rating, and repurposing.

A good first prompt:

```text
I want to set up this folder as an online writing project. Please guide me through the
initial setup: purpose, content buckets, and voice/tonality.
```

## Establish the foundation

This is the most important part of setup. The discovery skills build the durable context every other
skill reads — and they are what make the difference between output that sounds like *you* and output
that sounds like generic AI marketing copy.

:::caution[Don't skip this]
The production skills work without configuration, but without **purpose**, **content buckets**, and
especially **voice/tonality**, they fall back to safe, generic defaults — drafts drift toward a
sales-y, everyone's-voice register. The discovery skills are what calibrate the agent to your actual
audience, territory, and voice. A few interviews up front pay off across every post you write
afterward.
:::

The discovery skills are **interviews, not forms**. The agent asks questions, reflects a draft back
to you, and iterates until the result genuinely sounds like you. Run them **in order** — each one
builds on the last:

### 1. `discover-purpose` → `purpose.md`

**Why first:** purpose is the filter everything else passes through. Without it, ideas and angles have
nothing to align to.

It moves from a broad opening ("why are you thinking about writing online right now?") through the
dimensions that are most alive for you — motivation, audience, category, point of view, style
(educating vs. entertaining), and vision — then reflects back a draft you sharpen until it's yours.

**Produces** `purpose.md`: the labelled dimensions, a natural-language **Purpose Statement**, and a
five-question **Decision Filter** the other skills use to judge whether a topic is worth your time.

```text
Run discover-purpose with me — help me define why I write online and who it's for.
```

### 2. `discover-buckets` → `expertise.md` + `buckets.md`

**Why second:** once you know *why* you write, you decide *what* you own. This stops you from writing
about everything and being known for nothing.

It lists 10–20 of your expert zones (breadth first), finds your **One Big Key Zone**, overlaps it with
2–3 secondary zones to locate your **genius zone** (the unfair-advantage intersection), then translates
that into content buckets (General / Niche / Industry) and stress-tests them for sustainability.

**Produces** `expertise.md` (the full zone list) and `buckets.md` (your buckets and topic territory),
both read by `ideate` and the drafting skills.

```text
Run discover-buckets — help me map my expertise into content buckets and find my genius zone.
```

### 3. `discover-tonality` → `tonality.md`

**Why third (and highest-leverage):** this is the file that keeps every draft sounding like you. It
needs `purpose.md` and `buckets.md` so its examples are drawn from your real domain.

It weaves preference questions, comparisons, and rewrite prompts to extract your values across six
voice dimensions — Commitment, Reasoning Style, Reader Relationship, Emotional Register, Density, and
the failure modes the agent should resist — then checks how your voice shifts by piece type and
synthesises a profile you confirm.

**Produces** `tonality.md`: a voice summary, dimension profiles, agent-specific failure modes, register
tendencies, format rules, and 8–10 reference samples from your own rewrites. Every content skill loads
it to match your voice and check output against your anti-patterns.

```text
Run discover-tonality — build my voice profile from examples so drafts sound like me.
```

:::note[Writing in German?]
Run [`finde-stil`](/online-writing-skills/skills/german/) instead of `discover-tonality`. It produces
`stil.md` from scratch in German and is independent of `tonality.md`.
:::

You can run all three in one guided setup (use the first prompt above) or one at a time. They're also
re-runnable — revisit any of them later to refine the foundation as your writing evolves. For the full
phase-by-phase breakdown, see the [Discovery reference](/online-writing-skills/skills/discovery/).

## Then produce

After setup, prompts can be direct:

```text
Use my online-writing context to explore three angles for a post about AI adoption risk.
Diagnose this draft and tell me why it does not land yet.
Turn this article into five X posts and two LinkedIn shorts.
```

The skills guide both setup and execution — you do not need to fill every configuration file by hand.
The discovery skills interview you, create the initial configuration, and make later writing tasks
more consistent.
