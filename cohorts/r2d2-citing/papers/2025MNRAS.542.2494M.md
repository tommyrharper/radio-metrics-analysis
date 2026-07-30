# Strong gravitational lensing with upcoming wide-field radio surveys

**Bibcode:** 2025MNRAS.542.2494M
**Authors:** Samuel McCarty, Liam Connor
**ADS:** https://ui.adsabs.harvard.edu/abs/2025MNRAS.542.2494M/abstract
**arXiv:** https://arxiv.org/abs/2412.01746

## One-line summary
This paper forecasts strong gravitational lens discovery yields for upcoming wide-field radio surveys (DSA-2000, SKA-Mid, VLASS), predicting O(10⁴–10⁵) new lenses, and — beyond forecasting alone — includes a concrete demonstration using the deep-learning super-resolution/deconvolution method POLISH to recover lenses with image separations near or below the PSF scale.

## Method
The authors build a lensing-rate forecast pipeline combining deflector and source population models (galaxy, group, and cluster lenses) with survey-specific noise levels (σn) and PSF sizes (θPSF) for DSA-2000, SKA-Mid (AA* and AA4 configurations), and VLASS, computing lensing optical depth and applying discoverability criteria based on image separation Δθ relative to θPSF and total SNR of the lensed images. They adopt "conservative" (Δθ ≥ 3×θPSF, SNRtot ≥ 20, following Rezaei et al. 2022's CNN lens-finding study on simulated LOFAR data) and "optimistic" (Δθ ≥ θPSF, SNRtot ≥ 20) discoverability limits, the latter motivated explicitly by emerging super-resolution/ML imaging techniques. As a proof-of-concept, they train a POLISH network (a WDSR-architecture supervised super-resolution/image-plane deconvolution model, Connor et al. 2022) on forward-modelled synthetic DSA-2000 data (~3.3″ full-band-averaged PSF) with injected strongly lensed sources, showing that lenses undetectable in the dirty image become identifiable after POLISH reconstruction.

## Performance / fidelity metrics used
This is primarily a forecasting/survey paper, not a reconstruction-method paper, but it explicitly discusses imaging-fidelity/resolution requirements for lens *detectability* and reports a small original imaging demonstration:
- **Angular resolution / PSF (θPSF):** DSA-2000 θPSF = 2″ (top of 0.7–2 GHz band) to 3″ (band average, σn = 70 μJy/beam); SKA-Mid AA* θPSF = 1.3″ (σn = 2.7 μJy/beam), AA4 θPSF = 0.4″ (σn = 2 μJy/beam, 1.4 GHz).
- **Discoverability thresholds (from literature + adopted for this work):** image separation Δθ ≥ 3×θPSF (conservative, per Rezaei et al. 2022 CNN study) or Δθ ≥ θPSF (optimistic, assuming super-resolution); total SNR of combined lensed images SNRtot ≥ 20 (following Collett 2015; Wedig et al. 2025; Rezaei et al. 2022).
- **Baseline CNN lens-finder benchmark (cited, not original):** Rezaei et al. (2022) recover >90% of galaxy-scale lenses with a 0.008% false-positive rate on simulated ILT data, requiring 20σ detection and θE ≥ 3/2 beam size.
- **POLISH demonstration (original, qualitative):** trained on DSA-2000-PSF (~3.3″) forward-modelled sky images (800 images, 2048² px) with injected lenses and calibration-error perturbations; shown (Figure 6) to recover Einstein rings/arcs with separations below the PSF scale that are invisible in the undeconvolved "dirty image," and noted (citing Connor et al. 2022) to recover scales down to ~1″ for DSA-2000. No quantitative SNR/dynamic-range/purity/completeness metrics are reported for the POLISH reconstruction itself — the authors flag this as future work requiring physically realistic forward models with lensing.
- Real-world caveat cited: even the best optical/IR automated lens finders currently achieve purity ≲10% on real data (Pearce-Casey et al. 2025; Euclid Collaboration 2025).

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Directly relevant: the paper explicitly cites Aghabiglou et al. 2024 (R2D2) alongside Connor et al. 2022 (POLISH) and Mars et al. 2024 as examples of ML-based interferometric image reconstruction exploiting the deterministic, UV-sampling-derived PSF of radio interferometers, and argues that super-resolution/deep-learning deconvolution (of the R2D2/POLISH type) is a key enabling technology for pushing lens detectability below the classical PSF-limited resolution — directly motivating ML deconvolution work in the gridding→iFFT→deconvolution stage of the pipeline.
