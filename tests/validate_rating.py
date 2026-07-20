#!/usr/bin/env python3
"""Mechanical validator for `rate` skill JSON output.

Checks the properties of a rating that are decidable without judgment:
schema shape, weight arithmetic, VPM math against the actual word count,
ledger completeness, and readiness-tier consistency.

The tables below mirror skills/rate/SKILL.md (Step 4 VPM bands, Step 8
weight profiles, readiness conditions). If SKILL.md changes those, this
file must change with it.

Usage:
    tests/validate_rating.py rating.json tests/fixtures/strong-draft.md
    tests/validate_rating.py rating.json            # skips word-count checks

Exit code 0 = all checks pass, 1 = failures (listed on stdout).
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

DIMENSIONS = [
    "clarity_of_thesis",
    "originality_insight",
    "structure_flow",
    "credibility_rigor",
    "writing_quality",
    "positioning_power",
]

WEIGHTS = {
    "technical-educational": {
        "clarity_of_thesis": 0.15, "originality_insight": 0.20,
        "structure_flow": 0.10, "credibility_rigor": 0.25,
        "writing_quality": 0.10, "positioning_power": 0.10, "vpm": 0.10,
    },
    "opinion-thought-leadership": {
        "clarity_of_thesis": 0.15, "originality_insight": 0.25,
        "structure_flow": 0.10, "credibility_rigor": 0.15,
        "writing_quality": 0.15, "positioning_power": 0.10, "vpm": 0.10,
    },
    "narrative-personal": {
        "clarity_of_thesis": 0.15, "originality_insight": 0.15,
        "structure_flow": 0.20, "credibility_rigor": 0.10,
        "writing_quality": 0.25, "positioning_power": 0.05, "vpm": 0.10,
    },
}

FORMATS = {"article", "essay", "transcript", "social post", "thread", "draft"}
DEFECT_LEVELS = {"sentence", "conceptual", "none"}
GOALS = {"client_attraction", "reach_distribution", "thought_leadership", "conversion"}


def vpm_subscore(vpm_1dp):
    if vpm_1dp >= 2.0:
        return 95
    if vpm_1dp >= 1.0:
        return 80
    if vpm_1dp >= 0.5:
        return 60
    if vpm_1dp >= 0.2:
        return 40
    return 20


def count_words(text):
    out = subprocess.run(
        [str(REPO / "scripts" / "count-words")],
        input=text, capture_output=True, text=True, check=True,
    )
    return int(out.stdout.strip())


def norm_dim(name):
    """Map a display name like 'Credibility / rigor' to its JSON key."""
    slug = re.sub(r"[^a-z]", "", str(name).lower())
    for key in DIMENSIONS:
        if slug == re.sub(r"[^a-z]", "", key):
            return key
    aliases = {
        "clarityofthesis": "clarity_of_thesis", "clarity": "clarity_of_thesis",
        "originalityinsight": "originality_insight", "originality": "originality_insight",
        "structureflow": "structure_flow", "structure": "structure_flow",
        "credibilityrigor": "credibility_rigor", "credibility": "credibility_rigor",
        "writingquality": "writing_quality", "writing": "writing_quality",
        "positioningpower": "positioning_power", "positioning": "positioning_power",
    }
    return aliases.get(slug)


def parse_effect(s):
    m = re.search(r"[-+]?\d+(?:\.\d+)?", str(s))
    return float(m.group()) if m else None


def validate(rating, source_text=None):
    errors = []
    err = errors.append

    # --- shape ---
    for field in ("source", "format", "content_type", "word_count",
                  "estimated_content_minutes", "labels", "vpm",
                  "dimensions", "deduction_ledger", "goals", "content_score"):
        if field not in rating:
            err(f"missing top-level field: {field}")
    if errors:
        return errors

    if rating["format"] not in FORMATS:
        err(f"format {rating['format']!r} not in {sorted(FORMATS)}")
    if rating["content_type"] not in WEIGHTS:
        err(f"content_type {rating['content_type']!r} not in {sorted(WEIGHTS)}")
        return errors
    weights = WEIGHTS[rating["content_type"]]

    # --- dimensions ---
    dims = {}
    for key in DIMENSIONS:
        entry = rating["dimensions"].get(key)
        if not isinstance(entry, dict) or "score" not in entry:
            err(f"dimensions.{key} missing or malformed")
            continue
        score = entry["score"]
        if not (isinstance(score, int) and 1 <= score <= 10):
            err(f"dimensions.{key}.score {score!r} is not an integer in 1-10")
            continue
        dims[key] = score
    if len(dims) != len(DIMENSIONS):
        return errors

    # --- labels ---
    labels = rating["labels"]
    if not isinstance(labels, list) or len(labels) > 20:
        err(f"labels must be a list of at most 20 entries (got {len(labels)})")
    else:
        for label in labels:
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(label)):
                err(f"label {label!r} is not a lowercase single word")
        if len(set(labels)) != len(labels):
            err("labels contain duplicates")

    # --- VPM ---
    vpm = rating["vpm"]
    instances = vpm.get("value_instances_count")
    listed = vpm.get("instances", [])
    if instances != len(listed):
        err(f"vpm.value_instances_count={instances} but {len(listed)} instances listed")
    vpm_score = vpm.get("score")
    if not isinstance(vpm_score, (int, float)) or vpm_score < 0:
        err(f"vpm.score {vpm_score!r} is not a non-negative number")
        return errors
    expected_sub = vpm_subscore(round(vpm_score, 1))
    if vpm.get("subscore") != expected_sub:
        err(f"vpm.subscore={vpm.get('subscore')} but VPM {vpm_score} maps to {expected_sub}")

    # --- word count / duration (only with the source text) ---
    if source_text is not None:
        wc = count_words(source_text)
        if rating["word_count"] != wc:
            err(f"word_count={rating['word_count']} but count-words says {wc}")
        wpm = 180 if rating["format"] == "transcript" else 225
        raw_minutes = max(1.0, wc / wpm)
        if abs(rating["estimated_content_minutes"] - raw_minutes) > 0.5001:
            err(f"estimated_content_minutes={rating['estimated_content_minutes']} "
                f"but raw duration is {raw_minutes:.2f}")
        if isinstance(instances, int):
            expected_vpm = instances / raw_minutes
            if abs(vpm_score - round(expected_vpm, 1)) > 0.05:
                err(f"vpm.score={vpm_score} but {instances}/{raw_minutes:.2f} min = "
                    f"{expected_vpm:.2f}")

    # --- content score arithmetic ---
    weighted = sum(dims[k] * 10 * weights[k] for k in DIMENSIONS)
    weighted += expected_sub * weights["vpm"]
    reported = rating["content_score"].get("score")
    if not isinstance(reported, (int, float)) or abs(reported - weighted) > 1.0:
        err(f"content_score.score={reported} but weighted sum is {weighted:.1f}")

    # --- deduction ledger ---
    ledger = rating["deduction_ledger"]
    seen = {}
    for row in ledger:
        key = norm_dim(row.get("dimension"))
        if key is None:
            err(f"ledger dimension {row.get('dimension')!r} is not a known dimension")
            continue
        seen[key] = row
        if row.get("score") != dims[key]:
            err(f"ledger score for {key} is {row.get('score')}, dimensions say {dims[key]}")
        expected_next = min(dims[key] + 1, 10)
        if row.get("next_level") != expected_next:
            err(f"ledger next_level for {key} is {row.get('next_level')}, expected {expected_next}")
        if row.get("defect_level") not in DEFECT_LEVELS:
            err(f"ledger defect_level for {key} is {row.get('defect_level')!r}, "
                f"expected one of {sorted(DEFECT_LEVELS)}")
    missing = set(DIMENSIONS) - set(seen)
    if missing:
        err(f"ledger has no entry for: {', '.join(sorted(missing))}")

    # --- goals ---
    for goal in GOALS:
        entry = rating["goals"].get(goal)
        if not isinstance(entry, dict) or not (isinstance(entry.get("score"), int)
                                               and 1 <= entry["score"] <= 10):
            err(f"goals.{goal} missing or score not an integer in 1-10")

    # --- publishing readiness (own drafts only) ---
    pr = rating.get("publishing_readiness")
    if pr is not None:
        ready = pr.get("ready")
        if ready not in ("yes", "almost", "not yet"):
            err(f"publishing_readiness.ready {ready!r} invalid")
        recs = pr.get("recommendations", [])
        if len(recs) > 3:
            err(f"{len(recs)} recommendations; the maximum is 3")
        max_effect = 0.0
        for i, rec in enumerate(recs, 1):
            key = norm_dim(rec.get("dimension"))
            if key is None:
                err(f"recommendation {i} names unknown dimension {rec.get('dimension')!r}")
                continue
            cur, proj = rec.get("current_score"), rec.get("projected_score")
            if cur != dims[key]:
                err(f"recommendation {i} current_score={cur}, dimensions say {dims[key]}")
            if not (isinstance(proj, int) and isinstance(cur, int) and proj > cur):
                err(f"recommendation {i} projected_score must exceed current_score")
                continue
            row = seen.get(key)
            if row is not None and row.get("defect_level") == "none":
                err(f"recommendation {i} targets {key}, whose ledger row has no defect")
            effect = parse_effect(rec.get("expected_score_effect"))
            expected = 10 * weights[key] * (proj - cur)
            if effect is None or abs(effect - expected) > 0.75:
                err(f"recommendation {i} expected_score_effect={rec.get('expected_score_effect')!r}, "
                    f"formula gives {expected:+.1f}")
            if effect is not None:
                max_effect = max(max_effect, effect)
        # Mechanical parts of the readiness tiers (defect/voice judgments can't be checked here)
        if any(s < 6 for s in dims.values()) and ready != "not yet":
            err(f"a dimension is below 6 but ready={ready!r} (must be 'not yet')")
        if ready == "yes":
            if any(s < 7 for s in dims.values()):
                err("ready='yes' but a dimension is below 7")
            if max_effect >= 3:
                err(f"ready='yes' but a recommendation projects {max_effect:+.1f} (>= 3)")

    return errors


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    rating = json.loads(Path(sys.argv[1]).read_text())
    source = Path(sys.argv[2]).read_text() if len(sys.argv) > 2 else None
    errors = validate(rating, source)
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    print("PASS: all mechanical checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
