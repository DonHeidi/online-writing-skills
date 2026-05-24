# Midjourney Prompt Guide

A reference for writing Midjourney prompts that pair well with online articles. Distilled from Midjourney's official Prompt Basics and Parameter documentation, plus opinionated guidance specific to writing companion imagery (heading banners, detail illustrations).

---

## Core rules

**Short beats long.** Midjourney performs best with concise, evocative prompts. Think "a quick snapshot of your idea," not a detailed brief. A 10-word prompt with strong, specific words will often beat a 40-word prompt full of qualifiers.

**Specific beats vague.** "Enormous" over "big." "Fog" over "weather." "Brass pocket watch" over "old clock." Precise nouns and adjectives steer the model; generic ones let it drift.

**Positive beats negative.** Describe what you *want*, not what you don't. "Party with no cake" will often produce a cake. For true exclusions, use the `--no` parameter at the end.

**Numbers beat plurals.** "Cats" is ambiguous (one? ten? a hundred?). "Three cats" or "a flock of birds" anchors the count.

**One scene beats a list.** Don't stack unrelated elements ("a beach, a tree, a bird, sand, sun"). Write one coherent image.

---

## The seven areas

Every Midjourney prompt benefits from decisions across these seven dimensions (you don't need all seven — include the ones that matter):

| Area | Question | Examples |
|---|---|---|
| **Subject** | Who or what? | person, animal, character, location, object |
| **Medium** | In what form? | photograph, oil painting, watercolour, pencil sketch, 3D render, woodcut |
| **Environment** | Where? | indoors, outdoors, studio, underwater, on the moon |
| **Lighting** | What kind? | soft ambient, golden hour, overcast, neon, chiaroscuro, rim light |
| **Color** | What palette? | vibrant, muted, monochromatic, pastel, black and white, limited palette |
| **Mood** | What feeling? | serene, ominous, playful, contemplative, energetic |
| **Composition** | How framed? | wide shot, close-up, bird's-eye view, portrait, rule-of-thirds, centred |

---

## Parameter reference

Parameters go at the end of the prompt. Use a space before the `--`. No punctuation. Prompt text must come before, never after.

**Correct:** `a lone cyclist on a misty road --ar 16:9 --s 250`
**Wrong:** `a lone cyclist on a misty road, --ar 16:9`
**Wrong:** `--ar 16:9 a lone cyclist on a misty road`

### Essential

| Parameter | Syntax | Purpose | Typical values |
|---|---|---|---|
| Aspect ratio | `--ar W:H` | Frame shape | `16:9`, `3:2`, `2:3`, `4:5`, `1:1`, `9:16` |
| Version | `--v N` | Model version | Defer to user's Midjourney default unless they ask |
| Stylize | `--s N` or `--stylize N` | How artistic the interpretation | 0–1000. Default 100. 50 = close to literal, 250 = painterly, 750+ = heavily stylized |
| No | `--no THING` | Exclude something | `--no text`, `--no people`, `--no stock-photo` |
| Raw | `--raw` | Less stylized, more literal | Flag (no value) — useful for photographic realism. **Common mistake:** `--style raw` is not valid syntax; the correct form is `--raw` with no value. |

### Useful

| Parameter | Syntax | Purpose |
|---|---|---|
| Chaos | `--c N` or `--chaos N` | Variety across the four generated images. 0–100. Default 0. Raise to 25–50 when a prompt keeps producing near-identical variations. |
| Weird | `--w N` or `--weird N` | Unconventional interpretation. 0–3000. Default 0. Use sparingly. |
| Quality | `--q N` | Detail/processing cost. `0.25`, `0.5`, `1`, `2`. Higher ≠ always better. |
| Niji | `--niji N` | Anime / Eastern aesthetics model. Replaces `--v`. |
| Seed | `--seed N` | Reproducibility. Useful when iterating on one generation. |
| Tile | `--tile` | Seamlessly repeating pattern. Rare for article imagery. |

### Reference-based

| Parameter | Syntax | Purpose |
|---|---|---|
| Style reference | `--sref URL` | Match visual style of a reference image. |
| Omni reference | `--oref URL` | Use a specific person/object likeness (V7+). |
| Personalization | `--p CODE` or `--profile CODE` | Apply a saved personal style profile. |

### Modes

`--draft`, `--fast`, `--turbo`, `--relax` — GPU speed / cost. Don't hardcode in generated prompts unless the user asks.

---

## Aspect ratios for article imagery

| Ratio | Shape | Good for |
|---|---|---|
| `--ar 16:9` | Wide landscape | Blog heading banners (modern web standard), presentation covers |
| `--ar 3:2` | Landscape (photographic) | Heading banners that feel photographic rather than TV-like; classic 35mm frame |
| `--ar 21:9` | Ultra-wide cinematic | Dramatic heading banners. Experimental — can produce strange crops |
| `--ar 4:3` | Slightly landscape | Older-feel, less common for web |
| `--ar 1:1` | Square | Detail image for social embedding, inline illustrations |
| `--ar 4:5` | Slight portrait | Instagram-friendly, comfortable web detail image |
| `--ar 2:3` | Portrait (photographic) | Classic portrait framing, magazine-style detail image |
| `--ar 9:16` | Tall mobile | Reels/stories/TikTok — rare for articles |

**Heading default:** `--ar 16:9` (wide, modern, atmospheric). Use `--ar 3:2` when you want a more photographic feel.

**Detail default:** `--ar 2:3` for portrait, `--ar 1:1` for square. Pick portrait when the subject has a vertical spine (a person, a tall object, a ladder); square when it's balanced or pattern-like.

---

## Heading vs. detail: how they should differ

**Heading image (landscape)**
- **Role:** sets tone, invites the reader in, lives above the headline
- **Framing:** wide, with negative space where a headline overlay could sit
- **Subject treatment:** atmospheric, suggestive — evokes the *feeling* of the piece, not its plot. Avoid literal illustration of the headline.
- **Examples:** a misty forest for a piece about uncertainty; a lone figure on a ridge for a piece about conviction; a cluttered desk at dawn for a piece about discipline

**Detail image (portrait or square)**
- **Role:** accompanies a specific section or serves as a social share asset
- **Framing:** tighter, more specific. The subject is closer, more identifiable.
- **Subject treatment:** can be more literal — illustrates a concrete element, object, or moment from the piece
- **Examples:** a close-up of a brass compass for a section on direction-finding; a hand holding a single match for a section on starting

The two images should share a visual language (same palette, same medium, same era/register) so they read as a set — not as two unrelated pieces.

---

## Choosing a visual direction

Before writing either prompt, pick a register. The register should match the piece's tone.

| Piece tone | Visual direction |
|---|---|
| Sincere, personal, reflective | Photographic, muted palette, soft natural light, wide depth of field, film grain |
| Wry, contrarian, sharp | High-contrast, graphic, saturated, bold composition, editorial-style |
| Technical, authoritative | Clean, minimal, isometric or cross-section illustrations, restrained palette |
| Playful, entertaining | Illustrated, bright palette, character-driven, flat or stylised |
| Mythic, philosophical | Painterly, dramatic lighting, timeless setting, chiaroscuro |
| **Sensitive topics** (grief, trauma, mental health, illness, disability, loss) | Quiet, understated, metaphorical over literal. Natural environments, objects, light-and-shadow studies. **Avoid:** close-up human faces (invasive), literal symbols (ribbons, tears, chains), melodramatic lighting, stock-photo tropes of suffering. The goal is to sit alongside the piece with respect, not to illustrate the pain. |

Pick the register *before* you write the prompts so both heading and detail share it.

---

## Common pitfalls

**Stock-photo clichés.** "Diverse team in a modern office" / "Woman looking at sunset" / "Hands shaking across a desk." These look like what they are. Actively steer away.

**Over-literal imagery.** A post about productivity does not need a laptop next to a clock. A post about resilience does not need a sapling in cracked earth. Search for the *emotional truth* of the piece and illustrate that — usually via a scene, not a symbol.

**Generic style tokens.** "4K, hyperrealistic, trending on artstation, masterpiece, award-winning" do very little in modern Midjourney and clutter the prompt. Cut them.

**Too many subjects.** A heading image with "a person, a book, a cat, a window, sunrise, coffee" will produce a chaotic generation. Choose one subject, one atmosphere.

**Inconsistent register across the two images.** Heading is photographic, detail is an illustration — they won't read as a set. Lock the medium before prompting.

**Forgetting `--ar`.** Default is square; if you don't set `--ar`, your heading banner will come out as a 1:1.

---

## Prompt recipe (for reference when writing one)

```
[Subject + Action] + [Environment] + [Lighting] + [Medium/Style] + [Mood] + [Composition] --ar [ratio] --s [stylize] [other params]
```

**Example (heading, atmospheric):**
```
a lone figure walking a narrow ridge at first light, soft golden haze, 35mm film photograph, contemplative, wide shot with negative space above --ar 16:9 --s 250
```

**Example (detail, object-focused):**
```
a brass compass resting on weathered paper, warm window light, close-up macro photograph, shallow depth of field, quiet and deliberate --ar 2:3 --s 150
```

**Example (detail, illustrated):**
```
hand holding a single lit match in darkness, minimal ink-and-watercolour illustration, muted palette, focused mood --ar 1:1 --s 400
```
