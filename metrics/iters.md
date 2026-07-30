# Iters

## What this metric means here

**Iters** counts algorithmic cycles or iterations used to reach a reconstruction: CLEAN major and minor loops, Hogbom/Clark component subtractions, convex-optimization or proximal iterations, plug-and-play/denoiser steps, DNN-series outer iterations, diffusion sampling steps, or Bayesian major cycles. In this review the number may label qualitatively different units across methods; we record what each paper reports without forcing a single universal definition across CLEAN vs R2D2 vs AIRI.

## How papers use it

### CLEAN major/minor cycles and component counts (classic)

Högbom (1974) shows cleaned maps after 1, 2, and 6 iterations (gain 1) qualitatively. Clark (1980) describes major-cycle component counts ramping from ~5–6 toward ~250 at gain 0.5. Schwarz (1984) gives modified CLEAN 17 iterations vs standard CLEAN 2,000 subtractions on a 64×64 test, plus analytic work estimates \(N_s \approx 2Q_s M\) (standard) vs \(N_m \approx Q_m M(4\log M/2 + 4)\) (modified). MRC (1988) predicts lower operation counts for extended sources (ratios ~0.6 and ~0.25 vs CLEAN in PNR-20 tests). W-projection (2008) fixes **20,000 CLEAN iterations** (gain 0.1) for DR benchmarks; w-projection notes facet methods can skip empty facets early, affecting effective minor-cycle scaling. Multiscale CLEAN (2008) uses 1,000 iterations on real NGC 1058 data and 5,000 to converge on M31 simulation where Clark CLEAN diverged beyond ~300,000 components. WSClean accuracy tests use **five major iterations**; 3C147 faceting run uses **five HMP major cycles** to 0.4 mJy; IDG LOFAR example uses **four major cycles**.

### Minor-loop speed as iterations per second (classic)

Offringa wideband paper (2017) reports **minor iterations per second** excluding gridding: WSClean ~748 iter/s vs extrapolated CASA ~29 iter/s for 100,000 iterations on 2048² (15.6×); multi-frequency WSClean 323–771 iter/s vs CASA MSMFS ~0.42 iter/s (~400–900×), minor-loop only. Asp-Clean (2004) tracks active Aspen count and residual area vs iteration qualitatively without a convergence table.

### Optimization and plug-and-play iteration budgets (emerging-ml → r2d2)

uSARA and AIRI routinely require **hundreds to thousands** of iterations: generic R2D2 benchmark CLEAN **9±1 major cycles**; uSARA **1103±373**; AIRI **5000** fixed; HyperAIRI/Hyper-uSARA **3000** and **1827±675** respectively on hyperspectral VLA tests; WSClean **10±1** major cycles in the same table. Cygnus A head-to-head (2024): Hö-CLEAN 1; CS-CLEAN 7; MS-CLEAN 9; R2D2 15; R3D3 8; R2D2-Net 1; uSARA 477; AIRI 1783. ISCAD (2025) reports iteration counts alongside SNR and runtime (e.g. M106 SKA case: SARA/AIRI/LPG/ISCAD iteration totals embedded in SNR/S/N_log/time triplets).

### DNN series length and unrolled depth (r2d2-citing)

R2D2 treats **series iteration count** as the number of chained U-Net/U-WDSR steps: typically **7–18** at inference (R3D3-3L 7, R2D2 ~12–15, Robust R2D2 15.8–18.3±5.5) vs **~616–4995** for PnP/optimization baselines. R2D2-Net and U-Net collapse to **1 iteration** (single forward pass). NC-MRI R2D2 (2024): R2D2 converges by ~8 series iterations; iR2D2 needs ~11 vs R2D2 ~3 due to interlaced sensitivity calibration. S-R2D2 fixes **I=10** where logSNR plateaued on validation. Training uses more outer components (e.g. 25 series slots, 7–8 for R3D3) distinct from inference iteration count. DDRM (2026) uses **sampling steps K** (10–1000) as the iteration axis for quality/runtime trade-offs.

### Convergence diagnostics tied to iterations

Many papers plot **residual vs iteration** rather than reporting a single count: fast-resolve uses mean-squared log-brightness residual between successive iterations; CG/Momentum-CLEAN (2026) tracks χ² visibility residual per **major-loop** iteration; Autocorr-CLEAN (2025) plots residual vs subminor-cycle iterations with l ≪ k ≪ m; iR2D2 (2025) tracks RDR over series iterations with monotonic descent under an update condition. ALSB (2026) reaches convergence by ~iteration 15 across noise sweeps. QuantifAI and bootstrap UQ papers use iteration/sample counts for posterior draws rather than deconvolution loops.

