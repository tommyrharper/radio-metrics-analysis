#!/usr/bin/env python3
"""Inject rms_details into papers-data.json for RMS-positive papers.

Run from repo root: python3 scripts/inject_rms_details.py
Does not change top-level metrics.rms flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "papers-data.json"
MIRROR = ROOT / "data" / "rms-details.json"


def ctx(
    units=None,
    image_region=None,
    residual_vs_dirty=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "units": units,
        "image_region": image_region,
        "residual_vs_dirty": residual_vs_dirty,
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


# bibcode -> list of rms_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "1994A&AS..108..585S": [
        entry(
            "absolute_rms",
            "off_source_blank_rms",
            value=90,
            unit="μJy/beam (approx.)",
            scope="Blank regions of final multi-frequency CLEAN image (PKSB1733-565)",
            empirical=True,
            execution_context=ctx(
                units="μJy/beam",
                image_region="Blank / off-source regions",
                residual_vs_dirty="Residual (final CLEAN image)",
                simulation_vs_real="Real ATCA observation",
                frequency="4.418–6.099 GHz",
                array="ATCA (6-antenna east-west)",
            ),
            evidence=(
                "Blank regions have rms about 1.5× the stated 60 μJy/beam thermal-noise limit "
                "(≈90 μJy/beam). Remaining local errors near the core/hot spot are discussed; "
                "no single measured DR ratio for the final image."
            ),
        ),
    ],
    "2008A&A...487..419B": [
        entry(
            "absolute_rms",
            "off_source_blank_rms",
            value=1,
            unit="μJy/beam",
            scope="Simulated Stokes V with squint+pointing correction (Figure 4)",
            empirical=True,
            execution_context=ctx(
                units="μJy/beam",
                image_region="Off-source",
                residual_vs_dirty="Residual / corrected Stokes V image",
                simulation_vs_real="Simulation (VLA C-array 1.4 GHz)",
                frequency="1.4 GHz",
                array="VLA C-array",
            ),
            evidence=(
                "Figure 4 reports off-source RMS of 10 μJy/beam without squint and pointing "
                "correction and 1 μJy/beam with both corrections."
            ),
        ),
        entry(
            "absolute_rms",
            "residual_image_rms",
            value=0.15,
            unit="mJy/beam",
            scope="Real IC2233 Stokes V residual after A-projection correction",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                image_region="Full residual (Stokes V; extrema no longer source-correlated)",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real VLA observation (~11.6 h)",
                frequency="1.4 GHz",
                array="VLA",
            ),
            evidence=(
                "After time-varying primary-beam and polarization-squint correction, Stokes V "
                "residual extrema were about ±0.5 mJy/beam and the RMS was 0.15 mJy/beam, "
                "slightly above expected thermal noise (~0.13 mJy/beam)."
            ),
        ),
        entry(
            "comparative_rms",
            "rms_reduction_factor",
            value=10,
            unit="× (approx. order-of-magnitude)",
            scope="Simulated polarization-squint / pointing correction vs uncorrected",
            baseline="Uncorrected Stokes V / off-source RMS",
            empirical=True,
            execution_context=ctx(
                units="μJy/beam",
                image_region="Off-source",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation (and order-of-magnitude claim on real data)",
                frequency="1.4 GHz",
                array="VLA C-array",
            ),
            evidence=(
                "Simulated Stokes V RMS falls from ~2 mJy peak / 10 μJy/beam RMS to noise-like "
                "~1 μJy/beam (factor ≈10). Paper also characterizes systematic-error reduction "
                "as one order of magnitude on real data."
            ),
        ),
    ],
    "2008ISTSP...2..793C": [
        entry(
            "absolute_rms",
            "other_absolute_rms",
            value=4.9,
            unit="mJy/beam (RMS error vs smoothed truth)",
            scope="M31 VLA C-array simulation Table II (Multiscale CLEAN)",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                image_region="Full error image vs clean-beam-smoothed truth",
                residual_vs_dirty="Image-domain reconstruction error (not residual-dirty RDR)",
                simulation_vs_real="Simulation (M31 test image)",
                array="VLA C configuration",
            ),
            evidence=(
                "Table II image-domain RMS error: Högbom 8.8, Clark 25.6, Multi-Resolution 14.7, "
                "Multiscale CLEAN 4.9, maximum entropy 2.5 mJy/beam. Multiscale lowest among "
                "CLEAN-family methods. Peak/off-source RMS used only to define DR in other "
                "sweeps is not counted as a standalone RMS subtype here."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=4.9,
            unit="mJy/beam vs CLEAN-family baselines",
            scope="M31 Table II RMS error comparison",
            baseline="Högbom / Clark / Multi-Resolution CLEAN",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                simulation_vs_real="Simulation (M31)",
                array="VLA C configuration",
            ),
            evidence=(
                "Multiscale CLEAN's 4.9 mJy/beam RMS error is lower than Högbom (8.8), "
                "Multi-Resolution (14.7), and Clark (25.6); maximum entropy is lower still (2.5)."
            ),
        ),
    ],
    "2011A&A...532A..71R": [
        entry(
            "absolute_rms",
            "off_source_blank_rms",
            value=1.8,
            unit="mJy",
            scope="M87 L-band restored image (3 arcsec; C+B config)",
            empirical=True,
            execution_context=ctx(
                units="mJy (image RMS)",
                image_region="Off-source (also reports 3–10 mJy on-source RMS)",
                residual_vs_dirty="Restored / residual image noise",
                simulation_vs_real="Real VLA snapshots",
                frequency="L band",
                array="VLA",
            ),
            evidence=(
                "Central restored image peaked at 15 Jy, with 1.8 mJy off-source RMS and "
                "3–10 mJy on-source RMS."
            ),
        ),
        entry(
            "absolute_rms",
            "residual_image_rms",
            value=140,
            unit="μJy (near-source residual RMS, 4 Taylor terms)",
            scope="3C286 EVLA wideband test — RMS near source and 1° away",
            empirical=True,
            execution_context=ctx(
                units="mJy / μJy",
                image_region="Near 3C286 and 1° away (off-source)",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real EVLA snapshots",
                frequency="1.02–2.1 GHz (~1.5 GHz reference)",
                array="EVLA",
            ),
            evidence=(
                "Raising Taylor terms from one to four reduced RMS near 3C286 through 9 mJy, "
                "1 mJy, 200 μJy, and 140 μJy; RMS 1° away was 1 mJy, 200 μJy, 85 μJy, and "
                "80 μJy vs ~70 μJy thermal estimate."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="3C286 RMS vs fewer Taylor terms",
            baseline="1–3 Taylor-term reconstructions",
            empirical=True,
            execution_context=ctx(
                image_region="Near-source and off-source",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real EVLA",
                frequency="1.02–2.1 GHz",
                array="EVLA",
            ),
            evidence=(
                "Near-source and off-source residual RMS fall by orders of magnitude as Taylor "
                "terms increase from 1 to 4 (numerical comparison across configurations)."
            ),
        ),
    ],
    "2014MNRAS.444..606O": [
        entry(
            "absolute_rms",
            "residual_image_rms",
            value=0.94,
            unit="mJy/beam",
            scope="MWA 100-source simulation, zenith, 12 w-layers (WSClean)",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                image_region="Residual image (RMS flux density)",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation (no system noise; MWA field)",
                array="MWA (simulated)",
            ),
            evidence=(
                "At zenith with 12 w-layers/planes, WSClean reports 0.94 mJy/beam residual RMS "
                "vs CASA 1.90 mJy/beam; other zenith/plane settings tabulated similarly "
                "(e.g. 0.90–1.07 mJy/beam at 10° zenith angle)."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="WSClean vs CASA residual RMS on controlled MWA sims",
            baseline="CASA",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation",
                array="MWA (simulated)",
            ),
            evidence=(
                "Across tests, WSClean summarized as having 0–49% lower residual RMS than CASA "
                "(e.g. 0.94 vs 1.90 mJy/beam at 12 planes). Authors caution equal plane counts "
                "can disadvantage CASA at zenith."
            ),
        ),
        entry(
            "comparative_rms",
            "percentage_rms_change",
            value=49,
            unit="% lower residual RMS (upper end of stated range)",
            scope="WSClean vs CASA summary across controlled tests",
            baseline="CASA",
            empirical=True,
            execution_context=ctx(
                units="mJy/beam",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation",
                array="MWA (simulated)",
            ),
            evidence="Paper summarizes WSClean as 0–49% lower residual RMS than CASA across the controlled accuracy benchmarks.",
        ),
    ],
    "2017MNRAS.471..301O": [
        entry(
            "absolute_rms",
            "residual_image_rms",
            value=50,
            unit="mJy/PSF",
            scope="Real MWA Vela/Puppis A field (WSClean scale-bias 0.60)",
            empirical=True,
            execution_context=ctx(
                units="mJy/PSF",
                image_region="Residual image",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real MWA observation (2 min)",
                frequency="MWA band (Vela/Puppis A)",
                array="MWA",
            ),
            evidence=(
                "Default CASA multi-scale CLEAN 64 mJy/PSF residual RMS; WSClean bias 0.60 "
                "gives 50 mJy/PSF. Masked cleaning reduces residual RMS from 50 to 38 mJy/PSF "
                "(near 36 mJy/PSF Stokes V system-noise estimate). LOFAR imperfect-data run "
                "reaches 1.4 mJy/PSF RMS (WSClean MF multi-scale)."
            ),
        ),
        entry(
            "absolute_rms",
            "off_source_blank_rms",
            value=63,
            unit="μJy/PSF",
            scope="Wideband MWA simulation — multi-frequency multi-scale CLEAN",
            empirical=True,
            execution_context=ctx(
                units="μJy/PSF",
                image_region="Off-source",
                residual_vs_dirty="Residual (vs dirty RMS for reduction factor)",
                simulation_vs_real="Simulation (2 min zenith MWA, 149 MHz)",
                frequency="30 MHz centred at 149 MHz",
                array="MWA (simulated)",
            ),
            evidence=(
                "Figure 10 off-source residual RMS: 880, 310, 2000, 460, and 63 μJy/PSF for "
                "single-scale, multi-scale, MORESANE, MF single-scale, and MF multi-scale CLEAN. "
                "Masked MF multi-scale reaches 55 μJy/PSF."
            ),
        ),
        entry(
            "absolute_rms",
            "dirty_image_rms",
            value=280,
            unit="mJy/PSF",
            scope="Wideband MWA simulation dirty-image RMS (reference for reduction factor)",
            empirical=True,
            execution_context=ctx(
                units="mJy/PSF",
                image_region="Dirty image",
                residual_vs_dirty="Dirty",
                simulation_vs_real="Simulation",
                frequency="~149 MHz",
                array="MWA (simulated)",
            ),
            evidence=(
                "Dirty-image RMS quoted as 280 mJy/PSF; MF multi-scale residual 63–64 μJy/PSF "
                "is described as a factor of ~4400 below that dirty RMS (masked: factor ~5100)."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=50,
            unit="mJy/PSF vs CASA 64 mJy/PSF",
            scope="Real MWA Vela/Puppis A residual RMS",
            baseline="CASA multi-scale CLEAN",
            empirical=True,
            execution_context=ctx(
                units="mJy/PSF",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real MWA",
                array="MWA",
            ),
            evidence=(
                "WSClean 50 mJy/PSF vs CASA 64 mJy/PSF (and IUWT/MORESANE 63/75). Authors "
                "caution scale-bias/gridder differences; text/figure discrepancy on one WSClean "
                "setting (47 vs 62 mJy/PSF) unresolved."
            ),
        ),
        entry(
            "comparative_rms",
            "rms_reduction_factor",
            value=4400,
            unit="× below dirty-image RMS",
            scope="Wideband sim MF multi-scale residual vs dirty RMS",
            baseline="Dirty-image RMS (280 mJy/PSF)",
            empirical=True,
            execution_context=ctx(
                units="μJy/PSF vs mJy/PSF",
                image_region="Off-source residual vs dirty",
                residual_vs_dirty="Residual vs dirty (scalar factor; not ‖r̂‖₂/‖x_dirty‖₂ RDR)",
                simulation_vs_real="Simulation",
                frequency="~149 MHz",
                array="MWA (simulated)",
            ),
            evidence=(
                "MF multi-scale residual ~63–64 μJy/PSF called a factor of 4400 below 280 mJy/PSF "
                "dirty RMS; with automatic masking 55 μJy/PSF → factor ~5100. Treated as absolute "
                "RMS reduction vs dirty, not R2D2-style normalised RDR."
            ),
        ),
    ],
    "2018A&A...616A..27V": [
        entry(
            "absolute_rms",
            "residual_image_rms",
            value=7.6e-6,
            unit="Jy/beam",
            scope="Source-box residual image (IDG vs classical gridding)",
            empirical=True,
            execution_context=ctx(
                units="Jy/beam",
                image_region="Source box and full residual image",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Source-box residual RMS: IDG 7.6e-6 vs classical 1.3e-4 Jy/beam (~19× lower). "
                "Full residual image: 1.1e-6 vs 2.1e-5 Jy/beam (~17× lower). Visibility-domain "
                "RMS and PSF-sidelobe RMS are not counted as residual-image RMS subtypes."
            ),
        ),
        entry(
            "absolute_rms",
            "dirty_image_rms",
            value=None,
            unit="Jy/beam (caption values inconsistent)",
            scope="Out-of-field-source dirty-image RMS comparison",
            empirical=True,
            execution_context=ctx(
                units="Jy/beam",
                image_region="Dirty image (source outside imaged area)",
                residual_vs_dirty="Dirty",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Dirty-image RMS for a simulated out-of-field source reported 2% lower with IDG. "
                "Figure 8 caption absolute values are internally inconsistent with the 2% claim; "
                "percentage retained, absolute caption values not trusted without erratum."
            ),
        ),
        entry(
            "comparative_rms",
            "rms_reduction_factor",
            value=18,
            unit="× residual-noise reduction (approx.)",
            scope="IDG vs classical gridding residual RMS",
            baseline="Classical gridding",
            empirical=True,
            execution_context=ctx(
                units="Jy/beam",
                image_region="Source box / full residual",
                residual_vs_dirty="Residual",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "Text summarizes residual-noise reduction as roughly a factor of 18 "
                "(~17× full image, ~19× source box)."
            ),
        ),
        entry(
            "comparative_rms",
            "percentage_rms_change",
            value=2,
            unit="% lower dirty-image RMS",
            scope="Out-of-field-source suppression",
            baseline="Classical gridding",
            empirical=True,
            execution_context=ctx(
                residual_vs_dirty="Dirty",
                simulation_vs_real="Simulation",
            ),
            evidence="Out-of-field dirty-image RMS reported 2% lower with IDG than classical gridding.",
        ),
    ],
    "2025arXiv251213591C": [
        entry(
            "framework_defined",
            "named_core_quality_metric",
            value=None,
            unit="Jy/beam (σ_dirty definition)",
            scope="astroCAMP Table 2 core fidelity metric (not tabulated in §6 runs)",
            empirical=False,
            execution_context=ctx(
                units="Jy/beam",
                image_region="Dirty image (imstat / PyBDSF)",
                residual_vs_dirty="Dirty (σ_dirty); residual RMS appears only inside DR = I_max/σ_res",
                simulation_vs_real="Framework definition (WSClean+IDG matrix does not tabulate RMS values)",
            ),
            evidence=(
                "Defines dirty-image RMS σ_dirty = sqrt((1/N) Σ (I_i − Ī)²) as a core quality "
                "metric and uses it in the example quality tuple. Section 6 does not tabulate "
                "those RMS values. Residual RMS as DR denominator alone is not a separate "
                "measured RMS subtype here."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2023MNRAS.522.5558W": [
        entry(
            "absolute_rms",
            "residual_map_sigma",
            value=1.6,
            unit="μJy/pixel (example WSClean measured residual rms)",
            scope="ASKAP real-data fields (Abell 3395 / PKS 2014-55 / Dancing Ghosts)",
            empirical=True,
            execution_context=ctx(
                units="μJy/pixel",
                image_region="Residual map (contours at multiples of residual rms)",
                residual_vs_dirty="Residual-map rms",
                simulation_vs_real="Real ASKAP Early Science / Pilot data",
                frequency="~817–1139 MHz sub-bands",
                array="ASKAP",
            ),
            evidence=(
                "Reports measured residual-map rms as fidelity/sensitivity context: e.g. WSClean "
                "~1–2 μJy/pixel, 1.6 μJy/pixel (PKS 2014-55), and 1 μJy/pixel (Dancing Ghosts). "
                "Source boundaries drawn at multiples of residual rms vs calculated image-noise "
                "std. Not a normalised RDR score."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024ApJ...966L..34D": [
        entry(
            "absolute_rms",
            "residual_map_sigma",
            value=11.7e-4,
            unit="residual dirty-image std. dev. (linear; R2D2)",
            scope="Cygnus A deep imaging method comparison",
            empirical=True,
            execution_context=ctx(
                units="linear residual std. dev. (table ×10⁻⁴)",
                image_region="Residual dirty image",
                residual_vs_dirty="Residual (std of residual dirty image)",
                simulation_vs_real="Real Cygnus A imaging comparison",
                array="VLA (Cygnus A reduction context)",
            ),
            evidence=(
                "Primary quantitative fidelity metric: std. dev. of the residual dirty image — "
                "Hö-CLEAN 359×10⁻⁴; CS-CLEAN 8.6×10⁻⁴; MS-CLEAN 10.4×10⁻⁴; R2D2 11.7×10⁻⁴; "
                "R2D2-Net 13.4×10⁻⁴; R3D3 9.7×10⁻⁴; uSARA 7.2×10⁻⁴; AIRI 7.4×10⁻⁴."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="Residual std across CLEAN / R2D2 / uSARA / AIRI",
            baseline="CLEAN-family and other reconstructors in same table",
            empirical=True,
            execution_context=ctx(
                residual_vs_dirty="Residual dirty-image std",
                simulation_vs_real="Real Cygnus A",
            ),
            evidence=(
                "AIRI, uSARA, and CS-CLEAN achieve the lowest residual std; R2D2 variants are "
                "described as comparable, slightly above those top performers (numerical table)."
            ),
        ),
    ],
    "2025MNRAS.543.1727L": [
        entry(
            "absolute_rms",
            "residual_map_sigma",
            value=6.87e-4,
            unit="residual-map standard deviation (MROP)",
            scope="Real VLA 3C 273 X-band (D/N ≈ 0.98)",
            empirical=True,
            execution_context=ctx(
                units="residual-map std (linear)",
                image_region="Residual map",
                residual_vs_dirty="Residual",
                simulation_vs_real="Real VLA data (also used as sim diagnostic)",
                frequency="X band",
                array="VLA",
            ),
            evidence=(
                "Residual dirty image and its standard deviation used as data-fidelity diagnostic. "
                "Real-data residual-map std: classical 6.49×10⁻⁴; MROP 6.87×10⁻⁴ "
                "(highly comparable at high compression)."
            ),
        ),
        entry(
            "comparative_rms",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="MROP vs classical residual-map std (3C 273)",
            baseline="Classical (uncompressed) model",
            empirical=True,
            execution_context=ctx(
                residual_vs_dirty="Residual",
                simulation_vs_real="Real VLA",
                frequency="X band",
                array="VLA",
            ),
            evidence=(
                "MROP residual-map std 6.87×10⁻⁴ vs classical 6.49×10⁻⁴ — numerical comparison "
                "confirming fidelity preserved under compression."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    rms_papers = [p for p in papers if p["metrics"].get("rms") == 1]
    missing = [p["bibcode"] for p in rms_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in rms_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not rms=1: {extra}")

    for p in papers:
        p.pop("rms_details", None)

    mirror = {
        "schema_note": (
            "rms_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.rms binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in rms_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["rms_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "rms_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in rms_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["rms_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected rms_details for {len(rms_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    # Sanity: binary rms unchanged
    assert all(p["metrics"]["rms"] == 1 for p in rms_papers)
    assert sum(1 for p in papers if p["metrics"].get("rms") == 1) == 11
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
