#!/usr/bin/env python3
"""Inject credint_details into data/papers-data.json for CredInt-positive papers.

Run from repo root: python3 scripts/inject_credint_details.py
Does not change top-level metrics.credible_interval flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "credint-details.json"


def ctx(
    credible_level=None,
    spatial_aggregation=None,
    estimation_method=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "credible_level": credible_level,
        "spatial_aggregation": spatial_aggregation,
        "estimation_method": estimation_method,
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


# bibcode -> list of credint_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- emerging-ml ---
    "2023ApJ...943..144M": [
        entry(
            "posterior_sample_intervals",
            "parameter_posterior_intervals",
            value=None,
            unit=None,
            scope="PRIMO MCMC corner plots: eigenimage / structure-parameter posteriors vs ground truth",
            empirical=True,
            execution_context=ctx(
                credible_level="Posterior intervals (corner-plot; level not standardized in notes)",
                spatial_aggregation="Parameter (PCA / image-structure coefficients)",
                estimation_method="MCMC posterior sampling",
                simulation_vs_real="Simulation (2017 Apr 5 M87 EHT (u,v) + thermal noise)",
                frequency="EHT / mm-VLBI (M87)",
                array="EHT",
            ),
            evidence=(
                "Corner plots compare ground-truth parameters with highest-likelihood values and "
                "posterior intervals. Low-order component posteriors are narrower than priors; "
                "higher-order components are increasingly prior-dominated. No calibrated coverage "
                "summary across a test set."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024A&A...690A.387R": [
        entry(
            "posterior_sample_intervals",
            "relative_posterior_uncertainty_maps",
            value="~1e-3–1e-2",
            unit="relative posterior uncertainty (hotspot)",
            scope="fast-resolve variational posterior uncertainty maps (VLA Cygnus A / resolve comparison)",
            empirical=True,
            execution_context=ctx(
                credible_level="Relative posterior uncertainty (not a stated HPD %)",
                spatial_aggregation="Pixel-wise maps",
                estimation_method="Variational Bayesian posterior (resolve / fast-resolve)",
                simulation_vs_real="Real VLA observation (Cygnus A)",
                frequency=None,
                array="VLA",
            ),
            evidence=(
                "Pixelwise relative posterior uncertainty maps reported at ~10⁻³–10⁻² in hotspot "
                "(bright) regions, increasing toward lower-surface-brightness areas — Bayesian UQ "
                "not available from CLEAN. No tabulated HPD/LCI widths."
            ),
        ),
    ],
    "2024RASTI...3..505L": [
        entry(
            "hpd_local_credint",
            "hpd_credible_regions",
            value="100(1−α)%",
            unit="HPD credible level (Eq. 29–32)",
            scope="QuantifAI MAP-potential HPD regions (four test images; MCMC-free approximation)",
            empirical=True,
            execution_context=ctx(
                credible_level="100(1−α)% HPD (Pereyra 2017 concentration bound)",
                spatial_aggregation="Full-image / region potential",
                estimation_method="Analytic HPD from MAP potential (no MCMC)",
                simulation_vs_real="Simulation (gridded FFT + MeerKAT NUFFT experiments)",
                frequency=None,
                array="Simulated; MeerKAT visibility patterns (Section 6)",
            ),
            evidence=(
                "HPD credible regions at level 100(1−α)% approximated analytically from the MAP "
                "potential via a concentration bound, underwriting all downstream UQ tools."
            ),
        ),
        entry(
            "hpd_local_credint",
            "hpd_hypothesis_testing",
            value=0.01,
            unit="α (99% HPD isocontour γ̂₀.₀₁)",
            scope="Inpainting (Table 2) and Gaussian-blur (Table 3) surrogate hypothesis tests",
            baseline="SK-ROCK MCMC HPD tests (MAP vs MCMC outcomes agree)",
            empirical=True,
            execution_context=ctx(
                credible_level="99% HPD (α=0.01)",
                spatial_aggregation="Region-of-interest / surrogate image",
                estimation_method="MAP potential vs HPD isocontour; validated vs SK-ROCK MCMC",
                simulation_vs_real="Simulation (M31, W28, Cygnus A, 3C288)",
                array="Simulated RI",
            ),
            evidence=(
                "Surrogate potentials compared to the 99% HPD isocontour. QuantifAI correctly rejects "
                "artefact hypotheses for physical structures in M31, W28 and 3C288; inconclusive for "
                "a small Cygnus A feature. MAP and MCMC test outcomes agree in every reported case."
            ),
        ),
        entry(
            "hpd_local_credint",
            "local_credible_intervals",
            value="0.20 / 0.08 / 0.24 / 0.07",
            unit="mean LCI (16×16 superpixels; image order as Figure 7)",
            scope="Local Credible Intervals l_i = ξ+,Ωi − ξ−,Ωi on four test images",
            empirical=True,
            execution_context=ctx(
                credible_level="HPD-boundary LCI widths",
                spatial_aggregation="16×16 superpixels (also 8×8 timing tables)",
                estimation_method="Root-finding on HPD boundary; qualitative check vs posterior-sample std",
                simulation_vs_real="Simulation (four astronomical test images)",
                array="Simulated RI",
            ),
            evidence=(
                "Mean LCI values for 16×16 superpixels: 0.20, 0.08, 0.24, 0.07 (Figure 7 order); "
                "higher mean LCI flags M31 and 3C288 as more uncertain. Validated qualitatively "
                "against posterior-sample standard deviation."
            ),
        ),
    ],
    "2024arXiv241023178C": [
        entry(
            "bootstrap_conformal_intervals",
            "pixel_confidence_intervals",
            value=0.9,
            unit="target confidence level (1−δ)",
            scope="CARB conformalized augmented equivariant bootstrap pixel intervals (EVIL-Deconv)",
            baseline="Quantile regression / parametric & equivariant bootstrap / uncalibrated CARB",
            empirical=True,
            execution_context=ctx(
                credible_level="90% (α=δ=0.1)",
                spatial_aggregation="Pixel-wise (64×64 patches)",
                estimation_method="Augmented equivariant bootstrap + conformal calibration",
                simulation_vs_real="Simulation (MeerKAT PSFs; HST-derived ground truth)",
                array="MeerKAT (simulated PSFs)",
            ),
            evidence=(
                "CARB produces pixel-wise predictive intervals via RI-specific equivariant "
                "bootstrap group actions plus conformal calibration on EVIL-Deconv reconstructions."
            ),
        ),
        entry(
            "bootstrap_conformal_intervals",
            "interval_length_coverage",
            value="0.34 length ratio; 91% coverage",
            unit="mean ℓ2 interval-length / ‖x⋆‖₂; empirical coverage",
            scope="Table 1 CARB vs QR / bootstrap baselines (target ≥90% coverage)",
            baseline="QR 0.15/14%; CQR 204/92%; param boot 0.07/0%; equiv boot 0.13/7%; uncal. CARB 0.29/87%",
            empirical=True,
            execution_context=ctx(
                credible_level="90% target coverage",
                spatial_aggregation="Pixel / image ℓ2 aggregate",
                estimation_method="Conformalized Augmented Radio Bootstrap (CARB)",
                simulation_vs_real="Simulation",
                array="MeerKAT (simulated)",
            ),
            evidence=(
                "UQ interval tightness (mean ℓ2 length ratio) and empirical coverage: CARB 0.34 / 91% "
                "— best trade-off of tight intervals with valid coverage among reported methods."
            ),
        ),
    ],
    "2025arXiv250102473D": [
        entry(
            "posterior_sample_intervals",
            "pixel_percentile_ranges",
            value="16th–84th",
            unit="posterior percentile band",
            scope="IRIS score-based posterior samples on ALMA/DSHARP disks (pixel UQ)",
            empirical=True,
            execution_context=ctx(
                credible_level="16th–84th percentile (~68% central interval)",
                spatial_aggregation="Pixel-wise",
                estimation_method="Score-based posterior sampling (PC / Euler SDE); TARP-calibrated VP+PC",
                simulation_vs_real="Simulation + real ALMA DSHARP (e.g. RU Lup, WaOph 6)",
                frequency="ALMA (DSHARP)",
                array="ALMA",
            ),
            evidence=(
                "Posterior samples yield pixel-wise 16th–84th percentile ranges and per-pixel "
                "statistical moments. TARP used as primary calibration/coverage check (VP SDE + PC "
                "achieved calibrated posteriors); not a named HPD/LCI pipeline."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    credint_papers = [p for p in papers if p["metrics"].get("credible_interval") == 1]
    missing = [p["bibcode"] for p in credint_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in credint_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not credible_interval=1: {extra}")

    for p in papers:
        p.pop("credint_details", None)

    mirror = {
        "schema_note": (
            "credint_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.credible_interval binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in credint_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["credint_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "credint_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in credint_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["credint_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected credint_details for {len(credint_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["credible_interval"] == 1 for p in credint_papers)
    assert sum(1 for p in papers if p["metrics"].get("credible_interval") == 1) == 5
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
