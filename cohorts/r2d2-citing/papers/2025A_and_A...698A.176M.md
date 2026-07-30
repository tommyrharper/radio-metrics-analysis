# How to make CLEAN variants faster using clustered components informed by the autocorrelation function

**Bibcode:** 2025A&A...698A.176M
**Authors:** Hendrik Müller, Sanjay Bhatnagar
**ADS:** https://ui.adsabs.harvard.edu/abs/2025A%26A...698A.176M/abstract
**arXiv:** https://arxiv.org/abs/2504.16058

## One-line summary
The paper introduces Autocorr-CLEAN, a non-ML acceleration of multiscale CLEAN deconvolution that fits clustered components to the residual's autocorrelation function to build adaptive basis functions, reporting up to an order-of-magnitude speed-up over classical CLEAN with comparable or better fidelity.

## Method
Autocorr-CLEAN is a two-stage minor-cycle scheme: (1) it CLEAN-solves the autocorrelation function of the residual (equivalently, the mirrored self-convolution of the residual in image space) to obtain a clustered component model of the emission structure; (2) it then performs multiscale-CLEAN-like subminor loop steps using this clustered model as a continuously-adapted, non-radial basis function (of the form ω = Σ(δᵢᵚ)^γ, γ=2 heuristically), avoiding explicit computation of the convolution during minor-loop iterations. This lets the algorithm fit multiple, non-radial components per subminor cycle while keeping per-iteration cost close to standard CLEAN. It is framed as a proof-of-concept tested "in isolation" on the minor loop, not integrated into a full calibration/gridding/flagging pipeline. Tests used synthetic VLA A-configuration data (12-hr tracks, 60s integrations) on Cygnus A (S-band, 2.052 GHz), Hercules A, and M106 (the latter two scaled to 1 Jy for low-SNR regimes), with thermal noise derived from SEFD/correlator efficiency/integration time/bandwidth.

## Performance / fidelity metrics used
- **Wall-clock runtime vs. residual level**: primary comparison metric (Fig. 5, bottom panels) — residual magnitude plotted against computation time; Autocorr-CLEAN reaches a given residual level significantly faster than classical CLEAN and faster than Asp-CLEAN in nearly all cases (Asp-CLEAN only ahead on the very first iteration due to Autocorr-CLEAN's larger up-front "head-on" processing cost).
- **Iteration counts**: residual magnitude vs. number of (sub)minor-cycle iterations (Fig. 4); Autocorr-CLEAN needs substantially fewer iterations, with the relation l << k << m (subminor-loop iterations l much less than clustered basis components k, much less than total CLEAN iterations m needed by classical CLEAN).
- **Theoretical computational complexity**: derived scaling m·N·(8l/k) (m = total CLEAN iterations, N = number of pixels, l = subminor-loop iterations, k = number of autocorrelation basis components) — used to argue the method avoids super-linear complexity growth relative to CLEAN.
- **Reconstruction fidelity**: norm difference between ground-truth sky model and reconstructed image (available since tests are synthetic); a logarithmic-difference variant (Appendix, Fig. 11) is also used to avoid results being dominated by bright compact structure, letting faint/diffuse emission fidelity be assessed separately.
- **Qualitative structure-type breakdown**: performance separately assessed on (i) bright point-like sources, (ii) extended bright structure, (iii) diffuse faint emission. All algorithms (CLEAN, Asp-CLEAN, Autocorr-CLEAN) perform similarly on bright compact/extended features; Autocorr-CLEAN notably outperforms Asp-CLEAN on diffuse faint emission recovery, with a mild tendency to overestimate faint noisy structure.
- **Speed-up claim**: "up to a magnitude [order of magnitude] faster than the classical CLEAN procedure," with reconstruction fidelity comparable to or better than multiscale variants (Asp-CLEAN).

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Non-ML speed/fidelity baseline for the deconvolution (minor-cycle) stage: demonstrates classical algorithmic acceleration (not learned) achieving order-of-magnitude CLEAN speed-ups, useful as a comparison point against R2D2-style learned deconvolution for runtime and fidelity trade-offs.
