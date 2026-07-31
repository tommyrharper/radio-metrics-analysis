# radio-metrics-analysis

## Purpose

A literature-review repository tracking how radio-interferometric imaging methods — classic/current-practice pipelines (CLEAN-family, gridding, deconvolution) and ML/emerging methods — are evaluated: which reconstruction **performance and fidelity metrics** (SNR, PSNR, SSIM, dynamic range, flux recovery, astrometric accuracy, runtime, etc.) each paper reports, and how methods compare against one another.

This feeds the Cavendish Astrophysics UROP project on the visibility-data -> gridding -> iFFT -> deconvolution imaging pipeline, improved with ML. It is a standalone literature-tracking repo with **no dependency** on the separate PDF-extractor project.

## Status

See `PLAN.md` for staged milestones.

- `cohorts/r2d2-citing/` — **complete** (33/33 papers summarized and classified).
- `cohorts/classic/` — **extracted** (23 papers summarized and classified).
- `cohorts/emerging-ml/` — **extracted** (7 papers summarized and classified).
- Root `METRICS_TABLE.md` merges all three cohorts (63 papers).

## Cohorts

1. **`cohorts/r2d2-citing/`** — papers that cite the R2D2 source paper (Aghabiglou et al. 2024, ApJS 273, 3). Complete: 33 paper summaries + 33 classified metric rows.
2. **`cohorts/classic/`** — classic / current-practice imaging methods and software (WSClean, CASA, AIPS, MIRIAD, CLEAN-family, w-projection/w-stacking, SARA/PURIFY, etc.). Extracted: 23 paper summaries + 23 classified metric rows.
3. **`cohorts/emerging-ml/`** — ML / emerging imaging methods (uSARA, AIRI/HyperAIRI, R2D2 itself, POLISH, PRIMO, and related). Extracted: 7 paper summaries + 7 classified metric rows.

## Four-table model

Each cohort has its own `METRICS_TABLE.md`, plus one root aggregate:

1. `METRICS_TABLE.md` (root) — merged view of all three cohorts.
2. `cohorts/r2d2-citing/METRICS_TABLE.md` — complete, copied from the source review repo.
3. `cohorts/classic/METRICS_TABLE.md` — classic / current-practice extraction.
4. `cohorts/emerging-ml/METRICS_TABLE.md` — ML / emerging extraction.

## Metrics webpage

Interactive stacked bar chart of metric usage by cohort (`index.html` + `data/papers-data.json`).

**Layout:** project docs and cohorts stay at the repo root; the browsable site assets live under `site/` (shared CSS/JS, taxonomies, detail pages); structured site data under `data/`; metric overview markdown under `metrics/`; injectors under `scripts/`.

**Metric detail pages (shared shell):** Runtime, Compute, Iterations, DR, and RMS each have a bookmarkable second-level page under [`site/detail/`](site/detail/) (`runtime.html`, `compute.html`, …). Those HTML files are thin configs; shared UI lives in `site/css/metric-detail.css` + `site/js/metric-detail.js`, driven by `window.METRIC_DETAIL`. Per-metric taxonomies live in `site/js/taxonomies/`. To add another metric later: add a taxonomy JS, classify `*_details` on papers in `data/papers-data.json`, add a thin `site/detail/<metric>.html` stub, and one Explore link in `index.html`.

**Runtime:** **Explore Runtime Details** → [`site/detail/runtime.html`](site/detail/runtime.html). Categories: Wall-clock, Throughput, Relative Performance, Runtime Scaling (+ Unspecified). Context panel: Hardware / Parallelism / Software / Numerical Configuration / Workload. Data: `runtime_details` (`site/js/taxonomies/runtime-taxonomy.js`; mirror `data/runtime-details.json`). Binary `runtime` unchanged.

**Compute:** **Explore Compute Details** → [`site/detail/compute.html`](site/detail/compute.html). Categories: Resource Usage, Efficiency / Intensity, Relative Compute, Scaling / Complexity (+ Unspecified). Data: `compute_details` (`site/js/taxonomies/compute-taxonomy.js`). Binary `compute_cost` unchanged.

