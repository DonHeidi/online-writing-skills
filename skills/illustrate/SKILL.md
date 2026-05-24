---
name: illustrate
description: >
  Use when the user has a written piece that's missing accompanying imagery and needs visual assets to pair
  with it — banner, header, hero image, section illustration, social share graphic. Signals: the piece is
  publish-ready in words but has no imagery; the user mentions visuals, banners, or images to go with an
  article; the user is preparing a post for a platform that favours a hero image. This skill produces
  Midjourney prompts and may be followed by the `article-image-flow` automation for Midjourney submission,
  asset capture, and website wiring. Not for non-Midjourney generators, stock-photo search, or image editing.
  If the piece isn't written yet, use create-post or create-draft first.
---

# Illustrate

You generate Midjourney prompts that pair with a written piece — a **heading image** (landscape banner) and a **detail image** (portrait or square). Your job is to find the emotional truth of the piece and translate it into evocative, concise prompts that Midjourney can interpret well. Not literal illustrations of the headline; images that serve the piece.

## Setup

Read the Midjourney reference: `../../references/midjourney-prompt-guide.md` — core rules, the seven prompt areas (Subject, Medium, Environment, Lighting, Color, Mood, Composition), parameter table, aspect-ratio guide, and recipes for heading vs. detail imagery. Internalise it before proceeding.

Load config per `../../CONFIG.md` ("Applying Config in Skills"). This skill uses **`purpose.md`** and **`buckets.md`** — `purpose.md` shapes the visual register (a wry contrarian sounds visually different from a sincere personal writer); `buckets.md` anchors the topic territory (which influences subject conventions). Skips `expertise.md` — expertise matters for *what* the piece says, less for *how* it should look.

---

## Step 1 — Read the piece and find the spine

**First, verify a piece exists.** If the user has only a topic, outline, or partial draft and not a finished piece, **stop and route them to `create-post` or `create-draft` first.** Generating imagery for unfinished writing risks anchoring the piece to visuals that won't fit its final shape — the piece should dictate the imagery, not the other way around. Tell the user why and come back once they've drafted.

Read the article fully. Don't skim. Answer these for yourself before touching a prompt:

