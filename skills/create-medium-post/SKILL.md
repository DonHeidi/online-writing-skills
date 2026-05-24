---
name: create-medium-post
description: >
  Use when the user has raw material, notes, a brain dump, outline, transcript, or loose ideas and wants a
  Medium-ready 800-1,200 word article or essay saved directly as a Markdown file. Use for Medium-specific drafting with a
  stronger opening hook, compact sectioned flow, reader retention, title/subtitle treatment, and publication
  notes when needed. For generic 800-1,200 word short-form posts use create-post; for generic 2,500-3,000 word
  blog drafts use create-draft.
---

# Create Medium Post

Transform raw material into a Medium-ready article and save it directly as a Markdown draft in the current writing workspace. The default deliverable is a file, not just a chat response.

## Setup

Read `../../references/post-structure-guide.md` and use its frameworks as the structural playbook.

Read `../../references/tonality-guide.md` and apply register guidance on every piece. Medium amplifies register drift: a reflective essay that turns into an argument, or an instructional article that turns into a sales page, loses trust quickly.

Load config per `../../CONFIG.md` ("Applying Config in Skills"). Use **`purpose.md`**, **`expertise.md`**, **`buckets.md`**, and **`tonality.md`**. Apply the user's voice profile when populated, especially `Format Rules -> Long-form (Blog, Medium)`.

## Step 1 - Read For The Medium Promise

Read the user's input without drafting yet. Identify:

- **Central promise:** what the reader gets for spending 4-6 minutes with this piece.
- **Reader identity:** who this is for on Medium, not just generally. Medium readers often click because the title names a felt problem, professional tension, lived experience, or counterintuitive lesson.
- **Writing type:** Actionable Guide, Opinion, Curated List, Story, or Credible Talking Head from the structure guide.
- **Medium angle:** why this belongs as an article, not a LinkedIn post or micro-post. Look for depth, story, proof, nuance, examples, or a durable idea.

Ignore metadata, scaffolding, frontmatter, old headline lists, and notes-to-self unless they contain actual ideas. Use the user's substance, not the wrapper around it.

## Step 2 - Extract And Shape

Group the raw material into a Medium article skeleton:

1. **Opening tension:** the problem, contradiction, story beat, or observation that earns attention.
2. **Thesis or promise:** the point the article will prove, explain, or explore.
3. **Main sections:** usually 3-6 sections. Each section should advance the article, not merely rename the same point.
4. **Evidence:** examples, personal experience, practical steps, observations, comparisons, data, or credible reasoning.
5. **Landing:** a conclusion that leaves the reader with a sharper lens, not a generic motivational close.

Target **800-1,200 words** for the Medium post body. Compress aggressively: keep the strongest spine, merge overlapping points, and move secondary angles to discarded ideas.

If the material cannot be compressed into 800-1,200 words without damaging the argument, do not write an overstuffed single post. Instead, save a brief for two separate Medium posts and ask whether to create both articles from it. The brief should include each post's working title, subtitle/promise, target reader, core argument, 3-5 section beats, and source material to reuse.

After drafting, verify the body word count with `../../scripts/count-words` by piping only the article body through stdin. If it is outside 800-1,200 words, revise before saving. For a two-post brief, do not force a word count; save the brief instead.

## Step 3 - Choose The Article Form

Pick the form that best fits the material:

- **Personal lesson essay:** story-led opening, reflective sections, practical takeaway without over-instruction.
- **Actionable guide:** promise-led opening, clear section headers, examples before advice, concrete next steps.
- **Opinion essay:** strong thesis, fair framing of the opposing view, proof through examples and reasoning.
- **Credible talking head:** observation-led, concise authority, nuanced sections, no forced personal drama.
- **Curated list:** tight premise, scannable sections, each item with a reason and implication.

Medium readers reward clarity and momentum. Use H2 headers generously, but make them content-bearing. Avoid vague headers like "The Problem" unless the surrounding article makes them work.

## Step 4 - Write For Medium

Write the article body in Markdown.

Keep these craft rules in view:

- **Open with motion.** Start inside a tension, scene, contradiction, or precise claim. Avoid throat-clearing, biography, and broad trend summaries.
- **Use the subtitle as the contract.** The title earns the click; the subtitle explains the reader promise.
- **Make sections self-propelling.** Each section should reveal something new, deepen the stakes, or move from problem to insight to implication.
- **Use Medium-native pacing.** Short paragraphs are acceptable, but don't make every sentence a standalone line. Mix brief emphasis with developed paragraphs.
- **Preserve specificity.** Keep concrete examples, named situations, and lived detail. Do not sand the material into generic productivity or thought-leadership prose.
- **Avoid platform cliches.** No "In today's fast-paced world," "game-changer," "unlock your potential," "here's the thing," or moralizing closes unless the user's voice genuinely uses them.
- **Keep the reader central.** Personal anecdotes should illuminate the reader's problem. They are evidence, not autobiography by default.

