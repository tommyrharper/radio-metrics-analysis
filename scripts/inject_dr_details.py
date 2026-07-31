#!/usr/bin/env python3
"""Inject dr_details into data/papers-data.json for DR-positive papers.

Run from repo root: python3 scripts/inject_dr_details.py
Does not change top-level metrics.dynamic_range flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "dr-details.json"


def ctx(
    definition_used=None,
    noise_estimator=None,
    image_region=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "definition_used": definition_used,
        "noise_estimator": noise_estimator,
        "image_region": image_region,
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


# bibcode -> list of dr_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "2008A&A...487..419B": [
        entry(
            "dr_limits",
            "dd_calibration_leakage_ceilings",
            value=1e5,
            unit="pointing-error DR limit (approx.)",
            scope="Full-beam imaging DR ceilings from DD effects / pointing",
            empirical=False,
            execution_context=ctx(
                definition_used="Imaging dynamic-range limit from direction-dependent and pointing systematics",
                simulation_vs_real="Simulated 1.4 GHz EVLA field (pointing-error limit)",
                frequency="1.4 GHz",
                array="EVLA",
            ),
            evidence=(
                "First-/second-order polarization leakage (~1e-2 / ~1e-4) motivates full-Mueller treatment "
                "above DR of a few thousand; DD effects and pixelized sky models limit full-beam DR to ~1e4–1e5; "
                "conclusion quotes ~1e5:1 pointing-error limit. No tabulated achieved reconstruction DR."
            ),
        ),
    ],
    "2008ISTSP...2..647C": [
        entry(
            "reported_achieved",
            "peak_mad_dr",
            value=50888,
            unit="DR1 (peak / MAD)",
            scope="W-projection 256 w-planes (best table entry)",
            empirical=True,
            execution_context=ctx(
                definition_used="DR1 = peak brightness / median absolute deviation from image median",
                noise_estimator="MAD from image median",
                simulation_vs_real="Simulated / controlled w-term benchmark field",
                array="VLA-class (benchmark setup)",
            ),
            evidence=(
                "Reports DR1 across methods: 2D FFT 1,570; 9×9 facets 12,580; w-projection 64 planes 18,198; "
                "256 planes 50,888."
            ),
        ),
        entry(
            "reported_achieved",
            "other_measured_dr_formula",
            value=984,
            unit="DR2 (peak / strongest nearby negative)",
            scope="W-projection 256 w-planes (best table entry)",
            empirical=True,
            execution_context=ctx(
                definition_used="DR2 = peak / |strongest nearby negative feature| around a bright source",
                image_region="Source-local (nearby negative feature)",
                simulation_vs_real="Simulated / controlled w-term benchmark field",
            ),
            evidence="DR2 rises from 2.8 (2D FFT) and 40 (facets) to 524 (64 planes) and 984 (256 planes).",
        ),
        entry(
            "comparative_dr",
            "dr_improvement_factor",
            value=3,
            unit="× error-performance advantage (approx.)",
            scope="W-projection vs uvw-space faceting at comparable DR",
            baseline="uvw-space faceting",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Same controlled benchmark as DR1/DR2 table",
            ),
            evidence=(
                "Authors report about a factor of 3 in error performance over facets in favor of w-projection, "
                "alongside order-of-magnitude residual-time advantages at comparable dynamic range."
            ),
        ),
    ],
    "2008ISTSP...2..793C": [
        entry(
            "reported_achieved",
            "peak_rms_dr",
            value=4,
            unit="peak / off-source RMS (low-SNR floor)",
            scope="M51 noise-sweep simulations",
            empirical=True,
            execution_context=ctx(
                definition_used="Reconstructed-image peak / off-source RMS",
                noise_estimator="Off-source RMS",
                image_region="Off-source",
                simulation_vs_real="Simulation (M31/M51 models; VLA C array X-band)",
                frequency="X band",
                array="VLA C array",
            ),
            evidence=(
                "Source-size and noise sweeps report dynamic range as peak / off-source RMS; at low input SNR, "
                "reconstructed DR flattens near 4 as thermal noise dominates."
            ),
        ),
    ],
    "2011A&A...532A..71R": [
        entry(
            "reported_achieved",
            "peak_peak_residual_dr",
            value=110000,
            unit="peak-to-peak-residual DR",
            scope="3C286 EVLA wideband test (4 Taylor terms)",
            empirical=True,
            execution_context=ctx(
                definition_used="Peak-to-peak-residual dynamic range",
                noise_estimator="Peak residual (also reports nearby/off-source RMS)",
                image_region="Near 3C286 / 1° away RMS reported separately",
                simulation_vs_real="Real EVLA snapshots (1.02–2.1 GHz)",
                frequency="1.02–2.1 GHz (≈1.5 GHz reference)",
                array="EVLA",
            ),
            evidence=(
                "Peak-to-peak-residual DR rose from 1,600 (ignore spectral structure) to 110,000 with four "
                "Taylor terms; noise-free Taylor-order tests also quote DR ≈100,000."
            ),
        ),
        entry(
            "dr_limits",
            "dd_calibration_leakage_ceilings",
            value=1000,
            unit="primary-beam uncorrected DR limit (approx.)",
            scope="2:1 EVLA band primary-beam spectral effect",
            empirical=False,
            execution_context=ctx(
                definition_used="DR limit if primary-beam spectral variation ignored",
                simulation_vs_real="Simulated primary-beam effect across 2:1 EVLA band",
                frequency="EVLA 2:1 band around ~2 GHz",
                array="EVLA",
            ),
            evidence=(
                "Simulated primary beam can impose a dynamic-range limit near 1,000 if ignored "
                "(apparent spectral index ≈ −1.4 at half-power)."
            ),
        ),
    ],
    "2014MNRAS.444..606O": [
        entry(
            "reported_achieved",
            "tabulated_scalar_dr",
            value=1000,
            unit="operating DR (approx. 1:1000)",
            scope="Reduced-resolution inversion accuracy simulations",
            empirical=True,
            execution_context=ctx(
                definition_used="Operating/simulation dynamic range quoted as ~1:1000",
                simulation_vs_real="Simulations (plus real-field residual check)",
            ),
            evidence=(
                "Conclusion reports no noticeable accuracy loss in simulations reaching about 1:1000 dynamic "
                "range (and in a real field with 10.3 Jy/beam peak vs 67 mJy/beam residual noise)."
            ),
        ),
    ],
    "2018A&A...611A..87T": [
        entry(
            "comparative_dr",
            "higher_lower_than_baseline",
            value=None,
            unit=None,
            scope="SSDGA / HMP vs uncorrected faceting imaging",
            baseline="No beam / wideband correction",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Real VLA/MeerKAT-style faceting demonstrations",
                array="VLA / MeerKAT (representative L-band)",
            ),
            evidence=(
                "Authors state HMP or SSD increases dynamic range and reduces flux-density/spectral-index "
                "error; residual images improve after DD/wideband correction, but achieved DR is not tabulated."
            ),
        ),
    ],
    "2025arXiv251213591C": [
        entry(
            "reported_achieved",
            "peak_rms_dr",
            value=None,
            unit=None,
            scope="astroCAMP Table 2 quality-metric definition",
            empirical=False,
            execution_context=ctx(
                definition_used="DR = I_max / σ_res (peak over residual-image RMS)",
                noise_estimator="Residual-image RMS",
                simulation_vs_real="Framework definition; Section 6 runs do not tabulate achieved DR",
            ),
            evidence=(
                "Defines DR = I_max / σ_res as a core quality metric for faint-emission detectability. "
                "Named in the algorithmic-quality set with dirty RMS and PSNR/SSIM; not tabulated as a "
                "measured Section 6 result."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2022ApJ...939L...4D": [
        entry(
            "target_configured",
            "dirty_peak_noise_estimate",
            value=5e5,
            unit="nominal target DR (1053 MHz)",
            scope="MeerKAT ESO 137-006 regularization settings",
            empirical=False,
            execution_context=ctx(
                definition_used="Nominal target DR from normalized dirty-image peak / estimated image-domain noise",
                noise_estimator="Estimated image-domain noise (~0.0014–0.0017 mJy)",
                simulation_vs_real="Real MeerKAT data (configuration estimate, not calibrated achieved DR)",
                frequency="1053 and 1399 MHz",
                array="MeerKAT",
            ),
            evidence=(
                "Dirty peaks 0.69/0.37 Jy imply nominal target DR ≈5×10⁵ and 2.2×10⁵; authors caution "
                "reconstructed peaks (~0.05 Jy) are >10× lower — regularization estimates, not measured fidelity."
            ),
        ),
    ],
    "2023MNRAS.522.5576W": [
        entry(
            "target_configured",
            "dirty_peak_noise_estimate",
            value=None,
            unit="inverse target DR / denoiser noise levels",
            scope="ASKAP AIRI denoiser selection (shelf vs universal)",
            empirical=False,
            execution_context=ctx(
                definition_used="Training noise σ interpreted as inverse target image dynamic range; dirty peak as sky-peak upper bound",
                noise_estimator="Image-domain noise from visibility noise, spectral norm, weighting",
                simulation_vs_real="Real ASKAP (no calibrated DR benchmark reported)",
                array="ASKAP",
            ),
            evidence=(
                "Denoiser noise levels (2e-5, 4e-5, 8e-5) are inverse target DR; dirty-image peak used to "
                "rescale when true sky peak is unavailable. Paper explicitly does not report a calibrated "
                "achieved DR score."
            ),
        ),
    ],
    "2024ApJS..273....3A": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="ground-truth DR range 1e3–5e5",
            scope="R2D2 VLA simulation training and generic tests",
            empirical=False,
            execution_context=ctx(
                definition_used="Ground-truth dynamic range randomized for synthetic problems; also parameterizes log S/N transform",
                simulation_vs_real="Simulation only (VLA A/C)",
                array="VLA",
            ),
            evidence=(
                "Ground-truth DR randomized from 1e3 to 5e5; targeted experiments isolate low vs high DR "
                "(e.g. 5e3 vs 1e5) where residual ratios diverge. High-DR cases show residual structure around "
                "bright emission — DR is a configured test axis, not a tabulated achieved reconstruction DR."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024A&A...690A.387R": [
        entry(
            "comparative_dr",
            "higher_lower_than_baseline",
            value=None,
            unit=None,
            scope="VLA Cygnus A multi-frequency imaging",
            baseline="classical resolve",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Real VLA Cygnus A",
                frequency="2052 / 4811 / 8427 / 13,360 MHz",
                array="VLA",
            ),
            evidence=(
                "fast-resolve achieves higher dynamic range than classical resolve with improved "
                "low-surface-brightness detail; no explicit scalar DR formula tabulated."
            ),
        ),
    ],
    "2024ApJ...966L..34D": [
        entry(
            "reported_achieved",
            "tabulated_scalar_dr",
            value=1.7e5,
            unit="target/achieved DR (approx.)",
            scope="Real Cygnus A S-band VLA reconstruction",
            empirical=True,
            execution_context=ctx(
                definition_used="Quoted target/achieved dynamic range for the Cygnus A field",
                simulation_vs_real="Real VLA Cygnus A S-band",
                array="VLA",
            ),
            evidence="Target/achieved dynamic range for the Cygnus A reconstruction quoted as ~1.7×10⁵.",
        ),
    ],
    "2024arXiv240317905C": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="DR span 10–10⁴",
            scope="Non-Cartesian MRI R2D2 simulated test set",
            empirical=False,
            execution_context=ctx(
                definition_used="DR = max / faintest recoverable intensity (reciprocal of background noise std σ)",
                noise_estimator="Background noise std σ",
                simulation_vs_real="Simulation (MRI analogue)",
            ),
            evidence=(
                "DR defined as max/faintest intensity (1/σ); test set spans DR 10–10⁴ to stress high-DR "
                "performance; logSNR uses a = image DR."
            ),
        ),
    ],
    "2025MNRAS.537.1608T": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="observation DR ~2.9×10³–1.1×10⁴",
            scope="AIRI robustness simulations vs integration time",
            empirical=False,
            execution_context=ctx(
                definition_used="Ratio between brightest and faintest image features",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Ground-truth images had DR slightly above 10⁴; simulated observations averaged "
                "2.9×10³ (1 h) to 1.1×10⁴ (8 h). logSNR transform uses a = 2.5×10³ (lowest DR)."
            ),
        ),
    ],
    "2025MNRAS.542..426T": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="DR ∈ [10³, 5×10⁵]",
            scope="S-R2D2 spherical wide-field test suite",
            empirical=False,
            execution_context=ctx(
                definition_used="Target dynamic range for simulated problems; also sets logSNR rlog parameter a",
                simulation_vs_real="Simulation (sphere vs planar)",
            ),
            evidence=(
                "Table 1 aggregates 60 test problems with DR ∈ [10³, 5×10⁵]; per-image examples span "
                "≈8.9×10⁴–2.3×10⁵. DR is the configured test axis for SNR/logSNR/RDR comparisons."
            ),
        ),
    ],
    "2025MNRAS.543.1727L": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="d ∈ [10³, 10⁵] (low/high splits)",
            scope="MROP compressive RI simulations",
            empirical=False,
            execution_context=ctx(
                definition_used="d = reciprocal of faintest ground-truth intensity",
                simulation_vs_real="Simulation (VLA/MeerKAT model coverage); real 3C 273 check without scalar DR",
                array="VLA / MeerKAT (simulated); VLA real 3C 273",
            ),
            evidence=(
                "Images span d ∈ [10³,10⁵], split into low [10³,10⁴] and high [10⁴,10⁵] for SNR/logSNR "
                "reporting. Real-data note recovers features across 4 orders of magnitude without a calibrated "
                "DR score."
            ),
        ),
    ],
    "2025RASTI...4..25M": [
        entry(
            "reported_achieved",
            "tabulated_scalar_dr",
            value=600,
            unit="image DR (approx.)",
            scope="30 Doradus reconstruction stress case",
            empirical=True,
            execution_context=ctx(
                definition_used="Quoted ~600 dynamic-range image",
                simulation_vs_real="Real/test 30 Doradus image used as high-DR stress case",
            ),
            evidence="GU-Net successfully reconstructed the ~600 dynamic-range 30 Doradus image.",
        ),
        entry(
            "comparative_dr",
            "higher_lower_than_baseline",
            value=None,
            unit=None,
            scope="GU-Net vs U-Net on high-DR 30 Doradus",
            baseline="U-Net",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Same ~600 DR 30 Doradus case",
            ),
            evidence=(
                "Qualitative DR robustness: GU-Net succeeds on the ~600 DR image despite lower-DR training; "
                "U-Net struggled."
            ),
        ),
    ],
    "2025arXiv250102473D": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="IRIS vs CLEAN/MPoL qualitative DR claim",
            empirical=False,
            execution_context=ctx(
                simulation_vs_real="Figure 7 baseline comparison (no scalar DR)",
            ),
            evidence=(
                "Reports 'competitive resolution and dynamic range performance' vs CLEAN and MPoL without a "
                "measured DR formula, configured target, or numeric improvement. Left Unspecified."
            ),
        ),
    ],
    "2026A&A...706A..77M": [
        entry(
            "comparative_dr",
            "higher_lower_than_baseline",
            value=None,
            unit=None,
            scope="Real narrowband CG-CLEAN vs CLEAN",
            baseline="Cotton–Schwab / CLEAN",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Real narrowband (M31, Cygnus A, G055.7+3.4); also synthetic Cygnus A",
                array="VLA / VLBA regimes discussed",
            ),
            evidence=(
                "On real narrowband data, CG-CLEAN 'continues to attain higher dynamic ranges in later "
                "iterations' than CLEAN."
            ),
        ),
        entry(
            "comparative_dr",
            "dr_improvement_factor",
            value=10,
            unit="× order-of-magnitude DR/convergence claim (approx.)",
            scope="Combined CG-CLEAN + Asp-CLEAN",
            baseline="Upgrading minor loop alone / standard CLEAN path",
            empirical=True,
            execution_context=ctx(
                simulation_vs_real="Real + synthetic CLEAN acceleration study",
            ),
            evidence=(
                "Combined CG + Asp-CLEAN described as reaching close to an order-of-magnitude improvement in "
                "convergence speed and dynamic range."
            ),
        ),
    ],
    "2026arXiv260309162W": [
        entry(
            "target_configured",
            "simulation_draw_parameter",
            value=None,
            unit="T-RECS test DR 10⁴–10⁶",
            scope="POLISH++ strong-lens / wide-field test data",
            empirical=False,
            execution_context=ctx(
                definition_used="Ratio of brightest to dimmest recoverable pixel",
                simulation_vs_real="Simulation (T-RECS)",
            ),
            evidence="T-RECS test data characterized with DR 10⁴–10⁶.",
        ),
        entry(
            "target_configured",
            "capability_table_max_dr",
            value=1e6,
            unit="max DR (capability table)",
            scope="Table 1 method capability comparison",
            baseline="R2D2 ~5×10⁵; CLEAN several hundred; others lower",
            empirical=False,
            execution_context=ctx(
                definition_used="Capability-table max dynamic range (not shared-benchmark measured DR)",
                simulation_vs_real="Literature capability claims",
            ),
            evidence=(
                "Table 1 lists max DR: POLISH ~10², Radionets ~5, Deflation Net ~10², R2D2 ~5×10⁵, "
                "GU-Net/RI-GAN ~6×10², POLISH++ ~10⁶ (highest reported). Not a head-to-head measured score."
            ),
        ),
        entry(
            "dr_limits",
            "algorithm_divergence_limits",
            value=None,
            unit="CLEAN practical DR 'several hundred'",
            scope="Högbom loop divergence note in capability discussion",
            empirical=False,
            execution_context=ctx(
                definition_used="Practical CLEAN DR before Högbom loop diverges",
            ),
            evidence="CLEAN's practical dynamic range noted as 'several hundred' before the Högbom loop diverges.",
        ),
    ],
    "2026arXiv260628493D": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="SKA-era AI review qualitative DR phrasing",
            empirical=False,
            execution_context=ctx(
                simulation_vs_real="Review narrative (no new DR measurement)",
            ),
            evidence=(
                "R2D2 described as delivering 'high-dynamic-range imaging at CLEAN-like speeds' without a "
                "scalar DR, configured target, comparative number, or limit. Left Unspecified."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    dr_papers = [p for p in papers if p["metrics"].get("dynamic_range") == 1]
    missing = [p["bibcode"] for p in dr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in dr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not dynamic_range=1: {extra}")

    for p in papers:
        p.pop("dr_details", None)

    mirror = {
        "schema_note": (
            "dr_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.dynamic_range binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in dr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["dr_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "dr_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in dr_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["dr_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected dr_details for {len(dr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
