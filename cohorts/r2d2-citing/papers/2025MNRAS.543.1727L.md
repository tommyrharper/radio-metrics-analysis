# MROP: modulated rank-one projections for compressive radio interferometric imaging

**Bibcode:** 2025MNRAS.543.1727L
**Authors:** Olivier Leblanc, Chung San Chu, Laurent Jacques, Yves Wiaux
**ADS:** https://ui.adsabs.harvard.edu/abs/2025MNRAS.543.1727L/abstract
**arXiv:** https://arxiv.org/abs/2504.18446 (v2, revised Dec 2025, matches the published MNRAS version, including a real-data section)

## One-line summary
MROP is a data-acquisition-stage compression scheme that reduces radio-interferometric visibility data volume from O(Q²B) to a tunable O(PM) via random rank-one projections of the antenna covariance matrix combined with random temporal modulations, while preserving image reconstruction quality comparable to using the full (classical) visibility data.

## Method
For Q antennas and B short-time integration batches, MROP first compresses the Q×Q batchwise covariance matrix into P random rank-one projections (ROPs), computed either as random beamforming at the antenna level or as post-correlation compression on standard correlator output (two equivalent "dual" implementations). It then compresses across the B batches using M random modulation vectors, trading B for M ≪ B. The method is shown to preserve i.i.d. Gaussian measurement noise regardless of the visibility-weighting scheme (natural, uniform, Briggs), is self-calibration-friendly, and its memory/compute cost is analysed in detail against the classical model, subsampling, baseline-dependent averaging (BDA), a simpler "CROP" (unmodulated ROP) variant, and random Gaussian projections/IROP (deemed computationally non-viable). Images are reconstructed from the compressed measurements using the unconstrained Sparsity Averaging Reweighted Analysis (uSARA) optimisation algorithm — not R2D2/AIRI or a deep-learning deconvolution step. Validation is done both on simulations (VLA, 27 antennas; MeerKAT, 64 antennas; 4 ground-truth images across 100 dynamic-range/uv-coverage combinations) and, in the published version, on real VLA data of quasar 3C 273.

## Performance / fidelity metrics used
- **SNR (dB)**, defined as SNR(ũ,u) = 20·log₁₀(‖u‖₂ / ‖u−ũ‖₂), comparing reconstructed image ũ to ground truth u. Used as the primary quantitative fidelity metric throughout.
- **logSNR** — SNR computed on a logarithmically-remapped version of the images (rlog mapping using the image dynamic range d), used because target dynamic ranges are very high (10³–10⁵); captures faint/diffuse emission fidelity better than linear SNR.
- **Dynamic range (d)** — reciprocal of the faintest ground-truth intensity; images spanning d ∈ [10³,10⁵] were used, split into "low" ([10³,10⁴]) and "high" ([10⁴,10⁵]) categories for reporting.
- **Data-to-image ratio (D/N)** and **data-to-visibility ratio (D/VB)** — used as "compression ratio" axes (D = data size of the compressed model: PM for MROP, VB_sub for subsampling, VB_bda for BDA, P_crop·B for CROP).
- **Residual dirty image** and its **standard deviation** — used as a data-fidelity/goodness-of-fit diagnostic (should look noise-like if reconstruction succeeded).
- **Relative error map** — per-pixel relative difference between ground truth and reconstruction (only where ground truth exceeds assumed noise level).
- **Average per-iteration runtime** (uSARA, GPU: single Nvidia A40) — used to compare computational cost across sensing models.
- **Reported values / comparisons:**
  - Reference classical-model quality: VLA (VB/N=14.5), low/high DR → (SNR,logSNR) = (30.73, 20.90) / (28.50, 20.15) dB; MeerKAT (VB/N=83.1), low/high DR → (30.13, 22.08) / (27.95, 19.84) dB.
  - Classical, BDA, CROP (P_crop·B ≈ 2N), and MROP (PM ≈ N) all converge to very similar SNR/logSNR — i.e. MROP matches classical-model quality once D/N ≈ 1 (data size ≈ image size), roughly an order of magnitude below the raw visibility count (VB/N up to ~83). MROP is more memory-efficient than CROP for equal quality (O(N) vs O(2N)).
  - Below D/N ≈ 1, quality degrades progressively; e.g. for the Abell 2034 (VLA, d=8.6×10⁴) example, dropping D/N from ~1 to 3.8×10⁻¹ costs 0.1 dB (SNR) / 0.7 dB (logSNR); for 3c353 (MeerKAT, d=1.1×10³), the same drop costs 1.1 dB / 2.2 dB.
  - Plain subsampling performs markedly worse than MROP/CROP/BDA at equivalent data size.
  - MROP/CROP iterations are always less than 2x the classical model's per-iteration time.
  - **Real-data result (VLA, 3C 273, X band, D/N ≈ 0.98 ≈ N vs. VB/N=11.1):** MROP and classical reconstructions show nearly identical peak intensities (0.07) and recover features across 4 orders of magnitude; residual-map standard deviations are highly comparable (classical: 6.49×10⁻⁴; MROP: 6.87×10⁻⁴), confirming reconstruction fidelity is preserved at high compression.
  - No comparison to CLEAN, R2D2, or AIRI is performed — uSARA is the sole reconstruction algorithm used; R2D2 is explicitly named as future work for validating MROP with learned deconvolution methods.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
This paper operates entirely upstream of gridding, at the data-acquisition/compression stage — it does not touch gridding, iFFT, or deconvolution itself, but its uSARA-based reconstructions (and its explicit suggestion that R2D2 be tested as an alternative deconvolution back-end) make it directly relevant to whether an ML deconvolution pipeline could remain robust when fed heavily compressed (MROP-format) rather than classical gridded visibility data.
