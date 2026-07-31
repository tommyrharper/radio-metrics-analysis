#!/usr/bin/env python3
"""Classify snr_details for SNR-positive papers; write data/snr-details.json only.

Run from repo root: python3 scripts/inject_snr_details.py
Reads paper list from data/papers-data.json but does NOT mutate it.
Does not change top-level metrics.snr flags.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "snr-details.json"


def ctx(
    formula=None,
    simulation_vs_real=None,
    input_snr_setting=None,
    frequency=None,
    array=None,
):
    return {
        "formula": formula,
        "simulation_vs_real": simulation_vs_real,
        "input_snr_setting": input_snr_setting,
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


# bibcode -> list of snr_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "2008ISTSP...2..793C": [
        entry(
            "input_operating_snr",
            "image_plane_theoretical_snr",
            value=4,
            unit="SNR (flux-recovery threshold)",
            scope="M51 noise sweep; theoretical image-plane SNR = clean-beam-convolved model peak / image-plane noise",
            empirical=True,
            execution_context=ctx(
                formula="Peak(clean-beam⋆model) / image-plane noise",
                simulation_vs_real="Simulation (VLA C-array X band)",
                input_snr_setting="Swept image-plane SNR (flux accurate down to ~4; MEM fails near 100)",
                frequency="X band",
                array="VLA C-array",
            ),
            evidence=(
                "Noise sweep defines theoretical image-plane SNR and studies flux-recovery thresholds: "
                "MEM overestimates at SNR as high as 100; CLEAN / Maximum Emptiness / Multiscale CLEAN "
                "remain accurate down to SNR ~4; Högbom stays usable even below SNR 1."
            ),
        ),
    ],
    "2012MNRAS.426.1223C": [
        entry(
            "reconstruction_snr",
            "std_reconstruction_snr",
            value=38.43,
            unit="dB",
            scope="Example M31 reconstruction at 30% coverage (SARA); mean curves over 100 sims",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(σ_x / σ_{x−x̂})",
                simulation_vs_real="Simulation (variable-density Fourier coverage)",
                input_snr_setting="30 dB input SNR",
                frequency=None,
                array="Generic discrete Fourier (no telescope)",
            ),
            evidence=(
                "Primary fidelity metric is 20·log₁₀(σ_x/σ_{x−x̂}) dB. Example at 30% coverage: "
                "SARA 38.43 dB (M31) / 29.08 dB (30 Doradus) vs BP/TV/IUWT baselines."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value=30,
            unit="dB",
            scope="Complex Gaussian noise on visibilities for all coverage sweeps",
            empirical=True,
            execution_context=ctx(
                formula="Same σ form with per-visibility noise std in denominator",
                simulation_vs_real="Simulation",
                input_snr_setting="30 dB",
                frequency=None,
                array="Generic discrete Fourier",
            ),
            evidence="Complex Gaussian noise added at fixed 30 dB input SNR; 100 Monte Carlo runs per coverage.",
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value=6,
            unit="dB (lower bound at 10% coverage, M31)",
            scope="SARA vs BP / BPDb8 / TV / IUWT across 10–90% coverage",
            baseline="Directly run BP, BPDb8, TV, IUWT",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(σ_x / σ_{x−x̂})",
                simulation_vs_real="Simulation",
                input_snr_setting="30 dB",
                frequency=None,
                array="Generic discrete Fourier",
            ),
            evidence=(
                "SARA highest mean reconstruction SNR at every coverage; >6 dB gain over every other method "
                "at 10% coverage (M31) and ≥3 dB elsewhere; ≥2 dB on 30 Doradus at every coverage."
            ),
        ),
    ],
    "2014MNRAS.439.3591C": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            scope="Coverage sweep M/N=0.2–2 on M31 and 30 Doradus (mean of 30 sims)",
            unit="dB",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x‖₂ / ‖x−x̂‖₂)",
                simulation_vs_real="Simulation (continuous off-grid Fourier + AMI coverage test)",
                input_snr_setting="30 dB input visibility SNR",
                frequency=None,
                array="Generic + simulated AMI",
            ),
            evidence=(
                "Primary fidelity metric is L₂ reconstruction SNR vs noiseless model. "
                "SARA has the highest mean SNR throughout both M31 and 30 Doradus coverage sweeps."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value=30,
            unit="dB",
            scope="Fixed input visibility SNR for all PURIFY configurations",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖y₀‖₂ / ‖n‖₂)",
                simulation_vs_real="Simulation",
                input_snr_setting="30 dB",
                frequency=None,
                array="Generic + simulated AMI",
            ),
            evidence="Input visibility SNR fixed at 30 dB, distinct from the reconstruction SNR score.",
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value=4,
            unit="dB (upper gap vs next-best on M31)",
            scope="SARA vs RWBPDb8 / TV / RWTV / BP variants",
            baseline="RWBPDb8 (M31); TV/RWTV (30 Doradus)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x‖₂ / ‖x−x̂‖₂)",
                simulation_vs_real="Simulation",
                input_snr_setting="30 dB",
                frequency=None,
                array="Generic continuous Fourier",
            ),
            evidence=(
                "On M31, next-best RWBPDb8 remains as much as 4 dB below SARA; on 30 Doradus, "
                "TV/RWTV are at most 2 dB below SARA."
            ),
        ),
    ],
    "2018A&A...611A..87T": [
        entry(
            "input_operating_snr",
            "operational_tradeoff_snr",
            value=10,
            unit="× SNR reduction (sparsification factor 100)",
            scope="Early high-SNR CLEAN major cycles with visibility-block sparsification",
            empirical=False,
            execution_context=ctx(
                formula="Operational effective-SNR trade-off (not truth-based reconstruction SNR)",
                simulation_vs_real="Representative VLA / MeerKAT L-band rationale",
                input_snr_setting="DR ~1e4+; early cycles kept above noise floor",
                frequency="L band",
                array="VLA or MeerKAT (representative)",
            ),
            evidence=(
                "Sparsification factor of 100 is argued to reduce SNR by 10× while leaving early cycles "
                "above the noise floor (schedule 100, 100, 30, 10, 1). Operational rationale, not a "
                "measured end-to-end reconstruction-SNR benchmark."
            ),
        ),
    ],
    # --- emerging-ml ---
    "2024ApJS..273....3A": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=34.0,
            unit="dB (mean ± std)",
            scope="Generic 200-problem VLA simulation test; R3D3-6L best mean",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x_true‖₂ / ‖x_true − x̂‖₂)",
                simulation_vs_real="Simulation (VLA A/C; known 512² truth)",
                input_snr_setting="Gaussian visibility noise adapted to target image DR",
                frequency="1–4 channels (varied)",
                array="VLA",
            ),
            evidence=(
                "Linear S/N: CLEAN 13.6±3.6, uSARA 30.8±1.9, AIRI 31.3±2.3, R2D2 33.7±1.5, "
                "R3D3-3L 33.8±1.4, R3D3-6L 34.0±1.6 dB on the generic 200-problem test."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value="2.4–3.2",
            unit="dB mean gain",
            scope="Learned-series methods vs AIRI / uSARA on matched simulated test",
            baseline="AIRI and uSARA",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation (VLA)",
                input_snr_setting="Noise adapted to target DR",
                frequency=None,
                array="VLA",
            ),
            evidence=(
                "Across R2D2 / R3D3, mean gain is 2.4–2.7 dB over AIRI and 2.9–3.2 dB over uSARA; "
                "end-to-end U-Net only 20.5±2.7 dB."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024RASTI...3..505L": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=30.25,
            unit="dB",
            scope="QuantifAI MAP on Cygnus A (Table 1); MeerKAT synthesis-time sweep also reported",
            empirical=True,
            execution_context=ctx(
                formula="−20·log₁₀(‖x_gt − x‖₂ / ‖x_gt‖₂) ≡ 20·log₁₀ L₂ form",
                simulation_vs_real="Simulation + realistic MeerKAT ungridded-visibility experiment",
                input_snr_setting=None,
                frequency=None,
                array="MeerKAT (realistic experiment)",
            ),
            evidence=(
                "Table 1 QuantifAI MAP SNR: W28 26.85, M31 27.48, 3C288 24.10, Cygnus A 30.25 dB. "
                "MeerKAT M31 MAP SNR rises 25.29→34.42 dB over 1–8 h synthesis."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value="1.9–12.7",
            unit="dB (avg ~7)",
            scope="QuantifAI MAP vs wavelet-based MAP across four images",
            baseline="Wavelet-based sparsity MAP (Cai et al. 2018b style)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation (Table 1)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence="QuantifAI MAP beats wavelet-based MAP by 1.9–12.7 dB (average ~7 dB) across the dataset.",
        ),
    ],
    "2024arXiv240317905C": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=18.44,
            unit="dB (example validation sample)",
            scope="MRI R2D2 validation sample at DR=167, AF=16 (Fig. 2)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x̄‖₂ / ‖x̄ − x‖₂)",
                simulation_vs_real="Simulation (non-Cartesian MRI; RI analogue)",
                input_snr_setting=None,
                frequency=None,
                array="MRI (spokes / AF sweep)",
            ),
            evidence=(
                "Primary metric is L₂ SNR vs ground truth. Example at AF=16: R2D2 18.44 dB, "
                "R2D2-Net (NUFFT) 19.39 dB, AIRI 15.55 dB, U-Net 14.93 dB."
            ),
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="R2D2 / R2D2-Net vs AIRI, U-Net, NC-PDNet across AF and iteration sweeps",
            baseline="AIRI, U-Net, NC-PDNet",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation (MRI)",
                input_snr_setting=None,
                frequency=None,
                array="MRI",
            ),
            evidence=(
                "R2D2-Net (NUFFT) and R2D2 outperform AIRI/U-Net/NC-PDNet on SNR; Additional Acceleration "
                "Ratio table reports how much more undersampling R2D2 tolerates at matched SNR targets."
            ),
        ),
    ],
    "2024arXiv240318052A": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=33,
            unit="dB (approx. final)",
            scope="Simulated test set Fig. 2; 3C 353 case study to 37.7 dB",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x⋆‖₂ / ‖x⋆ − x̂‖₂)",
                simulation_vs_real="Simulation + real-data-like 3C 353 case study",
                input_snr_setting=None,
                frequency=None,
                array="Radio-interferometric simulation / 3C 353",
            ),
            evidence=(
                "R2D2 converges to ~33 dB on the simulated test set; 3C 353 case study rises "
                "35.0→37.7 dB across iterations 1→12."
            ),
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="R2D2 vs CLEAN, U-Net, uSARA (and qualitatively AIRI)",
            baseline="CLEAN (~15.9 dB), uSARA (~19.5 dB), U-Net (~28 dB first iteration)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "Simulated test: R2D2 ~33 dB vs U-Net ~28, uSARA 19.5, CLEAN 15.9 dB. "
                "Paper states image estimation largely superior to CLEAN, U-Net, uSARA, and AIRI."
            ),
        ),
    ],
    "2025AJ....169..289W": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            scope="Simulated Sgr B2 / Sgr C; S/N tracked per major cycle (Fig. 5)",
            unit="dB",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖i‖₂ / ‖i − î‖₂)",
                simulation_vs_real="Simulation (Sgr B2, Sgr C); real data use Wasserstein instead",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "S/N defined as 20·log₁₀ L₂ fidelity for simulated datasets with known truth; "
                "parallel and serial methods converge to comparable S/N across major cycles."
            ),
        ),
    ],
    "2025A&A...704A..43Y": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=34.63,
            unit="dB",
            scope="Messier 106 SKA sim at input S/N=35 dB (ISCAD)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x‖₂ / ‖x − x̃‖₂)",
                simulation_vs_real="Simulation",
                input_snr_setting="35 dB (tables); robustness sweep 15–55 dB",
                frequency=None,
                array="SKA (Messier 106 test)",
            ),
            evidence=(
                "At input S/N=35 dB on Messier 106: ISCAD 34.63 dB vs LPG 34.40, AIRI 33.12, SARA 31.95. "
                "ISCAD highest S/N on all three test cases."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value="15–55",
            unit="dB (sweep); 35 dB tabulated",
            scope="Noise-robustness Monte Carlo (100 realisations per point)",
            empirical=True,
            execution_context=ctx(
                formula="Input S/N swept; reconstruction S/N measured",
                simulation_vs_real="Simulation",
                input_snr_setting="15–55 dB sweep; 35 dB for table",
                frequency=None,
                array="SKA / RI simulations",
            ),
            evidence="S/N and S/N_log vs input S/N (15–55 dB), 100 Monte Carlo realisations per point.",
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="ISCAD vs SARA, AIRI, LPG across tests and noise sweep",
            baseline="SARA, AIRI, LPG",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting="15–55 dB",
                frequency=None,
                array=None,
            ),
            evidence="ISCAD attains the highest S/N on all three cases and across the 15–55 dB noise-robustness sweep.",
        ),
    ],
    "2025ApJS..280...63A": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=31.2,
            unit="dB (mean ± 2.4)",
            scope="Table 4 setup E2; R2D2_A2,T2 best model",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x⋆‖₂ / ‖x⋆ − x̂‖₂)",
                simulation_vs_real="Simulation (fully randomized E2 test)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "E2 benchmark: R2D2_A2,T2 31.2±2.4 dB; AIRI 28.3±3.1; uSARA 28.1±3.4; CLEAN 12.0±19.3 dB "
                "(diverged on 3 problems)."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value="2–4",
            unit="dB",
            scope="R2D2 models vs uSARA / AIRI on E2",
            baseline="uSARA / AIRI",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence="R2D2 models outperform uSARA/AIRI by roughly 2–4 dB in SNR on the harder E2 setup.",
        ),
    ],
    "2025ChJSS..45.1597F": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=35.73,
            unit="dB",
            scope="Simulated SKA array (MCP proposed); also 10%/50% undersampling tables",
            empirical=True,
            execution_context=ctx(
                formula="SNR in dB (reconstruction quality; formula not further specialized in notes)",
                simulation_vs_real="Simulation (undersampling + SKA array)",
                input_snr_setting=None,
                frequency=None,
                array="Simulated SKA",
            ),
            evidence=(
                "MCP SNR: 24.16 dB (10% undersampling), 27.78 dB (50%), 35.73 dB (SKA array) — "
                "highest in every tested condition."
            ),
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="MCP vs SARA and AIRI at 10%/50% undersampling and SKA array",
            baseline="SARA, AIRI",
            empirical=True,
            execution_context=ctx(
                formula="Reconstruction SNR (dB)",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array="Simulated SKA",
            ),
            evidence=(
                "MCP exceeds SARA and AIRI on SNR in every condition (e.g. SKA: MCP 35.73 vs AIRI 34.52 "
                "vs SARA 32.83 dB)."
            ),
        ),
    ],
    "2025MNRAS.537.1608T": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=28.65,
            unit="dB",
            scope="cAIRI-OAID at ΔT=8 h (example); sweeps over 1–8 h",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x̄‖ / ‖x̄ − x̂‖)",
                simulation_vs_real="Simulation (RI observations, varying integration time)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "At ΔT=8 h: MS-CLEAN 5.45, SARA 27.74, cAIRI-OAID 28.65 dB SNR. "
                "AIRI-family methods tracked across 1–8 h observation times."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value="1–2",
            unit="dB over uSARA/SARA; >20 dB over CLEAN",
            scope="AIRI / cAIRI vs uSARA / SARA / MS-CLEAN",
            baseline="uSARA, SARA, MS-CLEAN",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "AIRI/cAIRI improve by 1–2 dB over uSARA/SARA counterparts and dramatically outperform "
                "CLEAN (>20 dB) across observation times."
            ),
        ),
    ],
    "2025MNRAS.542..426T": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=21.7,
            unit="dB (mean ± 4.3 at Np=400²)",
            scope="S-R2D2 Table 1 means over 60 test problems on the sphere",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x*‖₂ / ‖x* − x̂‖₂) on the sphere",
                simulation_vs_real="Simulation (spherical wide-field)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "S-R2D2 SNR 21.7±4.3 / 21.2±3.9 / 20.8±3.7 dB at Np=400²/600²/800²; "
                "planar R2D2 degrades from 6.6±1.5 to 1.9±1.5 dB over the same resolutions."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value="14–19",
            unit="dB",
            scope="S-R2D2 vs planar R2D2 at matched resolutions",
            baseline="Planar R2D2",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR (sphere)",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence="S-R2D2 outperforms R2D2 by roughly 14–19 dB in SNR at matched resolutions.",
        ),
    ],
    "2025MNRAS.542.2494M": [
        entry(
            "input_operating_snr",
            "discoverability_threshold_snr",
            value=20,
            unit="SNR_tot (combined lensed images)",
            scope="Conservative/optimistic lens discoverability criteria for DSA-2000 / SKA-Mid / VLASS forecasts",
            empirical=False,
            execution_context=ctx(
                formula="Total SNR of combined lensed images (literature threshold)",
                simulation_vs_real="Forecast / simulation pipeline (not measured reconstruction SNR)",
                input_snr_setting="SNR_tot ≥ 20",
                frequency="0.7–2 GHz band context (DSA-2000)",
                array="DSA-2000, SKA-Mid AA*/AA4, VLASS",
            ),
            evidence=(
                "Adopted discoverability limits require SNR_tot ≥ 20 (Collett 2015; Rezaei et al. 2022). "
                "POLISH demo is qualitative only — no reconstruction SNR tabulated for the network itself."
            ),
        ),
    ],
    "2025MNRAS.543.1727L": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=30.73,
            unit="dB",
            scope="Classical-model reference, VLA low-DR; MROP matches at D/N≈1",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖u‖₂ / ‖u − ũ‖₂)",
                simulation_vs_real="Simulation (VLA/MeerKAT); real VLA 3C 273 residual check without SNR",
                input_snr_setting=None,
                frequency="X band (real 3C 273)",
                array="VLA / MeerKAT",
            ),
            evidence=(
                "Reference classical SNR: VLA low/high DR 30.73/28.50 dB; MeerKAT 30.13/27.95 dB. "
                "MROP matches classical-model SNR once D/N≈1."
            ),
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="MROP / BDA / CROP vs classical measurement model at matched data size",
            baseline="Classical visibility model (uSARA reconstructions)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array="VLA / MeerKAT",
            ),
            evidence=(
                "Classical, BDA, CROP, and MROP converge to very similar SNR at D/N≈1; "
                "dropping D/N to ~0.38 costs 0.1–1.1 dB SNR depending on source/array."
            ),
        ),
    ],
    "2025RASTI...4..25M": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            scope="U-Net / GU-Net box-plot SNR on IllustrisTNG test set and OOD 30 Doradus",
            unit="dB",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x_true‖ / ‖x_pred − x_true‖)",
                simulation_vs_real="Simulation (Gaussian uv + real MeerKAT coverage; OOD 30 Doradus)",
                input_snr_setting="ISNR = 30 dB",
                frequency=None,
                array="Gaussian random + MeerKAT coverage",
            ),
            evidence=(
                "Primary metric is L₂ SNR (box-plots Figs. 5, 8, 9). Comparisons are among U-Net/GU-Net "
                "coverage-training strategies; no numeric CLEAN SNR table in the extracted notes."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value=30,
            unit="dB (ISNR)",
            scope="Training/test observations: 32,768 measurements, ISNR 30 dB",
            empirical=True,
            execution_context=ctx(
                formula="Input SNR (ISNR)",
                simulation_vs_real="Simulation",
                input_snr_setting="30 dB",
                frequency=None,
                array="Gaussian / MeerKAT",
            ),
            evidence="Training data use input SNR (ISNR) of 30 dB.",
        ),
    ],
    "2025arXiv250721270M": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=46.03,
            unit="dB",
            scope="OOD 30 Doradus (DR~600); GU-Net RI-GAN",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x_true‖₂ / ‖x_true − x_pred‖₂)",
                simulation_vs_real="Simulation (in-distribution galaxies + OOD 30 Doradus)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "OOD 30 Doradus: GU-Net RI-GAN 46.03 dB, U-Net RI-GAN 30.80 dB, CLEAN 32.55 dB. "
                "In-distribution SNR shown as boxplots (Fig. 3)."
            ),
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="GU-Net RI-GAN vs U-Net RI-GAN, dirty image, and CLEAN",
            baseline="U-Net RI-GAN, dirty image, CLEAN",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "GU-Net improves SNR over dirty/U-Net in-distribution and beats U-Net and CLEAN by a wide "
                "margin on OOD 30 Doradus (46.03 vs 30.80 / 32.55 dB)."
            ),
        ),
    ],
    "2026AJ....171...44Y": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=36.39,
            unit="dB",
            scope="VLA/W28 Table 1 (ALSB); also SKA/3C353 and DART solar tables",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x‖₂ / ‖x − x̃‖₂)",
                simulation_vs_real="Simulation (VLA/SKA) + DART real solar data",
                input_snr_setting="iSNR=35 dB (VLA/SKA); 40 dB (DART)",
                frequency="425 MHz (DART)",
                array="VLA / SKA / DART (294 antennas)",
            ),
            evidence=(
                "ALSB best SNR: W28 36.39 dB, 3C353 33.97 dB, DART solar 33.93 dB "
                "(vs SARA/AIRI/WTF/MS-CLEAN baselines)."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value=35,
            unit="dB (iSNR; 40 dB on DART)",
            scope="Tabulated experiments and noise-robustness sweep across input SNR levels",
            empirical=True,
            execution_context=ctx(
                formula="Input SNR (iSNR)",
                simulation_vs_real="Simulation + real DART",
                input_snr_setting="35 dB (main tables); 40 dB DART; swept for robustness",
                frequency=None,
                array="VLA / SKA / DART",
            ),
            evidence="Main tables use iSNR=35 dB (40 dB DART); noise-robustness test sweeps input SNR levels.",
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="ALSB vs SARA, AIRI, WTF (and MS-CLEAN on DART)",
            baseline="SARA, AIRI, WTF, MS-CLEAN",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation + real DART",
                input_snr_setting="35–40 dB",
                frequency=None,
                array=None,
            ),
            evidence="ALSB reports the highest SNR on every tabulated test and across the input-SNR robustness sweep.",
        ),
    ],
    "2026AJ....171..220Y": [
        entry(
            "reconstruction_snr",
            "l2_reconstruction_snr",
            value=28.82,
            unit="dB (mean of 100 sims)",
            scope="VLA/3c353 Table 1 (GMCP); DART/Sun Table 2 also 32.47 dB",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖x‖₂ / ‖x − x̂‖₂)",
                simulation_vs_real="Simulation (avg. of 100)",
                input_snr_setting="iSNR=35 dB",
                frequency=None,
                array="VLA / DART",
            ),
            evidence=(
                "VLA/3c353: GMCP 28.82 dB vs R2D2 28.33, LPG 28.16, AIRI 26.84, SARA 24.38. "
                "DART/Sun: GMCP 32.47 dB (best)."
            ),
        ),
        entry(
            "input_operating_snr",
            "input_visibility_snr",
            value=35,
            unit="dB (iSNR)",
            scope="Main tables and noise-robustness sweep (Fig. 8)",
            empirical=True,
            execution_context=ctx(
                formula="Input SNR (iSNR)",
                simulation_vs_real="Simulation",
                input_snr_setting="35 dB; swept for robustness",
                frequency=None,
                array="VLA / DART",
            ),
            evidence="Tables use iSNR=35 dB; Fig. 8 sweeps input noise levels.",
        ),
        entry(
            "comparative_snr",
            "higher_lower_than_baseline",
            scope="GMCP vs SARA, AIRI, LPG, R2D2",
            baseline="SARA, AIRI, LPG, R2D2",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀ L₂ reconstruction SNR",
                simulation_vs_real="Simulation",
                input_snr_setting="35 dB",
                frequency=None,
                array=None,
            ),
            evidence=(
                "GMCP best aggregate SNR on both tables; noise-robustness sweep shows GMCP clearly beats "
                "SARA and slightly beats AIRI/LPG/R2D2 across input noise levels."
            ),
        ),
    ],
    "2026ApJS..283....9T": [
        entry(
            "reconstruction_snr",
            "frobenius_hyperspectral_snr",
            value=30.53,
            unit="dB (mean ± 1.87)",
            scope="Simulated VLA hyperspectral benchmark Table 1 (HyperAIRI)",
            empirical=True,
            execution_context=ctx(
                formula="20·log₁₀(‖X̄‖_F / ‖X̄ − X‖_F)",
                simulation_vs_real="Simulation (VLA hyperspectral)",
                input_snr_setting=None,
                frequency="Multi-channel (hyperspectral)",
                array="VLA",
            ),
            evidence=(
                "HyperAIRI mean SNR 30.53±1.87 dB vs Hyper-uSARA 29.30, AIRI 28.70, uSARA 28.32, "
                "WSClean 11.27 dB."
            ),
        ),
        entry(
            "reconstruction_snr",
            "spectral_index_snr",
            value=10.87,
            unit="dB (mean ± 3.91 sSNR)",
            scope="Spectral-index map SNR on same VLA hyperspectral benchmark",
            empirical=True,
            execution_context=ctx(
                formula="SNR between reconstructed and GT spectral-index maps",
                simulation_vs_real="Simulation (VLA hyperspectral)",
                input_snr_setting=None,
                frequency="Multi-channel",
                array="VLA",
            ),
            evidence=(
                "HyperAIRI sSNR 10.87±3.91 dB; Hyper-uSARA best sSNR 11.35±3.78; WSClean only 3.81±5.91 dB."
            ),
        ),
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value=1.8,
            unit="dB (approx. SNR gain vs AIRI)",
            scope="HyperAIRI vs monochromatic AIRI; Hyper-uSARA vs uSARA ~1 dB",
            baseline="AIRI / uSARA",
            empirical=True,
            execution_context=ctx(
                formula="Frobenius hyperspectral SNR",
                simulation_vs_real="Simulation",
                input_snr_setting=None,
                frequency="Multi-channel",
                array="VLA",
            ),
            evidence=(
                "HyperAIRI improves SNR over AIRI by ~1.8 dB; Hyper-uSARA improves over uSARA by ~1 dB. "
                "WSClean far lower (11.27 vs 30.53 dB)."
            ),
        ),
    ],
    "2026arXiv260115844M": [
        entry(
            "reconstruction_snr",
            "alternate_mse_snr",
            value=54.7,
            unit="dB (K=1000)",
            scope="DDRM Table 1 VLA; also EHT/ALMA at K=1000",
            empirical=True,
            execution_context=ctx(
                formula="10·log₁₀[(1/N)Σx⁽ʲ⁾ / MSE]",
                simulation_vs_real="Simulation (VLA / EHT / ALMA)",
                input_snr_setting=None,
                frequency=None,
                array="VLA / EHT / ALMA",
            ),
            evidence=(
                "Alternate SNR = 10·log₁₀[(1/N)Σx/MSE]. VLA K=1000: SNR 54.7 dB (PSNR 62.9); "
                "K=10 already SNR 36.8 dB. EHT/ALMA K=1000: 53.5 / 54.6 dB."
            ),
        ),
    ],
    "2026arXiv260628493D": [
        entry(
            "comparative_snr",
            "db_gain_vs_baseline",
            value=3,
            unit="dB (cited POLISH claim)",
            scope="Review citation of POLISH vs CLEAN dirty images",
            baseline="CLEAN dirty images",
            empirical=False,
            execution_context=ctx(
                formula="Cited SNR improvement (definition not re-derived in review)",
                simulation_vs_real="Secondary citation (review chapter)",
                input_snr_setting=None,
                frequency=None,
                array=None,
            ),
            evidence=(
                "Survey cites POLISH reporting a ≈3 dB SNR gain over CLEAN dirty images; "
                "no original reconstruction-SNR benchmark table in this review chapter."
            ),
        ),
    ],
}


def main() -> None:
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"] if isinstance(data, dict) else data
    snr_papers = [p for p in papers if p.get("metrics", {}).get("snr") == 1]

    missing = [p["bibcode"] for p in snr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in snr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Classifications for non-SNR papers: {extra}")

    mirror = {
        "schema_note": (
            "snr_details mirror: bibcode -> entries for inspection/tools. "
            "This script writes only this file (does not mutate papers-data.json). "
            "Top-level metrics.snr binary flags are unchanged. "
            "logSNR is a separate binary column and is not subtyped here."
        ),
        "papers": {},
    }

    for p in snr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "snr_details": details,
        }

    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    cat_papers: dict[str, set[str]] = defaultdict(set)
    sub_papers: dict[tuple[str, str], set[str]] = defaultdict(set)
    for p in snr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        seen_cats: set[str] = set()
        seen_subs: set[tuple[str, str]] = set()
        for d in details:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Wrote snr_details mirror for {len(snr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["snr"] == 1 for p in snr_papers)
    assert sum(1 for p in papers if p["metrics"].get("snr") == 1) == 23
    # Ensure papers-data.json was not written by this script's path
    print(f"Wrote {MIRROR.relative_to(ROOT)} only (papers-data.json untouched).")


if __name__ == "__main__":
    main()
