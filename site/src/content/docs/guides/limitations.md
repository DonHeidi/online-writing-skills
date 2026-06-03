---
title: Known Limitations
description: What this collection is not, and the constraints to be aware of before relying on it.
---

This collection is deliberately opinionated and useful within a specific scope. Being clear about
where it stops is part of using it well.

## It needs project context to be good

The single biggest limitation: without [discovery](/online-writing-skills/skills/discovery/)
(`purpose.md`, `buckets.md`, and especially `tonality.md`), the production skills fall back to safe,
generic defaults and drift toward a sales-y, everyone's-voice register. The skills work without
configuration, but they are not designed to produce *your* voice from nothing. Treat the
[discovery setup](/online-writing-skills/guides/getting-started/) as a prerequisite, not an optional
extra.

## It is opinionated, not universal

The frameworks, quality criteria, and defaults are closely aligned with one writer's workflow and a
particular school of social-first online writing. They encode real opinions about structure, pacing,
and voice. If your conventions differ (academic writing, long-form journalism, technical reference
docs), expect friction — the skills will nudge you toward their house style.

## English-first; partial German support

The collection is English-first and biased toward **American English** conventions. German support is
a smaller, intentionally scoped subset — source analysis (`analysiere-quelle`), long-form drafting
(`schreibe-entwurf`), EN→DE rewriting (`rewrite-de`), and style (`finde-stil`).

The German pipeline has **known gaps**: short-form German drafting (`schreibe-post`) and German
micro-post distillation (`destilliere`) are referenced as future skills and **do not exist yet**. See
the [German Workflow](/online-writing-skills/skills/german/) for what is currently covered. Other
languages are not supported.

## It is not a one-shot content generator

The skills package and structure *your* thinking — they do not replace it. You still have to decide
what matters, choose the point of view, supply the raw material, and take responsibility for the
result. Hand the skills an empty prompt and you get generic output; hand them real ideas and they help
you shape them.

## No SEO optimisation

The workflows are written for human readers (and, incidentally, AI readers). There is currently **no
support for search-engine optimisation** — keyword targeting, meta structuring, or SERP-oriented
formatting. If you need SEO, you will have to layer it on yourself.

## Imagery is Midjourney-only

The [`illustrate`](/online-writing-skills/skills/refine-repurpose/) skill produces **Midjourney
prompts** only. It does not target other image generators, search stock photography, or edit existing
images, and the end-to-end image workflow (submission, asset capture, wiring) is only partially built.

## Source material handling is evolving

The skills draw on external concepts and may use reference texts during the writing process. How
sources are used — and whether they are named in the output — is still being refined. By default the
skills use ideas without explicit attribution unless you ask for it. This collection is **not** a
substitute for, endorsement of, or official companion to the works it is inspired by.

## Output is non-deterministic

These are LLM-driven skills. The same input can produce different output across runs, and quality
varies with the model and runtime you use. The evaluation skills
([`rate`](/online-writing-skills/skills/refine-repurpose/),
[`diagnose`](/online-writing-skills/skills/refine-repurpose/)) are **guidance, not guarantees** — they
reflect the frameworks' judgement, not an objective ground truth. Always review output before
publishing.

## You maintain the configuration

The writer-specific configuration lives **outside** this repository, in each project's
`.online-writing/` folder (see [Configuration](/online-writing-skills/guides/configuration/)). You are
responsible for creating, curating, and keeping it current — including using separate project folders
when contexts should not mix. Nothing is synced or stored centrally for you.

## Runtime and model dependence

The collection is distributed as a plugin for Claude Code and OpenAI Codex CLI and relies on those
agent runtimes. Behaviour, skill discovery, and quality depend on the host agent and the underlying
model. Features that work in one runtime or model tier may behave differently in another.
