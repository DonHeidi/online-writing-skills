# Security Policy

## Scope

This project is a collection of writing **skills** for AI coding agents (Claude Code, Codex). It consists of:

- Markdown skill definitions (`skills/`), reference guides (`references/`), and configuration docs (`CONFIG.md`)
- One helper script, `scripts/count-words`, a Python utility that reads text from stdin and prints a word count

The skills contain **instructions for an AI agent**, not executable application code. They do not make network requests, handle credentials, or execute arbitrary code on their own. The most relevant security concerns are therefore:

- **Prompt-injection or unsafe-instruction issues** in a skill or reference guide (e.g. wording that could lead an agent to take an unintended or unsafe action).
- **Bugs in `scripts/count-words`** (the only executable code in the repo).

Writer-specific configuration (`purpose.md`, `tonality.md`, etc.) is expected to live **outside** this repository in the user's own project folder, and is never committed here.

## Reporting a vulnerability

Please report security issues **privately** — do not open a public issue for a suspected vulnerability.

- Preferred: open a private report via **GitHub Security Advisories** on this repository
  (`Security` tab → `Report a vulnerability`).
- Alternatively, email **me@sebastian-heitmann.dev** with a description and, if possible,
  steps to reproduce.

Please include the affected file(s), the version (see `version` in `.claude-plugin/plugin.json`), and the potential impact.

## What to expect

This is a personal, single-maintainer project, so responses are best-effort:

- Acknowledgement of your report within about **7 days**.
- An assessment and, where warranted, a fix released in a subsequent version with a note in the release.

Thanks for helping keep the project safe.
