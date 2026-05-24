# Online Writing — Configuration

Skills in this directory use a shared configuration folder to persist user-specific settings across sessions. This file documents where the config lives, what files it contains, and how each file should be structured.

---

## Config Location

```
<vault root>/.online-writing/
```

This folder lives at the vault root, **not** inside the skills directory. Skills reference it by this path. If the folder or any expected file does not exist, the skill that needs it should create it.

---

## Config Files

### `purpose.md`

**Created by:** discover-purpose
**Read by:** ideate, create-post, create-draft, improve-writing

Contains the user's writing purpose — their motivation, audience, category, POV, style, and vision. Used by other skills to align ideas, voice, and framing with the user's goals.

**How to detect if populated:** A placeholder `purpose.md` has empty fields after the labels. A completed one has content after each `**Label:**` line and a filled-in Purpose Statement section.

**Template:**

```markdown
# Writing Purpose

**Motivation:** [1 sentence — why you're writing online]
**Audience:** [1 sentence — who you're writing for]
**Category:** [1 sentence — what you want to be known for]
**POV:** [1 sentence — what makes your perspective unique]
**Style:** [Educating / Entertaining / Blend — with a note on tendency]
**Vision:** [1–2 sentences — what success looks like beyond metrics]

### Purpose Statement

[A 2–3 sentence synthesis that captures all of the above in natural language. This should read like something the user would say out loud to a friend, not like a corporate mission statement.]

### Decision Filter

Use this to evaluate future writing choices:
- Does this topic serve my purpose?
- Does this reach my audience?
- Does this strengthen my category?
- Does this reflect my POV?
- Does this move me toward my vision?
```

### `expertise.md`

**Created by:** discover-buckets
**Read by:** discover-buckets, ideate

Contains the user's full list of expert zones — all the skills, experiences, industries, hobbies, and perspectives they bring to their writing. This is the raw material from which the genius zone and content buckets are derived.

**How to detect if populated:** A placeholder `expertise.md` has no zones listed. A completed one has a bulleted list under Expert Zones and filled-in key zone fields.

**Template:**

```markdown
# Expert Zones

## All Zones

[Bulleted list of everything the user identified as an area of knowledge, skill, or experience]

## One Big Key Zone

[The central area of expertise — the one that has to be included]

## Secondary Key Zones

[2–4 zones that, combined with the big key zone, form the genius zone]

## Genius Zone

[1–2 sentence description of the unique intersection]
```

---

### `buckets.md`

**Created by:** discover-buckets
**Read by:** ideate, create-post, create-draft, improve-writing

Contains the user's three content buckets — audience-level categories with specific topics under each. Used by other skills to align ideation and writing with the user's content territory.

**How to detect if populated:** A placeholder `buckets.md` has empty fields after the labels. A completed one has topics listed under each bucket and a filled-in Territory Statement section.

**Template:**

```markdown
# Content Buckets

### General Audience
**Focus:** [1 sentence — what universal topics you cover]
**Topics:**
- [Topic 1]
- [Topic 2]
- [Topic 3+]

### Niche Audience
**Focus:** [1 sentence — what hyper-specific topics you own]
**Topics:**
- [Topic 1]
- [Topic 2]
- [Topic 3+]

### Company/Industry Audience
**Focus:** [1 sentence — what industry-specific topics you cover]
**Topics:**
- [Topic 1]
- [Topic 2]
- [Topic 3+]

### Territory Statement

[A 2–3 sentence synthesis that captures the genius zone and how it maps to content.]
```

---

### `tonality.md`

**Created by:** discover-tonality
**Read by:** create-post, create-draft, improve-writing, distill, rewrite-de, rate, diagnose

Contains the user's voice profile as agent drafting guidance — how an AI agent should produce text in the user's voice. Defines commitment as the root dimension (everything else derives from it), plus reasoning style, reader relationship, emotional register, and density. Includes agent-specific failure modes (LLM training-data priors to avoid), 8-10 reference samples spanning format range, annotated voice-drift failures for contrast-based calibration, and per-user register tendencies by writing type.

The universal register guidance (what descriptive / argumentative / instructional / referential pieces sound like by default, and which failure modes agents drift toward in each) lives in `references/tonality-guide.md` — that file ships with the plugin. The "Register by Writing Type" section in `tonality.md` captures the user's personal tendencies on top of that universal baseline.

**How to detect if populated:** A placeholder `tonality.md` has empty fields after the labels. A completed one has a filled-in Voice section, at least one failure mode listed, and reference samples present. The Register by Writing Type section is recommended but not required for a file to count as populated (older profiles predate it).

