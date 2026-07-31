#!/usr/bin/env python3
"""Inject wasserstein_details into data/papers-data.json for Wasserstein-positive papers.

Run from repo root: python3 scripts/inject_wasser_details.py
Does not change top-level metrics.wasserstein flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "wasser-details.json"


def ctx(
    window_size=None,
    distance_order=None,
    aggregation=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "window_size": window_size,
        "distance_order": distance_order,
        "aggregation": aggregation,
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


# bibcode -> list of wasserstein_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- r2d2-citing ---
    "2025AJ....169..289W": [
        entry(
            "windowed_distance",
            "w5_windowed_w1",
            value=None,
            unit="W₅ (dimensionless aggregate)",
            scope="HL Tau (ALMA) and Cygnus A (VLA) reconstructions without ground truth",
            empirical=True,
            execution_context=ctx(
                window_size="5×5 sliding window",
                distance_order="Wasserstein-1 (W₁)",
                aggregation="L2 norm of per-pixel W₁ over the image (W₅)",
                simulation_vs_real="Real (HL Tau, Cygnus A); sims use SNR instead",
                frequency="ALMA Band 6 (HL Tau); VLA (Cygnus A)",
                array="ALMA; VLA",
            ),
            evidence=(
                "Defines W₅ as the L2 norm of per-pixel Wasserstein-1 distances in 5×5 "
                "sliding windows between reconstructions — fidelity proxy where no ground "
                "truth exists."
            ),
        ),
        entry(
            "cross_iteration",
            "successive_reconstruction",
            value=None,
            unit=None,
            scope="W₅ vs major-cycle / iteration progress on real datasets",
            empirical=True,
            execution_context=ctx(
                window_size="5×5",
                distance_order="W₁",
                aggregation="W₅ (L2 of local W₁)",
                simulation_vs_real="Real (HL Tau, Cygnus A)",
                frequency=None,
                array="ALMA; VLA",
            ),
            evidence=(
                "W₅ decreases with iteration count and is used to argue convergence of "
                "the decentralized reconstruction on HL Tau and Cygnus A."
            ),
        ),
        entry(
            "cross_method",
            "parallel_vs_serial",
            value=None,
            unit=None,
            scope="Parallel (p-msc, p-L1) vs serial (msc, L1) output images",
            baseline="Serial ms-CLEAN / L1 reconstructions",
            empirical=True,
            execution_context=ctx(
                window_size="5×5",
                distance_order="W₁",
                aggregation="W₅",
                simulation_vs_real="Real (HL Tau, Cygnus A)",
                frequency=None,
                array="ALMA; VLA",
            ),
            evidence=(
                "W₅ between parallel and serial reconstructions used to argue similarity "
                "of decentralized vs serial output images on the same real data."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    wasser_papers = [p for p in papers if p["metrics"].get("wasserstein") == 1]
    missing = [p["bibcode"] for p in wasser_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in wasser_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not wasserstein=1: {extra}")

    for p in papers:
        p.pop("wasserstein_details", None)

    mirror = {
        "schema_note": (
            "wasserstein_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.wasserstein binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in wasser_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["wasserstein_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "wasserstein_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in wasser_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["wasserstein_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected wasserstein_details for {len(wasser_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["wasserstein"] == 1 for p in wasser_papers)
    assert sum(1 for p in papers if p["metrics"].get("wasserstein") == 1) == 1
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
