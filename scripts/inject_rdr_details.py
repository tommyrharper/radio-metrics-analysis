#!/usr/bin/env python3
"""Inject rdr_details into data/papers-data.json for RDR-positive papers.

Run from repo root: python3 scripts/inject_rdr_details.py
Mirror only: python3 scripts/inject_rdr_details.py --mirror-only
Does not change top-level metrics.rdr flags.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "rdr-details.json"


def ctx(
    domain=None,
    norm=None,
    reporting_scale=None,
    simulation_vs_real=None,
    frequency=None,
    array=None,
):
    return {
        "domain": domain,
        "norm": norm,
        "reporting_scale": reporting_scale,
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


# bibcode -> list of rdr_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- emerging-ml ---
    "2024ApJS..273....3A": [
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=13.5,
            unit="×10⁻⁴ (mean ± std)",
            scope="Generic VLA 512×512 sims — R2D2 mean residual-to-dirty ratio (Table 2)",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻⁴",
                simulation_vs_real="Simulation (VLA)",
                frequency="Monochromatic (sim)",
                array="VLA",
            ),
            evidence=(
                "Image-domain data fidelity ‖r̂‖₂/‖x_dirty‖₂; Table 2 means (×10⁻⁴): CLEAN 5.1±5.2, "
                "uSARA 6.5±8.2, AIRI 6.4±8.0, R2D2 13.5±46.9, R3D3-3L 7.6±7.6, R3D3-6L 7.9±7.8."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="Generic + high-DR targeted VLA experiments vs CLEAN / uSARA / AIRI / R3D3",
            baseline="CLEAN, uSARA, AIRI, R3D3",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻⁴",
                simulation_vs_real="Simulation (VLA)",
                array="VLA",
            ),
            evidence=(
                "CLEAN lowest mean RDR in generic tests; at DR≈10⁵ AIRI/uSARA beat R2D2 on RDR "
                "despite comparable morphology — truth fidelity distinguished from data-residual fidelity."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻⁴",
            ),
            evidence=(
                "Residual-to-dirty-image ratio introduced as the R2D2-family image-domain "
                "data-fidelity metric alongside SNR / logSNR."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2025ApJS..280...63A": [
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=2.22e-3,
            unit="(R2D2_A2,T2; Table 4)",
            scope="Simulated VLA monochromatic 512×512 — RDR(r̂, x_d)=‖r̂‖₂/‖x_d‖₂",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻³",
                simulation_vs_real="Simulation (VLA)",
                frequency="Monochromatic",
                array="VLA",
            ),
            evidence=(
                "Table 4: R2D2_A2,T2 2.22×10⁻³, AIRI 2.24×10⁻³, uSARA 2.15×10⁻³; "
                "CLEAN 3.29×10⁻³; older R2D2_A1,T2 4.07×10⁻³."
            ),
        ),
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=2.46e-3,
            unit="(R2D2_A2,T2 Cygnus A)",
            scope="Real Cygnus A data — converged RDR (Section 5 / Fig. 6)",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻³",
                simulation_vs_real="Real (Cygnus A)",
                array="VLA",
            ),
            evidence=(
                "Real-data RDR: R2D2_A1,T1 2.85×10⁻³, R2D2_A1,T2 2.68×10⁻³, "
                "R2D2_A2,T2 2.46×10⁻³ (best / lowest)."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="R2D2_A2,T2 vs CLEAN / AIRI / uSARA / older architecture",
            baseline="CLEAN, AIRI, uSARA, R2D2_A1",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻³",
                simulation_vs_real="Simulation (and real Cygnus A)",
                array="VLA",
            ),
            evidence=(
                "R2D2_A2,T2 RDR comparable to AIRI/uSARA; CLEAN ~50% higher; "
                "old architecture ~2× worse."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻³",
            ),
            evidence=(
                "RDR formalized as primary image-domain data-fidelity metric; "
                "also used in data-fidelity-based series convergence criterion."
            ),
        ),
        entry(
            "framework_operational",
            "adaptive_stopping_criterion",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                simulation_vs_real="Simulation and real Cygnus A",
                array="VLA",
            ),
            evidence=(
                "Data-fidelity-based series convergence criterion; Cygnus A iteration counts "
                "to convergence 12–16 depending on architecture/training."
            ),
        ),
    ],
    "2025MNRAS.542..426T": [
        entry(
            "reported_rdr",
            "spherical_rdr",
            value=1.2e-2,
            unit="(S-R2D2 best mean at Np=600²)",
            scope="S-R2D2 sphere RDR across Np=400²–800²",
            empirical=True,
            execution_context=ctx(
                domain="Sphere",
                norm="ℓ₂ (sphere via Γ†)",
                reporting_scale="×10⁻²",
                simulation_vs_real="Simulation (wide-field)",
            ),
            evidence=(
                "RDR(r,x^d)=‖r‖₂/‖x^d‖₂ on the sphere. S-R2D2: 1.5×10⁻² → 1.2×10⁻² (best) "
                "→ 2.1×10⁻² as Np increases 400²→800²."
            ),
        ),
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=14e-2,
            unit="(planar R2D2 at Np=800²)",
            scope="Planar R2D2 RDR degradation with resolution",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="×10⁻²",
                simulation_vs_real="Simulation (wide-field)",
            ),
            evidence=(
                "Planar R2D2 RDR worsens from 0.8×10⁻² (Np=400²) to 14×10⁻² (Np=800²) "
                "while S-R2D2 stays ≈1–2×10⁻²."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="S-R2D2 vs planar R2D2 across Np / sources",
            baseline="Planar R2D2",
            empirical=True,
            execution_context=ctx(
                domain="Sphere vs planar",
                norm="ℓ₂",
                reporting_scale="×10⁻²",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "S-R2D2 maintains low RDR as Np/SR increases; planar R2D2 data fidelity "
                "degrades sharply (super-resolving limitation)."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Sphere",
                norm="ℓ₂ (sphere via Γ†)",
            ),
            evidence=(
                "RDR defined as core data-fidelity metric for spherical R2D2 evaluation "
                "alongside SNR / logSNR."
            ),
        ),
    ],
    "2025arXiv250309559C": [
        entry(
            "reported_rdr",
            "backprojected_mri_rdr",
            value=None,
            unit=None,
            scope="iR2D2 RDR=‖r‖₂/‖x_b‖₂ tracked over series on simulated FastMRI + real 3T knee",
            empirical=True,
            execution_context=ctx(
                domain="MRI (non-Cartesian multi-coil)",
                norm="ℓ₂ (back-projected residual / dirty-like image)",
                reporting_scale="Ratio (unitless)",
                simulation_vs_real="Simulation (FastMRI) and real 15-coil 3T knee",
                frequency="MRI (bSSFP knee)",
                array="15-coil 3T",
            ),
            evidence=(
                "RDR used as data-fidelity/convergence metric on simulated and real knee data; "
                "real-data iR2D2 achieves best (lowest) RDR among benchmarks."
            ),
        ),
        entry(
            "comparative_rdr",
            "rdr_factor_vs_baseline",
            value=10,
            unit="× (approx. order-of-magnitude lower)",
            scope="Real 15-coil 3T knee (AF=4 and AF=8) vs benchmark methods",
            baseline="Benchmark MRI reconstruction methods",
            empirical=True,
            execution_context=ctx(
                domain="MRI (non-Cartesian multi-coil)",
                norm="ℓ₂",
                simulation_vs_real="Real 15-coil 3T knee",
                array="15-coil 3T",
            ),
            evidence=(
                "iR2D2 RDR roughly an order of magnitude lower than benchmarks; residual maps "
                "appear unstructured noise vs anatomy-correlated residuals for baselines."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="MRI",
                norm="ℓ₂",
            ),
            evidence=(
                "RDR (Residual Data Ratio) and RDR-bar (sensitivity residual) named as "
                "primary residual/convergence metrics."
            ),
        ),
        entry(
            "framework_operational",
            "adaptive_stopping_criterion",
            empirical=True,
            execution_context=ctx(
                domain="MRI",
                norm="ℓ₂",
                simulation_vs_real="Simulation and real",
            ),
            evidence=(
                "Adaptive error-controlled stopping driven by sufficient residual-energy descent "
                "(UC/UC-bar); ablation without update condition shows erratic residual spikes."
            ),
        ),
    ],
    "2026AJ....171...44Y": [
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=0.0067,
            unit="(ALSB; VLA/W28 Table 1)",
            scope="Image-domain data fidelity σ=‖r̂‖₂/‖x_dirty‖₂ — VLA/W28, SKA/3C353, DART/Sun",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="Raw ratio",
                simulation_vs_real="Simulation (VLA/SKA) and DART real solar",
                frequency="425 MHz (DART); sim otherwise",
                array="VLA / SKA-like / DART (294 ant.)",
            ),
            evidence=(
                "Following Aghabiglou et al. R2D2 fidelity metric. ALSB best σ: VLA/W28 0.0067 "
                "(vs AIRI 0.0106, SARA 0.0182); SKA/3C353 0.0103; DART/Sun 0.00281."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="ALSB vs SARA / AIRI / WTF / MS-CLEAN across three experiments",
            baseline="SARA, AIRI, WTF, MS-CLEAN",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="Raw ratio",
                simulation_vs_real="Simulation and real DART",
            ),
            evidence=(
                "ALSB reports lowest σ on all three tables; on DART ≈2.4× lower than WTF "
                "and ~11× lower than SARA."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
            ),
            evidence=(
                "Image-domain data fidelity σ explicitly adopted from R2D2 convention "
                "as a primary evaluation metric with SNR and runtime."
            ),
        ),
    ],
    "2026AJ....171..220Y": [
        entry(
            "reported_rdr",
            "planar_l2_rdr",
            value=3.054e-2,
            unit="(GMCP; VLA/3C353 Table 1)",
            scope="Image-domain data fidelity σ — VLA/3C353 and DART/Sun (avg. of 100 sims)",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                reporting_scale="Raw / ×10⁻²",
                simulation_vs_real="Simulation (VLA and DART)",
                array="VLA / DART",
            ),
            evidence=(
                "σ=‖r̂‖₂/‖x_dirty‖₂. VLA/3C353: GMCP 3.054e-2 (best) vs R2D2 3.919e-2, "
                "AIRI 4.740e-2, SARA 4.858e-2. DART/Sun: GMCP 1.756e-2 (best)."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="GMCP vs SARA / AIRI / LPG / R2D2 / MS-CLEAN",
            baseline="SARA, AIRI, LPG, R2D2, MS-CLEAN",
            empirical=True,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "GMCP lowest σ on both tables; adaptive-λ ablation also lowers σ vs fixed λ=1e-5."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Planar image",
                norm="ℓ₂",
            ),
            evidence=(
                "Image-domain data fidelity σ listed with SNR/SNRlog as a primary "
                "R2D2-convention evaluation metric."
            ),
        ),
    ],
    "2026ApJS..283....9T": [
        entry(
            "reported_rdr",
            "frobenius_cube_rdr",
            value=2.3e-3,
            unit="≈2.3–2.6×10⁻³ (all methods)",
            scope="Hyperspectral cube RDR=‖X^res‖_F/‖X^dirty‖_F vs truth reference 2.46×10⁻³",
            empirical=True,
            execution_context=ctx(
                domain="Hyperspectral cube",
                norm="Frobenius",
                reporting_scale="×10⁻³",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "All methods achieve broadly comparable RDR (~2.3–2.6×10⁻³), close to "
                "ground-truth reference (2.46±1.37)×10⁻³, despite large SNR spreads."
            ),
        ),
        entry(
            "comparative_rdr",
            "lower_higher_than_baseline",
            value=None,
            unit=None,
            scope="HyperAIRI vs WSClean / optimization baselines — RDR comparable, SNR not",
            baseline="WSClean and optimization-based methods",
            empirical=True,
            execution_context=ctx(
                domain="Hyperspectral cube",
                norm="Frobenius",
                reporting_scale="×10⁻³",
                simulation_vs_real="Simulation",
            ),
            evidence=(
                "WSClean matches RDR/data-fidelity of other methods yet has far lower SNR "
                "(11.27 dB vs HyperAIRI 30.53 dB) — RDR ≠ truth fidelity."
            ),
        ),
        entry(
            "framework_operational",
            "named_data_fidelity_metric",
            empirical=False,
            execution_context=ctx(
                domain="Hyperspectral cube",
                norm="Frobenius",
                reporting_scale="×10⁻³",
            ),
            evidence=(
                "RDR defined as primary image-domain data-fidelity metric for hyperspectral "
                "evaluation alongside SNR, logSNR, and sSNR."
            ),
        ),
    ],
}


def main():
    mirror_only = "--mirror-only" in sys.argv
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    rdr_papers = [p for p in papers if p["metrics"].get("rdr") == 1]
    missing = [p["bibcode"] for p in rdr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in rdr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not rdr=1: {extra}")

    if not mirror_only:
        for p in papers:
            p.pop("rdr_details", None)

    mirror = {
        "schema_note": (
            "rdr_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.rdr binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in rdr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        if not mirror_only:
            p["rdr_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "rdr_details": details,
        }

    if not mirror_only:
        PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in rdr_papers:
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

    print(f"{'Mirror-only: wrote' if mirror_only else 'Injected'} rdr_details for {len(rdr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["rdr"] == 1 for p in rdr_papers)
    assert sum(1 for p in papers if p["metrics"].get("rdr") == 1) == 7
    wrote = [str(MIRROR.relative_to(ROOT))]
    if not mirror_only:
        wrote.insert(0, str(PAPERS_DATA.relative_to(ROOT)))
    print(f"Wrote {', '.join(wrote)}")


if __name__ == "__main__":
    main()