## Step 5 - Package For Publication

Use Medium-specific publication assets to shape the article, but do not place them before the post body unless the user explicitly asks for headline options or a publication package.

- Treat the chosen headline as the article title.
- Treat the subtitle as the article's first explanatory line when it belongs in the post.
- Keep tags, dek/social preview, canonical-link notes, source-link reminders, disclosures, and image suggestions out of the default output unless the user asks for Medium publication metadata.
- If claims need sources, add a brief publication note after discarded ideas instead of fabricating citations.
- If the idea was split into two posts, skip article packaging and save the two-post brief.

## Step 6 - Save The File

Save the result directly to the current workspace. Do not ask whether to save unless the user explicitly asked for chat-only output.

- Do not assume the workspace has the standard online-writing folder structure.
- For drafts, save in `120-article-draft/` when it exists. If it does not exist and the current workspace clearly uses the online-writing folder structure, create `120-article-draft/` and save there. If folder creation would be surprising or the workspace structure is unclear, save in the current working directory.
- For already-published Medium posts, save in an existing Medium-published folder when available. Prefer `122-article-published-medium/`, then `151-medium-published/`. If neither exists, create `122-article-published-medium/` only when the current workspace clearly uses the online-writing folder structure; otherwise save in the current working directory.
- Use lowercase kebab-case names, usually `medium - [topic].md`.
- If a file with the same name exists, create a clear versioned filename such as `medium - [topic] - v2.md` rather than overwriting.
- Preserve wikilinks if the source material contains them.
- The saved file should contain only the Medium post body by default, plus `## Publication Notes` only when needed. Do not include discarded ideas in the saved post unless the user asks for process notes in the file.
- If saving a two-post brief, make the file clearly a brief, usually `medium - [topic] - two-post-brief.md`.

## Step 7 - If The User Approves The Split

When the user agrees to proceed from a saved two-post brief, create both Medium articles and save both files. Do not leave the user with only the brief after they approve the split.

- Use the brief as the source of truth for both articles.
- Each article must independently satisfy the 800-1,200 word target.
- Save each article as its own Markdown file using clear filenames such as `medium - [topic] - part-1.md` and `medium - [topic] - part-2.md`, or more specific kebab-case titles when obvious.
- Prefer deploying parallel subagents when the environment supports it: one subagent owns Post 1 and one owns Post 2. Give each subagent only its assigned brief section, the shared source material it needs, and a distinct output filename. Tell subagents not to edit each other's files.
- If subagents are unavailable, write the two posts sequentially, but still save both files before reporting completion.
- After saving, respond with both paths, then discarded ideas, then next steps.

## Saved File Format

```markdown
[Full Medium post body only, starting with the chosen title and subtitle if used. Use H2/H3 headers where useful.]

## Publication Notes

[Only include if needed: source needed, canonical link, disclosure, image suggestion, or other publishing caveat. Otherwise omit this section.]

```

## Two-Post Brief Format

Use this format only when the raw material cannot fit one 800-1,200 word Medium post without becoming rushed or overcrowded.

```markdown
# [Topic] - Two-Post Brief

## Why Split

[Brief explanation of why one post would be too compressed.]

## Post 1

**Working title:** [title]
**Subtitle/promise:** [subtitle]
**Target reader:** [reader]
**Core argument:** [argument]

### Section Beats

1. [beat]
2. [beat]
3. [beat]

### Source Material To Reuse

[Relevant notes, examples, or claims]

## Post 2

**Working title:** [title]
**Subtitle/promise:** [subtitle]
**Target reader:** [reader]
**Core argument:** [argument]

### Section Beats

1. [beat]
2. [beat]
3. [beat]

### Source Material To Reuse

[Relevant notes, examples, or claims]
```

## Chat Response After Saving

After saving the file, respond with:

```markdown
Saved: [path/to/file.md]

## Discarded Ideas

[Tangents or unused ideas from the raw material. Or "None."]

Next steps: [briefly offer diagnose, rate, or publication metadata if useful]
```

For an approved two-post split, respond with:

```markdown
Saved:
- [path/to/post-1.md]
- [path/to/post-2.md]

## Discarded Ideas

[Tangents or unused ideas from the raw material. Or "None."]

Next steps: [briefly offer diagnose, rate, or publication metadata if useful]
```

Show discarded ideas before asking for next steps.

- Run `diagnose` for structural review.
- Run `rate` for quality and VPM scoring.
- Generate Medium publication metadata if the user wants tags, headline alternatives, social preview, or canonical-link notes.

## Important Reminders

- Medium-specific does not mean generic Medium voice. Apply the user's tonality first.
- Do not invent expertise, statistics, or lived experience the user did not provide.
- If claims need sources, mark that clearly in publication notes instead of fabricating citations.
- Do not pad to hit length. Ask for more material or write the natural-length version.
