# CredInt

## What this metric means here
Bayesian credible intervals and Highest Posterior Density (HPD) regions on reconstructed radio images or image structures—per-pixel error bars, regional uncertainty envelopes, or isocontours derived from a posterior or MAP potential after the visibility → gridding → iFFT → deconvolution chain. In this review, **CredInt** also covers closely related calibrated reconstruction intervals (posterior percentile bands; conformalized bootstrap pixel intervals) used to quantify reconstruction uncertainty rather than point-estimate fidelity alone.

**Taxonomy:** **Uncertainty** — describes reported posterior or inferential uncertainty (distinct from `uncertainty_correlation`, which evaluates whether estimated uncertainty tracks actual error).

Root totals: classic CredInt = 0, emerging-ml CredInt = 1, r2d2-citing CredInt = 4 (grand total **5**). Binary `credible_interval: 0|1` flags are unchanged by the drill-down; subtype detail lives in `credint_details` ([`site/detail/credint.html`](../site/detail/credint.html)).

## How papers use it
**HPD / Local Credible Intervals (QuantifAI, 2024RASTI...3..505L).** Defines HPD credible regions at level 100(1−α)% approximated analytically from the MAP potential (Pereyra 2017), uses a 99% HPD isocontour (α=0.01) for hypothesis tests on inpainted or blurred surrogate images, and reports per–16×16-superpixel Local Credible Intervals l_i = ξ+,Ωi − ξ−,Ωi with mean values 0.20, 0.08, 0.24, and 0.07 across four test images.

**Posterior sample intervals.** IRIS (2025arXiv250102473D) reports pixel-wise 16th–84th percentile ranges from score-based posterior samples (TARP-calibrated). fast-resolve (2024A&A...690A.387R) reports pixelwise relative posterior uncertainty maps (~10⁻³–10⁻² in hotspots). PRIMO (2023ApJ...943..144M) reports MCMC parameter posterior intervals via corner plots (eigenimage / structure parameters), not image-domain HPD/LCI tables.

**Bootstrap / conformal intervals (CARB, 2024arXiv241023178C).** Conformalized augmented equivariant bootstrap produces pixel-wise 90% intervals on EVIL-Deconv reconstructions, scored by mean ℓ2 interval-length ratio (0.34) and empirical coverage (91%).

## Drill-down taxonomy (second-level page)
See [`site/detail/credint.html`](../site/detail/credint.html) / `site/js/taxonomies/credint-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| HPD / Local Credible Intervals | HPD credible regions; Local Credible Intervals (LCIs); HPD hypothesis testing |
| Posterior Sample Intervals | Pixel percentile ranges; Relative posterior uncertainty maps; Parameter posterior intervals |
| Bootstrap / Conformal Intervals | Pixel confidence intervals; Interval length & empirical coverage |
| Unspecified CredInt | Vague Bayesian/UQ framing already flagged credible_interval=1 but not subtypeable |

**CredInt Context** (credible level, spatial aggregation, estimation method, simulation vs real, frequency, array) is reporting completeness only — not itself a CredInt metric.

Structured data: `credint_details` arrays on CredInt-positive papers in `data/papers-data.json` (optional mirror `data/credint-details.json`). Injector: `scripts/inject_credint_details.py`.

## Popular measurement variants
- **HPD credible regions** at a stated level 100(1−α)%, often approximated without MCMC from a MAP potential.
- **Hypothesis testing via HPD isocontours**—compare a surrogate image’s potential to a fixed-level HPD boundary (e.g. 99%) to accept or reject structural hypotheses.
- **Local Credible Intervals (LCIs)**—superpixel-scale Bayesian error-bar widths from root-finding on HPD boundaries, summarized by mean LCI per image.
- **Posterior percentile bands**—e.g. pixel-wise 16th–84th ranges from sampled posteriors.
- **Relative posterior uncertainty maps**—pixelwise relative UQ without tabulated HPD/LCI widths.
- **Parameter posterior intervals**—MCMC corner-plot intervals on structure / PCA coefficients.
- **Conformalized bootstrap pixel intervals**—interval length (ℓ2 ratio) and empirical coverage vs a target level.

## Gaps and caveats
- Sample is small (5 papers) and dominated by one detailed HPD/LCI source (QuantifAI); other positives use posterior-sample or bootstrap/conformal interval forms.
- Credible level, spatial aggregation (pixel vs superpixel vs parameter), and whether intervals are on flux, potential, or structure differ across methods and are not harmonized.
- Do not conflate CredInt with `uncertainty_correlation` (calibration of uncertainty vs error).
- Cross-paper comparison of CredInt numbers is not yet meaningful without a shared reporting template.
