---
title: Configuration
description: The .online-writing/ folder that gives the skills your voice, audience, and strategy.
---

The skills expect writer-specific configuration to live **outside** the plugin, in a project- or
vault-level `.online-writing/` folder. This separation keeps the collection reusable while your own
strategy, voice, and examples stay local to your workspace.

```text
<project root>/.online-writing/
```

If the folder or an expected file does not exist, the skill that needs it creates it. The full
templates live in [`CONFIG.md`](https://github.com/DonHeidi/online-writing-skills/blob/main/CONFIG.md)
in the repository.

## Files

| File | Created by | Read by | Purpose |
| --- | --- | --- | --- |
| `purpose.md` | `discover-purpose` | ideate, create-post, create-draft, improve-writing | Motivation, audience, category, POV, style, vision, plus a Decision Filter. |
| `expertise.md` | `discover-buckets` | discover-buckets, ideate | The full list of expert zones — raw material for the genius zone. |
| `buckets.md` | `discover-buckets` | ideate, drafting skills | Content buckets (General / Niche / Industry) and topic territory. |
| `tonality.md` | `discover-tonality` | content skills | English voice profile: dimensions, failure modes, register tendencies, reference samples. |
| `stil.md` | `finde-stil` | German skills | German voice profile, produced from scratch in German. |

:::note[Voice is the highest-leverage file]
`tonality.md` (and `stil.md` for German) is what keeps output from sounding generic or
AI-generated. Content skills load it to match your voice, check against your anti-patterns, and
calibrate from your own reference samples.
:::

## How skills use it

Each skill documents which config files it reads in its own `SKILL.md`. The general pattern:

1. Load the relevant files from `.online-writing/`.
2. Detect whether each file is **populated** (a template has empty fields after the labels; a
   completed file has content and a filled-in statement section).
3. Apply the context — align ideas to purpose, draw examples from buckets, match the voice profile —
   and fall back to universal guidance when a file is still empty.

This means the skills degrade gracefully: they work without configuration, but get markedly better
once the [discovery skills](../../skills/discovery/) have run.
