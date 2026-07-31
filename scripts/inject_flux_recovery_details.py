#!/usr/bin/env python3
"""Inject flux_recovery_details into data/papers-data.json for Flux-positive papers.

Run from repo root: python3 scripts/inject_flux_recovery_details.py
Does not change top-level metrics.flux_recovery flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "flux-recovery-details.json"


def ctx(
    units=None,
    aperture_region=None,
    reference_type=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "units": units,
        "aperture_region": aperture_region,
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


# bibcode -> list of flux_recovery_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "1988A&A...200..312W": [
        entry(
            "truth_based_flux",
            "integrated_vs_true",
            value=962,
            unit="arbitrary flux units (of 1002 true)",
            scope="5′ circular Gaussian, peak-to-noise 20 (Table 1)",
            empirical=True,
            execution_context=ctx(
                units="Arbitrary model flux units",
                aperture_region="Source-dependent ring radii (Table 1)",
                reference_type="Known Gaussian model flux",
                simulation_vs_real="Simulation (WSRT dirty beam)",
                frequency=None,
                array="WSRT (simulated full-synthesis beam)",
            ),
            evidence=(
                "At peak-to-noise 20, the 5′ circular model has true flux 1002; MRC recovers 962 "
                "with a flat cumulative profile, while CLEAN recovers 563 with a strongly changing profile."
            ),
        ),
        entry(
            "truth_based_flux",
            "recovery_fraction",
            value=93.6,
            unit="%",
            scope="Realistic clean-map model reused as truth (≈30′ / 90 beams)",
            empirical=True,
            execution_context=ctx(
                units="% of true integrated flux",
                aperture_region="Full model extent in dirty-map experiment",
                reference_type="Known model flux (10,000 arb. units)",
                simulation_vs_real="Simulation (real-source map as model)",
                array="WSRT (simulated)",
            ),
            evidence=(
                "From a true flux of 10,000 arbitrary units, MRC recovers 9358 (93.6%); "
                "CLEAN recovers 6910 (69.1%) and leaves the negative bowl present."
            ),
        ),
        entry(
            "cross_method_flux",
            "comparative_recovered_flux",
            value=None,
            unit=None,
            scope="MRC vs conventional CLEAN recovered integrated flux (Table 1)",
            baseline="Högbom / conventional CLEAN",
            empirical=True,
            execution_context=ctx(
                units="Arbitrary model flux units",
                aperture_region="Source-dependent radii",
                reference_type="Known model + cross-method comparison",
                simulation_vs_real="Simulation",
                array="WSRT (simulated)",
            ),
            evidence=(
                "Across Table 1 models MRC recovers substantially more integrated flux than CLEAN "
                "(e.g. 962 vs 563 of 1002 at 5′; 2788 vs 653 of 4010 at 10′). At low SNR MRC can over-recover."
            ),
        ),
    ],
    "2008ISTSP...2..793C": [
        entry(
            "truth_based_flux",
            "integrated_vs_true",
            value=1495,
            unit="Jy",
            scope="M31 VLA C-config simulation (Table II total recovered flux)",
            empirical=True,
            execution_context=ctx(
                units="Jy",
                aperture_region="Full simulated M31 model",
                reference_type="Known model reference flux 1,495 Jy",
                simulation_vs_real="Simulation (VLA C-configuration)",
                frequency="X-band context in related sweeps; M31 table is continuum sim",
                array="VLA C-configuration",
            ),
            evidence=(
                "Table II: Multiscale CLEAN recovers 1,495 Jy (exact match to the table reference), "
                "vs Högbom 1,474 Jy, Clark 1,326 Jy, MRC 1,546 Jy, MEM 1,486 Jy."
            ),
        ),
        entry(
            "truth_based_flux",
            "recovery_fraction",
            value=None,
            unit="recovered-flux fraction (parameter sweeps)",
            scope="Source-size and visibility-noise sweeps (M31/M51 models)",
            empirical=True,
            execution_context=ctx(
                units="Fraction of true flux",
                aperture_region="Simulated source extent / masks",
                reference_type="Known model flux",
                simulation_vs_real="Simulation (VLA C-array)",
                frequency="X band (size/noise sweeps)",
                array="VLA C-array",
            ),
            evidence=(
                "Source-size and noise sweeps report recovered-flux fraction vs maximum scale and SNR; "
                "Multiscale CLEAN retains accurate flux estimates down to SNR ~4, while MEM overestimates "
                "from SNR as high as 100."
            ),
        ),
        entry(
            "cross_method_flux",
            "comparative_recovered_flux",
            value=3.08,
            unit="Jy (vs 0.32 Jy Högbom)",
            scope="Real VLA D-config H I channel of NGC 1058",
            baseline="Högbom CLEAN",
            empirical=True,
            execution_context=ctx(
                units="Jy",
                aperture_region="Source region (multiscale flux stable when enlarged)",
                reference_type="Cross-method (no known sky truth)",
                simulation_vs_real="Real VLA observation",
                array="VLA D-configuration",
            ),
            evidence=(
                "On real NGC 1058 H I data, Multiscale CLEAN recovered 3.08 Jy integrated flux vs "
                "0.32 Jy for Högbom CLEAN; Högbom flux was strongly region-dependent due to the negative bowl."
            ),
        ),
    ],
    "2011A&A...532A..71R": [
        entry(
            "truth_based_flux",
            "peak_flux_bias",
            value=0.001,
            unit="fractional peak-flux error (~1 part in 10³)",
            scope="Noise-free EVLA Taylor-order test, 2:1 band, four Taylor terms (Figure 4)",
            empirical=True,
            execution_context=ctx(
                units="Fractional error on reference-frequency peak",
                aperture_region="1 Jy point-source peak",
                reference_type="Known 1 Jy point-source model",
                simulation_vs_real="Simulation (noise-free EVLA)",
                frequency="~2 GHz centre; bandwidth ratios 1.1:1–3:1",
                array="EVLA",
            ),
            evidence=(
                "Noise-free Taylor-order test: for a 2:1 band and four Taylor terms, reference-frequency "
                "peak-flux error is about 1 part in 1,000 (with DR ~100,000 and spectral-index error ~0.01)."
            ),
        ),
    ],
    "2014MNRAS.444..606O": [
        entry(
            "truth_based_flux",
            "catalogue_flux_error",
            value=1.31,
            unit="% AEGEAN source-flux standard error",
            scope="100×1 Jy MWA simulation, zenith, 12 w-layers (vs CASA 1.34%)",
            empirical=True,
            execution_context=ctx(
                units="% source-flux standard error (AEGEAN)",
                aperture_region="AEGEAN catalogue on 100 simulated 1 Jy sources",
                reference_type="Known injected 1 Jy sources",
                simulation_vs_real="Simulation (MWA, no system noise)",
                frequency="MWA band",
                array="MWA",
            ),
            evidence=(
                "At zenith with 12 w-layers, WSClean reports 1.31% AEGEAN source-flux standard error "
                "(and 0.94 mJy/beam residual RMS) versus CASA 1.34% and 1.90 mJy/beam."
            ),
        ),
        entry(
            "cross_method_flux",
            "comparative_recovered_flux",
            value=None,
            unit="2–33% lower source-flux errors than CASA",
            scope="MWA simulation grid (zenith and 10° zenith angle)",
            baseline="CASA w-projection",
            empirical=True,
            execution_context=ctx(
                units="% source-flux standard error",
                aperture_region="AEGEAN catalogue",
                reference_type="Known injected sources + cross-method",
                simulation_vs_real="Simulation (MWA)",
                frequency="MWA band",
                array="MWA",
            ),
            evidence=(
                "Across controlled tests the paper summarizes WSClean as having 2–33% lower source-flux "
                "errors (and 0–49% lower residual RMS) than CASA."
            ),
        ),
    ],
    "2018A&A...611A..87T": [
        entry(
            "truth_based_flux",
            "relative_flux_density_error",
            value=None,
            unit="(Ŝ₅₀−S₅₀)/S₅₀",
            scope="LOFAR LBA semi-realistic simulation vs beam radius (Figure 9)",
            empirical=True,
            execution_context=ctx(
                units="Relative flux-density error at 50 MHz",
                aperture_region="Point sources vs distance from beam centre / HPBW",
                reference_type="Known simulated S₅₀",
                simulation_vs_real="Simulation (LOFAR LBA, DD Jones)",
                frequency="30–70 MHz (S₅₀ at 50 MHz)",
                array="LOFAR LBA (36 stations)",
            ),
            evidence=(
                "Simulation measures (estimated S₅₀ − true S₅₀)/true S₅₀ versus beam-radius distance. "
                "Direction-independent narrowband imaging shows strong negative radial bias; DD HMP-WB "
                "and SSD-WB cluster much closer to zero (SSD visually tighter)."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2022A&A...664A.134S": [
        entry(
            "truth_based_flux",
            "peak_flux_bias",
            value=-4.354,
            unit="% mean relative core specific-intensity deviation",
            scope="10,000 synthetic radio-galaxy tests, noiseless radionets model",
            empirical=True,
            execution_context=ctx(
                units="% relative deviation (arbitrary intensity units)",
                aperture_region="Brightest Gaussian core pixels averaged",
                reference_type="Synthetic Gaussian truth",
                simulation_vs_real="Simulation (gridded VLBA-like masks)",
                array="Simulated ten-antenna VLBA-like coverage",
            ),
            evidence=(
                "Core specific-intensity mean relative deviations: noiseless network −4.354% ± 6.662%; "
                "image-noise-trained 0.613% ± 12.402%; WSClean −13.645% ± 24.312%."
            ),
        ),
        entry(
            "cross_method_flux",
            "comparative_recovered_flux",
            value=None,
            unit=None,
            scope="Radionets vs fixed WSClean config on synthetic cores",
            baseline="WSClean (one fixed configuration)",
            empirical=True,
            execution_context=ctx(
                units="% relative core intensity deviation",
                aperture_region="Core Gaussian component",
                reference_type="Synthetic truth + cross-method",
                simulation_vs_real="Simulation",
                array="Simulated VLBA-like",
            ),
            evidence=(
                "Network core-intensity bias/scatter is smaller than the reported WSClean mean deviation "
                "(−13.6% ± 24.3%), though large dispersions show near-zero mean bias ≠ accurate per-source flux."
            ),
        ),
    ],
    "2022ApJ...939L...4D": [
        entry(
            "cross_method_flux",
            "cross_method_integrated",
            value=143,
            unit="mJy (uSARA/AIRI at 1053 MHz; CLEAN 146 mJy)",
            scope="ESO 137-006 AGN photometry, MeerKAT continuum bands",
            empirical=True,
            execution_context=ctx(
                units="mJy",
                aperture_region="AGN region (CLEAN within dirty-beam main lobe; ML over active pixels)",
                reference_type="Cross-method (no known sky truth)",
                simulation_vs_real="Real MeerKAT observation",
                frequency="1053 and 1399 MHz",
                array="MeerKAT",
            ),
            evidence=(
                "At 1053 MHz, uSARA, AIRI, and CLEAN recover 143, 143, and 146 mJy; at 1399 MHz "
                "124, 125, and 123 mJy. Agreement is a real-data consistency check, not truth error."
            ),
        ),
    ],
    "2023MNRAS.522.5558W": [
        entry(
            "cross_method_flux",
            "cross_method_integrated",
            value=117.2,
            unit="mJy (uSARA full-band; WSClean 115.5 mJy)",
            scope="ASKAP fields: Abell 3395, PKS 2014-55, SPT2023, PKS 2130-538",
            empirical=True,
            execution_context=ctx(
                units="mJy",
                aperture_region="Manually drawn regions (~2σ WSClean contour; shared per source/sub-band)",
                reference_type="Cross-method (no catalogue validation)",
                simulation_vs_real="Real ASKAP Early Science / Pilot",
                frequency="~817–1139 MHz sub-bands; 943 MHz full-band",
                array="ASKAP",
            ),
            evidence=(
                "Tabulated integrated diffuse fluxes across sub-bands for multiple sources (e.g. Abell 3395 "
                "phoenix Table 3; PKS 2014-55 Table 4; SPT2023 relic Table 5). Closest agreement on "
                "PKS 2130-538: 117.2 mJy uSARA vs 115.5 mJy WSClean restored/smoothed at 943 MHz."
            ),
        ),
    ],
    "2023MNRAS.522.5576W": [
        entry(
            "cross_method_flux",
            "cross_method_integrated",
            value=116.7,
            unit="mJy (AIRI full-band Dancing Ghosts)",
            scope="ASKAP AIRI vs uSARA / WSClean integrated fluxes (Tables 1–4)",
            empirical=True,
            execution_context=ctx(
                units="mJy",
                aperture_region="Hand-drawn regions adjusted to AIRI morphology",
                reference_type="Cross-method (no known sky truth)",
                simulation_vs_real="Real ASKAP Early Science / Pilot",
                frequency="~817–1139 MHz; 943 MHz full-band",
                array="ASKAP",
            ),
            evidence=(
                "AIRI integrated fluxes tabulated per field/sub-band (e.g. Abell phoenix Table 1; "
                "PKS 2014-55 Table 2; SPT2023 relic Table 3). PKS 2130-538 full-band AIRI 116.7 mJy "
                "agrees closely with companion uSARA/WSClean; apertures differ from the uSARA paper."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2026arXiv260309162W": [
        entry(
            "truth_based_flux",
            "catalogue_flux_error",
            value=3.2625e-4,
            unit="Jy/pixel flux RMSE (CLEAN; best)",
            scope="SEP flux RMSE on true-positive detections (Table 3)",
            empirical=True,
            execution_context=ctx(
                units="Jy/pixel RMSE",
                aperture_region="SEP-extracted true-positive sources",
                reference_type="Simulated ground-truth flux",
                simulation_vs_real="Simulation (strong-lens discovery setup)",
                array=None,
            ),
            evidence=(
                "Table 3 flux RMSE: CLEAN 3.2625×10⁻⁴ Jy/px (best), POLISH 1.9504×10⁻³, "
                "POLISH+ 3.8411×10⁻³, POLISH++ 3.1703×10⁻³ — CLEAN superior for flux fidelity."
            ),
        ),
        entry(
            "cross_method_flux",
            "comparative_recovered_flux",
            value=None,
            unit=None,
            scope="CLEAN vs POLISH / POLISH+ / POLISH++ flux RMSE",
            baseline="CLEAN",
            empirical=True,
            execution_context=ctx(
                units="Jy/pixel RMSE",
                aperture_region="SEP true positives",
                reference_type="Ground truth + cross-method",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Learned POLISH variants have higher flux RMSE than CLEAN; attributed to nonlinear "
                "learned reconstruction lacking explicit flux calibration."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    flux_papers = [p for p in papers if p["metrics"].get("flux_recovery") == 1]
    missing = [p["bibcode"] for p in flux_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in flux_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not flux_recovery=1: {extra}")

    for p in papers:
        p.pop("flux_recovery_details", None)

    mirror = {
        "schema_note": (
            "flux_recovery_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.flux_recovery binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in flux_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["flux_recovery_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "flux_recovery_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in flux_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["flux_recovery_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected flux_recovery_details for {len(flux_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["flux_recovery"] == 1 for p in flux_papers)
    assert sum(1 for p in papers if p["metrics"].get("flux_recovery") == 1) == 10
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