**Template:**

```markdown
# Tonality — Agent Drafting Guidance

This file is loaded by AI agents when producing text. It is not a style guide for human editing.

## Voice

[2-3 sentence summary — the root commitment and what follows from it]

## Dimensions

### Commitment (root)
**Tendency:** [what the user commits to — reasoning, verdicts, or both]
**Downstream effects:** [how this shapes sentence length, connective tissue, closure-resistance]
**Shifts:** [format/context-dependent variations]

### Reasoning Style
**Tendency:** [description]
**Shifts:** [format/context-dependent variations]

### Reader Relationship
**Tendency:** [description]
**Shifts:** [format/context-dependent variations]

### Emotional Register
**Tendency:** [description]
**Test:** [is the first-person subject the person who experienced the thing? If yes, drop analytical distance. If observing, analytical is correct.]
**Shifts:** [format/context-dependent variations]

### Density
**Tendency:** [description — downstream of closure-resistance]
**Shifts:** [format/context-dependent variations]

## Agent-Specific Failure Modes

You will be tempted toward these patterns. The temptation is the signal to stop, not to proceed.

- **[pattern name]:** [concrete example in the user's domain] — [why the user rejected it]

## Register by Writing Type

How the voice shifts by what the piece is trying to do. Distinct from Format Rules (which handle length). The universal baseline — what each register sounds like and which failure modes agents drift toward — lives in `references/tonality-guide.md`. This section captures personal tendencies on top of that baseline. If a register isn't one the user typically writes in, mark it as such and skip.

### Descriptive (Credible Talking Head, case study, build log, Story)
**Tendency:** [how this user describes — specifics-first habits, how reasoning gets woven in, how they close]
**Personal failure modes:** [register drift patterns this specific user has flagged — e.g. "drills the thesis when asked to write a case study"]

### Argumentative (Opinion)
**Tendency:** [how this user argues — where the thesis sits, how hard they defend, how they close]
**Personal failure modes:** [register drift patterns this specific user has flagged]

### Instructional (Actionable Guide)
**Tendency:** [how this user instructs — or "not a register this user typically writes in"]

### Referential (Curated List)
**Tendency:** [how this user curates — or "not a register this user typically writes in"]

## Format Rules

### Long-form (Blog, Medium)
[How the voice sounds at full length]

### Short-form (LinkedIn)
[How it compresses]

### Micros (X, Bluesky, Threads)
[What compressed means — the line between compressed and slogany, with examples]

## Reference Samples

[8-10 rewrite examples spanning: long-form analytical, long-form personal, short-form compressed]

## Voice-Drift Failures

[1-2 examples of what the voice sounds like when it drifts toward LLM defaults, annotated with what went wrong]

## Reload Rule

When refining or rewriting a draft across multiple passes, reload this file on every pass. The default behavior of "improve this" is regression toward training-data mean. This file counteracts that.
```

---

### `stil.md`

**Created by:** finde-stil
**Read by:** analysiere-quelle, schreibe-entwurf

Contains the user's German voice profile as agent drafting guidance — how an AI agent should produce German text in the user's voice. Sibling to `tonality.md` but independent: `finde-stil` does not read `tonality.md`, and the user can run either pipeline without the other. Adds two German-specific dimensions on top of the six in `tonality.md` (Sachlichkeit ↔ Polemik, Anglicism Stance), German-specific agent failure modes (English-coded rhythms, LinkedIn-coded structures, marketing vocab, anglicism splices), and German register tendencies.

The universal German register guidance and the cross-cutting LLM failure modes catalogue live in `references/stil-guide.md` — that file ships with the plugin. The "Register by Writing Type" section in `stil.md` captures the user's personal German tendencies on top of that universal baseline.

**How to detect if populated:** A placeholder `stil.md` has empty fields after the labels. A completed one has a filled-in Voice section, at least one failure mode listed, and reference samples present.

**Template:**

