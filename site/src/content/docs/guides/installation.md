---
title: Installation
description: Install the Online Writing plugin in Claude Code or OpenAI Codex CLI, or use the skills directly.
---

The collection ships as a plugin for both **Claude Code** and **OpenAI Codex CLI**, sharing the same
`skills/` directory. You can install it as a managed plugin or point your agent at a local clone.

## Claude Code

Claude Code supports plugin marketplaces. The canonical reference is the
[Claude Code plugin docs](https://code.claude.com/docs/en/discover-plugins.md).

You install the plugin **directly from the public GitHub repository**
([`github.com/DonHeidi/online-writing-skills`](https://github.com/DonHeidi/online-writing-skills)) — no
local clone required. Add the repository as a marketplace using its **HTTPS URL**, then install the
plugin:

```text
/plugin marketplace add https://github.com/DonHeidi/online-writing-skills.git
/plugin install online-writing@online-writing-marketplace
```

Claude Code clones the repository for you (you don't need a local copy) and reads
`.claude-plugin/marketplace.json` from the default branch.

:::caution[Use the HTTPS URL, not the `owner/repo` shorthand]
Claude Code also accepts the GitHub shorthand `/plugin marketplace add DonHeidi/online-writing-skills`,
but it clones over **SSH** (`git@github.com:…`), which only works if you have a GitHub **SSH key**
configured. The HTTPS URL above works on any machine — a public repo clones without authentication.
:::

You can also browse and install interactively:

```text
/plugin
```

To update later:

```text
/plugin marketplace update online-writing-marketplace
```

### From a local clone

If you prefer a local checkout you can keep up to date with Git:

```sh
mkdir -p ~/skills
cd ~/skills
git clone https://github.com/DonHeidi/online-writing-skills.git
```

```text
/plugin marketplace add ~/skills/online-writing-skills
```

## OpenAI Codex CLI

Codex CLI also supports skills and plugins. This repository ships a Codex manifest at
`.codex-plugin/plugin.json` and a repo-scoped marketplace at `.agents/plugins/marketplace.json`,
both pointing at the same shared `skills/` directory. The canonical reference is the
[Codex skills docs](https://developers.openai.com/codex/skills).

Clone the repository, then browse and install from inside Codex:

```sh
git clone https://github.com/DonHeidi/online-writing-skills.git
```

```text
/plugins
```

Alternatively, Codex discovers skills directly from `.agents/skills/` (repo) or `~/.agents/skills/`
(personal). Symlink or copy the `skills/` directory into one of those locations if you want
skill-level discovery without installing the full plugin.

## Use the skills directly

You do not need a plugin runtime at all. Clone or download the repository and tell any capable agent
to inspect it and set the skills up for your project. The important thing is that the agent can see
the `skills/`, `references/`, and `CONFIG.md` files.

:::tip[Set context first]
The skills are heavily affected by project context. Without **purpose**, **content buckets**, and
especially **voice/tonality**, output may sound generic or sales-driven. Run the
[discovery skills](/online-writing-skills/guides/discovery/) before producing content. See [Getting Started](/online-writing-skills/guides/getting-started/).
:::
