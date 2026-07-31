#!/usr/bin/env python3
"""Inject compute_details into papers-data.json for Compute-positive papers.

Run from repo root: python3 scripts/inject_compute_details.py
Does not change top-level metrics.compute_cost flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "papers-data.json"
MIRROR = ROOT / "data" / "compute-details.json"


def ctx(hardware=None, parallelism=None, software=None, numerical_configuration=None, workload=None):
    return {
        "hardware": hardware,
        "parallelism": parallelism,
        "software": software,
        "numerical_configuration": numerical_configuration,
        "workload": workload,
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


# bibcode -> list of compute_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- classic ---
    "1980A&A....89..377C": [
        entry(
            "resource_usage",
            "peak_memory",
            value=None,
            unit=None,
            scope="Main memory and CLEAN beam-patch dimensions",
            empirical=True,
            execution_context=ctx(
                hardware="PDP-11/70 with FPS AP-120B; 32 kwords main memory",
                workload="Beam patch constrained between 21×41 and 64×127 elements",
            ),
            evidence="Machine had 32 kwords of main memory; beam patch constrained between 21×41 and 64×127 elements. Implementation memory footprint, not a reconstruction-quality score.",
        ),
    ],
    "1984A&A...137..159S": [
        entry(
            "scaling_complexity",
            "asymptotic_complexity",
            value=None,
            unit=None,
            scope="Analytic operation-count models for standard vs modified CLEAN",
            empirical=False,
            execution_context=ctx(
                numerical_configuration="Standard CLEAN ≈2QsM ops; modified CLEAN ≈QmM(4log(M)/2+4) with FFTs",
            ),
            evidence="Analytical work estimates compare standard CLEAN, modified (SDI) CLEAN, and Clark CLEAN via operation-count formulae in image size M and iteration counts. Algorithmic models, not measured hardware timings.",
        ),
    ],
    "1988A&A...200..312W": [
        entry(
            "relative_compute",
            "cost_ratio",
            value=0.25,
            unit="MRC/CLEAN ops",
            scope="MRC-to-CLEAN operation ratios in PNR=20 tests",
            baseline="CLEAN operation count",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="In-core image-domain cost model; f=2–4, 3–6 search-mask iterations",
                workload="2 arcmin model ≈0.6 ratio; 5 arcmin model ≈0.25 ratio",
            ),
            evidence="Under an in-core cost model, reported MRC-to-CLEAN operation ratios are about 0.6 (2 arcmin) and 0.25 (5 arcmin). Analytic/relative compute, distinct from the paper's wall-clock caption.",
        ),
        entry(
            "scaling_complexity",
            "asymptotic_complexity",
            value=None,
            unit=None,
            scope="MRC vs CLEAN convolution/masking/recombination operation model",
            empirical=False,
            execution_context=ctx(),
            evidence="Authors count convolutions, masking, decimation, component subtraction, and map recombination to predict when MRC has lower operation count for extended sources vs overhead for compact sources.",
        ),
    ],
    "1994A&AS..108..585S": [
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="Multi-frequency synthesis vs Hogbom/Clark CLEAN",
            baseline="conventional Hogbom or Clark CLEAN",
            empirical=False,
            execution_context=ctx(),
            evidence="Authors estimate the method to be about 2–3 times more computationally expensive than corresponding conventional Hogbom or Clark CLEAN, plus guard-band overhead. No runtime, processor, or memory benchmark.",
        ),
    ],
    "2004A&A...426..747B": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="Asp-Clean performance claims without absolute resource metrics",
            empirical=False,
            execution_context=ctx(),
            evidence="Active-set heuristic and Asp vs MS-Clean comparisons are framed as wall-clock performance ('takes about three times as long'). No CPU-hours, memory, FLOPs, or energy. Left Unspecified for Compute; Runtime covers the ratios.",
        ),
    ],
    "2008ISTSP...2..647C": [
        entry(
            "resource_usage",
            "peak_memory",
            value=2,
            unit="MB per w-plane kernel",
            scope="W-projection kernel storage; host RAM context",
            empirical=True,
            execution_context=ctx(
                hardware="Dual 3.06 GHz Xeon, 512 kB cache/processor, 3 GB memory",
                software="AIPS++ GNU O2",
                numerical_configuration="Max kernel support 220 px FWHM; 512×512 complex kernels",
                workload="1536×1536 @ 60 arcsec/pix; 20,000 CLEAN iterations",
            ),
            evidence="Each w-plane used a 512×512 complex-pixel kernel requiring 2 MB; greater convolution support raises memory demand. Host machine had 3 GB RAM. Absolute memory footprint for w-projection kernels.",
        ),
    ],
    "2014MNRAS.444..606O": [
        entry(
            "resource_usage",
            "flops",
            value=None,
            unit="PFLOPS",
            scope="SKA1 real-time processing estimate from fitted timing model",
            empirical=False,
            execution_context=ctx(
                hardware="Desktop i7-3930K rated 138 GFLOPS; 32 GB RAM",
                software="WSClean 1.0 vs CASA 42.0",
                workload="Extrapolated 1 h SKA1-low data at 20° zenith, 5 major iterations",
            ),
            evidence="Full SKA1 aperture-array case extrapolated to ~48.8 yr (WSClean) vs ~643 yr (CASA) on the test desktop, corresponding to about 59–60 PFLOPS for real-time processing with modeled techniques. Facility-scale FLOP budget, not a measured job FLOP count.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="Reduced-resolution inversion cost vs full-resolution",
            baseline="full-resolution inversion",
            empirical=True,
            execution_context=ctx(
                hardware="Six-core 3.20 GHz i7-3930K, 32 GB RAM",
                workload="3072-pixel → ~1500 pixels; also 10,000 output pixels case",
            ),
            evidence="Reducing a 3072-pixel inversion to ~1500 pixels saved roughly a factor of 2 at 10° zenith; at 10,000 output pixels cost fell by about an order of magnitude. Framed as computational cost reduction for reduced-resolution inversion.",
        ),
    ],
    "2017MNRAS.471..301O": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="Minor-loop wall-clock and iterations/s only",
            empirical=False,
            execution_context=ctx(
                hardware="40-core Xeon E5-2660 v2, 128 GB RAM (benchmark context)",
                workload="2048×2048 multi-scale deconvolution minor loop",
            ),
            evidence="Quantitative compute claims are wall-clock seconds and minor iterations/s versus CASA/MORESANE/IUWT. No CPU-hours, energy, FLOPs, or memory scores. Left Unspecified for Compute; Runtime covers throughput/wall-clock.",
        ),
    ],
    "2018A&A...611A..87T": [
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="BDA per-facet gridding speedup vs no averaging",
            baseline="gridding without BDA",
            empirical=True,
            execution_context=ctx(
                workload="VLA B-configuration test; decorrelation limits 0.001–0.04",
            ),
            evidence="Baseline-dependent averaging yields per-facet gridding speedup rising to roughly 4–5× then flattening at about 4× because memory access becomes limiting. Computational savings test, not fidelity.",
        ),
    ],
    "2018A&A...616A..27V": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="IDG GPU Tflop rating and kernel-storage claims without absolute resource scores",
            empirical=False,
            execution_context=ctx(
                hardware="Tesla K40c rated 4.29 Tflop/s SP (context); GeForce 840M laptop GPU",
            ),
            evidence="Primary measured scores are visibility/s throughput and wall-clock (Runtime). Avoiding oversampled kernel storage is qualitative; GPU Tflop rating is hardware context, not a reported compute cost. Left Unspecified for Compute.",
        ),
    ],
    "SKA-MEMO-132": [
        entry(
            "resource_usage",
            "flops",
            value=0.3,
            unit="SP flop/byte",
            scope="Arithmetic intensity and achieved Gflop/s vs peak",
            empirical=True,
            execution_context=ctx(
                hardware="Tesla C2070; dual-socket Xeon X5570 / E5462; Opteron 2218; BG/P",
                numerical_configuration="8 FLOPs and 24 bytes traffic per grid point (complex SP model)",
                workload="4096×4096 grid, 129-pixel support benchmark",
            ),
            evidence="Inner loop modeled at ≈0.3 SP flop/byte. Xeon X5570 achieves 11.3 SP Gflop/s (6% of 187 Gflop/s peak); C2070 achieves 27.3 SP Gflop/s (~2.7% of 1.03 Tflop/s peak). Arithmetic intensity and sustained FLOPs as compute cost.",
        ),
        entry(
            "resource_usage",
            "other_absolute",
            value=None,
            unit=None,
            scope="Hardware utilisation vs memory-bandwidth roofline",
            empirical=True,
            execution_context=ctx(
                hardware="Xeon X5570 ~64 GB/s nominal BW; C2070 115.2 GB/s effective with ECC",
            ),
            evidence="Xeon reaches just over 50% of bandwidth-implied Mpoints/s bound; C2070 ~71%. Utilisation vs roofline treated as hardware-efficiency diagnostics alongside power/capacity modeling.",
        ),
        entry(
            "scaling_complexity",
            "hardware_scaling",
            value=None,
            unit=None,
            scope="ASKAP pipeline node/capacity estimates from measured throughput",
            empirical=False,
            execution_context=ctx(
                hardware="Capacity scaled from dual-socket Xeon X5570 throughput",
                workload="ASKAP 30-arcsec / 10-arcsec spectral-line and continuum pipelines",
            ),
            evidence="Measured throughput extrapolated to ~820–3404 nodes and 76–319 DP Tflop/s peak for stated ASKAP configurations. Model-based capacity (hardware scaling), not end-to-end runtimes.",
        ),
        entry(
            "relative_compute",
            "resource_reduction_pct",
            value=None,
            unit=None,
            scope="W-stacking vs W-projection operation-count estimate",
            baseline="ASKAP W-projection supports (>100 px)",
            empirical=False,
            execution_context=ctx(),
            evidence="Memo estimates W-stacking with ~15-pixel support can reduce gridding operations by one to two orders of magnitude vs large W-projection supports. Operation-count relative compute, not a measured implementation.",
        ),
    ],
    "2025arXiv251213591C": [
        entry(
            "resource_usage",
            "energy",
            value=None,
            unit="J",
            scope="Energy-to-solution Ec=∫P(t)dt on heterogeneous WSClean+IDG runs",
            empirical=True,
            execution_context=ctx(
                hardware="Heterogeneous node with CPU/GPU/IDG device layers; PDU/RAPL/NVML",
                software="WSClean+IDG",
                workload="Including 16,384² and 32,768² imaging cases",
            ),
            evidence="Core metric energy-to-solution from integrated system power. GPU/IDG layers ≈60–90% of active-compute energy at 32,768²; static (idle) energy ≈80–85% of total.",
        ),
        entry(
            "efficiency_intensity",
            "energy_efficiency",
            value=None,
            unit="visibilities/J",
            scope="η_E = N/Ec and location-dependent Mvis/kgCO₂",
            empirical=True,
            execution_context=ctx(
                hardware="Scenario carbon factors: South Africa 0.672 vs WA 0.321 kgCO₂/kWh",
            ),
            evidence="Energy efficiency η_E = N/Ec (visibilities/J) is a core derived metric; carbon efficiency and Mvis/kgCO₂ reported for location-dependent SDP scenarios.",
        ),
        entry(
            "resource_usage",
            "peak_memory",
            value=None,
            unit="GB",
            scope="Peak memory M_peak diagnostic",
            empirical=True,
            execution_context=ctx(),
            evidence="Table 2 includes peak memory M_peak among diagnostic hardware metrics for the co-design suite.",
        ),
        entry(
            "efficiency_intensity",
            "memory_efficiency",
            value=None,
            unit="GB/J",
            scope="Memory efficiency η_mem = Bytes/Ec",
            empirical=True,
            execution_context=ctx(),
            evidence="Memory efficiency η_mem and memory bandwidth B_mem are diagnostic Table 2 metrics alongside peak memory.",
        ),
        entry(
            "resource_usage",
            "other_absolute",
            value=None,
            unit=None,
            scope="Device utilisation U and carbon-to-solution",
            empirical=True,
            execution_context=ctx(
                parallelism="CPU end-to-end utilisation ≈2–18% from 1–64 threads",
            ),
            evidence="Device utilisation U = t_active/t_total; carbon-to-solution Cc = Ec·κ(t,r). CPU utilisation rises only ≈2% (1 thread) to ≈18% (64 threads) end-to-end.",
        ),
        entry(
            "scaling_complexity",
            "hardware_scaling",
            value=None,
            unit=None,
            scope="CPU strong-scaling and PREESM CPU/FPGA energy–latency Pareto",
            empirical=True,
            execution_context=ctx(
                hardware="CPU thread scaling; KRIA KR260 FPGA DSE",
                parallelism="1–64 CPU threads; GPU IDG ≈flat wall time",
            ),
            evidence="Strong-scaling wall times accompany utilisation/energy analysis; PREESM DSE shows latency vs energy and occupancy Pareto fronts. Hardware scaling framed with energy/cost co-design, not Runtime alone.",
        ),
        entry(
            "relative_compute",
            "resource_reduction_pct",
            value=None,
            unit=None,
            scope="Modeled co-design energy/carbon reduction scenarios",
            baseline="baseline utilisation scenarios",
            empirical=False,
            execution_context=ctx(),
            evidence="Scenario claims of up to ~81% energy and ~97% carbon reduction under improved-utilisation models — modeled co-design savings, not shipped optimisations.",
        ),
    ],
    # --- emerging-ml ---
    "2022A&A...664A.134S": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=14,
            unit="h training",
            scope="Radionets training wall duration on stated GPU (training budget)",
            empirical=True,
            execution_context=ctx(
                hardware="NVIDIA GeForce RTX 2080 8 GB; 12-core i7-8700K; 512 GB SSD",
                numerical_configuration="~170 s/epoch; 300 epochs; fine-tune 20 epochs ~30 min",
                workload="Training maps 64×64 then fine-tune to 128×128",
            ),
            evidence="Training takes about 170 s per epoch and just over 14 h for 300 epochs on an RTX 2080. Training compute budget (GPU time), not inference wall-clock alone. CPU/GPU utilisation and energy not separated.",
        ),
    ],
    "2022ApJ...939L...4D": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=None,
            unit="CPU-h / GPU-h",
            scope="Operator construction and imaging on Cirrus for ESO 137-006",
            empirical=True,
            execution_context=ctx(
                hardware="Cirrus UK Tier-2 (CPU/GPU models not named)",
                parallelism="Construction 240–280 CPUs; forward 99–180 CPUs; AIRI 1 GPU faceting",
                workload="Low band 1053 MHz and high band 1399 MHz ASKAP fields",
            ),
            evidence="Low band: construction 427 CPU-h; imaging 1120 CPU-h (uSARA), 480 CPU-h+5 GPU-h (AIRI), 132 CPU-h (CLEAN). High band: construction 652 CPU-h; imaging 2377 / 1028+6 / 236 correspondingly. Reports CPU/GPU hours rather than wall time.",
        ),
        entry(
            "resource_usage",
            "peak_memory",
            value=None,
            unit="GB",
            scope="Holographic normal-operator storage vs de-gridding matrices",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="12–14 w-stacks (holographic) vs WSClean 72",
            ),
            evidence="Holographic encoding reduces reported storage from 470→81 GB (1053 MHz) and 645→159 GB (1399 MHz).",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="AIRI vs uSARA vs WSClean imaging CPU-hours",
            baseline="uSARA / WSClean imaging CPU-hours",
            empirical=True,
            execution_context=ctx(),
            evidence="AIRI imaging uses about 2.3× fewer CPU-hours than uSARA but about 4× the imaging compute of WSClean; including operator construction makes AIRI about 7× as costly as WSClean.",
        ),
    ],
    "2022MNRAS.514.2614C": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=300,
            unit="GPU-h",
            scope="POLISH training on TITAN RTX",
            empirical=True,
            execution_context=ctx(
                hardware="24 GB TITAN RTX",
                workload="~20 GPU-h per model; ~300 GPU-h total training",
            ),
            evidence="Training takes about 20 GPU-h per model and about 300 GPU-h in total. Inference 'few seconds on a laptop' is wall-clock without protocol — Compute subtype is the GPU-hour training budget.",
        ),
    ],
    "2023MNRAS.522.5558W": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=770,
            unit="CPU-h",
            scope="uSARA operator precomputation and deconvolution on ASKAP full-band",
            empirical=True,
            execution_context=ctx(
                hardware="Cirrus UK Tier-2: 36 physical cores, 72 threads, 256 GB/node",
                workload="467 M visibilities, SB9442 full-band, 19 w-stacks, 64 facets",
            ),
            evidence="Operator precomputation 281 CPU core-hours; deconvolution 770 CPU core-hours (4.3 h wall). WSClean same field 58 CPU core-hours. Core-hour resource accounting.",
        ),
        entry(
            "resource_usage",
            "peak_memory",
            value=80,
            unit="GB",
            scope="Holographic normal-operator storage",
            baseline="de-gridding matrices (~5× larger)",
            empirical=True,
            execution_context=ctx(),
            evidence="Holographic encoding reduces normal-operator storage to 80 GB, nearly a factor-of-five reduction relative to de-gridding matrices.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=20,
            unit="x",
            scope="uSARA MATLAB prototype vs WSClean average cost",
            baseline="WSClean",
            empirical=True,
            execution_context=ctx(),
            evidence="Paper characterizes uSARA's MATLAB prototype as about 20× more costly on average and WSClean as roughly an order of magnitude faster (resource/cost framing alongside wall time).",
        ),
    ],
    "2023MNRAS.522.5576W": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=203,
            unit="CPU-h",
            scope="AIRI sub-band and full-band CPU core-hours on Cirrus GPU nodes",
            empirical=True,
            execution_context=ctx(
                hardware="Cirrus GPU nodes: 4 GPUs, 40 CPU cores, 384 GB shared memory",
                parallelism="1–5 nodes; CPUs for measurement operator, 4 GPUs for denoiser facets",
                workload="ASKAP SB8275/SB9351/SB9442 sub-bands and SB9442 full-band",
            ),
            evidence="Sub-bands 45–144 CPU core-hours; SB9442 full-band 203 CPU core-hours (Table 6). GPU model and training cost not reported.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="AIRI vs uSARA vs WSClean deconvolution cost",
            baseline="uSARA / WSClean",
            empirical=True,
            execution_context=ctx(
                hardware="Not hardware-matched: uSARA on CPU nodes, AIRI on newer mixed nodes",
            ),
            evidence="DNN backward step 10–30× faster than uSARA denoiser; total AIRI deconvolution on average 4× lower than uSARA and 5× higher than WSClean.",
        ),
    ],
    "2024ApJS..273....3A": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=None,
            unit="GPU-h / CPU-h",
            scope="R2D2 / R3D3 series training on Cirrus",
            empirical=True,
            execution_context=ctx(
                hardware="Cirrus: Xeon E5-2695 CPU nodes; Xeon Gold 6148 + 4×V100-SXM2 GPU nodes",
                parallelism="R2D2: 4 GPUs+6 CPUs; R3D3: 12 GPUs+6 CPUs",
                workload="398–605 cumulative epochs depending on series",
            ),
            evidence="R2D2: 160 GPU-h + 4757 CPU-h. R3D3-3L: 1291 GPU-h + 2165 CPU-h; R3D3-6L: 1276 GPU-h + 2244 CPU-h. R2D2 uses ~80% fewer training GPU-hours than R3D3 but about twice the CPU-hours.",
        ),
    ],
    # --- r2d2-citing ---
    "2024A&A...690A.387R": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=24,
            unit="GPU-h",
            scope="MeerKAT ESO 137-006 fast-resolve scalability run",
            empirical=True,
            execution_context=ctx(
                workload="~400× larger than VLA case; 25–28 major cycles; +~2 CPU-h kernel precomputation",
            ),
            evidence="fast-resolve completes in ~24 GPU-hours plus ~2 CPU-hours kernel precomputation — dataset described as out of reach for resolve; prior convex/CLEAN-family work cited at 900–3000 CPU-hours per band.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="fast-resolve GPU/CPU-hours vs prior convex/CLEAN-family CPU-hours",
            baseline="Dabbech et al. 2022 (~900–3000 CPU-h/band)",
            empirical=True,
            execution_context=ctx(),
            evidence="Scalability demonstration contrasts ~24 GPU-h (+2 CPU-h precompute) against 900–3000 CPU-hours per band for prior methods on the large MeerKAT field.",
        ),
    ],
    "2024ApJ...966L..34D": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=None,
            unit=None,
            scope="DNN series upfront training described as thousands of CPU-core and GPU hours",
            empirical=False,
            execution_context=ctx(
                workload="One-off training amortized across future VLA observations",
            ),
            evidence="Training is a one-off cost of thousands of CPU-core and GPU hours (amortized). Reconstruction seconds are Runtime; Compute subtype is the stated training resource budget.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="R2D2 variants vs AIRI/uSARA reconstruction cost (fraction)",
            baseline="AIRI / uSARA optimization methods",
            empirical=True,
            execution_context=ctx(),
            evidence="Paper concludes R2D2 variants incur only a fraction of the reconstruction cost of optimization-based methods. Numeric seconds remain Runtime; the cross-method cost framing supports a relative Compute entry.",
        ),
    ],
    "2024arXiv240317905C": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=None,
            unit="h training",
            scope="Table II training time (TT) across architectures",
            empirical=True,
            execution_context=ctx(
                workload="Averaged over 160 test inverse problems for IT; TT hours per model",
            ),
            evidence="Training times: AIRI 48 h, U-Net 52 h, R2D2-Net (FFT) 152 h, R2D2 140 h, NC-PDNet 230 h, R2D2-Net (NUFFT) 315 h. NUFFT backend adds ~163 extra training hours vs FFT.",
        ),
        entry(
            "resource_usage",
            "other_absolute",
            value=248,
            unit="M parameters",
            scope="Trainable parameter counts (Table II)",
            empirical=True,
            execution_context=ctx(),
            evidence="Parameter counts reported alongside training/inference cost: AIRI 0.6M, U-Net 31M, R2D2/R2D2-Net 248M, NC-PDNet 1.6M — model size as resource footprint.",
        ),
    ],
    "2025A&A...698A..61J": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=30,
            unit="s/epoch",
            scope="ZINGULARITY/EHT training epoch cost on A100",
            empirical=True,
            execution_context=ctx(
                hardware="NVIDIA A100; Horovod distributed training",
                parallelism="Scales efficiently to 128 GPUs",
                workload="600,000 samples × 21,956 visibility points per epoch",
            ),
            evidence="One training epoch over 600k samples takes ~30 s on a single A100; obtaining 100 posterior samples from 100 bootstrapped datasets takes ~20 s. Training/inference compute on stated GPU.",
        ),
        entry(
            "resource_usage",
            "other_absolute",
            value=12,
            unit="M parameters",
            scope="Representative BANN model size",
            empirical=True,
            execution_context=ctx(),
            evidence="Representative BANN has ~12M trainable parameters, reported with training/inference compute context.",
        ),
        entry(
            "scaling_complexity",
            "hardware_scaling",
            value=128,
            unit="GPUs",
            scope="Horovod distributed training scaling",
            empirical=True,
            execution_context=ctx(
                software="Horovod over native TensorFlow",
                parallelism="Up to 128 GPUs",
            ),
            evidence="Distributed training via Horovod scales efficiently over native TensorFlow up to 128 GPUs — hardware scaling of training compute.",
        ),
    ],
    "2025A&A...698A.176M": [
        entry(
            "scaling_complexity",
            "asymptotic_complexity",
            value=None,
            unit=None,
            scope="Autocorr-CLEAN theoretical complexity m·N·(8l/k)",
            empirical=False,
            execution_context=ctx(
                numerical_configuration="m iterations, N pixels, l subminor loops, k autocorrelation basis components",
            ),
            evidence="Derived scaling m·N·(8l/k) used to argue the method avoids super-linear complexity growth relative to CLEAN. Analytic compute complexity; wall-clock residual curves are Runtime.",
        ),
    ],
    "2025AJ....169..289W": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="Distributed stage timings and resolution scaling are wall-clock",
            empirical=False,
            execution_context=ctx(),
            evidence="Profiling covers degridding/gridding/deconvolution/I/O/idle wall-clock and resolution-scaling time factors. No CPU-hours, energy, FLOPs, or memory scores. Left Unspecified for Compute; Runtime Scaling covers image-size timing.",
        ),
    ],
    "2025ApJS..280...63A": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=None,
            unit="GPU·hr",
            scope="Robust R2D2 series and standalone network training (Table 2)",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="R2D2_A1,T2: 25 iters, 31M U-Net; R2D2_A2,T2: 25 iters, 20.9M U-WDSR",
            ),
            evidence="Full series training: R2D2_A1,T2 231.6 GPU·hr; R2D2_A2,T2 420.9 GPU·hr. Standalone single-network training 85.6 GPU·hr (U-Net) and 165.7 GPU·hr (U-WDSR). Reconstruction seconds remain Runtime.",
        ),
    ],
    "2025MNRAS.542..426T": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="t_tot on A40 is wall-clock reconstruction time",
            empirical=False,
            execution_context=ctx(
                hardware="Nvidia A40 48 GB (context)",
            ),
            evidence="Reported 'Runtime / compute cost' values are total reconstruction seconds (t_tot≈2–3.3 s) and a <1.5× slowdown vs planar R2D2. No CPU/GPU-hours, energy, or memory scores. Left Unspecified for Compute; Runtime covers the timings.",
        ),
    ],
    "2025RASTI...4..25M": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="CLEAN/MS-CLEAN described as computationally costly without numbers",
            empirical=False,
            execution_context=ctx(),
            evidence="CLEAN and multi-scale CLEAN are described only qualitatively as computationally costly. No CPU-hours, memory, FLOPs, energy, or numeric cost ratios. Unspecified Compute.",
        ),
    ],
    "2025arXiv250102473D": [
        entry(
            "resource_usage",
            "cpu_gpu_hours",
            value=0.72,
            unit="A100 GPU-years",
            scope="IRIS calibration/simulation testing and posterior sampling cost",
            empirical=True,
            execution_context=ctx(
                hardware="10× V100 for sampling; A100 GPU-years for full testing",
                parallelism="10 V100 GPUs",
                workload="250 posterior samples per disk",
            ),
            evidence="0.72 A100 GPU-years for full calibration/simulation testing; 250 posterior samples in ~2.5 h on 10 V100s. Explicitly slower than CLEAN/MPoL. GPU-year resource budget is the Compute subtype (sampling duration also noted as Runtime).",
        ),
    ],
    "2025arXiv250309559C": [
        entry(
            "resource_usage",
            "other_absolute",
            value=315.7,
            unit="M parameters",
            scope="iR2D2(U-WDSR) model size",
            empirical=True,
            execution_context=ctx(),
            evidence="iR2D2(U-WDSR) reported at 315.7M parameters — model size as resource footprint alongside reconstruction runtime (Runtime).",
        ),
        entry(
            "scaling_complexity",
            "problem_size_scaling",
            value=None,
            unit=None,
            scope="Training-time growth with coil count L vs unrolled baselines",
            empirical=True,
            execution_context=ctx(
                workload="Coil count scaling; example ~4× faster training than R2D2-Net at L=64",
            ),
            evidence="iR2D2 shows shallower (near-linear) training-time growth with number of coils than unrolled architectures, attributed to avoiding NUFFT inside backprop. Problem-size scaling of training compute.",
        ),
    ],
    "2025arXiv250915176M": [
        entry(
            "resource_usage",
            "flops",
            value=None,
            unit="Tflop/s–Pflop/s",
            scope="Cited ALMA WSU and ngVLA computational budgets",
            empirical=False,
            execution_context=ctx(
                workload="Facility-scale imaging; gridding identified as dominant cost",
            ),
            evidence="Cites ~100 Tflop/s for ALMA WSU and ~50 Pflop/s for ngVLA, with gridding as dominant computational cost (NRAO/ALMA memos). Facility FLOP/s budgets framed as compute cost; fidelity comparisons remain qualitative.",
        ),
    ],
    "2026A&A...706A..77M": [
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="Major-loop iteration reduction as numerical/compute cost vs CLEAN",
            baseline="standard Cotton–Schwab CLEAN major loops",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="Momentum overhead ≈ one minor-loop image-sum; no added gridding/FFT",
            ),
            evidence="CG-CLEAN reaches same accuracy in ~1/5 major-loop iterations (synthetic) and 3–5× fewer on real data. Gains framed as lower numerical cost via fewer major loops (gridding/FFT dominated), not measured wall-clock tables.",
        ),
        entry(
            "scaling_complexity",
            "asymptotic_complexity",
            value=None,
            unit=None,
            scope="Momentum-CLEAN overhead vs minor-loop numerical cost",
            empirical=False,
            execution_context=ctx(),
            evidence="Momentum-CLEAN overhead is an image-sum with the numerical cost of one minor-loop iteration; combined CG+Asp approach claimed near order-of-magnitude improvement at lower numerical cost than upgrading the minor loop alone.",
        ),
    ],
    "2026ApJS..283....9T": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="HyperAIRI 'computational cost' table is wall-clock hours",
            empirical=False,
            execution_context=ctx(),
            evidence="Table reports iterations and wall-clock reconstruction hours (e.g. HyperAIRI 1.90±0.14 hr). No CPU/GPU-hours, energy, or memory scores. Left Unspecified for Compute; Runtime covers the timings.",
        ),
    ],
    "2026arXiv260526347D": [
        entry(
            "resource_usage",
            "peak_memory",
            value=None,
            unit=None,
            scope="Holographic H vs explicit G measurement-matrix memory",
            baseline="explicit de-gridding matrix G",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="m_G(P)=24K(P)+4N′; asymptotic m_G*≈24MQ",
            ),
            evidence="Holographic H formulation gives a reported 7-fold reduction in memory to store the operator vs explicit G, at roughly 30% higher precomputation cost.",
        ),
        entry(
            "relative_compute",
            "resource_reduction_pct",
            value=None,
            unit=None,
            scope="~7× operator memory reduction (H vs G)",
            baseline="explicit G matrix",
            empirical=True,
            execution_context=ctx(),
            evidence="Seven-fold memory reduction for holographic operator storage; paired with ~30% higher precomputation cost and amortization within tens to hundreds of iterations.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="Imaging cost vs CLEAN; precomputation vs apply amortization",
            baseline="CLEAN; on-the-fly vs precomputed operator",
            empirical=True,
            execution_context=ctx(
                workload="MeerKAT ESO 137-006 among test cases",
            ),
            evidence="High-precision measurement operator imaging cost 'within one order of magnitude of CLEAN'. Precomputation matched by application within tens of iterations and exceeded ~10× within a few hundred.",
        ),
        entry(
            "scaling_complexity",
            "hardware_scaling",
            value=None,
            unit=None,
            scope="1–10 CPU-node distributed planning and worker adaptation",
            empirical=True,
            execution_context=ctx(
                parallelism="1–10 CPU nodes; workers adapted to available cores",
            ),
            evidence="Distributed runs from 1 to 10 CPU nodes; planning adapts workers to cores (e.g. switch to on-the-fly when workers exceed cores). Communication overhead tracked as part of total cost.",
        ),
        entry(
            "relative_compute",
            "cost_ratio",
            value=None,
            unit=None,
            scope="Fewer w-layers vs WSClean as efficiency proxy",
            baseline="WSClean recommended w-layer counts",
            empirical=True,
            execution_context=ctx(
                numerical_configuration="e.g. 23 vs 126; 14 vs 40; 12 vs 48–73 w-layers",
            ),
            evidence="Number of w-layers used as computational-efficiency proxy: fewer layers at comparable/better efficiency vs WSClean recommendations across test configurations.",
        ),
    ],
    "2026arXiv260628493D": [
        entry(
            "unspecified",
            "unspecified",
            value=None,
            unit=None,
            scope="SKA-era AI review qualitative compute/speed claims",
            empirical=False,
            execution_context=ctx(),
            evidence="Review cites R2D2/AIRI/U-Net computational cost and inference speed qualitatively ('CLEAN-like speeds', 'significantly reduced computational cost') without primary resource measurements. Unspecified Compute.",
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    compute_papers = [p for p in papers if p["metrics"].get("compute_cost") == 1]
    missing = [p["bibcode"] for p in compute_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in compute_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not compute_cost=1: {extra}")

    for p in papers:
        p.pop("compute_details", None)

    mirror = {
        "schema_note": (
            "compute_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.compute_cost binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in compute_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["compute_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "compute_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import Counter, defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in compute_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["compute_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected compute_details for {len(compute_papers)} papers.")
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
