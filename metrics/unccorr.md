# UncCorr

## What this metric means here
**UncCorr** (`uncertainty_correlation`) covers correlation-style checks on uncertainty maps from radio-interferometric reconstruction—whether predicted or bootstrap-derived uncertainty aligns with empirical error, residual structure, or another uncertainty estimate after visibilities → gridding → iFFT → deconvolution. It flags uncertainty *calibration* via correlation (or closely related agreement measures), not credible intervals or scalar image fidelity alone.

**Taxonomy:** **Uncertainty** — evaluates whether estimated uncertainty corresponds to actual error or another reliability signal (distinct from `credible_interval`, which reports the uncertainty itself).

Root totals: classic = 0, emerging-ml = 0, r2d2-citing = 1 (grand total **1**). Binary `uncertainty_correlation: 0|1` flags are unchanged by the drill-down; subtype detail lives in `uncertainty_correlation_details` ([`site/detail/unccorr.html`](../site/detail/unccorr.html)).

## How papers use it
**Uncertainty–error Pearson correlation (r2d2-citing).** Generative imaging for radio interferometry with fast uncertainty quantification (2025arXiv250721270M, RI-GAN) reports Pearson correlation between per-pixel predicted uncertainty (std across posterior samples) and per-pixel absolute reconstruction error `|x_true − x_pred|`. With 32 samples: **GU-Net r = 0.69**, **U-Net r = 0.58** — GU-Net tracks true error better. An ablation shows both SNR and this correlation improve with sample count and plateau around 32 samples (low-N correlation interpreted as sample diversity / no mode collapse). Coverage of credible intervals is explicitly left as future work (not CredInt here).

## Drill-down taxonomy (second-level page)
See [`site/detail/unccorr.html`](../site/detail/unccorr.html) / `site/js/taxonomies/unccorr-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| Uncertainty–Error Correlation | Pearson uncertainty vs \|error\|; Other uncertainty–error agreement |
| Inter-Estimate Correlation | Pairwise uncertainty-map correlation |
| Comparative UncCorr | Higher / lower correlation than baseline; Correlation vs sample count |
| Unspecified UncCorr | Vague UQ-calibration mentions already flagged but not subtypeable |

**UncCorr Context** (correlation statistic, uncertainty source, error reference, sample count, simulation vs real, array) is reporting completeness only — not itself an UncCorr metric.

## Popular measurement variants
- **Pearson r (uncertainty vs \|error\|):** RI-GAN GU-Net / U-Net posterior-sample std maps vs absolute reconstruction error (only concrete operationalization in the current set).
- **Sample-count ablation of that correlation:** plateau around 32 posterior samples in RI-GAN.

## Gaps and caveats
- Extremely sparse sample (**1** paper); taxonomy slots for inter-estimate correlation and non-Pearson agreement exist for future papers but are empty.
- Credible-interval coverage is not UncCorr; RI-GAN flags coverage analysis as future work.
- Qualitative uncertainty maps without a numeric correlation/agreement score → UncCorr=0.
- Auto-matched `metric_details` text for this paper was a placeholder; subtype evidence is taken from the paper summary’s dedicated uncertainty–error correlation bullet.
