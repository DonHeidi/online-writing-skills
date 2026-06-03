---
title: Discovery
description: Establish the durable foundation — purpose, content buckets, and voice — that every other skill reads.
---

Discovery is the foundation of the whole workflow and the most important part of setup. The discovery
skills build the durable context every other skill reads — and they are what make the difference
between output that sounds like *you* and output that sounds like generic AI marketing copy.

:::caution[Don't skip this]
The production skills work without configuration, but without **purpose**, **content buckets**, and
especially **voice/tonality**, they fall back to safe, generic defaults — drafts drift toward a
sales-y, everyone's-voice register. The discovery skills calibrate the agent to your actual audience,
territory, and voice. A few interviews up front pay off across every post you write afterward.
:::

The discovery skills are **interviews, not forms**. The agent asks questions, reflects a draft back to
you, and iterates until the result genuinely sounds like you. Run them **in order** — each one builds
on the last.

## 1. `discover-purpose` → `purpose.md`

**Why first:** purpose is the filter everything else passes through. Without it, ideas and angles have
nothing to align to.

It moves from a broad opening ("why are you thinking about writing online right now?") through the
dimensions that are most alive for you — motivation, audience, category, point of view, style
(educating vs. entertaining), and vision — then reflects back a draft you sharpen until it's yours.

**Produces** `purpose.md`: the labeled dimensions, a natural-language **Purpose Statement**, and a
five-question **Decision Filter** the other skills use to judge whether a topic is worth your time.

```text
Run discover-purpose with me — help me define why I write online and who it's for.
```

## 2. `discover-buckets` → `expertise.md` + `buckets.md`

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

## 3. `discover-tonality` → `tonality.md`

**Why third (and highest-leverage):** this is the file that keeps every draft sounding like you. It
needs `purpose.md` and `buckets.md` so its examples are drawn from your real domain.

It weaves preference questions, comparisons, and rewrite prompts to extract your values across six
voice dimensions — Commitment, Reasoning Style, Reader Relationship, Emotional Register, Density, and
the failure modes the agent should resist — then checks how your voice shifts by piece type and
synthesizes a profile you confirm.

**Produces** `tonality.md`: a voice summary, dimension profiles, agent-specific failure modes, register
tendencies, format rules, and 8–10 reference samples from your own rewrites. Every content skill loads
it to match your voice and check output against your anti-patterns.

```text
Run discover-tonality — build my voice profile from examples so drafts sound like me.
```

:::note[Writing in German?]
Run [`finde-stil`](/online-writing-skills/skills/finde-stil/) instead of `discover-tonality`. It produces
`stil.md` from scratch in German and is independent of `tonality.md`.
:::

## When discovery is "done"

You have a populated `purpose.md`, `buckets.md`, and `tonality.md` (or `stil.md`) that you actually
recognize as yours. They're **re-runnable** — revisit any of them later to refine the foundation as
your writing evolves.

With the foundation in place, move on to **[Production](/online-writing-skills/guides/production/)**.
For each interview's details, see [`discover-purpose`](/online-writing-skills/skills/discover-purpose/),
[`discover-buckets`](/online-writing-skills/skills/discover-buckets/), and
[`discover-tonality`](/online-writing-skills/skills/discover-tonality/).
