# Runtime

## What this metric means here

In this review, **Runtime** is elapsed wall-clock time to reach a stated imaging outcome—typically a reconstructed (and often cleaned) image at a defined stopping criterion—across the radio-interferometry imaging chain from visibilities through gridding, inverse FFT, and deconvolution/regularized inversion. We record seconds, minutes, or hours (and occasionally days or years in extrapolated SKA projections), not normalized hardware-independent scores unless papers explicitly provide them.

## How papers use it

### Relative speedups and throughput (classic CLEAN era)

Early classic papers often report **implementation throughput** or **relative speed** rather than full end-to-end wall time. Clark (1980) reports ~15 components/s in the minor cycle on a PDP-11/70 with an FPS AP-120B, plus 2–10× savings over conventional CLEAN depending on map size and gain. Multi-Resolution CLEAN (1988) compares 90 min vs 15 min for equivalent component recovery (with an internal 6× vs "one third" inconsistency). Asp-Clean (2004) gives order-of-magnitude heuristic gains and ~3× overhead vs MS-Clean without absolute timings.

### Stage-resolved and per-residual timings (gridding / w-projection)

W-projection (2008) tabulates **per-residual-calculation time** and **total deconvolution time** on a dual 3.06 GHz Xeon (e.g. 27 s/residual and 216 s total for a 2D transform vs 607 s/residual and 3,161 s total for 64 w-planes at higher DR). WSClean (2014) separates **imaging-only** wall time (synthesized PSF + image, excluding cleaning) from **end-to-end accuracy tests** with five major iterations (e.g. 8.5 vs 19.3 min WSClean vs CASA at zenith with 12 w-planes; 15.3 vs 178.2 min at 10° zenith with 195 planes). Faceting/SSDGA (2018) reports ~12 h single-core wall time for a 5100×5100, 529-facet 3C147 run (94% in gridding), with ~12× speedup at 16 physical cores. IDG (2018) reports low-level gridding at 4.3 M visibilities/s (22 s for ~93 M visibilities on a laptop GPU) and LOFAR major cycles of ~20 min each on Tesla K40 nodes.

### Convex optimization and sparsity methods (minutes to hours)

SARA/PURIFY (2012–2014) plot log10 wall-clock seconds vs coverage on a 2.4 GHz quad-core Xeon: reweighted methods tens of minutes to ~1 h at full coverage; non-reweighted mostly <10 min. WSClean wideband comparisons (2017) give CPU MORESANE 256 min vs IUWT 44–179 min vs WSClean 223 s (single-frequency) / 600 s (8-channel) on 2048×2048 data—though these exclude full gridding/inversion. uSARA/AIRI on ASKAP (2023) report **wall time alongside CPU core-hours**: uSARA deconvolution 4.3 h vs WSClean 0.8 h on the same full-band field; AIRI sub-bands 1.0–2.9 h wall time.

### ML inference: seconds vs hours (emerging-ml and r2d2-citing)

The R2D2 family dominates runtime reporting in newer cohorts. Generic tests (ApJS 2024) show CLEAN ~66 s, uSARA ~4,184 s, AIRI ~3,479 s vs R2D2 ~2.9–18.6 s depending on GPU/MATLAB/Python backend; R3D3 variants ~1.9–15 s. Cygnus A comparisons (2024) tighten this: R2D2 ~3.3 s, R2D2-Net ~0.97 s, uSARA ~1,197 s, AIRI ~672 s. fast-resolve (2024) reports time-to-residual ~10⁻³: ~10 min (A100), ~20 min (RTX 3090), ~200 min (8-core Xeon) vs resolve ~1,416 min. Diffusion DDRM (2026) scales sampling time linearly with steps K: 0.44 s (K=10) to 45.47 s (K=1000) on an NVIDIA GH200. HyperAIRI (2026) still reports hours (~1.9 hr) for hyperspectral VLA benchmarks vs WSClean ~0.56 hr.

### Benchmark frameworks and SKA-scale projections

