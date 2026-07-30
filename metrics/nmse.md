# NMSE

## What this metric means here
**NMSE** in this review marks papers reporting normalized mean squared error—or its decibel form **NRMSE**—as a quantitative fidelity or accuracy metric somewhere in the radio interferometry imaging pipeline. Our column includes visibility-domain NMSE (forward-model accuracy) and image-domain NMSE against ground truth, without requiring a single normalization convention.

## How papers use it
**Visibility-domain NMSE (classic).** HVOX (2023) is the clearest classic use: NMSE between visibilities from direct point-source sky evaluation vs HVOX, chunked HVOX, NIFTY (DUCC W-gridder), and NIFTY 2D without w-term. Requested error targets are swept on direction-cosine and HEALPix meshes; monolithic HVOX tracks targets down to ~10⁻⁹ (FINUFFT upsampling floor); chunked HVOX slightly misses targets due to summed-block error; NIFTY exceeds requested accuracy by ~1 order; omitting w-term yields much larger error insensitive to target. HEALPix requires NIFTY bilinear interpolation (~1% error) before gridding—mesh conversion loss isolated from restored-image quality. This measures synthesis/analysis operator fidelity, not deconvolved image NMSE.

**Image-domain NMSE in dB (r2d2-citing).** EVIL-Deconv equivariant bootstrap paper defines `NMSE [-dB] = −20·log₁₀(‖x⋆−x̂‖₂/‖x⋆‖₂)` alongside SSIM: CLEAN 4.2 dB, PnP (DnCNN) 16.3 dB, EVIL-Deconv 19.9 dB (median), at 51 ms vs 794 ms CLEAN. Negative dB notation means higher is better (inverse of relative L₂ error)—distinct from HVOX’s fractional NMSE target.

**Classification without extracted image NMSE.** Several papers are flagged NMSE=1 from summaries but lack dedicated bullets: 1984 CLEAN enhancements, 2018 IDG (residual RMS reported, not NMSE), DDRM 2026 (uses MSE/PSNR/SNR explicitly, not NMSE label), POLISH++ 2026 (PSNR robustness, no NMSE in notes). The column therefore mixes confirmed NMSE reporting with broader classification hits.

## Popular measurement variants
- **Fractional NMSE target on visibilities:** requested vs achieved accuracy sweep (HVOX vs NIFTY gridder)—operator-level, double-precision synthesis.
- **NMSE in decibels (image domain):** `−20·log₁₀(‖x⋆−x̂‖₂/‖x⋆‖₂)` — EVIL-Deconv benchmark vs CLEAN and PnP.
- **Related but distinct: MSE with PSNR/SNR:** DDRM reports MSE and PSNR = 10·log₁₀(MAX/MSE) but not NMSE by name.
- **Chunked vs monolithic accumulation:** HVOX chunked mode needs tighter per-block targets to hit global NMSE.

## Gaps and caveats
- **Rare in imaging benchmarks:** Only six NMSE-flagged papers; SNR and residual metrics dominate restored-image evaluation.
- **Domain split:** HVOX NMSE is visibility forward-model accuracy; EVIL-Deconv NMSE is image truth error—same column, different pipeline stages.
- **Sign/scale conventions:** HVOX uses fractional NMSE targets (10⁻⁹ floor); EVIL-Deconv uses positive dB where larger is better—easy to misread across papers.
- **No end-to-end restored-image NMSE from HVOX:** gridding accuracy is not propagated to a deconvolved image NMSE in the notes.
- **Four of six classifications lack dedicated bullets** (1984 CLEAN, 2018 IDG, DDRM, POLISH++)—rely on paper-page context or summary-level flags only.
- **NRMSE label unused in notes:** column is `nmse_nrmse` but extracted text only shows NMSE formulations explicitly.
