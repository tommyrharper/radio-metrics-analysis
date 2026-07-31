#!/usr/bin/env python3
"""Inject astrometric_accuracy_details into data/papers-data.json for Astrometry-positive papers.

Run from repo root: python3 scripts/inject_astrometric_accuracy_details.py
Does not change top-level metrics.astrometric_accuracy flags.

Current review has zero positives under the strict include rules; CLASSIFICATIONS
is empty and the mirror papers map is empty. Add entries here when papers score 1.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "astrometric-accuracy-details.json"


def ctx(
    units=None,
    reference_type=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "units": units,
        "reference_type": reference_type,
        "simulation_vs_real": simulation_vs_real,
        "frequency": frequency,
        "array": array,
    }


def entry(
    category,
    submetric,
    *,
    value=None,
    unit=None,
    scope=None,
    baseline=None,
    empirical=True,
    execution_context=None,
    evidence=None,
):
    return {
        "category": category,
        "submetric": submetric,
        "value": value,
        "unit": unit,
        "scope": scope,
        "baseline": baseline,
        "empirical": empirical,
        "execution_context": execution_context or ctx(),
        "evidence": evidence,
    }


# bibcode -> list of astrometric_accuracy_details entries
# Empty: no paper has astrometric_accuracy: 1 under current strict rules.
CLASSIFICATIONS: dict[str, list[dict]] = {}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    prior_had = any("astrometric_accuracy_details" in p for p in papers)
    astro_papers = [
        p for p in papers if p["metrics"].get("astrometric_accuracy") == 1
    ]
    missing = [
        p["bibcode"] for p in astro_papers if p["bibcode"] not in CLASSIFICATIONS
    ]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in astro_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not astrometric_accuracy=1: {extra}")

    for p in papers:
        p.pop("astrometric_accuracy_details", None)

    mirror = {
        "schema_note": (
            "astrometric_accuracy_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.astrometric_accuracy binary flags are unchanged. "
            "Empty papers map: zero positives under current strict include rules."
        ),
        "papers": {},
    }

    for p in astro_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["astrometric_accuracy_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "astrometric_accuracy_details": details,
        }

    # Avoid dirtying shared papers-data.json on a no-op zero-positive run.
    if astro_papers or prior_had:
        PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    cat_papers: dict[str, set[str]] = defaultdict(set)
    sub_papers: dict[tuple[str, str], set[str]] = defaultdict(set)
    for p in astro_papers:
        seen_cats: set[str] = set()
        seen_subs: set[tuple[str, str]] = set()
        for d in p["astrometric_accuracy_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected astrometric_accuracy_details for {len(astro_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["astrometric_accuracy"] == 1 for p in astro_papers)
    assert sum(1 for p in papers if p["metrics"].get("astrometric_accuracy") == 1) == 0
    if astro_papers or prior_had:
        print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")
    else:
        print(
            f"Wrote {MIRROR.relative_to(ROOT)} "
            "(papers-data unchanged: zero positives)"
        )


if __name__ == "__main__":
    main()
