# fast-resolve: Fast Bayesian Radio Interferometric Imaging

**Bibcode:** 2024A&A...690A.387R
**Authors:** Jakob Roth, Philipp Frank, Hertzog L. Bester, Oleg M. Smirnov, Rüdiger Westermann, Torsten A. Enßlin
**ADS:** https://ui.adsabs.harvard.edu/abs/2024A%26A...690A.387R/abstract
**arXiv:** https://arxiv.org/abs/2406.09144

## One-line summary
Fast-resolve accelerates the Bayesian imaging algorithm resolve by combining it with CLEAN-style major/minor-cycle computational shortcuts, retaining full posterior (uncertainty-quantified) sky reconstructions while running 7x-144x faster.

## Method
Fast-resolve reformulates the radio-interferometric measurement equation as an image-space deconvolution problem instead of evaluating the full response R(I) at every likelihood evaluation. It projects the data to image space via R†N⁻¹ to get a dirty image, approximates the full response operator R' = R†N⁻¹R as a PSF convolution computed via FFT, and approximates the noise-covariance inverse N'⁻¹ via convolution with an optimized kernel K. It then runs CLEAN-inspired major/minor cycles: cheap minor cycles perform fast approximate Bayesian posterior inference (variational inference over image-space priors for diffuse emission and point sources), while occasional major cycles use the exact interferometric response to correct approximation errors accumulated in the minor cycles. Unlike CLEAN, the output is a full posterior distribution (with uncertainty maps) rather than a point-estimate CLEAN image. Implemented in JAX for GPU acceleration (resolve is NumPy/CPU-based).

## Performance / fidelity metrics used
- **Dynamic range** (VLA Cygnus A, 2052/4811/8427/13,360 MHz): fast-resolve achieves higher dynamic range than classical resolve, with visibly improved detail recovery in low-surface-brightness regions; resolution in high-surface-brightness regions (e.g. eastern hotspot) is on par with resolve and shows superresolution relative to multi-scale CLEAN.
- **Pixelwise relative posterior uncertainty maps**: reported at ~10⁻³-10⁻² in hotspot (bright) regions, increasing toward lower-surface-brightness areas — direct Bayesian uncertainty quantification not available from CLEAN.
- **Convergence / mean-squared residual** (in log-brightness) between successive iterations, used as the main convergence and accuracy diagnostic (Fig. 5), tracked over wall-clock time across hardware.
- **Runtime / speedup vs. resolve** (VLA Cygnus A, single channel, S-band) to reach residual ~10⁻³:
  - NVIDIA A100 GPU: ~10 min → **144x** speedup vs. resolve
  - NVIDIA RTX 3090 GPU: ~20 min → **72x** speedup
  - Intel Xeon CPU (8 cores): ~200 min → **7.2x** speedup
  - resolve (CPU baseline): 1416 min (~1 day)
- **Scalability demonstration** (MeerKAT ESO 137-006, ~400x larger dataset than the VLA case, multi-channel): fast-resolve completes in ~24 GPU-hours plus ~2 CPU-hours kernel precomputation over 25-28 major cycles — a dataset described as computationally out of reach for resolve; compared against convex-optimization/CLEAN-family results (Dabbech et al. 2022) that needed 900-3000 CPU-hours per band.
- **Imaging artifacts**: qualitative comparison — minimal artifacts around the Cygnus A hotspot, consistent with resolve; on MeerKAT data, fast-resolve shows somewhat higher background artifacts than convex-optimization maps, attributed via synthetic-data tests (Appendix D) to calibration imperfections rather than the algorithm itself.
- No explicit SNR/PSNR/normalized-RMSE metric against ground truth was reported (real-data study); fidelity is instead assessed via dynamic range, residual convergence, posterior uncertainty, and visual/artifact comparison to resolve and CLEAN-family methods.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Directly relevant: fast-resolve reframes the classic gridding/iFFT/deconvolution pipeline as an approximate, FFT-based PSF-convolution likelihood with CLEAN-like major/minor cycles, and pairs it with variational Bayesian inference for uncertainty-quantified reconstructions — a template for where ML/GPU-accelerated approximations could replace or augment resolve's exact (but expensive) response evaluation while preserving posterior uncertainty.