```markdown
# Stil — Anweisungen für Agenten

Diese Datei wird von KI-Agents geladen, wenn sie deutschen Text produzieren. Sie ist kein Stil-Leitfaden für menschliches Editieren.

## Voice

[2-3 Sätze, die den übergreifenden Charakter erfassen]

## Dimensions

### Commitment (root)
**Tendenz:** [worauf der Autor sich festlegt]
**Folgen:** [wie das Satzlänge, Verbindungselemente, Schluss-Resistenz prägt]
**Verschiebungen:** [format- oder kontextabhängige Variationen]

### Reasoning Style
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

### Reader Relationship
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

### Emotional Register
**Tendenz:** [Beschreibung]
**Test:** [Ist die Ich-Perspektive die Person, die das Erlebnis hatte?]
**Verschiebungen:** [Beschreibung]

### Density
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

### Sachlichkeit ↔ Polemik (deutsch-spezifisch)
**Tendenz:** [Beschreibung]
**Verschiebungen:** [Beschreibung]

## Anglicism Stance

**Beibehalten:** [Liste englischer Begriffe, die der Autor im Deutschen behält]
**Ersetzen:** [Liste englischer Begriffe, die der Autor ersetzt]
**Grenzfälle:** [Wo der Autor je nach Kontext entscheidet]

## Agent-Specific Failure Modes

Du wirst zu diesen Mustern gedrängt sein. Die Drängung ist das Stoppsignal.

- **[Mustername]:** [konkretes Beispiel] — [warum der Autor das ablehnt]

## Register by Writing Type

### Beschreibend (Fallstudie, Build-Log, Story)
**Tendenz:** [Beschreibung]
**Persönliche Failure Modes:** [Driften]

### Argumentativ (Opinion, Essay, These)
**Tendenz:** [Beschreibung]
**Persönliche Failure Modes:** [Driften]

### Anleitend (Anleitung, Praxisleitfaden)
**Tendenz:** [Beschreibung oder "kein typisches Register dieses Autors"]

### Referierend (Übersicht, Liste, Vergleich)
**Tendenz:** [Beschreibung oder "kein typisches Register dieses Autors"]

## Format Rules

### Long-form (Blog, Medium, Fachartikel)
[Beschreibung]

### Short-form (LinkedIn-DE)
[Beschreibung]

### Micros (X-DE, Bluesky-DE, Threads-DE)
[Beschreibung]

## Reference Samples

[8-10 Umschreibungs-Beispiele aus dem Interview]

## Voice-Drift Failures

[1-2 Beispiele für Drift, mit Anmerkungen]

## Reload Rule

Wenn du Entwürfe in mehreren Durchgängen verfeinerst, lade diese Datei bei jedem Durchgang neu. Lade `references/stil-guide.md` zusammen mit ihr.
```

---

### `settings.md`

**Location:** `<vault root>/.online-writing/settings.md` — same folder as the other config files.
**Created by:** any skill on first use, when a needed preference is missing
**Read by:** any skill with configurable stylistic preferences

Holds per-skill preferences that don't belong in `purpose.md`, `expertise.md`, or `buckets.md` — stylistic choices, output defaults, platform options. One H2 section per skill, keyed by the skill's folder name (e.g. `## rewrite-de`). Skills read only their own section. Settings for one skill never affect another.

**How to detect if populated (per skill):** look for an H2 heading matching the skill's name in `.online-writing/settings.md`. If the file is missing, the heading is absent, or every field under the heading is empty, the skill has no saved settings for that user.

**Template:**

```markdown
# Settings

## rewrite-de

**Gender style:** [one of the options below]
  - `Generic masculine` — *Entwickler, Mitarbeiter, Nutzer*
  - `Paired forms` — *Entwicklerinnen und Entwickler, Mitarbeiterinnen und Mitarbeiter*
  - `Gender colon` — *Entwickler:innen, Mitarbeiter:innen, Nutzer:innen*
  - `Gender star` — *Entwickler\*innen, Mitarbeiter\*innen, Nutzer\*innen*
  - `Gender gap` — *Entwickler_innen, Mitarbeiter_innen*
  - `Binnen-I` — *EntwicklerInnen, MitarbeiterInnen*
  - `Neutral forms` — participles and neutral nouns (*Entwickelnde, Studierende, Fachkraft, Person*)
  - `Mirror source` — follow whatever the English source implies; default to generic masculine when the source is ungendered
  - `Ask each time` — prompt per rewrite
**Address form:** [Mirror source / Always Sie / Always du / Ask each time]

## schreibe-entwurf

**Gender style:** [one of the options below — same options as rewrite-de]
  - `Generic masculine` — *Entwickler, Mitarbeiter, Nutzer*
  - `Paired forms` — *Entwicklerinnen und Entwickler, Mitarbeiterinnen und Mitarbeiter*
  - `Gender colon` — *Entwickler:innen, Mitarbeiter:innen, Nutzer:innen*
  - `Gender star` — *Entwickler\*innen, Mitarbeiter\*innen, Nutzer\*innen*
  - `Gender gap` — *Entwickler_innen, Mitarbeiter_innen*
  - `Binnen-I` — *EntwicklerInnen, MitarbeiterInnen*
  - `Neutral forms` — participles and neutral nouns (*Entwickelnde, Studierende, Fachkraft, Person*)
  - `Ask each time` — prompt per draft
**Address form:** [Always Sie / Always du / Ask each time] — defaulted to `Sie` if unset

## [other-skill-name]

...
```

