# RDR

## What this metric means here
**RDR** is the residual-to-dirty ratio `‖r̂‖₂ / ‖x_dirty‖₂` (or Frobenius analogue on cubes/spheres) as used in the R2D2 family — a normalised data-fidelity score (lower = cleaner fit to the measured visibilities after imaging/deconvolution). It is **not** absolute residual RMS in Jy/beam (see **RMS**).

Classic cohort almost never reports this normalised ratio (classic RDR total = 0 after the split). Emerging-ml and r2d2-citing still need a careful RMS vs RDR pass; site data currently parks their old combined `rdr_residual` flag on **RDR** with `rms: 0` as a temporary placeholder.

## How papers use it
**RDR as quantitative data-fidelity metric (emerging-ml + r2d2-citing).** R2D2 (2024ApJS) introduces residual-to-dirty-image ratio `‖r̂‖₂/‖x_dirty‖₂` (×10⁻⁴ in tables): CLEAN lowest mean (≈5.1) in generic tests; uSARA/AIRI/R3D3 ≈6–8; plain R2D2 ≈13.5 with high dispersion; at DR ≈10⁵, optimization methods beat R2D2 on RDR despite comparable morphology. Robust R2D2 (2025ApJS) formalizes RDR(r̂, x_d) = ‖r̂‖₂/‖x_d‖₂ (≈10⁻³ scale): R2D2_A2,T2 ≈2.22×10⁻³ comparable to AIRI/uSARA (≈2.15–2.24×10⁻³), CLEAN ≈50% higher, old architecture ≈2× worse. HyperAIRI uses Frobenius RDR on hyperspectral cubes (≈2.3–2.6×10⁻³ for all methods, near truth reference 2.46×10⁻³)—high image SNR with matched data fidelity. S-R2D2 extends RDR to the sphere; planar R2D2 RDR degrades from 0.8×10⁻² to 14×10⁻² as Np increases while S-R2D2 stays ≈1–2×10⁻².

**Qualitative and proxy residual assessments (not RDR).** SARA/PURIFY inspect dirty residuals (observed minus predicted dirty image) but reject flat residuals as sufficient fidelity indicator — qualitative residual discussion alone is neither RMS nor RDR. R2D2 Cygnus A real-data: homogeneous residuals around hotspots with U-WDSR vs structured residuals for U-Net. iR2D2 MRI paper uses RDR for adaptive stopping and reports order-of-magnitude lower RDR than baselines on knee data. CG-CLEAN and Asp-CLEAN discuss reaching noise floor in major loops—iteration-based convergence rather than normalised RDR.

## Popular measurement variants
- **RDR = ‖residual dirty‖₂ / ‖dirty image‖₂:** R2D2, robust R2D2, HyperAIRI (Frobenius on cubes), S-R2D2 on sphere; typical scale 10⁻³–10⁻².
- **Residual-to-dirty ratio (×10⁻⁴ reporting):** R2D2 generic benchmark Table 2.
- **Dirty residual = observed dirty − predicted dirty from reconstruction:** often qualitative only (SARA); not RDR unless the normalised ratio is reported.

## Gaps and caveats
- **Two families formerly under one column:** Classical papers rarely compute RDR ratios; R2D2 papers rarely report absolute residual RMS in mJy/beam—hence the classic-first split into RMS and RDR.
- **RDR ≠ truth fidelity:** HyperAIRI and R2D2 papers stress comparable RDR across methods while SNR spreads by tens of dB; WSClean can match RDR yet have far lower SNR.
- **Real-data gap for RDR:** Most normalised RDR values are simulated; real Cygnus A reports RDR ≈2.5–2.9×10⁻³ without ground-truth SNR pairing in same table.
- **Many former RDR/Resid=1 classifications lack dedicated bullets** (Cygnus A R2D2, IRIS, ngVLA CLEAN review, GMCP, ALSB, clustered CLEAN)—pending careful reclassification for non-classic cohorts.
- **Classic status:** After reclassification, classic RDR=0 for all 23 papers; absolute residual scores live under **RMS**.
