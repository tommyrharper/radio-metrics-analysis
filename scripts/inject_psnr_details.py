#!/usr/bin/env python3
"""Inject psnr_details for PSNR-positive papers.

Run from repo root: python3 scripts/inject_psnr_details.py

By default writes only data/psnr-details.json (parallel-safe; does not mutate
papers-data.json). Pass --into-papers-data to also inject psnr_details onto
each paper in data/papers-data.json. Does not change top-level metrics.psnr.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "psnr-details.json"


def ctx(
    formulation=None,
    max_definition=None,
    image_domain=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "formulation": formulation,
        "max_definition": max_definition,
        "image_domain": image_domain,
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


# bibcode -> list of psnr_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "2025arXiv251213591C": [
        entry(
            "framework_defined",
            "named_core_quality_metric",
            value=None,
            unit="dB (defined)",
            scope="astroCAMP Table 2 core algorithmic-quality pair (PSNR/SSIM)",
            empirical=False,
            execution_context=ctx(
                formulation="10·log₁₀(I_max² / MSE)",
                max_definition="I_max from reference image",
                image_domain="Reconstruction Î vs reference I_ref",
                simulation_vs_real="Framework definition (WSClean+IDG matrix skips computing quality scores)",
            ),
            evidence=(
                "Table 2 names PSNR as a core quality metric via "
                "10 log₁₀(I_max²/MSE) vs reference (scikit-image / OpenCV style). "
                "PSNR appears in the co-design quality tuple with dirty-image RMS and DR, "
                "but Section 6 does not tabulate PSNR for the WSClean+IDG experimental release."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2022MNRAS.514.2614C": [
        entry(
            "absolute_psnr",
            "ten_log10_psnr",
            value=55.9,
            unit="dB (mean ± std)",
            scope="DSA-2000 full-band sim (1300 MHz, 15 min PSF; 50 validation images)",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR in dB (pixel-wise truth; integer-range normalised)",
                max_definition="Normalised to available integer range before evaluation",
                image_domain="Normalized 16-bit single-channel dirty→restored images",
                simulation_vs_real="Simulation (DSA-2000 radio-galaxy skies; 0.5 μJy/pixel noise)",
                frequency="1300 MHz (full-band PSF); also 10 MHz narrow-band",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "Full-band: POLISH mean PSNR 55.9±4.7 dB vs CLEAN 50.0±6.0 dB. "
                "Narrow-band snapshot PSF: POLISH 55.1±3.8 dB vs CLEAN 47.4±3.6 dB. "
                "Real VLA transfer is qualitative only — no PSNR on observed data."
            ),
        ),
        entry(
            "comparative_psnr",
            "psnr_gain_db",
            value=5.9,
            unit="dB mean improvement",
            scope="POLISH vs image-plane CLEAN on DSA-2000 validation",
            baseline="Image-plane CLEAN",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR in dB",
                image_domain="Normalized integer-range images",
                simulation_vs_real="Simulation (DSA-2000)",
                frequency="1300 MHz full-band (+7.7 dB on 10 MHz narrow-band)",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "Reported mean PSNR improvements: +5.9 dB (full-band) and +7.7 dB "
                "(narrow-band) over image-plane CLEAN on the same 50-image validation set."
            ),
        ),
        entry(
            "comparative_psnr",
            "higher_lower_than_baseline",
            value=55.9,
            unit="dB vs CLEAN ~47–50 dB",
            scope="DSA-2000 simulated radio-galaxy task",
            baseline="Image-plane CLEAN",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR in dB",
                simulation_vs_real="Simulation (DSA-2000)",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "POLISH mean PSNR (~55 dB) exceeds CLEAN (~47–50 dB) on both full-band "
                "and narrow-band DSA-2000 simulations."
            ),
        ),
        entry(
            "parameter_sweep_psnr",
            "vs_hyperparameter",
            value=50,
            unit="dB (floor across γ grid)",
            scope="PSF-mismatch ablation: train γ∈[0,20], test to γ=30 and 1.4× radial stretch",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR in dB",
                image_domain="Normalized images under synthetic PSF warp",
                simulation_vs_real="Simulation (PSF-warp ablation)",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "PSNR decreases outside the training warp distribution but remains above "
                "50 dB across the displayed 3×3 γ / stretch grid."
            ),
        ),
        entry(
            "parameter_sweep_psnr",
            "checkpoint_selection",
            value=None,
            unit="validation PSNR",
            scope="Model checkpoint selection during training",
            empirical=True,
            execution_context=ctx(
                formulation="Validation PSNR",
                simulation_vs_real="Simulation (training/validation pairs)",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "Network minimizes pixel-wise ℓ1 loss; model checkpoints are selected by "
                "validation PSNR."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2025arXiv250309559C": [
        entry(
            "absolute_psnr",
            "ten_log10_psnr",
            value=40.21,
            unit="dB (mean ± std)",
            scope="iR2D2(U-WDSR) non-Cartesian MRI magnitude reconstructions",
            empirical=True,
            execution_context=ctx(
                formulation="10·log₁₀(NM² / ‖|x⋆|−|x̂|‖₂²)",
                max_definition="M = max pixel value; N = image size",
                image_domain="Magnitude images |x⋆| vs |x̂|",
                simulation_vs_real="Simulation / MRI benchmark (non-Cartesian)",
            ),
            evidence=(
                "iR2D2(U-WDSR) achieves 40.21±6.67 dB; other reported means include "
                "R2D2 35.08±4.67, R2D2-Net 36.46±5.23, U-WDSR 34.38±4.19, "
                "NC-PDNet 34.11±5.01, DDS 33.73±6.80, iR2D2(U-Net) 38.01±6.57 dB."
            ),
        ),
        entry(
            "comparative_psnr",
            "psnr_gain_db",
            value=5.13,
            unit="dB",
            scope="iR2D2(U-WDSR) vs R2D2(U-WDSR) from interlaced self-calibration",
            baseline="R2D2(U-WDSR)",
            empirical=True,
            execution_context=ctx(
                formulation="10·log₁₀(NM² / ‖|x⋆|−|x̂|‖₂²)",
                max_definition="M = max pixel; N = image size",
                image_domain="Magnitude images",
                simulation_vs_real="Simulation / MRI benchmark",
            ),
            evidence=(
                "+5.13 dB mean gain over R2D2(U-WDSR); advantage largest (~6 dB) in the "
                "high dynamic-range regime. Also ~6 dB over NC-PDNet and ~6.5 dB over DDS."
            ),
        ),
        entry(
            "comparative_psnr",
            "higher_lower_than_baseline",
            value=40.21,
            unit="dB vs R2D2 / NC-PDNet / DDS",
            scope="Non-Cartesian MRI benchmark table",
            baseline="R2D2(U-WDSR), NC-PDNet, DDS, U-WDSR",
            empirical=True,
            execution_context=ctx(
                formulation="10·log₁₀ magnitude PSNR",
                image_domain="Magnitude images",
                simulation_vs_real="Simulation / MRI benchmark",
            ),
            evidence=(
                "iR2D2(U-WDSR) reports the highest mean PSNR among listed baselines "
                "(R2D2, R2D2-Net, U-WDSR, NC-PDNet, DDS)."
            ),
        ),
    ],
    "2026A&A...706A..77M": [
        entry(
            "absolute_psnr",
            "twenty_log10_linear_psnr",
            value=None,
            unit="dB (formula; no single scalar headline)",
            scope="Synthetic Cygnus A and ENZO simulation reconstructions",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR = 20·log₁₀(max(I) / ‖θ−I‖)",
                max_definition="max(I) from ground-truth image",
                image_domain="Linear image intensity vs reconstruction θ",
                simulation_vs_real="Simulation (synthetic Cygnus A; ENZO)",
                array="Interferometric simulations (CLEAN-family tests)",
            ),
            evidence=(
                "Linear PSNR defined as 20 log₁₀(max(I)/‖θ−I‖). CG-CLEAN and Momentum-CLEAN "
                "score highest on synthetic Cygnus A and ENZO; CG-CLEAN leads overall vs "
                "standard CLEAN."
            ),
        ),
        entry(
            "absolute_psnr",
            "log_domain_psnr",
            value=None,
            unit="dB (PSNR_log)",
            scope="Synthetic Cygnus A and ENZO (faint/diffuse emphasis)",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR_log = 20·log₁₀(max(log I) / ‖log θ − log I‖)",
                max_definition="max(log I)",
                image_domain="Log-scaled image intensities",
                simulation_vs_real="Simulation (synthetic Cygnus A; ENZO)",
            ),
            evidence=(
                "Log-domain PSNR emphasises diffuse/faint emission fidelity. CG-CLEAN and "
                "Momentum-CLEAN score highest on both PSNR variants; not classified under "
                "the separate logSNR column."
            ),
        ),
        entry(
            "comparative_psnr",
            "higher_lower_than_baseline",
            value=None,
            unit="highest among CLEAN / Momentum-CLEAN / CG-CLEAN",
            scope="Synthetic Cygnus A and ENZO PSNR / PSNR_log",
            baseline="Standard Cotton–Schwab CLEAN; Momentum-CLEAN",
            empirical=True,
            execution_context=ctx(
                formulation="20·log₁₀ linear and log-domain PSNR",
                simulation_vs_real="Simulation (synthetic Cygnus A; ENZO)",
            ),
            evidence=(
                "CG-CLEAN outperforms Momentum-CLEAN and standard CLEAN overall on both "
                "linear PSNR and PSNR_log."
            ),
        ),
    ],
    "2026arXiv260115844M": [
        entry(
            "absolute_psnr",
            "ten_log10_psnr",
            value=62.9,
            unit="dB",
            scope="DDRM VLA config at K=1000 sampling steps (flux-normalised)",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR = 10·log₁₀(MAX / MSE)",
                max_definition="MAX = 1 (flux-normalised images)",
                image_domain="Flux-normalised reconstructed images",
                simulation_vs_real="Simulation (VLA / EHT / ALMA sampling configs)",
                array="VLA (primary sweep); EHT; ALMA",
            ),
            evidence=(
                "VLA K-sweep: PSNR 45.0 (K=10) → 49.9 → 51.8 → 59.8 → 62.9 (K=1000). "
                "EHT K=1000: 61.7 dB; ALMA K=1000: 62.8 dB. Reported alongside MSE/SNR/SRE."
            ),
        ),
        entry(
            "parameter_sweep_psnr",
            "vs_hyperparameter",
            value=62.9,
            unit="dB at K=1000 (VLA)",
            scope="PSNR vs diffusion sampling steps K on VLA config",
            empirical=True,
            execution_context=ctx(
                formulation="10·log₁₀(MAX/MSE), MAX=1",
                max_definition="MAX = 1",
                image_domain="Flux-normalised",
                simulation_vs_real="Simulation (VLA sampling)",
                array="VLA",
            ),
            evidence=(
                "PSNR rises monotonically with sampling steps K from 45.0 dB at K=10 to "
                "62.9 dB at K=1000; K=1000 used for subsequent telescope configs."
            ),
        ),
    ],
    "2026arXiv260309162W": [
        entry(
            "parameter_sweep_psnr",
            "vs_hyperparameter",
            value=None,
            unit="dB vs PSF-warp γ ∈ [0, 30]",
            scope="POLISH++ model-mismatch / robustness experiment (Fig. 8)",
            empirical=True,
            execution_context=ctx(
                formulation="PSNR in dB (pixel-level fidelity under PSF warp)",
                image_domain="Reconstructed images under synthetic PSF warping",
                simulation_vs_real="Simulation (PSF-mismatch; train γ=0, test γ∈[0,30])",
            ),
            evidence=(
                "PSNR degrades predictably as PSF warp γ increases outside training "
                "(γ=0 only). Authors note PSNR is more sensitive to model mismatch than "
                "visual quality, which remains comparatively stable even at γ=30."
            ),
        ),
        entry(
            "parameter_sweep_psnr",
            "checkpoint_selection",
            value=11,
            unit="epochs to peak PSNR (fine-tune)",
            scope="Fine-tuning under PSF mismatch vs train-from-scratch",
            baseline="Train from scratch (57 epochs to peak PSNR)",
            empirical=True,
            execution_context=ctx(
                formulation="Peak validation / reconstruction PSNR epoch",
                simulation_vs_real="Simulation (PSF-mismatch fine-tuning)",
            ),
            evidence=(
                "Fine-tuning an existing POLISH++ model reaches peak PSNR in 11 epochs "
                "vs 57 epochs training from scratch (>5× speedup); both beat the "
                "unadapted mismatched baseline. No head-to-head PSNR vs R2D2 on shared data."
            ),
        ),
    ],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--into-papers-data",
        action="store_true",
        help="Also write psnr_details onto papers in data/papers-data.json",
    )
    args = parser.parse_args()

    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    psnr_papers = [p for p in papers if p["metrics"].get("psnr") == 1]
    missing = [p["bibcode"] for p in psnr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in psnr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not psnr=1: {extra}")

    mirror = {
        "schema_note": (
            "psnr_details live primarily on each paper in papers-data.json when injected. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.psnr binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in psnr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "psnr_details": details,
        }

    if args.into_papers_data:
        for p in papers:
            p.pop("psnr_details", None)
        for p in psnr_papers:
            p["psnr_details"] = CLASSIFICATIONS[p["bibcode"]]
        PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in psnr_papers:
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

    print(f"Classified psnr_details for {len(psnr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["psnr"] == 1 for p in psnr_papers)
    assert len(psnr_papers) == 6
    wrote = [str(MIRROR.relative_to(ROOT))]
    if args.into_papers_data:
        wrote.insert(0, str(PAPERS_DATA.relative_to(ROOT)))
    print(f"Wrote {' and '.join(wrote)}")


if __name__ == "__main__":
    main()
