# RDR

## What this metric means here
**RDR** is the residual-to-dirty ratio `‖r̂‖₂ / ‖x_dirty‖₂` (or Frobenius analogue on cubes/spheres) as used in the R2D2 family — a normalised data-fidelity score (lower = cleaner fit to the measured visibilities after imaging/deconvolution). It is **not** absolute residual RMS in Jy/beam (see **RMS**).

Root totals after the split: classic RDR = 0, emerging-ml RDR = 1 (2024ApJS..273....3A), r2d2-citing RDR = 6 (grand total **7**).

## How papers use it
**RDR as quantitative data-fidelity metric (emerging-ml + r2d2-citing).** R2D2 (2024ApJS) introduces residual-to-dirty-image ratio `‖r̂‖₂/‖x_dirty‖₂` (×10⁻⁴ in tables): CLEAN lowest mean (≈5.1) in generic tests; uSARA/AIRI/R3D3 ≈6–8; plain R2D2 ≈13.5 with high dispersion; at DR ≈10⁵, optimization methods beat R2D2 on RDR despite comparable morphology. Robust R2D2 (2025ApJS..280...63A) formalizes RDR(r̂, x_d) = ‖r̂‖₂/‖x_d‖₂ (≈10⁻³ scale): R2D2_A2,T2 ≈2.22×10⁻³ comparable to AIRI/uSARA (≈2.15–2.24×10⁻³), CLEAN ≈50% higher, old architecture ≈2× worse. HyperAIRI (2026ApJS..283....9T) uses Frobenius RDR on hyperspectral cubes (≈2.3–2.6×10⁻³ for all methods, near truth reference 2.46×10⁻³)—high image SNR with matched data fidelity. S-R2D2 (2025MNRAS.542..426T) extends RDR to the sphere; planar R2D2 RDR degrades from 0.8×10⁻² to 14×10⁻² as Np increases while S-R2D2 stays ≈1–2×10⁻². iR2D2 MRI (2025arXiv250309559C) uses RDR = ‖r‖₂/‖x_b‖₂ for adaptive stopping and reports order-of-magnitude lower RDR than baselines on knee data. ALSB / generalized soft-thresholding papers (2026AJ....171...44Y, 2026AJ....171..220Y) tabulate image-domain data fidelity σ = ‖r̂‖₂/‖x_dirty‖₂ following the R2D2 convention.

**Not RDR after reclassification.** uSARA ASKAP (2023MNRAS.522.5558W) reports absolute residual-map rms and contour multiples → **RMS**, not RDR. PRIMO (2023ApJ...943..144M) shows visibility-amplitude/closure-phase residual plots normalised by observational uncertainties — neither absolute residual RMS nor ‖r̂‖₂/‖x_dirty‖₂ → both flags 0. In r2d2-citing, Cygnus A R2D2 real-data (2024ApJ...966L..34D) and MROP (2025MNRAS.543.1727L) report residual dirty-image / residual-map **standard deviation** → **RMS**, not RDR. Autocorr-CLEAN residual-magnitude curves, IRIS Fourier-space χ², Momentum-CLEAN qualitative residual/DR discussion, and ngVLA perspective figure-based residual convergence → both 0 (former combined `rdr_residual=1` false positives under the split).

**Qualitative and proxy residual assessments (not RDR).** SARA/PURIFY inspect dirty residuals (observed minus predicted dirty image) but reject flat residuals as sufficient fidelity indicator — qualitative residual discussion alone is neither RMS nor RDR. R2D2 Cygnus A real-data: homogeneous residuals around hotspots with U-WDSR vs structured residuals for U-Net. CG-CLEAN and Asp-CLEAN discuss reaching noise floor in major loops—iteration-based convergence rather than normalised RDR.

## Popular measurement variants
- **RDR = ‖residual dirty‖₂ / ‖dirty image‖₂:** R2D2, robust R2D2, HyperAIRI (Frobenius on cubes), S-R2D2 on sphere; typical scale 10⁻³–10⁻².
- **Residual-to-dirty ratio (×10⁻⁴ reporting):** R2D2 generic benchmark Table 2.
- **Image-domain data fidelity σ (same ratio):** ALSB / soft-thresholding papers following Aghabiglou et al.
- **Dirty residual = observed dirty − predicted dirty from reconstruction:** often qualitative only (SARA); not RDR unless the normalised ratio is reported.

## Gaps and caveats
- **Two families formerly under one column:** Classical papers rarely compute RDR ratios; many R2D2-family papers report RDR without absolute residual RMS in mJy/beam—hence the split into RMS and RDR.
- **RDR ≠ truth fidelity:** HyperAIRI and R2D2 papers stress comparable RDR across methods while SNR spreads by tens of dB; WSClean can match RDR yet have far lower SNR.
- **Real-data gap for RDR:** Most normalised RDR values are simulated; real Cygnus A RDR in robust R2D2 is ≈2.5–2.9×10⁻³; the earlier Cygnus A letter reports residual std, not the normalised ratio.
- **Classic / emerging / r2d2 status:** Classic RDR=0 for all 23 papers; emerging-ml RDR=1 only for 2024ApJS..273....3A; r2d2-citing RDR=6. Absolute residual scores live under **RMS**.
