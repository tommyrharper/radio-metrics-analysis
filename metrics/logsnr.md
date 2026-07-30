# logSNR

## What this metric means here
**logSNR** in this review denotes papers that report SNR *after* a logarithmic intensity remapping of the reconstruction and ground truth, used to stress fidelity to faint, low-surface-brightness structure in high-dynamic-range radio images. It complements linear SNR, which is dominated by bright pixels. Our column flags any such log-transformed SNR variant, regardless of the exact transform parameterization.

## How papers use it
**R2D2-family standard (r2d2-citing + emerging-ml).** The dominant pattern applies a per-image reversible log map `r_log(x) = x_max·log_a(a·x/x_max + 1)` with parameter *a* set to the target or known dynamic range, then computes SNR on the transformed images. The original R2D2 paper (2024ApJS) reports log S/N separately from linear S/N on a 200-problem generic test: CLEAN ~10 dB vs R2D2 ~25 dB logSNR, a much larger gap than on linear SNR, highlighting faint-structure recovery. Subsequent R2D2, AIRI, S-R2D2, HyperAIRI, and robustness papers pair logSNR with linear SNR in tables, per-iteration plots, and Briggs-weighting sweeps; R2D2_A2,T2 peaks in logSNR at natural weighting (ρ_br = 1) while linear SNR peaks at ρ_br = 0.

**Optimization and non-convex regularization.** ISCAD (2025) defines S/N_log via log₁₀ stretch with noise floor ε: `20·log₁₀(‖log₁₀(x/ε + I_N)‖₂ / ‖…error…‖₂)`. GMCP (2026) uses SNRlog following Thouvenin et al. with a similar log-stretch; GMCP leads R2D2 on aggregate SNRlog in VLA/3C353 tables but qualitative comparison notes R2D2 preserves diffuse emission better despite lower log-scale scores on some features.

**Coverage, resolution, and compression experiments.** MROP reports (SNR, logSNR) pairs for VLA and MeerKAT at low/high dynamic range; logSNR degrades faster than linear SNR when data size D/N drops below ~1 (e.g. 0.7 dB vs 0.1 dB loss for Abell 2034). S-R2D2 tracks logSNR across spherical pixel counts Np; best logSNR at Np = 600² (SR = 2.25) while planar R2D2 logSNR collapses at high resolution. AIRI (2025) fixes transform parameter a = 2.5×10³ (lowest DR in the test set) for cross-method consistency.

**Cross-domain and MRI analogues.** The scalable non-Cartesian MRI R2D2 paper uses the same logSNR concept with DR as transform parameter, reporting paired (SNR, logSNR) vs acceleration factor and iteration count—treated as a direct analogue of visibility undersampling in radio. Learned imaging for varying coverage uses simpler `SNR(log₁₀(x_true), log₁₀(x_pred))`.

## Popular measurement variants
- **R2D2 reversible log map:** `r_log(x) = x_max·log_a(a·x/x_max + 1)` then standard L₂ SNR in dB — R2D2, AIRI, S-R2D2, HyperAIRI, MROP, robust R2D2 ablations.
- **log_a(a·x + 1) with DR = a:** used in MRI-transfer R2D2 paper before SNR computation.
- **log₁₀ pixel stretch with ε floor:** ISCAD S/N_log and GMCP SNRlog variants.
- **Plain log₁₀ on truth and prediction:** Learned RI for varying coverage (no DR-parameterized map).
- **Paired reporting:** almost always alongside linear SNR in tables, boxplots, or per-iteration curves; rarely standalone.

## Gaps and caveats
- **Transform parameter choices differ:** a may be ground-truth DR, lowest DR in the test suite (AIRI: 2.5×10³), or image-specific max; cross-paper logSNR values are not directly comparable without the transform definition.
- **Aggregate vs visual trade-offs:** GMCP vs R2D2 shows higher SNRlog can coexist with staircasing or suppressed faint emission — logSNR alone may not capture preferred morphology.
- **Higher variance:** Training-realization spreads are larger for logSNR than linear SNR (AIRI: ~4 dB vs ~1.5 dB across 15 denoisers).
- **Sparse classic use:** logSNR is essentially absent from the classic cohort; it emerges with high-DR simulated benchmarks in emerging-ml and r2d2-citing.
- **Some logSNR classifications lack dedicated bullets** in extraction notes (papers flagged from summaries only).
