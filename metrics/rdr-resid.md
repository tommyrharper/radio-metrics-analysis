# RDR/Resid

## What this metric means here
**RDR/Resid** in this review covers papers that assess reconstruction quality through *residual* images or residual-derived ratios—evidence that the model fits the measured visibilities and leaves noise-like, unstructured remainder in image or visibility space after gridding, iFFT, and deconvolution. The column includes classical residual RMS/standard-deviation reporting and the R2D2-family **residual-to-dirty ratio (RDR)**, `‖r̂‖₂ / ‖x_dirty‖₂` (lower = cleaner data fit).

## How papers use it
**Classical residual RMS and morphology (classic cohort).** Asp-CLEAN, WSClean, and wideband deconvolution papers treat residual images as primary fidelity evidence: Asp-CLEAN residuals statistically consistent with noise vs correlated MS-CLEAN structure; WSClean compares residual RMS (μJy/beam or mJy/PSF) against CASA on MWA simulations (e.g. 0.94 vs 1.90 mJy/beam at 12 w-planes) and real MWA Vela field (50 vs 64 mJy/PSF). Wideband MS tests report off-source residual RMS from 880 μJy/PSF (single-scale CLEAN) down to 55–64 μJy/PSF (multi-frequency multi-scale CLEAN)—factor ≈4400–5100 below dirty RMS. IDG reports ≈17–19× lower residual RMS than classical gridding in source box and full image. Multi-frequency paper warns unchanged low residual can mask wrong spectral solutions when short spacings are missing.

**RDR as quantitative data-fidelity metric (emerging-ml + r2d2-citing).** R2D2 (2024ApJS) introduces residual-to-dirty-image ratio `‖r̂‖₂/‖x_dirty‖₂` (×10⁻⁴ in tables): CLEAN lowest mean (≈5.1) in generic tests; uSARA/AIRI/R3D3 ≈6–8; plain R2D2 ≈13.5 with high dispersion; at DR ≈10⁵, optimization methods beat R2D2 on RDR despite comparable morphology. Robust R2D2 (2025ApJS) formalizes RDR(r̂, x_d) = ‖r̂‖₂/‖x_d‖₂ (≈10⁻³ scale): R2D2_A2,T2 ≈2.22×10⁻³ comparable to AIRI/uSARA (≈2.15–2.24×10⁻³), CLEAN ≈50% higher, old architecture ≈2× worse. HyperAIRI uses Frobenius RDR on hyperspectral cubes (≈2.3–2.6×10⁻³ for all methods, near truth reference 2.46×10⁻³)—high image SNR with matched data fidelity. S-R2D2 extends RDR to the sphere; planar R2D2 RDR degrades from 0.8×10⁻² to 14×10⁻² as Np increases while S-R2D2 stays ≈1–2×10⁻².

**Qualitative and proxy residual assessments.** SARA/PURIFY inspect dirty residuals (observed minus predicted dirty image) but reject flat residuals as sufficient fidelity indicator. Real-data examples compare residual-map σ (MROP 3C 273: classical 6.49×10⁻⁴ vs MROP 6.87×10⁻⁴). R2D2 Cygnus A real-data: homogeneous residuals around hotspots with U-WDSR vs structured residuals for U-Net. iR2D2 MRI paper uses RDR for adaptive stopping and reports order-of-magnitude lower RDR than baselines on knee data. CG-CLEAN and Asp-CLEAN discuss reaching noise floor in major loops—iteration-based convergence rather than normalized RDR.

**Flux and integrated-emission proxies (emerging real-data).** uSARA ASKAP validation uses source-boundary contours at multiples of measured residual RMS vs calculated image noise—evidence of low-surface-brightness recovery, not a normalized RDR score.

**Framework residual RMS (classic).** astroCAMP defines dirty-image RMS `σ_dirty` and residual-based dynamic range `DR = I_max / σ_res` as core Table 2 fidelity metrics (and uses dirty-image RMS in the example quality tuple); Section 6 does not tabulate those RMS values for the WSClean+IDG matrix.

## Popular measurement variants
- **Residual RMS or std (mJy/beam, μJy/PSF, Jy/beam):** WSClean, wideband MS-CLEAN, IDG, MWA real-data comparisons.
- **RDR = ‖residual dirty‖₂ / ‖dirty image‖₂:** R2D2, robust R2D2, HyperAIRI (Frobenius on cubes), S-R2D2 on sphere; typical scale 10⁻³–10⁻².
- **Residual-to-dirty ratio (×10⁻⁴ reporting):** R2D2 generic benchmark Table 2.
- **Dirty residual = observed dirty − predicted dirty from reconstruction:** SARA qualitative assessment; nearly flat residual can mislead (IUWT, RWBPDb8 examples).
- **Residual peak vs σ stopping criterion:** wideband simulations stop when residual peak < 3σ.
- **Residual-map σ on real data:** MROP vs classical VLA 3C 273 comparison.
- **Visual artifact/residual structure:** multifrequency CLEAN comparison figures; Asp vs MS residual correlation scale.

## Gaps and caveats
- **Two families under one column:** Classical papers rarely compute RDR ratios; R2D2 papers rarely report absolute residual RMS in mJy/beam—cohort tendencies differ sharply.
- **RDR ≠ truth fidelity:** HyperAIRI and R2D2 papers stress comparable RDR across methods while SNR spreads by tens of dB; WSClean can match RDR yet have far lower SNR.
- **Low residual can mislead:** Wrong spectral index with excellent residual RMS (multi-frequency); flat dirty residual with poor truth SNR (PURIFY, SARA).
- **Real-data gap for RDR:** Most normalized RDR values are simulated; real Cygnus A reports RDR ≈2.5–2.9×10⁻³ without ground-truth SNR pairing in same table.
- **Many RDR/Resid=1 classifications lack dedicated bullets** (Cygnus A R2D2, IRIS, ngVLA CLEAN review, GMCP, ALSB, clustered CLEAN, several classic flags)—classified from paper summaries without extracted residual metrics.
- **Figure/table inconsistencies:** WSClean MWA paper notes conflicting residual RMS labels (47 vs 62 mJy/PSF) unresolved in text.