astroCAMP (2025) formalizes **time-to-solution** `T_c` (seconds) as full end-to-end elapsed wall time from POSIX timing, logs, or scheduler timestamps, plus derived throughput `Θ = N/T_c` (visibilities/s). It documents CPU strong-scaling saturation (e.g. 3:13:10 → 1:08:06 from 1 to 64 cores on a 16,384² image) and notes I/O is ~1% of wall time despite misaligned small reads. WSClean (2014) extrapolates desktop timings to SKA1-low: ~48.8 years (WSClean) vs ~643 years (CASA w-projection) for one hour of data—model projections, not measurements. HVOX (2023) benchmarks synthesis/analysis on an i9-10900X workstation with sparse vs dense grid regimes.

### Residual-level and convergence-time curves

Several papers plot **wall time vs residual level** rather than fixed iteration counts: Autocorr-CLEAN (2025), ngVLA review (2025) with Högbom ~4000 iterations / 227 s vs Autocorr-CLEAN reaching the same residual faster, and fast-resolve tracking mean-squared log-brightness residual over wall time across hardware.

### Cohort tendencies

**Classic** papers mix relative ratios, stage timings, and hardware-specific benchmarks; many omit full pipeline scope. **Emerging-ml** introduces training-amortized inference comparisons (Radionets: 0.003–0.407 s pure network vs 0.43–9 s WSClean by image size). **r2d2-citing** overwhelmingly reports sub-minute GPU reconstruction vs multi-minute/hour optimization baselines, often with explicit per-step breakdowns (`t_dat` vs `t_reg`).

## Popular measurement variants

- **End-to-end time-to-solution (`T_c`)**: full workflow elapsed wall clock from input visibilities to final image (astroCAMP, decentralized framework, many r2d2 papers).
- **Imaging-only / gridding-only wall time**: excludes cleaning, prediction, or calibration (WSClean Figure 7; IDG low-level routine vs WSClean overhead).
- **Per-stage wall time**: gridding, degridding, FFT, deconvolution, I/O, inter-node idle (faceting paper, decentralized framework, distributed measurement-model paper).
- **Per-residual or per-major-cycle time**: w-projection residual calculation seconds; LOFAR ~20 min/major cycle; five major iterations in WSClean accuracy tests.
- **Relative speedup vs baseline**: factors vs CASA, conventional CLEAN, resolve, or serial vs parallel (2× theoretical for two nodes).
- **Throughput**: components/s (CLEAN minor cycle), visibilities/s (IDG, astroCAMP `Θ`), Mpoints/s (SKA-MEMO gridding), images/s (astroCAMP text).
- **Time-to-convergence threshold**: wall clock to reach a residual, SNR, or log-residual target (fast-resolve, Autocorr-CLEAN, QuantifAI UQ tables).
- **Per-iteration or per-step timing**: data-fidelity vs regularization/DNN step seconds (R2D2 Table 2; HyperAIRI gradient vs denoising step).
- **Training excluded vs included**: inference-only seconds vs end-to-end framework with I/O (Radionets); amortized training noted as one-off cost.
- **Hardware-scaling wall time**: strong scaling curves (faceting 1–16 cores; astroCAMP 1–64 CPU cores with GPU IDG ~flat ~1:09).
- **Extrapolated / modelled runtime**: SKA desktop-year projections, real-time PFLOPS estimates, co-design scenario energy/time trade-offs (not measured speedups).

## Gaps and caveats

- **Scope ambiguity** is common: minor-loop-only, deconvolution-only, gridding-only, or "imaging without cleaning" timings are often not comparable to full pipeline runtime.
- **Hardware and software context** varies widely (PDP-11 through GH200; MATLAB prototypes vs production WSClean/CASA); cross-paper ranking requires matched problem size, visibility count, and stopping rules.
- **Missing baselines**: many optimization papers lack same-hardware CLEAN/WSClean runs; cross-paper MS-Clean comparisons appear in early SARA work.
- **Internal inconsistencies** appear in some classic figures (MRC 6× vs "one third"; IDG LOFAR image dimensions differ between text and figure captions).
- **Training and operator precomputation** are frequently excluded from inference runtime but dominate total cost for AIRI/uSARA on real ASKAP fields (hundreds of CPU core-hours precompute).
- **Stopping criteria differ**: fixed iteration budgets (20,000 CLEAN iterations in w-projection benchmarks), residual thresholds, or validation-plateau iteration counts (S-R2D2 I=10) produce non-equivalent "runtime" labels.
- **Two papers** (IRIS 2025, SKA-AI review 2026) were classified under Runtime from summaries without dedicated timing bullets in the notes.
