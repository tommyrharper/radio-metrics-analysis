#!/usr/bin/env python3
"""Inject uncertainty_correlation_details into data/papers-data.json for UncCorr-positive papers.

Run from repo root: python3 scripts/inject_unccorr_details.py
Does not change top-level metrics.uncertainty_correlation flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "unccorr-details.json"


def ctx(
    correlation_statistic=None,
    uncertainty_source=None,
    error_reference=None,
    sample_count=None,
    simulation_vs_real=None,
    array=None,
):
    return {
        "correlation_statistic": correlation_statistic,
        "uncertainty_source": uncertainty_source,
        "error_reference": error_reference,
        "sample_count": sample_count,
        "simulation_vs_real": simulation_vs_real,
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


# bibcode -> list of uncertainty_correlation_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- r2d2-citing ---
    "2025arXiv250721270M": [
        entry(
            "uncertainty_error_correlation",
            "pearson_uncertainty_vs_abs_error",
            value=0.69,
            unit="Pearson r",
            scope="GU-Net RI-GAN; per-pixel uncertainty (std across 32 posterior samples) vs |x_true − x_pred|",
            empirical=True,
            execution_context=ctx(
                correlation_statistic="Pearson r",
                uncertainty_source="Per-pixel std across posterior samples (RI-GAN)",
                error_reference="Absolute reconstruction error vs ground truth",
                sample_count="32 (main experiments)",
                simulation_vs_real="Simulation (galaxy images; OOD 30 Doradus also discussed for SNR)",
            ),
            evidence=(
                "Uncertainty–error correlation (UQ calibration proxy): Pearson correlation between "
                "per-pixel predicted uncertainty (std across samples) and per-pixel absolute "
                "reconstruction error |x_true − x_pred|. With 32 posterior samples, GU-Net RI-GAN "
                "reaches r = 0.69 (U-Net RI-GAN r = 0.58)."
            ),
        ),
        entry(
            "comparative_unccorr",
            "higher_lower_than_baseline",
            value=0.69,
            unit="Pearson r (GU-Net) vs 0.58 (U-Net)",
            scope="GU-Net vs plain U-Net RI-GAN uncertainty–error correlation (32 samples)",
            baseline="U-Net RI-GAN (no embedded measurement operator)",
            empirical=True,
            execution_context=ctx(
                correlation_statistic="Pearson r",
                uncertainty_source="Per-pixel std across posterior samples",
                error_reference="Absolute reconstruction error vs ground truth",
                sample_count="32",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "GU-Net uncertainty maps track true error better than the plain U-Net variant: "
                "r = 0.69 vs r = 0.58 at 32 samples."
            ),
        ),
        entry(
            "comparative_unccorr",
            "correlation_vs_sample_count",
            value=32,
            unit="samples (plateau)",
            scope="Number-of-samples ablation for uncertainty–error correlation (and SNR)",
            empirical=True,
            execution_context=ctx(
                correlation_statistic="Pearson r (vs sample count)",
                uncertainty_source="Per-pixel std across N posterior samples",
                error_reference="Absolute reconstruction error vs ground truth",
                sample_count="Ablation; plateaus around 32",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Both SNR and the uncertainty–error correlation improve as the number of posterior "
                "samples increases and plateau around 32 samples; low sample counts give markedly "
                "lower correlation (interpreted as evidence of sample diversity / no mode collapse)."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    unccorr_papers = [
        p for p in papers if p["metrics"].get("uncertainty_correlation") == 1
    ]
    missing = [p["bibcode"] for p in unccorr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in unccorr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not uncertainty_correlation=1: {extra}")

    for p in papers:
        p.pop("uncertainty_correlation_details", None)

    mirror = {
        "schema_note": (
            "uncertainty_correlation_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.uncertainty_correlation binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in unccorr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["uncertainty_correlation_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "uncertainty_correlation_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in unccorr_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["uncertainty_correlation_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected uncertainty_correlation_details for {len(unccorr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["uncertainty_correlation"] == 1 for p in unccorr_papers)
    assert sum(1 for p in papers if p["metrics"].get("uncertainty_correlation") == 1) == 1
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
