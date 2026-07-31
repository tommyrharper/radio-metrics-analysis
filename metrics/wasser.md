# Wasser

## What this metric means here
Earth-mover (Wasserstein) distances between radio reconstructions, used when pixel-wise ground truth is unavailable to quantify how much an image changes across iterations, algorithms, or parallel vs serial runs in the visibility → gridding → iFFT → deconvolution pipeline. In this review, **Wasser** marks any Wasserstein-based fidelity or convergence proxy on reconstructed intensity maps.

Root total: **1** Wasserstein-positive paper (r2d2-citing only). Binary `wasserstein: 0|1` flags are unchanged by the drill-down; subtype detail lives in `wasserstein_details` ([`site/detail/wasser.html`](../site/detail/wasser.html)).

## How papers use it
A single paper (A Decentralized Framework for Radio-interferometric Image Reconstruction, 2025AJ....169..289W) reports the metric. On real datasets without ground truth (HL Tau, Cygnus A), the authors define **W₅** as the L2 norm of per-pixel Wasserstein-1 distances computed in 5×5 sliding windows between reconstructions across iterations or methods. W₅ decreases with iteration count and is used to argue convergence and similarity of parallel versus serial output images. Simulated datasets in the same paper use SNR instead.

## Drill-down taxonomy (second-level page)
See [`site/detail/wasser.html`](../site/detail/wasser.html) / `site/js/taxonomies/wasser-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| Windowed Wasserstein Distance | W₅ (5×5 windowed W₁ + L2); Other windowed Wasserstein |
| Cross-Iteration Wasserstein | Successive-reconstruction distance |
| Cross-Method Wasserstein | Parallel vs serial similarity; Other method / implementation comparison |
| Unspecified Wasserstein | Vague Wasserstein mentions already flagged wasserstein=1 but not subtypeable |

**Wasserstein Context** (window size, distance order, aggregation, simulation vs real, frequency, array) is reporting completeness only — not itself a Wasserstein metric.

Structured data: `wasserstein_details` arrays on Wasserstein-positive papers in `data/papers-data.json` (optional mirror `data/wasser-details.json`). Taxonomy: `site/js/taxonomies/wasser-taxonomy.js`. Injector: `scripts/inject_wasser_details.py`.

## Popular measurement variants
- **Windowed Wasserstein-1 per pixel** in 5×5 neighborhoods, aggregated by an L2 norm over the image (**W₅**).
- **Cross-iteration comparison**—distance between successive reconstructions as a convergence diagnostic.
- **Cross-method / cross-implementation comparison**—distance between parallel and serial reconstructions on the same data.

## Gaps and caveats
- Sample size is 1 paper; no cross-study baseline for acceptable W₅ values.
- Applied only where ground truth is absent, so it complements rather than replaces supervised fidelity metrics.
- Window size (5×5), distance order (Wasserstein-1), and aggregation (L2 norm) are method-specific and not standardized across the literature in this review.
- Do not count Wasserstein-GAN adversarial training losses alone as this metric.