**Writing rules:**
- Create `.online-writing/settings.md` if it doesn't exist.
- Append a new `## <skill-name>` section if the skill's section is missing; never overwrite another skill's section.
- Within the skill's own section, update fields in place.

---

## Rules for Skills

1. **Reading config:** Before using a config file, check if it exists and whether it's populated (not just a placeholder). If the file doesn't exist or is a placeholder, proceed without it — don't fail or ask the user to run another skill first.

2. **Writing config:** The skill that owns a config file (listed under "Created by") is responsible for:
   - Creating the `.online-writing/` folder if it doesn't exist
   - Creating the file if it doesn't exist
   - Overwriting placeholder content with the real output
   - Never deleting or clearing a populated file without user confirmation

3. **Don't duplicate:** Config files are the single source of truth for their content. Skills should read from config, not ask the user to re-enter information that's already stored there.

4. **Keep it human-readable:** Config files are Markdown. They should be readable and editable by the user directly in Obsidian or any text editor.

---

## Applying Config in Skills

Skills that consume config should declare which files they use and apply the following defaults. Individual skills can override or add nuance inline (e.g. "ignore channel length targets") — but they shouldn't restate the defaults below.

**Loading pattern (all consuming skills):**

1. For each declared file, check if `.online-writing/<file>.md` exists at the vault root.
2. If it exists, check whether it's populated (not just a placeholder — see "How to detect if populated" in each file's section above).
3. If any file is missing or unpopulated, proceed without it. Do not fail. Do not ask the user to run another skill first.

**Default application per file (when populated):**

- **`purpose.md`** — Align voice, audience framing, and category positioning to the stated purpose. The output should plausibly serve the user's Motivation, Audience, Category, POV, and Vision. When rewriting existing work, preserve this alignment rather than drifting.
- **`expertise.md`** — Ground the output in the user's genius zone and expert zones. Reach for examples, analogies, and evidence from within the user's authentic expertise. Avoid framings that pull outside their zones unless the user explicitly invites it.
- **`buckets.md`** — Identify which bucket (General / Niche / Industry) the output serves, and keep the topic inside the user's defined territory. For skills that produce multiple outputs (e.g. ideate), tag each output with the bucket it belongs to.
- **`tonality.md`** — Agent drafting guidance. Match dimension tendencies for the target format (long-form, short-form, micros), match register tendencies for the piece type (descriptive, argumentative, instructional, referential), check output against agent-specific failure modes, and pattern-match against reference samples and voice-drift failures for calibration. **Also read `references/tonality-guide.md`** — it holds the universal register guidance and cross-cutting LLM register failure modes that apply regardless of user-specific voice data. `tonality.md` overrides the guide where the user has expressed personal tendencies; the guide fills in the baseline everywhere else, including when `tonality.md` isn't populated. Reload both files on every refinement pass — voice drift in multi-turn rewriting regresses toward training-data defaults. For evaluation skills (rate, diagnose), check voice and register consistency against both sources rather than applying them to output.
- **`stil.md`** — German agent drafting guidance. Sibling to `tonality.md` but independent — German skills (`finde-stil`, `analysiere-quelle`, `schreibe-entwurf`, future German skills) read `stil.md` and not `tonality.md`. Match dimension tendencies, Sachlichkeit/Polemik position, anglicism stance, register tendencies, and pattern-match against German reference samples. **Also read `references/stil-guide.md`** — it holds the universal German register baselines, cross-cutting German LLM failure modes catalogue (English-coded rhythms, LinkedIn-coded structures, marketing vocab, anglicism splices, stock translation patterns), and German Textkultur rules. `stil.md` overrides the guide where the user has expressed personal tendencies; the guide fills in the baseline everywhere else. Reload both files on every refinement pass — drift in German multi-turn rewriting regresses toward translated-English-thought-leadership and German-LinkedIn defaults.

Skills that want different behaviour from these defaults should say so explicitly in their Setup section.
