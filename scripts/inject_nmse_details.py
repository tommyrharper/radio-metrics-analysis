#!/usr/bin/env python3
"""Inject nmse_details into data/papers-data.json for NMSE-positive papers.

Run from repo root: python3 scripts/inject_nmse_details.py
Use --mirror-only to write only data/nmse-details.json (no papers-data.json edit).
Does not change top-level metrics.nmse_nrmse flags.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "nmse-details.json"


def ctx(
    domain=None,
    formula_scale=None,
    reference=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "domain": domain,
        "formula_scale": formula_scale,
        "reference": reference,
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


# bibcode -> list of nmse_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "1984A&A...137..159S": [
        entry(
            "unspecified",
            "unspecified",
            scope="SDI CLEAN synthetic contour comparisons",
            empirical=False,
            execution_context=ctx(
                domain="Image (qualitative / unreported RMS)",
                formula_scale=None,
                reference="Original synthetic object",
                simulation_vs_real="Noise-free and noisy synthetic tests",
            ),
            evidence=(
                "Flagged nmse_nrmse=1, but the summary reports only that modified CLEAN has "
                "lower RMS error against the original object with no numeric RMS/NMSE values, "
                "and no explicit NMSE/NRMSE formulation. Left unspecified rather than overclassified."
            ),
        ),
    ],
    "2018A&A...616A..27V": [
        entry(
            "unspecified",
            "unspecified",
            scope="IDG vs classical gridding accuracy tests",
            empirical=True,
            execution_context=ctx(
                domain="Visibility RMS / residual-image RMS (not NMSE)",
                formula_scale=None,
                reference="Direct measurement-equation evaluation",
                simulation_vs_real="LOFAR Toothbrush metadata simulation",
                frequency="130–132 MHz",
                array="LOFAR (55 stations)",
            ),
            evidence=(
                "Reports visibility-domain RMS error and residual-image RMS vs classical gridding, "
                "plus analytic aliasing energy — not NMSE/NRMSE by name. Flagged nmse_nrmse=1 from "
                "classification; left unspecified on this drill-down."
            ),
        ),
    ],
    "2023arXiv230606007K": [
        entry(
            "visibility_domain",
            "fractional_visibility_nmse",
            value=1e-9,
            unit="fractional NMSE floor (double precision)",
            scope="Direction-cosine and HEALPix accuracy sweeps vs direct point-source evaluation",
            empirical=True,
            execution_context=ctx(
                domain="Visibility",
                formula_scale="Fractional NMSE (requested vs achieved accuracy targets)",
                reference="Direct evaluation of point-source sky model visibilities",
                simulation_vs_real="Simulation (SKA-Low-style setups; also LOFAR dirty demo without NMSE)",
                frequency="150 MHz (default SKA-Low sim channel)",
                array="SKA-Low (simulated); LOFAR-HBA demo (no NMSE)",
            ),
            evidence=(
                "Controlled accuracy experiment measures NMSE between visibilities from direct "
                "point-source evaluation vs HVOX, chunked HVOX (500 MB partition limit), NIFTY "
                "(DUCC W-gridder), and NIFTY 2D without w-term. Monolithic HVOX tracks requested "
                "NMSE down to ≈10⁻⁹ (FINUFFT upsampling floor); chunked HVOX slightly misses "
                "targets due to summed-block error; HEALPix matches direction-cosine NMSE for HVOX."
            ),
        ),
        entry(
            "comparative_nmse",
            "higher_lower_than_baseline",
            scope="HVOX / chunked HVOX vs NIFTY and NIFTY 2D (no w-term) on visibility NMSE",
            baseline="NIFTY (DUCC W-gridder); NIFTY 2D without w-term; direct-evaluation target",
            empirical=True,
            execution_context=ctx(
                domain="Visibility",
                formula_scale="Fractional NMSE vs requested target",
                reference="Direct point-source evaluation",
                simulation_vs_real="Simulation",
                frequency="150 MHz (default setup)",
                array="SKA-Low (simulated)",
            ),
            evidence=(
                "NIFTY generally exceeds its requested accuracy by about one order of magnitude; "
                "omitting the w-term yields much larger error insensitive to the target. HEALPix "
                "requires NIFTY bilinear interpolation (≈1% error) before gridding — mesh-conversion "
                "loss isolated from restored-image quality."
            ),
        ),
        entry(
            "comparative_nmse",
            "nmse_improvement_factor",
            value=10,
            unit="× (approx. order-of-magnitude overshoot of requested target by NIFTY)",
            scope="NIFTY achieved vs requested visibility NMSE",
            baseline="Requested NMSE target",
            empirical=True,
            execution_context=ctx(
                domain="Visibility",
                formula_scale="Fractional NMSE",
                reference="Direct evaluation / requested target",
                simulation_vs_real="Simulation",
                array="SKA-Low (simulated)",
            ),
            evidence=(
                "NIFTY typically beats the requested NMSE target by ≈1 order of magnitude; "
                "chunked HVOX needs tighter per-block targets to hit the global NMSE."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024arXiv241023178C": [
        entry(
            "image_domain",
            "image_nmse_db",
            value=19.9,
            unit="NMSE [−dB] (median)",
            scope="EVIL-Deconv vs CLEAN and PnP (Table 2; 64×64 HST patches / MeerKAT PSFs)",
            empirical=True,
            execution_context=ctx(
                domain="Image",
                formula_scale="NMSE [−dB] = −20·log₁₀(‖x⋆−x̂‖₂/‖x⋆‖₂) (higher dB better)",
                reference="Hubble Space Telescope ground-truth patches",
                simulation_vs_real="Simulation (MeerKAT PSFs; 40 dB training/eval SNR)",
                array="MeerKAT (simulated PSFs)",
            ),
            evidence=(
                "Appendix A.2 defines NMSE [−dB] = −20·log₁₀(‖x⋆−x̂‖₂/‖x⋆‖₂). Median Table 2: "
                "CLEAN 4.2 dB, PnP (DnCNN) 16.3 dB, EVIL-Deconv 19.9 dB (with SSIM 0.970 at 51 ms)."
            ),
        ),
        entry(
            "comparative_nmse",
            "higher_lower_than_baseline",
            value=19.9,
            unit="NMSE [−dB] vs CLEAN 4.2 / PnP 16.3",
            scope="EVIL-Deconv reconstruction fidelity vs CLEAN and PnP",
            baseline="CLEAN; PnP (DnCNN)",
            empirical=True,
            execution_context=ctx(
                domain="Image",
                formula_scale="NMSE [−dB]",
                reference="HST ground-truth patches",
                simulation_vs_real="Simulation (MeerKAT PSFs)",
                array="MeerKAT (simulated PSFs)",
            ),
            evidence=(
                "EVIL-Deconv median NMSE 19.9 dB beats PnP (16.3 dB) and CLEAN (4.2 dB) on the "
                "same simulated reconstruction benchmark used for the UQ study."
            ),
        ),
    ],
    "2026arXiv260115844M": [
        entry(
            "unspecified",
            "unspecified",
            scope="DDRM vs CLEAN / MS-CLEAN / IUWT CS on VLA/EHT/ALMA sims",
            empirical=True,
            execution_context=ctx(
                domain="Image (MSE / PSNR / SNR — not NMSE label)",
                formula_scale="MSE = (1/NM)ΣΣ(x−x̂)²; PSNR = 10·log₁₀(MAX/MSE)",
                reference="Flux-normalized VLA FIRST test images / synthetic skies",
                simulation_vs_real="Simulation (VLA, EHT, ALMA configs)",
                array="VLA / EHT / ALMA (simulated)",
            ),
            evidence=(
                "Primary fidelity metrics are MSE, PSNR, SNR, and SRE. The notes explicitly state "
                "MSE/PSNR/SNR are used — not NMSE by name. Flagged nmse_nrmse=1; left unspecified."
            ),
        ),
    ],
    "2026arXiv260309162W": [
        entry(
            "unspecified",
            "unspecified",
            scope="POLISH++ source detection / shape / flux / PSNR robustness",
            empirical=True,
            execution_context=ctx(
                domain="Image (detection F1; parameter RMSE; PSNR — not image NMSE)",
                formula_scale=None,
                reference="T-RECS ground-truth radio sky",
                simulation_vs_real="Simulation (DSA PSF / T-RECS)",
                array="DSA (simulated)",
            ),
            evidence=(
                "Reports precision/recall/F1, shape and flux RMSE on true positives, and PSNR under "
                "PSF mismatch — no explicit NMSE/NRMSE image score in the notes. Flagged "
                "nmse_nrmse=1; left unspecified."
            ),
        ),
    ],
}


def main():
    mirror_only = "--mirror-only" in sys.argv
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    nmse_papers = [p for p in papers if p["metrics"].get("nmse_nrmse") == 1]
    missing = [p["bibcode"] for p in nmse_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in nmse_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not nmse_nrmse=1: {extra}")

    if not mirror_only:
        for p in papers:
            p.pop("nmse_details", None)

    mirror = {
        "schema_note": (
            "nmse_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.nmse_nrmse binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in nmse_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        if not mirror_only:
            p["nmse_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "nmse_details": details,
        }

    if not mirror_only:
        PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in nmse_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        seen_cats = set()
        seen_subs = set()
        for d in details:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"{'Mirrored' if mirror_only else 'Injected'} nmse_details for {len(nmse_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["nmse_nrmse"] == 1 for p in nmse_papers)
    assert sum(1 for p in papers if p["metrics"].get("nmse_nrmse") == 1) == 6
    wrote = [MIRROR.relative_to(ROOT)]
    if not mirror_only:
        wrote.insert(0, PAPERS_DATA.relative_to(ROOT))
    print(f"Wrote {' and '.join(str(w) for w in wrote)}")


if __name__ == "__main__":
    main()
