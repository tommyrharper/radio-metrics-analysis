# Metric overviews

Cross-paper syntheses of how each canonical performance/fidelity metric is used in the extracted literature. Built from the cohort paper summaries (`cohorts/*/papers/*.md`) and used by the metrics webpage overview toggle.

## Taxonomy (webpage chart)

Canonical keys are grouped on the metrics webpage (`index.html` → `metricCategories`):

1. **Observational** — `snr`, `dynamic_range`, `rms`, `rdr`
2. **Computational** — `runtime`, `compute_cost`, `iterations`
3. **Fidelity** — `psnr`, `ssim`, `nmse_nrmse`, `mae`, `wasserstein`
4. **Scientific** — `flux_recovery`, `astrometric_accuracy`, `classification_metrics` (`spectral_accuracy` is listed in the taxonomy config for future use but is absent from the schema, so it is not plotted)
5. **Uncategorised** (fallback, only when present) — `logsnr`, `credible_interval`, `uncertainty_correlation`, `text_metrics`

Category and cohort filters combine; zero-total metrics for visible cohorts remain hidden. Chart order follows the category groups above.

## Overview files

| File | Metric |
|---|---|
| `snr.md` | SNR |
| `logsnr.md` | logSNR |
| `psnr.md` | PSNR |
| `ssim.md` | SSIM |
| `dr.md` | DR |
| `rms.md` | RMS |
| `rdr.md` | RDR |
| `nmse.md` | NMSE |
| `mae.md` | MAE |
| `flux-recovery.md` | Flux Recovery |
| `astrometric-accuracy.md` | Astrometric Accuracy |
| `runtime.md` | Runtime |
| `iters.md` | Iters |
| `credint.md` | CredInt |
| `unccorr.md` | UncCorr |
| `wasser.md` | Wasser |
| `class.md` | Class |
| `text.md` | Text |
| `compute.md` | Compute |

Each file covers: meaning in this review, how papers use it, popular measurement variants, and gaps/caveats.