- **What is the core idea?** Not the headline, not the topic — the *one thing* the reader should feel or understand after finishing. That's your emotional target for both images.
- **What tone is this written in?** Sincere / wry / technical / playful / mythic. The tone determines the visual register (see the reference guide's table).
- **Is there a concrete scene, object, or moment at the piece's heart?** If yes, note it — it's a candidate for the detail image. (Headings should stay atmospheric, not literal.)
- **Does the piece contain its own metaphor or recurring image?** If it does, that's almost always the strongest source for the heading. A piece about waiting for permission that describes "being in the hallway" beats a writer-at-desk heading every time. Reach for the article's own imagery before inventing one.
- **Who is this for — and which bucket?** If `buckets.md` is populated, identify which bucket (General / Niche / Industry) this piece serves. The bucket determines the visual language in Step 2. If `buckets.md` is missing or the piece doesn't map cleanly to one bucket, ask the user: *"Is this for a general audience, your niche, or an industry audience?"* — you need the answer before picking a visual direction.

If the user has `purpose.md` loaded, use it: the Category, POV, and Style fields will often tell you the visual register directly.

## Step 2 — Pick the visual direction

Before writing either prompt, commit to one register. Both images must share it — otherwise they won't read as a set. Use the "Choosing a visual direction" table in the reference guide as a starting point.

### Bucket-driven visual constraints

The bucket identified in Step 1 narrows the visual field before you lock in medium, palette, and era. Apply the constraint that matches:

| Bucket | Visual constraint | Subject guidance |
|---|---|---|
| **General** | Universally readable. Broad metaphors, no domain-specific artifacts. A reader outside any niche should parse the image immediately — if the subject requires insider knowledge to interpret, it's too narrow. | Landscapes, universal human gestures, natural textures, everyday objects in unexpected light. Avoid tools, dashboards, code, industry artifacts. |
| **Niche** | Domain-fluent. Imagery the niche audience recognises as *theirs* — tools, environments, artifacts, visual shorthand that signals "this is for people like you." An outsider might find it interesting but wouldn't feel targeted. | Workspaces, tools-of-the-trade, domain-specific environments, insider details. The subject should feel earned, not generic. |
| **Industry** | Professional register. Clean, polished, industry-signaling. The image should read as "this belongs in a serious publication for people who work here" — not playful, not raw, not ambient. | Corporate environments, architecture, structured compositions, restrained colour. Lean photographic or editorial illustration over painted or rendered. |

The constraint shapes subject and register — it doesn't override medium or palette, but it sets the floor. A General piece can still be photographic or illustrated; it just can't show a Kubernetes dashboard as its heading image.

### Lock in

- **Medium.** Photographic (film, digital, specific era), painted (oil, watercolour, gouache), illustrated (line, flat, editorial), rendered (3D, isometric). One choice — don't hedge.
- **Palette.** Muted / saturated / monochrome / limited / high-contrast. One direction.
- **Era / mood.** Timeless / contemporary / retro / futuristic. One choice.

Default: **atmospheric, not literal.** Most online-writing headings benefit from mood-led imagery over plot-led imagery — literal illustrations of headlines usually produce stock-photo clichés. If the user explicitly asks for literal, go literal; otherwise, lean atmospheric and tell them you did.

## Step 3 — Heading prompt (landscape)

Write the heading prompt. This is the banner above the article — it sets tone and invites the reader in. Rules:

- **Atmospheric over literal.** Evoke the *feeling* of the piece, not its headline. A piece about uncertainty is better served by a misty forest than by a question mark.
- **Wide framing with negative space.** Leave room where a headline overlay might sit. Phrases like "wide shot," "negative space," "minimal foreground detail on [left/top]" help.
- **One subject, one atmosphere.** Don't stack. A single figure, a single landscape, a single object-in-context.
- **Aspect ratio:** `--ar 16:9` by default. Use `--ar 3:2` when you want a more photographic feel. Use `--ar 21:9` only when the user explicitly wants cinematic (experimental).
- **Stylize:** `--s 250` as a general atmospheric starting point (Midjourney's default is `--s 100`, which reads more literal; `--s 500+` pushes heavily painterly). These are conventions at current model versions; they may shift — treat as a starting point, not a law.

Follow the recipe in the reference guide: `[Subject + Action] [Environment] [Lighting] [Medium/Style] [Mood] [Composition] --ar [ratio] --s [stylize] [other]`.

Include a **one-line rationale** with the prompt — why this framing, why this medium, why this mood serves this specific piece. Explain the editorial choice, not the prompt mechanics. Example: *"Atmospheric rather than literal because the piece is about doubt, not a specific decision — a misty ridge carries ambiguity that a close-up of a signpost wouldn't."*

## Step 4 — Detail prompt (portrait or square)

Write the detail prompt. This accompanies a specific section or serves as a social asset — tighter framing, more specific subject. Rules:

- **More literal is okay.** The detail image can illustrate a concrete element from the piece — an object, a gesture, a close-up scene.
- **Tighter framing.** Close-up, macro, portrait. The subject is identifiable, not ambient.
- **Pick portrait or square based on subject shape:**
  - **Portrait (`--ar 2:3` or `--ar 4:5`)** when the subject has a vertical spine — a person, a tall object, a staircase, a ladder, a candle, a figure in motion.
  - **Square (`--ar 1:1`)** when the subject is balanced or pattern-like — an object on a surface, a symmetrical composition, an abstract texture.
- **Share visual language with the heading.** Same medium, same palette, same era. Otherwise the two images won't read as a set.
- **Stylize:** match the heading's `--s` unless you're deliberately pushing the detail harder (e.g., `--s 400` for a more illustrated detail against a `--s 250` atmospheric heading).

Include a **one-line rationale** as in Step 3 — why this framing, medium, and mood serve this piece.

## Step 5 — Variants (only if asked)

By default, produce **one primary prompt each** for heading and detail. Don't offer variants upfront — the user came for *a* prompt, not a menu.

Offer variants as part of the after-delivery soft prompts (see below). If the user then asks for a variant, push in a deliberate direction:

- **Primary atmospheric?** Variant goes literal.
- **Primary photographic?** Variant goes illustrated (or painted, or 3D).
- **Primary quiet / muted?** Variant goes bolder (higher contrast, saturated palette).

Keep the register family consistent across variants within a prompt type — both heading variants should still read as heading material.

---

## Output Format

Produce the output as structured markdown. Each prompt goes in its own **indented code block** (4 spaces) — not a fenced block — so the output can be copy-pasted into Midjourney verbatim without worrying about nested fence conflicts.

Structure:

> `# Midjourney Prompts — [Post title or 1-line summary]`
>
> **Visual direction:** [medium + palette + era, e.g. "35mm film photography, muted palette, timeless"]
>
> ---
>
> ## Heading image (landscape)
>
> *Prompt:*
>
>     [Full Midjourney prompt with parameters — indented 4 spaces so it renders as a code block]
>
> *Rationale:* [one-line editorial reasoning]
>
> ---
>
> ## Detail image (portrait or square)
>
> *Prompt:*
>
>     [Full Midjourney prompt with parameters — indented 4 spaces]
>
> *Rationale:* [one-line editorial reasoning]
>
> ---
>
> **Aspect ratio choices:** heading at [ratio] because [reason]; detail at [ratio] because [reason].

Do not include variants in the primary output — they come only when the user asks (see soft prompts below).

---

## After delivery — soft prompts

After producing the output above, offer two optional next steps. Keep it brief and non-blocking — the user decides.

- **Save to a file?** Ask whether to write the prompts to a file. If yes, ask the user where and what to name it (defer to whatever conventions apply in their environment — don't assume a specific vault layout or naming scheme).
- **Want a variant?** Offer to produce another version of either prompt pushed in a deliberate direction — "more atmospheric," "more literal," "different medium," "different palette," or "different aspect ratio." Only generate the variant when the user asks.

---

## Important Reminders

- **Midjourney prefers short, specific, positive prompts.** Long prompts with many qualifiers dilute the focus. Cut anything that isn't pulling weight.
- **Describe what you want, not what you don't.** For true exclusions, use `--no` at the end (`--no text`, `--no people`, `--no stock-photo aesthetic`).
- **Numbers beat plurals.** "Three climbers on a ridge" is better than "climbers on a ridge."
- **One scene, not a list.** Don't stack unrelated elements. Midjourney renders coherent imagery from coherent prompts.
- **Don't include `--v` unless the user specifies a version.** Let Midjourney use the user's configured default.
- **Don't include generic style tokens.** "4K, hyperrealistic, trending on artstation, masterpiece, award-winning" — these add noise, not quality. Cut them.
- **The two images are a set.** Matching medium and palette is non-negotiable. If the user likes the heading and wants to regenerate only the detail, keep the visual direction locked unless they ask to break it.
- This subskill's core output is prompts. In Sebastian's article workflow, continue with `article-image-flow` when the user asked for images rather than prompt text only.
