#!/usr/bin/env python3
"""Run the `rate` skill headlessly N times on a fixture and report
validity plus score variance.

Each run launches `claude -p` in the repo root, tells it to follow
skills/rate/SKILL.md on the fixture, and requests JSON output. Every
result is checked with validate_rating.py, then the spread of the
content score and dimension scores across runs is reported. Low spread
is the point of the deterministic scoring rework — this measures it.

Requires the `claude` CLI and consumes real tokens (one full skill run
per repetition — expect roughly a minute per run).

Usage:
    tests/rate_eval.py --fixture tests/fixtures/strong-draft.md --runs 3
    tests/rate_eval.py --fixture tests/fixtures/padded-draft.md --own-draft
    tests/rate_eval.py --fixture ... --keep out/   # save raw JSON per run
"""

import argparse
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_rating import DIMENSIONS, validate  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def build_prompt(fixture, own_draft):
    role = (
        "my own draft that I am considering publishing"
        if own_draft else
        "external content written by someone else"
    )
    return (
        f"Read skills/rate/SKILL.md and follow its instructions exactly to rate "
        f"the content of the file {fixture}. Treat the piece as {role}. "
        f"There is no .online-writing config directory in this project — proceed "
        f"with the documented no-config fallback; do not ask about it. "
        f"Use the JSON output format: reply with a single raw JSON object only — "
        f"no markdown fences, no commentary before or after."
    )


def extract_json(text):
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object in output")
    return json.loads(text[start:end + 1])


def run_once(prompt, model, timeout):
    cmd = ["claude", "-p", prompt, "--allowedTools", "Read,Glob,Grep,Bash"]
    if model:
        cmd += ["--model", model]
    out = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, timeout=timeout)
    if out.returncode != 0:
        raise RuntimeError(f"claude exited {out.returncode}: {out.stderr.strip()[:300]}")
    return extract_json(out.stdout)


def spread(name, values):
    if not values:
        return f"  {name:<22} —"
    mean = statistics.mean(values)
    sd = statistics.stdev(values) if len(values) > 1 else 0.0
    return (f"  {name:<22} mean {mean:5.1f}   sd {sd:4.2f}   "
            f"range {min(values)}–{max(values)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fixture", required=True, type=Path)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--own-draft", action="store_true",
                    help="rate as the user's own draft (adds publishing_readiness)")
    ap.add_argument("--model", default=None, help="model override for claude -p")
    ap.add_argument("--timeout", type=int, default=600, help="seconds per run")
    ap.add_argument("--keep", type=Path, default=None,
                    help="directory to save each run's raw rating JSON")
    args = ap.parse_args()

    source_text = args.fixture.read_text()
    prompt = build_prompt(args.fixture, args.own_draft)
    if args.keep:
        args.keep.mkdir(parents=True, exist_ok=True)

    ratings, failures = [], 0
    for i in range(1, args.runs + 1):
        try:
            rating = run_once(prompt, args.model, args.timeout)
        except Exception as e:
            failures += 1
            print(f"run {i}: ERROR — {e}")
            continue
        if args.keep:
            name = re.sub(r"\W+", "-", args.fixture.stem)
            (args.keep / f"{name}-run{i}.json").write_text(json.dumps(rating, indent=2))
        errors = validate(rating, source_text)
        score = rating.get("content_score", {}).get("score")
        status = "valid" if not errors else f"{len(errors)} check(s) FAILED"
        print(f"run {i}: score {score} — {status}")
        for e in errors:
            print(f"        FAIL: {e}")
        if errors:
            failures += 1
        ratings.append(rating)

    if len(ratings) < 2:
        print("\nNeed at least 2 successful runs for variance stats.")
        return 1 if failures else 0

    print(f"\nVariance across {len(ratings)} runs "
          f"({args.fixture.name}{', own draft' if args.own_draft else ''}):")
    scores = [r["content_score"]["score"] for r in ratings
              if isinstance(r.get("content_score", {}).get("score"), (int, float))]
    print(spread("content score", scores))
    for dim in DIMENSIONS:
        vals = [r["dimensions"][dim]["score"] for r in ratings
                if isinstance(r.get("dimensions", {}).get(dim, {}).get("score"), int)]
        print(spread(dim, vals))
    vpms = [round(r["vpm"]["score"], 1) for r in ratings
            if isinstance(r.get("vpm", {}).get("score"), (int, float))]
    print(spread("vpm", vpms))

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