### Major-loop acceleration as primary speed lever

CG-CLEAN (2026) emphasizes **major-loop iteration count** because gridding/FFT cost dominates: ~5× fewer major cycles than Cotton–Schwab CLEAN on synthetic Cygnus A, 3–5× on real narrowband data, similar on VLBA; Momentum-CLEAN adds negligible overhead (~one minor-loop cost) and wins early iterations; combined CG + Asp-CLEAN reaches noise floor in few major cycles. ngVLA review (2025) cites Autocorr-CLEAN and Asp-CLEAN reducing minor iterations and wall time by up to an order of magnitude vs Högbom (~4000 iterations / 227 s for Högbom to match Autocorr residual level on Cygnus A).

### Cohort tendencies

**Classic** papers count CLEAN components, major/minor cycles, or fixed large iteration budgets (20,000) for algorithm comparison; analytical operation-count ratios supplement timings. **Emerging-ml** papers classified under Iters often lack dedicated iteration bullets (Radionets, PRIMO, uSARA ASKAP paper) but sit in a literature where optimization methods use 10²–10³ iterations. **r2d2-citing** overwhelmingly contrasts **O(1)–O(20) learned series iterations** with **O(10²–10³) PnP/ proximal iterations**, treating iteration count as a proxy for automation and pipeline complexity.

## Popular measurement variants

- **Högbom/Cotton–Schwab minor-cycle iterations / component subtractions**: per-major-cycle component removals or total subtractions to threshold (Clark 1980, Schwarz 1984, ngVLA Högbom ~4000).
- **Major cycles / major loops**: outer gridding–deconvolution loops (WSClean 5–10; HMP 5; fast-resolve 25–28; CG-CLEAN major-loop counts).
- **Fixed iteration budget**: run exactly N iterations regardless of convergence (w-projection 20,000; AIRI 5000; HyperAIRI 3000).
- **Iterations to convergence threshold**: count until residual, χ², SNR, or RDR criterion met (ISCAD, ALSB ~15, R2D2 series until logSNR plateaus).
- **Minor iterations per second**: throughput metric in wideband deconvolution benchmarks (748 vs 29 iter/s).
- **Convex/proximal/PnP iterations**: uSARA ~1100–1482; AIRI ~1783–4995; SARA proximal steps per ADMM loop.
- **DNN series iterations (I)**: outer unrolled or iterative network applications (R2D2 7–18; R3D3 7–8; iR2D2 ~11).
- **Single-pass / 1 iteration**: end-to-end U-Net, R2D2-Net, pseudo-inverse (explicitly 1 operator evaluation).
- **Diffusion sampling steps K**: DDRM 10–1000 steps as iteration axis.
- **MCMC / bootstrap sample counts**: posterior draws or ensemble size (QuantifAI MCMC vs LCI samples; R2D2 UQ L=5 reconstructions)—sometimes classified alongside iterations.
- **Subminor vs clustered basis iterations**: Autocorr-CLEAN l subminor loops with k basis components vs m classical CLEAN iterations.
- **Analytic iteration-count models**: operation ratios (MRC/CLEAN ~0.25–0.6; modified vs standard CLEAN work formulas).
- **Active-set / Aspen count**: Asp-Clean dynamic search-space size vs iteration (qualitative convergence plots).

## Gaps and caveats

- **Incommensurable units**: one R2D2 series iteration (data fidelity + DNN) is not equivalent to one CLEAN minor cycle or one uSARA proximal step; cross-method iteration comparison is indicative, not normalized compute.
- **Fixed budgets vs adaptive stopping**: AIRI/HyperAIRI often fix 3000–5000 iterations while R2D2 stops at ~15; WSClean reports major cycles to threshold—counts are not fairness-matched.
- **Major vs minor conflation**: papers and our table may label "iterations" without stating loop level; WSClean "10 iterations" are major cycles, while uSARA "1103" are outer algorithm steps.
- **Missing iteration data**: several emerging-ml papers (Radionets, PRIMO, EHT PRIMO, uSARA ASKAP I) were classified from summaries without auto-matched iteration bullets.
- **Component count ≠ iteration count**: Clark CLEAN and MRC report delta-function or component totals separately from loop indices.
- **Training series depth ≠ inference iterations**: R2D2 may train 25 components but deploy 15.8±5.5 at test time.
- **Convergence vs quality**: fewer major cycles (CG-CLEAN) or fewer minor iterations (Autocorr-CLEAN) are often shown at matched residual, but not always at matched dynamic range or flux recovery.
- **Diffusion and Bayesian sample counts** blur the line between "iterations" and Monte Carlo ensemble size; context from each paper is required.
