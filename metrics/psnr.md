# PSNR

## What this metric means here
**PSNR** in this review flags papers that report peak signal-to-noise ratio as a pixel-wise reconstruction fidelity metric against known truth (or normalized reference images) after gridding, iFFT, and deconvolution or learned reconstruction. Our column covers PSNR in decibels on restored image pixels, including both standard `10·log₁₀` and `20·log₁₀` formulations used in the literature.

Binary `psnr: 0|1` flags are unchanged by the drill-down; subtype detail lives in `psnr_details` ([`site/detail/psnr.html`](../site/detail/psnr.html); mirror [`data/psnr-details.json`](../data/psnr-details.json)). Grand total **6** PSNR-positive papers (classic 1, emerging-ml 1, r2d2-citing 4).

## How papers use it
**Deep-learning super-resolution (emerging-ml).** POLISH (2022) is the main radio-focused PSNR user: PSNR in dB as pixel-wise truth metric alongside SSIM on DSA-2000 simulated radio-galaxy skies (normalized integer range, 0.5 μJy/pixel noise, 3× upsampling). Mean PSNR ≈55 dB for POLISH vs ≈47–50 dB for image-plane CLEAN (+5.9 to +7.7 dB); PSF-mismatch ablations show PSNR > 50 dB even outside training warp range. Real VLA transfer is qualitative only—no PSNR on observed data.

**R2D2-citing extensions and diffusion.** iR2D2 MRI paper reports PSNR on magnitude images: `10·log₁₀(NM²/‖|x⋆|−|x̂|‖₂²)` with iR2D2(U-WDSR) at 40.21±6.67 dB vs R2D2 at 35.08±4.67 dB (+5.13 dB), advantage largest at high DR. CG-CLEAN (2026) defines linear and logarithmic PSNR on synthetic Cygnus A and ENZO data: `PSNR = 20 log₁₀(max(I)/‖θ−I‖)` and `PSNR_log = 20 log₁₀(max(log I)/‖log θ − log I‖)`, with CG-CLEAN leading standard CLEAN. DDRM (2026) uses flux-normalized `PSNR = 10·log₁₀(MAX/MSE)`, MAX = 1, swept vs diffusion sampling steps K (45 dB at K=10 to 62.9 dB at K=1000 on VLA; 61–63 dB on EHT/ALMA configs).

**Robustness and capability framing.** POLISH++ (2026) uses PSNR in PSF-warp robustness experiments (γ ∈ [0,30]); authors note PSNR is *more* sensitive to model mismatch than visual quality, flagging it as a limited fidelity proxy under calibration error. No head-to-head PSNR vs R2D2 on shared data in that paper—comparisons to R2D2 are qualitative via capability table (max image size, DR).

**Framework-defined quality suite (classic).** astroCAMP (2025) lists PSNR/SSIM as a core Table 2 algorithmic-quality pair (`10 log₁₀(I_max²/MSE)` vs reference), alongside dirty-image RMS and dynamic range, inside a multi-objective co-design quality tuple. The WSClean+IDG experimental release measures system/energy metrics and intentionally skips computing these quality scores pending community tolerances—so PSNR is defined and formulated, not tabulated as a WSClean result in that paper.

## Drill-down taxonomy (second-level page)
See [`site/detail/psnr.html`](../site/detail/psnr.html) / `site/js/taxonomies/psnr-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| Measured PSNR (Absolute) | 10·log₁₀ PSNR; 20·log₁₀ linear PSNR; Log-domain PSNR (PSNR_log) |
| Comparative PSNR | Higher / lower PSNR than baseline; PSNR gain / delta (dB) |
| PSNR vs Parameter / Ablation | PSNR vs hyperparameter / perturbation; Training / fine-tuning peak PSNR |
| Framework / Defined PSNR | Named core quality metric (no tabulated run values) |
| Unspecified PSNR | Vague PSNR mentions already flagged psnr=1 but not subtypeable |

**PSNR Context** (formulation, MAX / peak definition, image domain / normalisation, simulation vs real, frequency, array) is reporting completeness only — not itself a PSNR metric.

## Popular measurement variants
- **10·log₁₀(MAX/MSE) with MAX = 1:** DDRM on flux-normalized images; reported with MSE and alternate SNR definition.
- **10·log₁₀(I_max² / MSE) vs reference:** astroCAMP Table 2 framework definition (scikit-image / OpenCV).
- **10·log₁₀(NM² / squared L₂ error on magnitudes):** iR2D2 non-Cartesian MRI benchmark (M = max pixel, N = image size).
- **20·log₁₀(max(I) / reconstruction error):** CG-CLEAN linear PSNR on synthetic interferometric images.
- **20·log₁₀(max(log I) / log-domain error):** CG-CLEAN PSNR_log — faint-emission analogue, not classified under logSNR column.
- **Normalized integer-range PSNR (dB):** POLISH DSA-2000 simulations before/after upsampling; sensitive to astrometric shifts per paper.
- **PSNR vs training/perturbation parameter:** POLISH PSF warp γ ablation; POLISH++ fine-tuning convergence tracked via peak PSNR epoch.

## Gaps and caveats
- **Still uncommon as a measured score:** Most ML imaging papers prefer SNR/logSNR; PSNR appears in a minority of corpus papers.
- **Inconsistent dB base and dynamic range:** Mix of 10·log₁₀ and 20·log₁₀ definitions; magnitude-only vs complex/real image; MAX from data vs fixed normalization.
- **Astrometric sensitivity:** POLISH notes PSNR penalizes small shifts that may be visually acceptable.
- **Model-mismatch paradox:** POLISH++ reports PSNR degrades under PSF perturbation faster than perceived image quality—caveat for using PSNR alone in calibration-error regimes.
- **Real-data gap:** No PSNR on real interferometric fields with unknown truth in the extracted notes (VLA transfer is visual only).
- **Framework vs measured:** astroCAMP illustrates the opposite extreme—PSNR is a named core metric in the co-design backbone but not numerically evaluated in the published WSClean+IDG runs.
