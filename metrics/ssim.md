# SSIM

## What this metric means here
**SSIM** in this review marks papers that report the structural similarity index as a reconstruction fidelity metric—typically comparing local means, variances, and cross-covariance of patches in the restored image against ground truth after the full imaging chain. Our column captures standard SSIM (1 = perfect match) used alongside or instead of pixel-wise error metrics.

## How papers use it
**POLISH super-resolution (emerging-ml).** The primary radio-astronomy SSIM user pairs SSIM with PSNR on DSA-2000 simulated radio-galaxy fields. Full-band (1300 MHz, 15 min PSF): POLISH mean SSIM 0.998±0.0016 vs CLEAN 0.989±0.007 (+0.009); narrow-band (10 MHz snapshot PSF): 0.988±0.0016 vs 0.976±0.009 (+0.012). Inputs and targets normalized to integer range; SSIM described as local structural/perceptual metric, less sensitive to global scaling than MSE but complementary to PSNR (which is astrometric-shift sensitive). Real VLA transfer has no SSIM—qualitative comparison only.

**Uncertainty-quantification reconstruction (r2d2-citing).** EVIL-Deconv / equivariant bootstrap paper reports median SSIM with NMSE in dB: CLEAN SSIM 0.296, PnP (DnCNN) 0.869, EVIL-Deconv 0.970 (NMSE 19.9 dB), at ~51 ms reconstruction time vs 794 ms CLEAN. SSIM here validates the fast deconv network used for UQ experiments, not a full visibility-to-image pipeline benchmark in isolation.

**MRI-transfer iR2D2 (r2d2-citing).** Interlaced R2D2 paper reports SSIM on magnitude reconstructions: iR2D2(U-WDSR) 0.96±0.05 vs R2D2 0.93±0.06, NC-PDNet 0.90±0.08, DDS 0.85±0.13—consistent with PSNR rankings on the same non-Cartesian benchmark.

## Popular measurement variants
- **Standard SSIM (mean over image):** POLISH vs CLEAN on simulated DSA-2000 skies; EVIL-Deconv vs PnP vs CLEAN.
- **SSIM on magnitude images:** iR2D2 MRI benchmark (|x⋆| vs |x̂|).
- **Reported with PSNR and/or NMSE:** always as part of a small metric bundle, never alone in the corpus.
- **Median vs mean aggregation:** EVIL-Deconv table uses medians; POLISH and iR2D2 use means ± std over validation sets.

## Gaps and caveats
- **Very sparse usage:** Only three papers report SSIM across all cohorts; most ML imaging papers prefer SNR/logSNR.
- **No real-sky SSIM:** All quantitative SSIM values are simulation-based (or MRI transfer); real VLA POLISH experiment lacks truth for SSIM.
- **Normalization dependence:** POLISH normalizes to integer range before SSIM/PSNR; definitions may differ from default SSIM implementations.
- **Limited dynamic-range stress:** SSIM values near 0.99 in POLISH runs may saturate discrimination among strong methods; EVIL-Deconv spread (0.3–0.97) shows wider separation.
- **DDRM explicitly omits SSIM** despite using PSNR/SNR/MSE—authors note SSIM is common elsewhere but not used in that paper.
- **Several SSIM=0 classifications** across the corpus reflect non-use; no papers beyond the three above contribute extracted SSIM bullets.
