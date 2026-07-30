# RMS

## What this metric means here
**RMS** covers absolute residual / dirty / off-source RMS (or equivalent standard deviation) reported as a fidelity or noise score in physical units (Jy/beam, mJy/beam, μJy/PSF, etc.), or explicitly named as a core framework quality metric (e.g. astroCAMP dirty-image RMS / residual RMS). It is **not** the R2D2-family normalised residual-to-dirty ratio (see **RDR**).

Root totals after the split: classic RMS = 8, emerging-ml RMS = 1, r2d2-citing RMS = 2 (grand total **11**).

## How papers use it
**Classical residual RMS and morphology (classic cohort).** Asp-CLEAN, WSClean, and wideband deconvolution papers treat residual images as primary fidelity evidence: Asp-CLEAN residuals statistically consistent with noise vs correlated MS-CLEAN structure (Asp itself is qualitative morphology only under the new split — RMS=0); WSClean compares residual RMS (μJy/beam or mJy/PSF) against CASA on MWA simulations (e.g. 0.94 vs 1.90 mJy/beam at 12 w-planes) and real MWA Vela field (50 vs 64 mJy/PSF). Wideband MS tests report off-source residual RMS from 880 μJy/PSF (single-scale CLEAN) down to 55–64 μJy/PSF (multi-frequency multi-scale CLEAN)—factor ≈4400–5100 below dirty RMS. IDG reports ≈17–19× lower residual RMS than classical gridding in source box and full image. Multi-frequency paper warns unchanged low residual can mask wrong spectral solutions when short spacings are missing. Bhatnagar et al. report off-source and Stokes V residual RMS; Cornwell MS-CLEAN tabulates image-domain RMS error vs smoothed truth; Rau & Cornwell report on-/off-source residual RMS on M87/3C286.

**Framework residual RMS (classic).** astroCAMP defines dirty-image RMS `σ_dirty` and residual-based dynamic range `DR = I_max / σ_res` as core Table 2 fidelity metrics (and uses dirty-image RMS in the example quality tuple); Section 6 does not tabulate those RMS values for the WSClean+IDG matrix.

**Real-data residual-map RMS (emerging-ml).** uSARA ASKAP validation (2023MNRAS.522.5558W) reports measured residual-map rms (e.g. WSClean ≈1–2 μJy/pixel) and draws source-boundary contours at multiples of that residual RMS vs calculated image noise—evidence of low-surface-brightness recovery, not a normalised RDR score. Other emerging-ml papers either lack numeric residual RMS (qualitative residual images only) or use estimated image-domain noise only for regularisation/DR parameter setting (AIRI MeerKAT / ASKAP), which does not score as standalone RMS under the split rules. Emerging-ml RMS total = 1.

**Absolute residual / image RMS (r2d2-citing).** CLEANing Cygnus A with R2D2 (2024ApJ...966L..34D) and MROP (2025MNRAS.543.1727L) report absolute residual or image-domain RMS-style scores as fidelity evidence (r2d2-citing RMS total = 2). Most other R2D2-family papers score data fidelity with normalised **RDR** instead.

## Popular measurement variants
- **Residual RMS or std (mJy/beam, μJy/PSF, Jy/beam):** WSClean, wideband MS-CLEAN, IDG, MWA real-data comparisons.
- **Off-source / blank-region RMS:** multi-frequency synthesis; A-Projection / direction-dependent gain papers.
- **Dirty-image RMS (`σ_dirty`):** astroCAMP framework metric.
- **Residual-map rms on real data:** uSARA ASKAP vs WSClean contour/sensitivity context.
- **Residual peak vs σ stopping criterion:** wideband simulations stop when residual peak < 3σ (algorithmic; not always scored as standalone RMS).

## Gaps and caveats
- **RMS ≠ RDR:** Classical papers rarely compute normalised residual-to-dirty ratios; do not conflate absolute RMS with ‖r̂‖₂/‖x_dirty‖₂.
- **DR denominator alone is not enough:** RMS appearing only inside `DR = I_max / σ_res` without standalone RMS reporting does not justify RMS=1 under the split rules (astroCAMP is an exception because RMS is also a named core framework metric).
- **Low residual can mislead:** Wrong spectral index with excellent residual RMS (multi-frequency); flat dirty residual with poor truth SNR (PURIFY, SARA).
- **Qualitative residuals:** Looking at residual maps or saying residuals are “noise-like” without a numeric RMS → RMS=0.
- **Figure/table inconsistencies:** WSClean MWA paper notes conflicting residual RMS labels (47 vs 62 mJy/PSF) unresolved in text.
