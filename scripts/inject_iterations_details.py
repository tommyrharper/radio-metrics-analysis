#!/usr/bin/env python3
"""Inject iterations_details into data/papers-data.json for Iterations-positive papers.

Run from repo root: python3 scripts/inject_iterations_details.py
Does not change top-level metrics.iterations flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "iterations-details.json"


def ctx(
    stopping_criterion=None,
    convergence_threshold=None,
    maximum_iterations=None,
    optimiser=None,
    learning_rate=None,
    batch_size=None,
    initialisation_method=None,
    regularisation_parameters=None,
):
    return {
        "stopping_criterion": stopping_criterion,
        "convergence_threshold": convergence_threshold,
        "maximum_iterations": maximum_iterations,
        "optimiser": optimiser,
        "learning_rate": learning_rate,
        "batch_size": batch_size,
        "initialisation_method": initialisation_method,
        "regularisation_parameters": regularisation_parameters,
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


# bibcode -> list of iterations_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "1974A&AS...15..417H": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=6,
            unit="CLEAN iterations",
            scope="Green Bank 3C 244.1 qualitative CLEAN study",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Stop when next residual peak is no longer significant relative to map noise",
                regularisation_parameters="Loop gain 1",
            ),
            evidence="Figure 3 compares dirty and cleaned maps after 1, 2, and 6 CLEAN iterations (gain 1). Reported algorithmic cycle counts, not wall-clock.",
        ),
    ],
    "1980A&A....89..377C": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=None,
            unit=None,
            scope="Clark CLEAN major-cycle structure and stopping",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Major-cycle ends minor iteration N when map max falls below S_limit",
                regularisation_parameters="Gain-dependent minor-cycle limit (e.g. ~250 at gain 0.5)",
            ),
            evidence="Describes major cycles that batch approximate minor-cycle components then correct in the Fourier domain; empirical major/minor stopping behaviour.",
        ),
        entry(
            "iteration_count",
            "inner_iterations",
            value=250,
            unit="components per major cycle (approx.)",
            scope="Minor-cycle component counts vs gain",
            empirical=True,
            execution_context=ctx(
                regularisation_parameters="Typically ~250 components at gain 0.5; first major cycle often 5–6",
            ),
            evidence="First major cycle usually removes ~5–6 components, increasing toward a map- and gain-dependent limit (~250 at gain 0.5).",
        ),
    ],
    "1984A&A...137..159S": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=17,
            unit="modified CLEAN iterations",
            scope="Noise-free 64×64 synthetic test",
            empirical=True,
            execution_context=ctx(
                regularisation_parameters="Modified CLEAN Tc=0.55; comparison CLEAN 15% central beam spike",
            ),
            evidence="Modified CLEAN uses 17 iterations vs standard CLEAN 2,000 subtractions on the same 64×64 test.",
        ),
        entry(
            "comparative_iteration",
            "iteration_ratio",
            value=None,
            unit=None,
            scope="Modified vs standard CLEAN iteration counts",
            baseline="standard CLEAN (2,000 subtractions)",
            empirical=True,
            execution_context=ctx(),
            evidence="17 modified-CLEAN iterations versus 2,000 standard CLEAN subtractions on the noise-free test — large iteration-count ratio.",
        ),
        entry(
            "iteration_scaling",
            "image_size",
            value=None,
            unit=None,
            scope="Analytic work vs iteration count and image size M",
            empirical=False,
            execution_context=ctx(),
            evidence="Work estimates Ns≈2QsM and Nm≈QmM(4log(M)/2+4) couple iteration counts Q to image size M (and Clark major/minor counts).",
        ),
    ],
    "1988A&A...200..312W": [
        entry(
            "iteration_count",
            "inner_iterations",
            value=None,
            unit="search-mask iterations",
            scope="MRC search-mask iteration range in cost model",
            empirical=False,
            execution_context=ctx(
                regularisation_parameters="Typical f=2–4; 3–6 search-mask iterations",
            ),
            evidence="Cost model assumes 3–6 search-mask iterations (with decimation factor f=2–4). Iteration counts enter the work estimate; MRC/CLEAN op ratios are Compute, not Iterations.",
        ),
    ],
    "2004A&A...426..747B": [
        entry(
            "convergence_behaviour",
            "stable_solution_achieved",
            value=None,
            unit=None,
            scope="Asp-Clean residual/active-set vs iteration plots",
            empirical=True,
            execution_context=ctx(
                convergence_threshold="Components dropped below L0=λΣIR",
                regularisation_parameters="User λ trades sparsity vs residual",
            ),
            evidence="Figures track Asp width, active Aspen count, and residual area vs iteration; large components stabilize and leave the active set. Qualitative convergence behaviour without a numeric iterations-to-solution table.",
        ),
    ],
    "2008ISTSP...2..647C": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=20000,
            unit="CLEAN iterations",
            scope="Fixed CLEAN budget for all w-projection DR benchmarks",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="20,000 CLEAN iterations",
                regularisation_parameters="Loop gain 0.1",
            ),
            evidence="Every image CLEANed for 20,000 iterations (gain 0.1) on 1536×1536. Fixed iteration budget, not wall-clock.",
        ),
    ],
    "2008ISTSP...2..793C": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=1000,
            unit="multiscale CLEAN iterations",
            scope="NGC 1058 VLA D-config channel",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Stopping threshold 4σ",
                regularisation_parameters="Loop gain 1.0; scales 0–24 px",
            ),
            evidence="Multiscale CLEAN used 1,000 iterations on NGC 1058 real data.",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=5000,
            unit="iterations",
            scope="M31 simulation multiscale CLEAN",
            empirical=True,
            execution_context=ctx(),
            evidence="Multiscale CLEAN converged in 5,000 iterations on the M31 simulation.",
        ),
        entry(
            "convergence_behaviour",
            "divergence_failure",
            value=300000,
            unit="components",
            scope="Clark CLEAN on M31 simulation",
            baseline="Multiscale CLEAN (converged)",
            empirical=True,
            execution_context=ctx(),
            evidence="Clark CLEAN diverged beyond ~300,000 components while still ~7% low in flux vs truth.",
        ),
    ],
    "2011A&A...532A..71R": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=10,
            unit="iterations (max)",
            scope="Taylor-order EVLA point-source numerical tests",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="At most ten iterations",
                convergence_threshold="1 μJy stopping threshold",
                regularisation_parameters="Loop gain 1",
            ),
            evidence="Noise-free EVLA simulations used at most ten iterations (gain 1, 1 μJy stop).",
        ),
    ],
    "2014MNRAS.444..606O": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=5,
            unit="major iterations",
            scope="WSClean accuracy-test and cross-array projections",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="Five major iterations in Table 3 / projections",
            ),
            evidence="Accuracy tests and SKA-era projections fix five major iterations (Cotton–Schwab outer loops).",
        ),
    ],
    "2017MNRAS.471..301O": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=3,
            unit="major cycles",
            scope="WSClean single-frequency minor-loop speed test",
            empirical=True,
            execution_context=ctx(),
            evidence="WSClean three major cycles perform 142, 2409, and 97,449 minor iterations on 2048² multi-scale CLEAN.",
        ),
        entry(
            "iteration_count",
            "inner_iterations",
            value=100000,
            unit="minor iterations",
            scope="Minor-loop throughput benchmarks vs CASA",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="100,000 minor iterations in speed tests",
            ),
            evidence="Benchmarks quote 10k–100k minor iterations and iterations/s (throughput is Runtime; the iteration counts are Iterations).",
        ),
    ],
    "2018A&A...611A..87T": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=5,
            unit="HMP major cycles",
            scope="3C147 faceted L-band imaging",
            empirical=True,
            execution_context=ctx(
                convergence_threshold="Clean to 0.4 mJy",
            ),
            evidence="Five HMP major cycles clean the 5100×5100 / 529-facet 3C147 image to 0.4 mJy.",
        ),
    ],
    "2018A&A...616A..27V": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=4,
            unit="major cycles",
            scope="LOFAR observed-data IDG scaling run",
            empirical=True,
            execution_context=ctx(
                convergence_threshold="100 mJy cleaning threshold",
            ),
            evidence="LOFAR job with Briggs robust 0 requires four major cycles (~20 min each) to the 100 mJy threshold.",
        ),
    ],
    # --- emerging-ml ---
    "2022A&A...664A.134S": [
        entry(
            "iteration_count",
            "epochs",
            value=300,
            unit="epochs",
            scope="Radionets CNN training",
            empirical=True,
            execution_context=ctx(
                optimiser="ADAM",
                learning_rate="2×10⁻⁴",
                batch_size="64",
                maximum_iterations="300 epochs",
            ),
            evidence="Training uses ADAM for 300 epochs (batch 64, lr 2e-4); ~170 s/epoch.",
        ),
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=50000,
            unit="CLEAN iterations",
            scope="CLEAN baseline imaging setup for 10,000 sources",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="50,000 CLEAN iterations",
                regularisation_parameters="Major-cycle gain 0.3; gain 0.005",
            ),
            evidence="CLEAN comparison path uses 50,000 iterations (major-cycle gain 0.3, gain 0.005) on 64-pixel maps.",
        ),
    ],
    "2022ApJ...939L...4D": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="AIRI/uSARA described as iterative PnP without reported iteration counts",
            empirical=False,
            execution_context=ctx(
                optimiser="Forward-backward / plug-and-play iterations",
            ),
            evidence="Method uses forward-backward PnP iterations, but this paper does not report countable iteration totals, epochs, or convergence iteration results. Left Unspecified.",
        ),
    ],
    "2023ApJ...943..144M": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="PRIMO MCMC inference without imaging-iteration counts",
            empirical=False,
            execution_context=ctx(
                optimiser="MARCH MCMC",
            ),
            evidence="PRIMO fits PCA coefficients via MCMC and contrasts with CLEAN minor cycles conceptually, but reports no imaging iteration counts or epochs-to-solution. Left Unspecified.",
        ),
    ],
    "2023MNRAS.522.5558W": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="uSARA ASKAP imaging; max CLEAN iters only as config",
            empirical=False,
            execution_context=ctx(
                maximum_iterations="WSClean at most 1,000,000 iterations",
                stopping_criterion="WSClean stop at residual standard deviation; auto-mask 2.5× residual σ",
                regularisation_parameters="WSClean loop gain 0.8; uSARA step 1.98/L; ASKAP λ scaled to 0.7–0.8 of heuristic",
                optimiser="Forward-backward iterations with iterative reweighting",
            ),
            evidence="uSARA is iterative and WSClean is capped at 1e6 iterations, but the paper does not report achieved iteration counts or convergence-iteration results. Stopping/max-iter config only → Unspecified (context captured separately).",
        ),
    ],
    "2024ApJS..273....3A": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=9,
            unit="CLEAN major cycles (mean)",
            scope="Generic R2D2 benchmark Table 2",
            empirical=True,
            execution_context=ctx(),
            evidence="CLEAN averages 9±1 major cycles on the generic test set.",
        ),
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=5000,
            unit="iterations",
            scope="uSARA / AIRI vs R2D2-family on generic tests",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="AIRI often fixed at 5000",
            ),
            evidence="uSARA 1103±373 iterations; AIRI 5000 fixed; contrasts with short R2D2 series lengths.",
        ),
        entry(
            "iteration_count",
            "inference_iterations",
            value=15,
            unit="R2D2 series iterations (training/inference setup)",
            scope="R2D2 / R3D3 series length",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="Plain R2D2 trained for 15 outer iterations; R3D3 7–8",
            ),
            evidence="R2D2 trains ~15 outer residual-series iterations (R3D3 variants 7–8); inference series length fixed during training.",
        ),
        entry(
            "iteration_count",
            "training_iterations",
            value=15,
            unit="outer training series slots",
            scope="Sequential per-iteration DNN training",
            empirical=True,
            execution_context=ctx(),
            evidence="Experiments train plain R2D2 for 15 outer iterations and R3D3 for 7–8 — training-series depth distinct from single-pass U-Net.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="R2D2 O(10) series vs uSARA/AIRI O(10³)",
            baseline="uSARA / AIRI iteration counts",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2-family needs far fewer iterations than uSARA (~1100) and AIRI (5000) while matching morphology.",
        ),
    ],
    # --- r2d2-citing ---
    "2024A&A...690A.387R": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=28,
            unit="major cycles",
            scope="MeerKAT ESO 137-006 scalability run",
            empirical=True,
            execution_context=ctx(),
            evidence="fast-resolve completes MeerKAT case over 25–28 major cycles (CLEAN-style outer loops).",
        ),
        entry(
            "convergence_behaviour",
            "convergence_rate",
            value=None,
            unit=None,
            scope="Mean-squared log-brightness residual between successive iterations",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Successive-iteration mean-squared residual in log-brightness (Fig. 5)",
            ),
            evidence="Convergence diagnostic tracks mean-squared residual between successive iterations over wall-clock/hardware — convergence behaviour, not Runtime.",
        ),
    ],
    "2024ApJ...966L..34D": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=1783,
            unit="iterations",
            scope="Cygnus A head-to-head iteration table",
            empirical=True,
            execution_context=ctx(),
            evidence="Reported iterations: Hö-CLEAN 1; CS-CLEAN 7; MS-CLEAN 9; R2D2 15; R3D3 8; R2D2-Net 1; uSARA 477; AIRI 1783.",
        ),
        entry(
            "iteration_count",
            "inference_iterations",
            value=15,
            unit="series iterations",
            scope="R2D2 / R3D3 / R2D2-Net on Cygnus A",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 15 series iterations; R3D3 8; R2D2-Net single unrolled iteration.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="R2D2-family vs uSARA/AIRI iteration counts",
            baseline="uSARA 477 / AIRI 1783",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2-Net needs only 1 iteration and R3D3 8 vs hundreds/thousands for uSARA/AIRI.",
        ),
        entry(
            "comparative_iteration",
            "iteration_ratio",
            value=None,
            unit=None,
            scope="Cross-method iteration table on Cygnus A",
            baseline="CLEAN-family and PnP baselines",
            empirical=True,
            execution_context=ctx(),
            evidence="Direct iteration-count comparison across CLEAN variants, R2D2-family, uSARA, and AIRI.",
        ),
    ],
    "2024RASTI...3..505L": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=11000000,
            unit="measurement-operator evaluations",
            scope="W28 UQ Table 5 operator-evaluation counts",
            empirical=True,
            execution_context=ctx(
                optimiser="FISTA MAP; SK-ROCK MCMC for UQ baseline",
            ),
            evidence="Reports measurement-operator evaluation counts as iteration-like work: MCMC 11×10⁶; LCIs 21k–81k; fast pixel UQ 28.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="Fast pixel UQ vs MCMC/LCI operator evaluations",
            baseline="MCMC sampling operator evaluations",
            empirical=True,
            execution_context=ctx(),
            evidence="Fast pixel UQ uses 3–6 orders of magnitude fewer likelihood/operator evaluations than LCIs and MCMC.",
        ),
        entry(
            "comparative_iteration",
            "iteration_ratio",
            value=None,
            unit=None,
            scope="Orders-of-magnitude fewer operator evaluations",
            baseline="MCMC / LCI evaluation counts",
            empirical=True,
            execution_context=ctx(),
            evidence="Headline claim: fast UQ uses orders of magnitude fewer operator evaluations than MCMC-based UQ.",
        ),
    ],
    "2024arXiv240317905C": [
        entry(
            "iteration_count",
            "inference_iterations",
            value=8,
            unit="R2D2 series iterations",
            scope="NC-MRI R2D2 SNR vs series length",
            empirical=True,
            execution_context=ctx(),
            evidence="SNR/logSNR vs R2D2 iterations (1–8); R2D2 needs ~8 networks. U-Net/R2D2-Net reported as 1 iteration.",
        ),
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=616,
            unit="AIRI PnP iterations",
            scope="Table II iteration counts vs learned methods",
            empirical=True,
            execution_context=ctx(),
            evidence="AIRI 616±138 PnP iterations vs U-Net/R2D2-Net 1 and short R2D2 series.",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=8,
            unit="series iterations",
            scope="Performance rises and plateaus vs series length",
            empirical=True,
            execution_context=ctx(),
            evidence="SNR/logSNR rises with series length and converges by ~8 R2D2 iterations.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="R2D2 ~8 vs AIRI ~616",
            baseline="AIRI PnP iteration count",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 needs only ~8 networks versus AIRI's hundreds of PnP iterations.",
        ),
    ],
    "2024arXiv240318052A": [
        entry(
            "iteration_count",
            "inference_iterations",
            value=12,
            unit="R2D2 series iterations",
            scope="Simulated test + 3C 353 case study",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 12 iterations (2.0±0.4 s); U-Net baseline is iteration 1 of the series.",
        ),
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=4995,
            unit="iterations",
            scope="Table I CLEAN / AIRI / uSARA iteration counts",
            empirical=True,
            execution_context=ctx(),
            evidence="CLEAN 8±1; AIRI 4995±50; uSARA 1107±377 iterations alongside R2D2's 12.",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=12,
            unit="series iterations",
            scope="SNR/logSNR progression across R2D2 series",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 converges to ~33 dB SNR by final iteration i=12 (from ~28 dB at iteration 1).",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="R2D2 12 vs AIRI/uSARA thousands",
            baseline="AIRI / uSARA",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 uses orders of magnitude fewer iterations than AIRI (~5000) and uSARA (~1100).",
        ),
    ],
    "2025A&A...698A.176M": [
        entry(
            "iteration_count",
            "inner_iterations",
            value=None,
            unit="subminor / minor-cycle iterations",
            scope="Autocorr-CLEAN residual vs (sub)minor iterations",
            empirical=True,
            execution_context=ctx(),
            evidence="Fig. 4: residual vs subminor-cycle iterations with l ≪ k ≪ m (subminor loops ≪ basis components ≪ classical CLEAN iterations).",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="Autocorr-CLEAN vs classical CLEAN / Asp-CLEAN",
            baseline="classical CLEAN minor-cycle iterations",
            empirical=True,
            execution_context=ctx(),
            evidence="Autocorr-CLEAN needs substantially fewer (sub)minor iterations than classical CLEAN to reach a given residual.",
        ),
        entry(
            "iteration_scaling",
            "image_size",
            value=None,
            unit=None,
            scope="Complexity model m·N·(8l/k)",
            empirical=False,
            execution_context=ctx(),
            evidence="Derived scaling m·N·(8l/k) couples total CLEAN iterations m and pixel count N to argue against super-linear growth vs CLEAN.",
        ),
        entry(
            "iteration_scaling",
            "algorithm_parameters",
            value=None,
            unit=None,
            scope="Dependence on l, k relative to m",
            empirical=False,
            execution_context=ctx(),
            evidence="Iteration relation l ≪ k ≪ m ties subminor loops and autocorrelation basis size to classical CLEAN iteration count.",
        ),
    ],
    "2025A&A...704A..43Y": [
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=None,
            unit=None,
            scope="ISCAD vs SARA/AIRI/LPG iteration counts with SNR/runtime",
            empirical=True,
            execution_context=ctx(),
            evidence="Iteration count reported alongside S/N and runtime for SARA/AIRI/LPG/ISCAD on Messier 106 and other cases.",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=None,
            unit=None,
            scope="ISCAD converges in fewer iterations than LPG",
            empirical=True,
            execution_context=ctx(),
            evidence="ISCAD converges in fewer iterations than LPG while attaining higher S/N / S/N_log.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="ISCAD vs LPG iteration counts",
            baseline="LPG",
            empirical=True,
            execution_context=ctx(),
            evidence="Explicit fewer-iterations claim vs LPG (with matched fidelity/runtime tables).",
        ),
    ],
    "2025ApJS..280...63A": [
        entry(
            "iteration_count",
            "inference_iterations",
            value=15.8,
            unit="series iterations (mean)",
            scope="Robust R2D2 Table 4 setup E2",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Data-fidelity-based series convergence criterion on residual dirty image",
            ),
            evidence="R2D2_A2,T2 needs 15.8±5.5 series iterations; R2D2_A1,T2 18.3±5.6; vs AIRI 5000 and uSARA ~1482.",
        ),
        entry(
            "iteration_count",
            "training_iterations",
            value=25,
            unit="training series iterations",
            scope="Table 2 full R2D2 series training",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="25 training-series iterations",
            ),
            evidence="Full R2D2 series training uses 25 iterations (U-Net / U-WDSR); distinct from adaptive inference length.",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=15,
            unit="series iterations",
            scope="Cygnus A real-data convergence",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Series halts once residual dirty image compatible with noise",
            ),
            evidence="Cygnus A iteration counts to convergence: 12 / 16 / 15 for R2D2_A1,T1 / A1,T2 / A2,T2.",
        ),
        entry(
            "convergence_behaviour",
            "early_stopping",
            value=None,
            unit=None,
            scope="Adaptive series halt vs fixed AIRI budget",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Data-fidelity residual dirty-image compatibility criterion",
            ),
            evidence="Introduces a convergence criterion that halts the DNN series once the residual dirty image is noise-compatible, rather than always running a fixed max.",
        ),
        entry(
            "convergence_behaviour",
            "divergence_failure",
            value=None,
            unit=None,
            scope="CLEAN diverged on 3 of the test problems",
            baseline="R2D2 models",
            empirical=True,
            execution_context=ctx(),
            evidence="CLEAN diverged on 3 test problems in setup E2 (alongside poor mean SNR).",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="R2D2 ~16 vs AIRI 5000 / uSARA ~1482",
            baseline="AIRI / uSARA",
            empirical=True,
            execution_context=ctx(),
            evidence="R2D2 inference series (~16) vs AIRI fixed 5000 and uSARA ~1482 iterations.",
        ),
        entry(
            "comparative_iteration",
            "more_than_baseline",
            value=None,
            unit=None,
            scope="R2D2 series vs single-iteration U-Net/U-WDSR",
            baseline="standalone end-to-end U-Net / U-WDSR (1 iteration)",
            empirical=True,
            execution_context=ctx(),
            evidence="Standalone U-Net/U-WDSR use 1 iteration only (and underperform); R2D2 uses a multi-iteration series.",
        ),
    ],
    "2025arXiv250309559C": [
        entry(
            "iteration_count",
            "inference_iterations",
            value=11,
            unit="series iterations",
            scope="iR2D2 vs R2D2 U-WDSR series length",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="Adaptive stopping via RDR / update condition (UC)",
            ),
            evidence="R2D2(U-WDSR) converges at i≈3; iR2D2(U-WDSR) at i≈11 due to interlaced image/sensitivity structure.",
        ),
        entry(
            "iteration_count",
            "outer_iterations",
            value=11,
            unit="DNN series steps",
            scope="Interlaced outer residual series",
            empirical=True,
            execution_context=ctx(),
            evidence="Series length is the outer residual-DNN iteration count (not CLEAN minor cycles).",
        ),
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=11,
            unit="series iterations",
            scope="RDR-tracked adaptive stopping",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="RDR-driven adaptive stopping with monotonic residual-energy update condition",
            ),
            evidence="Converges at series length i≈3 (R2D2) or i≈11 (iR2D2); ablation without UC shows residual spikes.",
        ),
        entry(
            "convergence_behaviour",
            "convergence_tolerance_reached",
            value=None,
            unit=None,
            scope="RDR / update-condition halt",
            empirical=True,
            execution_context=ctx(
                convergence_threshold="RDR = ‖r‖₂/‖x_b‖₂ used to drive stopping",
            ),
            evidence="RDR tracked over series iterations to diagnose and drive the adaptive stopping condition.",
        ),
    ],
    "2025arXiv250915176M": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=None,
            unit="major-loop iterations",
            scope="ngVLA review of CG/Momentum-CLEAN residual vs major-loop iteration",
            empirical=True,
            execution_context=ctx(),
            evidence="Review shows CG-CLEAN and Momentum-CLEAN drive major-loop residuals down more efficiently than traditional CLEAN.",
        ),
        entry(
            "iteration_count",
            "inner_iterations",
            value=4000,
            unit="Högbom iterations (example)",
            scope="Cygnus A Autocorr-CLEAN vs Högbom",
            empirical=True,
            execution_context=ctx(),
            evidence="Högbom needs ~4000 iterations / 227 s to match a residual level Autocorr-CLEAN reaches with far fewer minor iterations.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="Autocorr-CLEAN / Asp-CLEAN / CG-CLEAN vs Högbom",
            baseline="Högbom CLEAN",
            empirical=True,
            execution_context=ctx(),
            evidence="Autocorr-CLEAN and Asp-CLEAN reduce minor-loop iteration counts by up to an order of magnitude vs Högbom; CG-CLEAN reduces major loops.",
        ),
        entry(
            "comparative_iteration",
            "percentage_iteration_reduction",
            value=None,
            unit="up to ~order of magnitude",
            scope="Minor-loop iteration reduction cited for Autocorr/Asp-CLEAN",
            baseline="Högbom CLEAN",
            empirical=True,
            execution_context=ctx(),
            evidence="Review cites up to an order-of-magnitude reduction in minor iterations (and wall time) vs Högbom.",
        ),
    ],
    "2026AJ....171...44Y": [
        entry(
            "convergence_behaviour",
            "iterations_to_convergence",
            value=15,
            unit="iterations",
            scope="ALSB across noise sweeps",
            empirical=True,
            execution_context=ctx(
                optimiser="Split Bregman iteration",
                regularisation_parameters="Optimum sparsity level L=4; K=256 dictionary atoms",
            ),
            evidence="Convergence reached by ~iteration 15 across noise levels.",
        ),
        entry(
            "iteration_scaling",
            "noise_level",
            value=None,
            unit=None,
            scope="Convergence iteration vs input noise / SNR",
            empirical=True,
            execution_context=ctx(),
            evidence="Reports convergence by ~iteration 15 across noise levels in noise-robustness sweeps.",
        ),
        entry(
            "iteration_scaling",
            "algorithm_parameters",
            value=None,
            unit=None,
            scope="Patch size and sparsity L sweeps",
            empirical=True,
            execution_context=ctx(
                regularisation_parameters="Sparsity level L (optimum L=4)",
            ),
            evidence="Parameter sweeps over patch size and sparsity level L accompany the convergence study.",
        ),
    ],
    "2026A&A...706A..77M": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=None,
            unit="major-loop iterations",
            scope="CG-CLEAN / Momentum-CLEAN vs CLEAN",
            empirical=True,
            execution_context=ctx(
                stopping_criterion="χ² visibility residual tracked per major-loop iteration",
            ),
            evidence="Primary speed metric is major-loop iteration count (gridding/FFT dominated).",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="CG-CLEAN major loops vs Cotton–Schwab CLEAN",
            baseline="standard CLEAN major-loop count",
            empirical=True,
            execution_context=ctx(),
            evidence="CG-CLEAN reaches matched accuracy in roughly a fifth of the major-loop iterations on synthetic Cygnus A; 3–5× fewer on real narrowband data.",
        ),
        entry(
            "comparative_iteration",
            "iteration_ratio",
            value=0.2,
            unit="major-loop ratio (approx.)",
            scope="Synthetic Cygnus A",
            baseline="CLEAN major loops",
            empirical=True,
            execution_context=ctx(),
            evidence="About one-fifth the major-loop iterations of CLEAN on synthetic Cygnus A.",
        ),
        entry(
            "comparative_iteration",
            "percentage_iteration_reduction",
            value=None,
            unit="~order of magnitude (combined CG+Asp)",
            scope="Combined CG + Asp-CLEAN convergence speed claim",
            baseline="standard CLEAN",
            empirical=True,
            execution_context=ctx(),
            evidence="Combined CG + Asp-CLEAN described as close to an order-of-magnitude improvement in convergence speed.",
        ),
        entry(
            "convergence_behaviour",
            "convergence_rate",
            value=None,
            unit=None,
            scope="Momentum early speed vs CG later superlinear behaviour",
            empirical=True,
            execution_context=ctx(),
            evidence="Momentum-CLEAN fastest in first few iterations; CG-CLEAN overtakes once Krylov orthogonalization builds up (superlinear-type later convergence).",
        ),
        entry(
            "convergence_behaviour",
            "stable_solution_achieved",
            value=None,
            unit=None,
            scope="CG + Asp-CLEAN reaches noise floor in few major loops",
            empirical=True,
            execution_context=ctx(),
            evidence="Combining CG-CLEAN with Asp-CLEAN reaches the noise floor after just a few major-loop iterations.",
        ),
    ],
    "2026ApJS..283....9T": [
        entry(
            "iteration_count",
            "outer_iterations",
            value=10,
            unit="WSClean major cycles (mean)",
            scope="Hyperspectral VLA Table 1",
            empirical=True,
            execution_context=ctx(),
            evidence="WSClean 10±1 iterations (major cycles) on the simulated VLA hyperspectral benchmark.",
        ),
        entry(
            "iteration_count",
            "total_optimisation_iterations",
            value=3000,
            unit="iterations",
            scope="HyperAIRI / AIRI fixed budgets; Hyper-uSARA / uSARA adaptive",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="AIRI/HyperAIRI fixed at 3000",
            ),
            evidence="Table 1: HyperAIRI/AIRI fixed 3000; Hyper-uSARA 1827±675; uSARA similar O(10³) iteration totals.",
        ),
        entry(
            "iteration_count",
            "inference_iterations",
            value=3000,
            unit="PnP series iterations",
            scope="Plug-and-play denoiser series length",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="3000 fixed for AIRI/HyperAIRI",
            ),
            evidence="PnP methods report series iteration counts (fixed 3000 for AIRI/HyperAIRI) with per-step timing breakdown.",
        ),
        entry(
            "comparative_iteration",
            "more_than_baseline",
            value=None,
            unit=None,
            scope="PnP fixed budgets vs WSClean major cycles",
            baseline="WSClean ~10 major cycles",
            empirical=True,
            execution_context=ctx(),
            evidence="Despite needing more iterations than WSClean/optimization methods' major-cycle counts, PnP remains competitive in wall-clock (Runtime separate).",
        ),
    ],
    "2026arXiv260115844M": [
        entry(
            "iteration_count",
            "training_iterations",
            value=300000,
            unit="optimizer steps",
            scope="DDPM prior training on VLA FIRST",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="300,000 optimizer steps",
                batch_size="Training; inference Table 1 uses batch size 128",
            ),
            evidence="DDPM prior trained unconditionally for 300,000 optimizer steps on FIRST radio-galaxy images.",
        ),
        entry(
            "iteration_count",
            "inference_iterations",
            value=None,
            unit="DDRM sampling steps K",
            scope="Table 1 sampling steps K vs quality/runtime",
            empirical=True,
            execution_context=ctx(
                batch_size="128",
                regularisation_parameters="η=0.85, η_b=1.0",
            ),
            evidence="DDRM uses sampling steps K (swept, e.g. 10–1000 class) as the inference iteration axis for quality/runtime trade-offs.",
        ),
        entry(
            "iteration_scaling",
            "algorithm_parameters",
            value=None,
            unit=None,
            scope="Quality/runtime vs sampling steps K",
            empirical=True,
            execution_context=ctx(),
            evidence="Reports fidelity vs K sampling steps; complexity O(K·N·log N).",
        ),
        entry(
            "iteration_scaling",
            "image_size",
            value=None,
            unit=None,
            scope="O(K·N·log N) complexity",
            empirical=False,
            execution_context=ctx(),
            evidence="Analytic complexity O(K·N·log N) couples sampling steps to pixel count N.",
        ),
    ],
    "2026arXiv260309162W": [
        entry(
            "iteration_count",
            "epochs",
            value=11,
            unit="epochs",
            scope="POLISH++ fine-tuning vs train-from-scratch under PSF mismatch",
            empirical=True,
            execution_context=ctx(
                maximum_iterations="11 fine-tune epochs vs 57 from scratch",
            ),
            evidence="Fine-tuning reaches peak PSNR in 11 epochs vs 57 epochs training from scratch.",
        ),
        entry(
            "comparative_iteration",
            "fewer_than_baseline",
            value=None,
            unit=None,
            scope="Fine-tune epochs vs scratch",
            baseline="training from scratch (57 epochs)",
            empirical=True,
            execution_context=ctx(),
            evidence="Fine-tuning needs fewer epochs than training from scratch to peak PSNR.",
        ),
        entry(
            "comparative_iteration",
            "iteration_ratio",
            value=5,
            unit="× epoch speedup (approx.)",
            scope="11 vs 57 epochs",
            baseline="train from scratch",
            empirical=True,
            execution_context=ctx(),
            evidence="Authors state >5× speedup in epochs to peak PSNR for fine-tuning vs scratch.",
        ),
    ],
    "2026arXiv260526347D": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="Operator precomputation amortization phrased in iteration budgets",
            empirical=False,
            execution_context=ctx(),
            evidence="Mentions cost crossover within 'tens' / 'few hundred' iterations of iterative imagers, but does not report algorithm iteration performance or convergence results. Left Unspecified.",
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    iter_papers = [p for p in papers if p["metrics"].get("iterations") == 1]
    missing = [p["bibcode"] for p in iter_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in iter_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not iterations=1: {extra}")

    for p in papers:
        p.pop("iterations_details", None)

    mirror = {
        "schema_note": (
            "iterations_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.iterations binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in iter_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["iterations_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "iterations_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in iter_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["iterations_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected iterations_details for {len(iter_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