**Iterations:** **Explore Iterations Details** → [`site/detail/iterations.html`](site/detail/iterations.html). Categories: Iteration Count, Convergence Behaviour, Comparative Iteration Performance, Iteration Scaling (+ Unspecified). Context: stopping / optimiser / LR / etc. Data: `iterations_details`. Binary `iterations` unchanged.

**DR:** **Explore DR Details** → [`site/detail/dr.html`](site/detail/dr.html). Categories: Reported / Achieved, Target / Configured, Comparative, Limits / System Effects (+ Unspecified). Data: `dr_details`. Binary `dynamic_range` unchanged.

**RMS:** **Explore RMS Details** → [`site/detail/rms.html`](site/detail/rms.html). Categories: Absolute, Comparative, Framework / Defined (+ Unspecified). Data: `rms_details`. Binary `rms` unchanged. RMS used only as a DR denominator is not a subtype; RDR is not RMS.

Interaction on every detail page mirrors the main graph: all positive papers by default, bar click focuses a sub-metric, title opens Overview / By paper, **All papers** / empty chart returns to browse. Papers may count in more than one sub-metric.

Metrics are grouped by a five-category taxonomy:

| Category | Metrics |
|---|---|
| Observational | SNR, logSNR, DR, RMS, RDR |
| Computational | Runtime, Compute, Iters |
| Fidelity | PSNR, SSIM, NMSE, MAE, Wasser |
| Uncertainty | CredInt, UncCorr |
| Scientific | Flux, Astrometry, Class, Text (`spectral_accuracy` reserved but not in schema yet — omitted from the chart, not shown as zero) |

**Uncertainty** metrics assess the quality, calibration, or usefulness of uncertainty estimates rather than reconstructed-image fidelity alone: **CredInt** (`credible_interval`) is reported posterior or inferential uncertainty; **UncCorr** (`uncertainty_correlation`) checks whether estimated uncertainty tracks actual error or another reliability signal.

Unknown schema keys would fall into an internal Uncategorised fallback (logged in the browser console) and only appear in the UI if any such keys exist.

**Visuals:** cohort colours fill the stacked bar segments; category is shown with a coloured outline, x-tick colour, and legend swatch (border style differs by category — Uncertainty uses blue with a dashed border). Membership lives in `metricCategories` inside `index.html`.

**Filters:** cohort checkboxes and a category dropdown (**All categories**, or one taxonomy at a time) combine. Metrics with zero total for the visible cohorts stay hidden. Chart order is descending paper count for the visible cohorts (taxonomy tags visuals/filters only).

**Start** (from the repo root):

```bash
python3 -m http.server
```

**Open:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (default port is **8000** — include it in the URL).

**Stop:** press `Ctrl+C` in the terminal running the server.

Needs a local HTTP server (not `file://`) so the page can load `data/papers-data.json` and `metrics/*.md`. If port 8000 is taken, pick another and match the URL, e.g. `python3 -m http.server 8765` → `http://127.0.0.1:8765/`.

### Metric overviews

Cross-paper syntheses of how each canonical metric is used live in `metrics/` (e.g. `metrics/runtime.md`, `metrics/compute.md`). The webpage “How papers report …” panel can toggle between the per-paper note list and these overviews.

## Bibliography review before extraction (gate)

`PAPERS.md` lists candidate papers per method family with stable landing-page links (ADS/DOI/arXiv/publisher), status `pending captain approval`.

**No candidate paper or PDF listed in `PAPERS.md` may be opened, downloaded, or have content/metrics extracted from it until the captain has reviewed and approved the candidate list.** Only the already-complete `cohorts/r2d2-citing/` material and the R2D2 source paper's existing published metadata are exempt, since they were preserved from prior completed work, not newly extracted here. See `AGENTS.md` for the durable version of this rule.
