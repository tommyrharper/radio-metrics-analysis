#!/usr/bin/env python3
"""Inject ssim_details into data/papers-data.json for SSIM-positive papers.

Run from repo root: python3 scripts/inject_ssim_details.py
Does not change top-level metrics.ssim flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "ssim-details.json"


def ctx(
    aggregation=None,
    image_domain=None,
    normalization=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "aggregation": aggregation,
        "image_domain": image_domain,
        "normalization": normalization,
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


# bibcode -> list of ssim_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "2025arXiv251213591C": [
        entry(
            "framework_defined",
            "named_core_quality_metric",
            value=None,
            unit=None,
            scope="astroCAMP Table 2 algorithmic-quality pair (PSNR / SSIM)",
            empirical=False,
            execution_context=ctx(
                aggregation=None,
                image_domain="Reconstruction Î vs reference I_ref",
                normalization=None,
                simulation_vs_real="Framework definition (WSClean+IDG runs skip computing SSIM)",
                frequency=None,
                array="SKA-scale co-design / WSClean+IDG workloads",
            ),
            evidence=(
                "Table 2 lists SSIM with PSNR as a core algorithmic-quality pair "
                "(dimensionless structural similarity). Both appear in co-design quality "
                "examples; the WSClean+IDG experimental release does not compute SSIM "
                "pending community tolerances."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2022MNRAS.514.2614C": [
        entry(
            "absolute_ssim",
            "mean_image_ssim",
            value=0.998,
            unit="mean ± 0.0016 (dimensionless)",
            scope="Full-band DSA-2000 sim (1300 MHz, 15 min PSF); POLISH on 50 validation fields",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean ± std over validation images",
                image_domain="Intensity / restored vs truth",
                normalization="Inputs and targets normalized to integer range before SSIM",
                simulation_vs_real="Simulation (DSA-2000 synthetic radio-galaxy skies)",
                frequency="1300 MHz full-band",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "Full-band: POLISH mean SSIM 0.998±0.0016 vs CLEAN 0.989±0.007 "
                "on the same simulated radio-galaxy task."
            ),
        ),
        entry(
            "absolute_ssim",
            "mean_image_ssim",
            value=0.988,
            unit="mean ± 0.0016 (dimensionless)",
            scope="Narrow-band DSA-2000 sim (10 MHz snapshot PSF); POLISH on 50 validation fields",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean ± std over validation images",
                image_domain="Intensity / restored vs truth",
                normalization="Inputs and targets normalized to integer range before SSIM",
                simulation_vs_real="Simulation (DSA-2000 synthetic radio-galaxy skies)",
                frequency="10 MHz snapshot",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "Narrow-band: POLISH mean SSIM 0.988±0.0016 vs CLEAN 0.976±0.009 "
                "with the more structured 10 MHz snapshot PSF."
            ),
        ),
        entry(
            "comparative_ssim",
            "ssim_delta",
            value=0.009,
            unit="mean SSIM improvement",
            scope="Full-band DSA-2000: POLISH vs image-plane CLEAN",
            baseline="Image-plane CLEAN (mean SSIM 0.989±0.007)",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean improvement over validation set",
                image_domain="Intensity / restored vs truth",
                normalization="Integer-range normalization",
                simulation_vs_real="Simulation (DSA-2000)",
                frequency="1300 MHz full-band",
                array="DSA-2000 (simulated)",
            ),
            evidence="Reported mean SSIM improvement +0.009 (full-band) vs CLEAN.",
        ),
        entry(
            "comparative_ssim",
            "ssim_delta",
            value=0.012,
            unit="mean SSIM improvement",
            scope="Narrow-band DSA-2000: POLISH vs image-plane CLEAN",
            baseline="Image-plane CLEAN (mean SSIM 0.976±0.009)",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean improvement over validation set",
                image_domain="Intensity / restored vs truth",
                normalization="Integer-range normalization",
                simulation_vs_real="Simulation (DSA-2000)",
                frequency="10 MHz snapshot",
                array="DSA-2000 (simulated)",
            ),
            evidence="Reported mean SSIM improvement +0.012 (narrow-band) vs CLEAN.",
        ),
        entry(
            "comparative_ssim",
            "higher_lower_than_baseline",
            value=None,
            unit=None,
            scope="POLISH vs image-plane CLEAN on DSA-2000 sims",
            baseline="Image-plane CLEAN",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean SSIM",
                image_domain="Intensity / restored vs truth",
                normalization="Integer-range normalization",
                simulation_vs_real="Simulation (DSA-2000); real VLA transfer has no SSIM",
                frequency="1300 MHz / 10 MHz",
                array="DSA-2000 (simulated)",
            ),
            evidence=(
                "POLISH beats CLEAN on both full-band and narrow-band mean SSIM; "
                "real VLA transfer is qualitative only (no SSIM)."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024arXiv241023178C": [
        entry(
            "absolute_ssim",
            "median_ssim",
            value=0.970,
            unit="median (dimensionless)",
            scope="EVIL-Deconv base network vs CLEAN / PnP (Table 2 medians)",
            empirical=True,
            execution_context=ctx(
                aggregation="Median over test set",
                image_domain="Reconstruction vs truth (UQ appendix fidelity table)",
                normalization=None,
                simulation_vs_real="Simulation / controlled reconstruction benchmark",
                frequency=None,
                array="Radio interferometry (EVIL-Deconv / equivariant bootstrap paper)",
            ),
            evidence=(
                "Table 2 median SSIM: CLEAN 0.296; PnP (DnCNN) 0.869; "
                "EVIL-Deconv 0.970 (with NMSE 19.9 dB)."
            ),
        ),
        entry(
            "comparative_ssim",
            "higher_lower_than_baseline",
            value=0.970,
            unit="median SSIM",
            scope="EVIL-Deconv vs CLEAN and PnP (DnCNN)",
            baseline="CLEAN (0.296) / PnP DnCNN (0.869)",
            empirical=True,
            execution_context=ctx(
                aggregation="Median",
                image_domain="Reconstruction vs truth",
                normalization=None,
                simulation_vs_real="Simulation / controlled reconstruction benchmark",
                frequency=None,
                array="Radio interferometry (EVIL-Deconv)",
            ),
            evidence=(
                "EVIL-Deconv median SSIM 0.970 exceeds PnP (0.869) and CLEAN (0.296); "
                "SSIM validates the fast deconv network used for UQ experiments."
            ),
        ),
    ],
    "2025arXiv250309559C": [
        entry(
            "absolute_ssim",
            "magnitude_image_ssim",
            value=0.96,
            unit="mean ± 0.05 (dimensionless)",
            scope="iR2D2(U-WDSR) magnitude reconstructions vs FastMRI / non-Cartesian MRI truth",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean ± std",
                image_domain="Magnitude images (|x⋆| vs |x̂|)",
                normalization=None,
                simulation_vs_real="Simulated multi-coil radial FastMRI knee; real 15-coil 3T validation uses RDR/qualitative (no SSIM table)",
                frequency="MRI (3T bSSFP / FastMRI knee)",
                array="Multi-coil non-Cartesian MRI (iR2D2 transfer of R2D2 paradigm)",
            ),
            evidence=(
                "SSIM on magnitude: iR2D2(U-WDSR) 0.96±0.05 vs R2D2 0.93±0.06, "
                "NC-PDNet 0.90±0.08, DDS 0.85±0.13."
            ),
        ),
        entry(
            "comparative_ssim",
            "higher_lower_than_baseline",
            value=0.96,
            unit="mean SSIM",
            scope="iR2D2(U-WDSR) vs R2D2 / NC-PDNet / DDS on magnitude images",
            baseline="R2D2(U-WDSR) 0.93±0.06; NC-PDNet 0.90±0.08; DDS 0.85±0.13",
            empirical=True,
            execution_context=ctx(
                aggregation="Mean ± std",
                image_domain="Magnitude images (|x⋆| vs |x̂|)",
                normalization=None,
                simulation_vs_real="Simulated FastMRI knee benchmark",
                frequency="MRI (FastMRI knee)",
                array="Multi-coil non-Cartesian MRI",
            ),
            evidence=(
                "iR2D2(U-WDSR) SSIM 0.96±0.05 ranks above R2D2, NC-PDNet, and DDS, "
                "consistent with PSNR rankings on the same non-Cartesian benchmark."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    ssim_papers = [p for p in papers if p["metrics"].get("ssim") == 1]
    missing = [p["bibcode"] for p in ssim_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in ssim_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not ssim=1: {extra}")

    for p in papers:
        p.pop("ssim_details", None)

    mirror = {
        "schema_note": (
            "ssim_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.ssim binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in ssim_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["ssim_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "ssim_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in ssim_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["ssim_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected ssim_details for {len(ssim_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["ssim"] == 1 for p in ssim_papers)
    assert sum(1 for p in papers if p["metrics"].get("ssim") == 1) == 4
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
