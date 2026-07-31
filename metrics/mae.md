# MAE

## What this metric means here
**MAE (mean absolute error)** in this review flags papers that report mean absolute error as a reported performance metric in the radio interferometry imaging literature surveyed here. In the current corpus it is *not* used as a standard restored-image pixel fidelity score against sky truth; our column captures any MAE reporting tied to the imaging or inference workflow.

Root total: **1** MAE-positive paper (r2d2-citing). Binary `mae: 0|1` flags are unchanged by the drill-down; subtype detail lives in `mae_details` ([`site/detail/mae.html`](../site/detail/mae.html)).

## How papers use it
**Parameter-regression MAE (r2d2-citing, EHT context).** The sole extracted MAE use is ZINGULARITY (2025A&A...698A..61J): mean absolute error tracks Bayesian neural-network regression performance for physical parameters inferred from Event Horizon Telescope data—spin, R_high, inclination, and position angle—on training vs validation sets across epochs (Fig. 4 validation curves). This is downstream inference accuracy on source parameters, not MAE between reconstructed and true radio sky brightness maps after gridding, iFFT, and deconvolution.

No other paper in the notes reports image-domain MAE, flux MAE, or visibility MAE as a headline imaging fidelity metric.

## Drill-down taxonomy (second-level page)
See [`site/detail/mae.html`](../site/detail/mae.html) / `site/js/taxonomies/mae-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| Parameter-Regression MAE | Physical-parameter MAE; Other parameter-regression MAE |
| Image-Domain MAE | Pixel MAE vs ground truth; Other image-domain MAE |
| Unspecified MAE | Vague MAE mentions already flagged mae=1 but not subtypeable |

**MAE Context** (target parameters, train vs validation, domain, simulation vs real, frequency, array) is reporting completeness only — not itself an MAE metric.

Current subtype count: **1** paper in Parameter-Regression / Physical-parameter MAE (ZINGULARITY). Image-Domain and Unspecified have zero papers in this corpus.

## Popular measurement variants
- **MAE on inferred physical parameters (EHT):** spin, R_high, inclination, position angle—training/validation curves over epochs, qualitative reporting in extracted text without single summary scalars.
- **(Not observed in corpus) Pixel-wise image MAE against ground truth:** absent from all cohort notes despite being common in general ML imaging.

## Gaps and caveats
- **Extremely sparse:** Only one paper (ZINGULARITY) contributes MAE content; the column is effectively unused for interferometric image reconstruction fidelity in this review.
- **Scope mismatch risk:** MAE here measures parameter regression, not brightness reconstruction—readers should not equate this column with image MAE used in computer vision papers.
- **No numeric summary in notes:** Validation-curve behaviour is described qualitatively; extracted text does not give final MAE values per parameter.
- **All other MAE=0 papers:** the vast majority of the corpus does not report MAE at all; no classic or emerging-ml imaging paper in the notes uses MAE on restored images.
