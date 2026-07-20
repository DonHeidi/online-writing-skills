# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Codex, and others) when working with code in this repository.

## What this repository is

This is **not a software application** — it is a distributable collection of AI-agent *skills* for online writing, plus a docs site. There is no skill runtime or build step; a skill is a Markdown file (`SKILL.md`) of instructions an agent loads and follows. "Code" here means skill prose, a few helper scripts, plugin manifests, and an Astro docs site. The only automated checks are the `rate`-skill eval harness under `tests/` (see Commands and `tests/README.md`).

## Commands

The only executable pieces are the word-count script and the docs site.

```sh
# Word counting (used by skills; also runnable directly)
cat draft.md | scripts/count-words        # prints a single integer

# Rate-skill eval harness (see tests/README.md)
tests/validate_rating.py rating.json tests/fixtures/strong-draft.md   # mechanical checks on one rating JSON
tests/rate_eval.py --fixture tests/fixtures/strong-draft.md --runs 3  # headless runs + variance report (claude CLI, costs tokens)
# validate_rating.py mirrors SKILL.md's weight profiles, VPM bands, and
# readiness tiers — change them together in the same commit.

# Docs site (Astro Starlight), from site/
cd site
npm install
npm run dev       # http://localhost:4321/online-writing-skills/
npm run build     # production build to site/dist
npm run preview
```

Pushes to `main` that touch `site/**` (or the workflow file) auto-deploy the docs to GitHub Pages via `.github/workflows/deploy-docs.yml`. Nothing else is built or published from CI.

## Architecture

### Two-stage workflow: discovery feeds production

The whole system rests on a separation between **durable per-writer context** and **the skills that consume it**:

- **Discovery skills** (`discover-purpose`, `discover-buckets`, `discover-tonality`; `finde-stil` for German) are *interviews* that produce config files describing the writer's purpose, expertise/content buckets, and voice.
- **Production skills** (`ideate`, `explore-idea`, `create-post`, `create-draft`, `create-medium-post`, `improve-writing`, `diagnose`, `rate`, `distill`, `tldr`, `headlines`, `illustrate`) read that config to align output to the writer's voice and strategy.

Output quality is intentionally gated on this context — without it, drafts drift toward generic, sales-driven defaults.

### Config lives *outside* this repository

Writer-specific state is **never** stored in this repo. It lives at the user's vault root in `.online-writing/*.md` (`purpose.md`, `expertise.md`, `buckets.md`, `tonality.md`, `stil.md`, …). `CONFIG.md` is the **contract**: it documents every config file, its template, how to detect whether it's populated, and the shared loading rules under "Applying Config in Skills." A skill consuming config must:

1. Declare which config files it uses (see its Setup section).
2. Follow the loading pattern in `CONFIG.md` — proceed gracefully if a file is missing or is still a placeholder; **never** block to ask the user to run another skill first.

When you change config semantics in a skill, update `CONFIG.md` (and vice-versa) so the contract stays consistent.

### How skills reference shared assets (relative paths)

Skills load shared material by path *relative to the SKILL.md's own directory*:

- `../../references/*.md` — deep reusable guides (`post-structure-guide`, `tonality-guide`, `ideation-guide`, `buckets-guide`, `purpose-guide`, `stil-guide`, `midjourney-prompt-guide`). `tonality-guide.md` and `post-structure-guide.md` are the most heavily loaded.
- `../../scripts/count-words` — word counting. Skills that classify length (`diagnose`, `create-draft`, `create-medium-post`) **must pipe text through this script rather than estimating** — model word-counting is unreliable and that unreliability cascades into every length-dependent check.
- `../../CONFIG.md` — the config contract.

### Skill descriptions are the routing layer

Each `SKILL.md` frontmatter `description` follows a strict **"Use when … Not for X (see other-skill)"** shape. This cross-referencing is how the agent picks the right skill among near-neighbours (e.g. `create-post` 800–1,200 words vs `create-draft` 2,500–3,000 vs `distill` micro-posts vs `improve-writing` for existing drafts). When adding or editing a skill, keep these boundaries and back-references accurate — they are load-bearing, not documentation.

### English and German are parallel, independent tracks

German skills (`analysiere-quelle`, `schreibe-entwurf`, `finde-stil`, `rewrite-de`) form a separate family that reads `stil.md` + `stil-guide.md` and deliberately does **not** read `tonality.md`. Don't cross-wire the two voice systems. German support is experimental and partially built (e.g. `schreibe-post`, `destilliere` are referenced but not yet implemented).

### Length conventions (recurring constraint)

Word-count bands recur across skills and descriptions: short-form **800–1,200 words**, long-form **2,500–3,000 words**, micro-posts **≤280 chars**, LinkedIn shorts **800–1,200 chars**. Keep these consistent when editing skills or docs.

## Distribution & cross-file invariants

The same `skills/` directory is published through three manifests — keep them in sync when relevant:

- `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` (Claude Code)
- `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` (Codex)

**Version is duplicated** in `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` — bump both together. The long plugin `description` fields also enumerate the pipeline; update them when the skill set changes materially.

The `site/src/content/docs/skills/*.md` pages are **hand-maintained mirrors** of the skills (one per skill, plus `overview.md`), not generated. Adding, renaming, or significantly changing a skill should be reflected there. Internal links in the site must be **absolute, base-prefixed** (`/online-writing-skills/...`) — Astro does not auto-prefix the configured `base`.

## Status flags to respect

`create-post` is **deprecated** (being reworked); `illustrate`, `headlines`, and the German workflow are **experimental/beta**. The README's Disclaimer and `site` Known Limitations page are the source of truth for current scope — don't present experimental pieces as stable.
