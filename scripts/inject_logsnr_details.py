#!/usr/bin/env python3
"""Inject logsnr_details mirror for logSNR-positive papers.

Run from repo root: python3 scripts/inject_logsnr_details.py

Writes data/logsnr-details.json only. Does not mutate data/papers-data.json
or top-level metrics.logsnr flags (safe for parallel metric agents).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "logsnr-details.json"


def ctx(
    transform_definition=None,
    transform_parameter=None,
    paired_with_linear_snr=None,
    simulation_vs_real=None,
    array_or_domain=None,
    frequency=None,
):
    return {
        "transform_definition": transform_definition,
        "transform_parameter": transform_parameter,
        "paired_with_linear_snr": paired_with_linear_snr,
        "simulation_vs_real": simulation_vs_real,
        "array_or_domain": array_or_domain,
        "frequency": frequency,
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


# bibcode -> list of logsnr_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- emerging-ml ---
    "2024ApJS..273....3A": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=25.0,
            unit="dB (mean ± std)",
            scope="Generic 200-problem VLA test; R2D2 / R3D3 log S/N",
            empirical=True,
            execution_context=ctx(
                transform_definition="Logarithmic image transform then L₂ S/N (R2D2-family)",
                transform_parameter="Ground-truth dynamic range",
                paired_with_linear_snr="Yes (linear S/N + log S/N)",
                simulation_vs_real="Simulation (VLA A/C; 512×512)",
                array_or_domain="VLA",
            ),
            evidence=(
                "Generic-test log S/N means: CLEAN 10.3±3.5 dB; uSARA/AIRI 21.9 dB; "
                "R2D2 ≈25.0–25.1±4.9 dB; R3D3-3L/6L ≈25.3 dB. End-to-end U-Net only 6.6±3.3 dB."
            ),
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="R2D2/R3D3 vs CLEAN, uSARA, AIRI, end-to-end U-Net",
            baseline="CLEAN / uSARA / AIRI / U-Net",
            empirical=True,
            execution_context=ctx(
                transform_definition="Logarithmic image transform parameterized by GT DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA",
            ),
            evidence=(
                "R2D2-family log S/N (~25 dB) exceeds CLEAN (~10 dB) and optimisation baselines "
                "(~22 dB); gap vs linear S/N is larger, stressing faint-structure recovery."
            ),
        ),
        entry(
            "comparative_logsnr",
            "logsnr_gain_db",
            value=15,
            unit="dB (approx. vs CLEAN)",
            scope="Generic test mean log S/N: R2D2 ≈25 vs CLEAN ≈10",
            baseline="Multiscale CLEAN",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA",
            ),
            evidence="Mean log S/N rises from CLEAN 10.3 dB to R2D2/R3D3 ≈25 dB (~15 dB gain).",
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="S/N after logarithmic image transform parameterized by known GT DR",
                transform_parameter="Ground-truth dynamic range",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA",
            ),
            evidence=(
                "Introduces faint-structure log S/N via a DR-parameterised logarithmic remapping "
                "of reconstruction and ground truth (R2D2-family template used by later papers)."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2024arXiv240317905C": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=25.10,
            unit="dB",
            scope="Fig. 2 validation sample DR=167, AF=16; R2D2-Net (NUFFT)",
            empirical=True,
            execution_context=ctx(
                transform_definition="rlog(x)=log_a(a·x+1) then SNR",
                transform_parameter="a = image Dynamic Range",
                paired_with_linear_snr="Yes (SNR, logSNR pairs)",
                simulation_vs_real="Simulation (non-Cartesian MRI)",
                array_or_domain="MRI (radial k-space; R2D2 analogue)",
            ),
            evidence=(
                "Paired (SNR, logSNR): AIRI (15.55, 18.96); U-Net (14.93, 17.88); "
                "NC-PDNet (14.40, 17.65); R2D2 (18.44, 23.15); R2D2-Net NUFFT (19.39, 25.10)."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="SNR/logSNR vs acceleration factor (spokes 10–80) and vs R2D2 iterations 1–8",
            empirical=True,
            execution_context=ctx(
                transform_definition="log_a(a·x+1) with a=DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (MRI)",
                array_or_domain="MRI non-Cartesian",
            ),
            evidence=(
                "Reports SNR/logSNR as a function of AF and DNN-series length; performance rises "
                "and converges by ~8 R2D2 networks."
            ),
        ),
        entry(
            "absolute_logsnr",
            "per_iteration_curve",
            scope="logSNR vs number of R2D2 iterations (1–8)",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (MRI)",
                array_or_domain="MRI non-Cartesian",
            ),
            evidence="SNR/logSNR reported vs iteration count; series converges with few networks vs PnP AIRI.",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="R2D2 / R2D2-Net vs AIRI, U-Net, NC-PDNet",
            baseline="AIRI / U-Net / NC-PDNet",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (MRI)",
                array_or_domain="MRI non-Cartesian",
            ),
            evidence="R2D2 and R2D2-Net (NUFFT) give the highest logSNR on the illustrated validation sample.",
        ),
        entry(
            "transform_family",
            "log_a_ax_plus_1",
            empirical=False,
            execution_context=ctx(
                transform_definition="rlog(x)=log_a(a·x+1)",
                transform_parameter="a = image Dynamic Range",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (MRI)",
                array_or_domain="MRI non-Cartesian",
            ),
            evidence="Log map uses DR as base parameter a before SNR; analogue of radio high-DR logSNR.",
        ),
    ],
    "2024arXiv240318052A": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=30,
            unit="dB (approx. final)",
            scope="Simulated test set Fig. 2 (center); final R2D2",
            empirical=True,
            execution_context=ctx(
                transform_definition="r_log(x)=x_max·log_a(a/x_max·x+1) then SNR",
                transform_parameter="a (reversible log map; DR-style)",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (+ 3C 353 case study)",
                array_or_domain="Radio RI (R2D2 UQ paper)",
            ),
            evidence="Simulated test: R2D2 final ~30 dB logSNR vs CLEAN 19.2 dB and uSARA 10.2 dB.",
        ),
        entry(
            "absolute_logsnr",
            "per_iteration_curve",
            value=35.3,
            unit="dB (final)",
            scope="3C 353 case study: iteration 1 → final",
            empirical=True,
            execution_context=ctx(
                transform_definition="Reversible r_log then SNR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulated case study (3C 353)",
                array_or_domain="Radio RI",
            ),
            evidence="Case study logSNR rises from 29.2 dB (iteration 1) to 35.3 dB (final iteration).",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="R2D2 vs CLEAN, U-Net, uSARA, AIRI (qualitative + numeric)",
            baseline="CLEAN / uSARA / U-Net",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "Claims superior image estimation vs CLEAN, U-Net, uSARA, and AIRI, combining "
                "higher SNR/logSNR with lower compute and low epistemic uncertainty."
            ),
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="Eq. 7–8 reversible r_log then SNR",
                transform_parameter="a in r_log",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence="Defines logSNR via reversible log-transformed images (Eq. 7–8) for faint HDR structure.",
        ),
    ],
    "2025A&A...704A..43Y": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=21.97,
            unit="dB",
            scope="Messier 106 SKA 512×512; input S/N=35 dB; ISCAD",
            empirical=True,
            execution_context=ctx(
                transform_definition="S/N_log via log₁₀(x/ε + I_N) stretch",
                transform_parameter="ε noise floor",
                paired_with_linear_snr="Yes (S/N and S/N_log)",
                simulation_vs_real="Simulation",
                array_or_domain="SKA-like (Messier 106 test)",
            ),
            evidence=(
                "At input S/N=35 dB: SARA 20.14; AIRI 21.23; LPG 21.75; ISCAD 21.97 dB S/N_log "
                "(highest of the four; also best on other test cases)."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="S/N_log vs input S/N 15–55 dB (100 MC realisations)",
            empirical=True,
            execution_context=ctx(
                transform_definition="log₁₀ stretch with ε",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="SKA-like / RI simulations",
            ),
            evidence="Noise-robustness curves: ISCAD stays highest in S/N and S/N_log across the sweep.",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="ISCAD vs SARA, AIRI, LPG",
            baseline="SARA / AIRI / LPG",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="RI simulations",
            ),
            evidence="ISCAD attains the highest S/N_log on all three reported test cases.",
        ),
        entry(
            "transform_family",
            "log10_stretch_epsilon",
            empirical=False,
            execution_context=ctx(
                transform_definition="S/N_log = 20·log₁₀(‖log₁₀(x/ε+I_N)‖₂ / ‖…error…‖₂)",
                transform_parameter="ε",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="RI simulations",
            ),
            evidence="Explicit log₁₀ stretch with noise floor ε for dynamic-range / faint-structure fidelity.",
        ),
    ],
    "2025ApJS..280...63A": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=24.6,
            unit="dB (mean ± std)",
            scope="Table 4 setup E2; R2D2_A2,T2 best model",
            empirical=True,
            execution_context=ctx(
                transform_definition="r_log(x)=x_max·log_a(a/x_max·x+1)",
                transform_parameter="a = target dynamic range",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (fully-randomized E2)",
                array_or_domain="Radio RI (robust R2D2)",
            ),
            evidence=(
                "E2: CLEAN 9.4±18.9; uSARA 20.4±3.4; AIRI 21.1±3.8; U-Net/U-WDSR ~6.6–6.8; "
                "R2D2_A2,T2 24.6±4.2 dB logSNR."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="Briggs weighting ρ_br sweep; logSNR peaks at natural weighting",
            empirical=True,
            execution_context=ctx(
                transform_definition="R2D2 r_log",
                transform_parameter="a = target DR",
                paired_with_linear_snr="Yes (SNR peaks at ρ_br=0; logSNR at ρ_br=1)",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "R2D2_A2,T2 peaks in logSNR at ρ_br=1 (natural weighting) while linear SNR peaks "
                "at ρ_br=0."
            ),
        ),
        entry(
            "comparative_logsnr",
            "logsnr_gain_db",
            value=3,
            unit="dB (approx. vs AIRI/uSARA)",
            scope="Table 4 E2: R2D2_A2,T2 vs uSARA/AIRI",
            baseline="uSARA / AIRI",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence="R2D2 models outperform uSARA/AIRI by roughly 2–4 dB in both SNR and logSNR.",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="Architecture ablation A1,T1 vs A2,T2; vs CLEAN/U-Net",
            baseline="R2D2_A1,T1 / CLEAN / end-to-end U-Net",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "Old stack collapses to logSNR 12.4±12.2 dB; new A2,T2 reaches 24.6±4.2 dB; "
                "CLEAN/U-Net far lower."
            ),
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="Per-image r_log with target DR a",
                transform_parameter="a = target dynamic range",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence="Standard R2D2 reversible log map before SNR for faint-structure sensitivity.",
        ),
    ],
    "2025MNRAS.537.1608T": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=26.29,
            unit="dB",
            scope="ΔT=8h example: cAIRI-OAID (SNR, logSNR)",
            empirical=True,
            execution_context=ctx(
                transform_definition="logSNR=SNR(rlog_a(·), rlog_a(·))",
                transform_parameter="a = 2.5×10³ (lowest DR in test set)",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI (AIRI robustness)",
            ),
            evidence=(
                "At ΔT=8h: MS-CLEAN (5.45, 7.07); SARA (27.74, 25.16); cAIRI-OAID (28.65, 26.29) dB. "
                "AIRI/cAIRI improve 1–2 dB over uSARA/SARA across observation times."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="Observation time ΔT ∈ {1h, 2h, 4h, 8h}; training-realisation spread",
            empirical=True,
            execution_context=ctx(
                transform_definition="rlog_a with fixed a",
                transform_parameter="a = 2.5×10³",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "SNR/logSNR vs ΔT; across K=15 denoisers logSNR varies ~4 dB vs ~1.5 dB for linear SNR."
            ),
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="AIRI/cAIRI vs MS-CLEAN, SARA/uSARA; MRID vs OAID training",
            baseline="MS-CLEAN / SARA / uSARA",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "AIRI-family dramatically outperforms CLEAN (>20 dB) and modestly beats SARA/uSARA; "
                "MRI-trained denoisers match OAID on SNR/logSNR."
            ),
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="rlog_a(x)=x_max·log_a(a·x/x_max+1)",
                transform_parameter="a = 2.5×10³ (lowest DR; cross-method consistency)",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence="Fixes a to lowest test-set DR so logSNR comparisons stay consistent across methods.",
        ),
    ],
    "2025MNRAS.542..426T": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=18.7,
            unit="dB (mean ± std)",
            scope="Table 1; S-R2D2 at Np=600² (best logSNR)",
            empirical=True,
            execution_context=ctx(
                transform_definition="rlog(x,a)=x_max·log_a(a·x/x_max+1)",
                transform_parameter="a = target DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (spherical wide-field)",
                array_or_domain="Spherical RI (S-R2D2)",
            ),
            evidence=(
                "S-R2D2 logSNR 17.5±3.2 (400²) → 18.7±2.9 (600² peak) → 15.9±3.5 (800²); "
                "planar R2D2 collapses 7.3→1.6 dB as Np grows."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="logSNR vs spherical pixel count Np / super-resolution",
            empirical=True,
            execution_context=ctx(
                transform_definition="R2D2 rlog with a=DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Spherical RI",
            ),
            evidence="Best S-R2D2 logSNR at Np=600² (SR=2.25); planar R2D2 degrades sharply with resolution.",
        ),
        entry(
            "absolute_logsnr",
            "per_iteration_curve",
            scope="Per-iteration metrics to I=10 (logSNR plateau beyond)",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Spherical RI",
            ),
            evidence="Fixed I=10 because logSNR stopped improving beyond that on validation data.",
        ),
        entry(
            "comparative_logsnr",
            "logsnr_gain_db",
            value=14,
            unit="dB (approx. range 10–17)",
            scope="S-R2D2 vs planar R2D2 at matched Np",
            baseline="Planar R2D2",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Spherical RI",
            ),
            evidence="S-R2D2 outperforms planar R2D2 by roughly 10–17 dB in logSNR at matched resolutions.",
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="rlog with a fixed to target DR",
                transform_parameter="a = target DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Spherical RI",
            ),
            evidence="Same R2D2-family reversible log map; emphasises faint structure on the sphere.",
        ),
    ],
    "2025MNRAS.543.1727L": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=20.90,
            unit="dB",
            scope="Classical-model reference: VLA low-DR (SNR, logSNR)=(30.73, 20.90)",
            empirical=True,
            execution_context=ctx(
                transform_definition="rlog mapping using image dynamic range d",
                transform_parameter="d = image DR (10³–10⁵)",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / MeerKAT",
            ),
            evidence=(
                "Reference pairs: VLA low/high DR (20.90 / 20.15); MeerKAT low/high (22.08 / 19.84) dB logSNR. "
                "MROP matches classical/BDA/CROP quality once D/N≈1."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="logSNR vs data size D/N below ≈1",
            empirical=True,
            execution_context=ctx(
                transform_definition="rlog with DR d",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / MeerKAT",
            ),
            evidence=(
                "Abell 2034 (VLA): D/N drop costs 0.1 dB SNR / 0.7 dB logSNR; "
                "3c353 (MeerKAT): 1.1 / 2.2 dB — logSNR degrades faster than linear SNR."
            ),
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="MROP vs classical / BDA / CROP / plain subsampling",
            baseline="Classical full model / plain subsampling",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / MeerKAT",
            ),
            evidence=(
                "MROP converges to similar SNR/logSNR as classical once D/N≈1; plain subsampling "
                "is markedly worse at equal data size."
            ),
        ),
        entry(
            "comparative_logsnr",
            "logsnr_gain_db",
            value=-0.7,
            unit="dB (loss vs D/N≈1)",
            scope="Abell 2034 VLA; D/N from ~1 to 3.8×10⁻¹",
            baseline="D/N ≈ 1 classical-quality operating point",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA",
            ),
            evidence="Same D/N drop costs 0.7 dB logSNR vs only 0.1 dB linear SNR.",
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="rlog using image dynamic range d",
                transform_parameter="d = image DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / MeerKAT",
            ),
            evidence="LogSNR via DR-parameterised logarithmic remapping for high-DR compressive RI tests.",
        ),
    ],
    "2025RASTI...4..25M": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            scope="Box-plots of SNR/logSNR (Figs. 5, 8, 9); U-Net vs GU-Net coverage strategies",
            empirical=True,
            execution_context=ctx(
                transform_definition="SNR(log₁₀(x_true), log₁₀(x_pred))",
                transform_parameter="None (plain log₁₀)",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation (+ high-DR 30 Doradus qualitative)",
                array_or_domain="Radio RI (varying uv-coverage)",
            ),
            evidence=(
                "logSNR used in box-plots rather than in-text scalar tables; primary faint-region "
                "fidelity metric alongside linear SNR."
            ),
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="GU-Net vs U-Net under coverage-training strategies",
            baseline="Decoupled U-Net post-processing",
            empirical=True,
            execution_context=ctx(
                transform_definition="Plain log₁₀ SNR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence=(
                "Comparisons are between U-Net and GU-Net variants (no numeric CLEAN logSNR in text); "
                "measurement-operator-aware GU-Net generalises better across uv-coverage."
            ),
        ),
        entry(
            "transform_family",
            "plain_log10",
            empirical=False,
            execution_context=ctx(
                transform_definition="logSNR = SNR(log₁₀(x_true), log₁₀(x_pred))",
                transform_parameter="None",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="Radio RI",
            ),
            evidence="Simpler plain log₁₀ on truth and prediction — no DR-parameterised reversible map.",
        ),
    ],
    "2026AJ....171..220Y": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            value=16.19,
            unit="dB",
            scope="VLA/3C353 Table 1; GMCP avg of 100 sims, iSNR=35 dB",
            empirical=True,
            execution_context=ctx(
                transform_definition="SNRlog on log-stretched image (Thouvenin et al. 2023)",
                transform_parameter="ε noise level + I_N",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA (3C353) / DART Sun",
            ),
            evidence=(
                "VLA/3C353 SNRlog: SARA 8.06; AIRI 14.12; LPG 14.95; R2D2 15.36; GMCP 16.19 dB. "
                "DART/Sun: GMCP 14.16 best (R2D2 not tested)."
            ),
        ),
        entry(
            "absolute_logsnr",
            "parameter_sweep_logsnr",
            scope="Noise-robustness and γ/λ ablations (Figs. 5–8)",
            empirical=True,
            execution_context=ctx(
                transform_definition="SNRlog log-stretch",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / DART",
            ),
            evidence="Adaptive λ raises SNR/SNRlog vs fixed λ; GMCP leads across input-noise sweeps.",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="GMCP vs R2D2/AIRI/LPG/SARA (aggregate) with morphology caveat",
            baseline="R2D2 / AIRI / LPG / SARA",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA",
            ),
            evidence=(
                "GMCP leads aggregate SNRlog, but qualitative comparison notes R2D2 better preserves "
                "diffuse emission despite lower log-scale scores on some features."
            ),
        ),
        entry(
            "transform_family",
            "log10_stretch_epsilon",
            empirical=False,
            execution_context=ctx(
                transform_definition="SNRlog following Thouvenin et al. (log-stretch + ε)",
                transform_parameter="ε estimated noise level",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA / DART",
            ),
            evidence="Log-scale SNR variant for faint emission; same family as ISCAD S/N_log.",
        ),
    ],
    "2026ApJS..283....9T": [
        entry(
            "absolute_logsnr",
            "tabulated_mean_db",
            scope="Table 1 simulated VLA hyperspectral benchmark (mean ± std logSNR)",
            empirical=True,
            execution_context=ctx(
                transform_definition="r_log(X)=max(X)·log_a(a·X/max(X)+1)",
                transform_parameter="a = target dynamic range",
                paired_with_linear_snr="Yes (+ sSNR)",
                simulation_vs_real="Simulation",
                array_or_domain="VLA hyperspectral",
                frequency="Multi-channel / hyperspectral",
            ),
            evidence=(
                "Reports mean±std logSNR for WSClean, uSARA, AIRI, Hyper-uSARA, HyperAIRI, etc. "
                "alongside SNR, RDR, sSNR."
            ),
        ),
        entry(
            "comparative_logsnr",
            "logsnr_gain_db",
            value=2.4,
            unit="dB (approx.)",
            scope="HyperAIRI vs monochromatic AIRI",
            baseline="AIRI (monochromatic)",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA hyperspectral",
                frequency="Multi-channel",
            ),
            evidence="HyperAIRI improves logSNR over AIRI by ~2.4 dB (and SNR by ~1.8 dB).",
        ),
        entry(
            "comparative_logsnr",
            "higher_lower_than_baseline",
            scope="Hyperspectral vs monochromatic counterparts; vs WSClean",
            baseline="AIRI / uSARA / WSClean",
            empirical=True,
            execution_context=ctx(
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA hyperspectral",
            ),
            evidence="Power-law-coupled hyperspectral methods consistently beat monochromatic counterparts on logSNR.",
        ),
        entry(
            "transform_family",
            "r2d2_reversible_rlog",
            empirical=False,
            execution_context=ctx(
                transform_definition="Per-image/channel r_log with target DR a",
                transform_parameter="a = target DR",
                paired_with_linear_snr="Yes",
                simulation_vs_real="Simulation",
                array_or_domain="VLA hyperspectral",
                frequency="Multi-channel",
            ),
            evidence="Standard R2D2-family reversible log map applied for faint structure across channels.",
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    logsnr_papers = [p for p in papers if p["metrics"].get("logsnr") == 1]
    missing = [p["bibcode"] for p in logsnr_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in logsnr_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not logsnr=1: {extra}")

    mirror = {
        "schema_note": (
            "logsnr_details mirror: bibcode -> entries for inspection/tools. "
            "This script does not mutate data/papers-data.json. "
            "Top-level metrics.logsnr binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in logsnr_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "logsnr_details": details,
        }

    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in logsnr_papers:
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

    print(f"Wrote logsnr_details mirror for {len(logsnr_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["logsnr"] == 1 for p in logsnr_papers)
    assert len(logsnr_papers) == 11
    print(f"Wrote {MIRROR.relative_to(ROOT)} only (papers-data.json untouched)")


if __name__ == "__main__":
    main()
