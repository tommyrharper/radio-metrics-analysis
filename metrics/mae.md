# MAE

## What this metric means here
**MAE (mean absolute error)** in this review flags papers that report mean absolute error as a reported performance metric in the radio interferometry imaging literature surveyed here. In the current corpus it is *not* used as a standard restored-image pixel fidelity score against sky truth; our column captures any MAE reporting tied to the imaging or inference workflow.

## How papers use it
**Parameter-regression MAE (r2d2-citing, EHT context).** The sole extracted MAE use is ZINGULARITY (2025A&A): mean absolute error tracks Bayesian neural-network regression performance for physical parameters inferred from Event Horizon Telescope data—spin, R_high, inclination, and position angle—on training vs validation sets across epochs (Fig. 4 validation curves). This is downstream inference accuracy on source parameters, not MAE between reconstructed and true radio sky brightness maps after gridding, iFFT, and deconvolution.

No other paper in the notes reports image-domain MAE, flux MAE, or visibility MAE as a headline imaging fidelity metric.

## Popular measurement variants
- **MAE on inferred physical parameters (EHT):** spin, R_high, inclination, position angle—training/validation curves over epochs, qualitative reporting in extracted text without single summary scalars.
- **(Not observed in corpus) Pixel-wise image MAE against ground truth:** absent from all cohort notes despite being common in general ML imaging.

## Gaps and caveats
- **Extremely sparse:** Only one paper (ZINGULARITY) contributes MAE content; the column is effectively unused for interferometric image reconstruction fidelity in this review.
- **Scope mismatch risk:** MAE here measures parameter regression, not brightness reconstruction—readers should not equate this column with image MAE used in computer vision papers.
- **No numeric summary in notes:** Validation-curve behaviour is described qualitatively; extracted text does not give final MAE values per parameter.
- **All other MAE=0 papers:** the vast majority of the corpus does not report MAE at all; no classic or emerging-ml imaging paper in the notes uses MAE on restored images.
