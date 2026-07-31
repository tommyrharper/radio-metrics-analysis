# UncCorr

## What this metric means here
Correlation-style checks on uncertainty maps from radio-interferometric reconstruction—whether predicted or bootstrap-derived uncertainty aligns with empirical spread, residual structure, or another uncertainty estimate after visibilities → gridding → iFFT → deconvolution. In this review, **UncCorr** flags papers that evaluate uncertainty *calibration* via correlation (or closely related agreement measures) rather than reporting credible intervals or scalar image fidelity alone.

**Taxonomy:** **Uncertainty** — evaluates whether estimated uncertainty corresponds to actual error or another reliability signal (distinct from `credible_interval`, which reports the uncertainty itself).

## How papers use it
Only one paper is tagged (Generative imaging for radio interferometry with fast uncertainty quantification, 2025arXiv250721270M). The extracted notes contain no dedicated summary bullet for this metric; it was classified from the paper’s overall uncertainty-quantification content. No concrete correlation coefficients, paired uncertainty fields, or comparison protocols appear in the notes.

## Popular measurement variants
- No distinct operationalizations are documented in the current note set beyond the general classification above.

## Gaps and caveats
- Extremely sparse sample (1 paper) with zero metric-specific extracted detail—this overview cannot summarize technical measurement patterns yet.
- Without a dedicated bullet, it is unclear which uncertainty fields are correlated (e.g. bootstrap vs posterior, pixel-wise vs aggregated) or what threshold defines acceptable calibration.
- Treat **UncCorr** as a placeholder column until more papers report explicit correlation-based UQ validation in extractable form.
