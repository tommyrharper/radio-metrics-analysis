#!/usr/bin/env python3
"""Inject mae_details into data/papers-data.json for MAE-positive papers.

Run from repo root: python3 scripts/inject_mae_details.py
Does not change top-level metrics.mae flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "mae-details.json"


def ctx(
    target_parameters=None,
    train_vs_validation=None,
    domain=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "target_parameters": target_parameters,
        "train_vs_validation": train_vs_validation,
        "domain": domain,
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


# bibcode -> list of mae_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- r2d2-citing ---
    "2025A&A...698A..61J": [
        entry(
            "parameter_regression",
            "physical_parameter_mae",
            value=None,
            unit=None,
            scope=(
                "ZINGULARITY BANN regression: spin, R_high, inclination, position angle "
                "(Fig. 4 train/validation MAE curves)"
            ),
            empirical=True,
            execution_context=ctx(
                target_parameters="spin, R_high, inclination, position angle",
                train_vs_validation="Training vs validation curves across epochs (Fig. 4)",
                domain="Visibility-domain input → physical-parameter outputs (not image MAE)",
                simulation_vs_real="Synthetic EHT training (SYMBA); validation on held-out synthetic",
                frequency="EHT (mm / 230 GHz class)",
                array="EHT (M87* / Sgr A* synthetic campaigns)",
            ),
            evidence=(
                "Mean absolute error tracks Bayesian neural-network regression performance for "
                "spin, R_high, inclination, and position angle on training vs validation data "
                "across epochs; reported qualitatively via validation curves (Fig. 4) rather "
                "than single summary scalars in the extracted text. Downstream inference "
                "accuracy on source parameters — not MAE between reconstructed and true sky "
                "brightness maps."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    mae_papers = [p for p in papers if p["metrics"].get("mae") == 1]
    missing = [p["bibcode"] for p in mae_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in mae_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not mae=1: {extra}")

    for p in papers:
        p.pop("mae_details", None)

    mirror = {
        "schema_note": (
            "mae_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.mae binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in mae_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["mae_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "mae_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in mae_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["mae_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected mae_details for {len(mae_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    # Sanity: binary mae unchanged
    assert all(p["metrics"]["mae"] == 1 for p in mae_papers)
    assert sum(1 for p in papers if p["metrics"].get("mae") == 1) == 1
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
