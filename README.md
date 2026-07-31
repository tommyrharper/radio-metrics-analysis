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

Interactive stacked bar chart of metric usage by cohort (`index.html` + `papers-data.json`).

**Runtime second-level page:** when Runtime is selected on the main graph, an accessible **Explore Runtime Details** link opens [`runtime.html`](runtime.html) (bookmarkable; ← Back to all metrics). That page subtypes Runtime-positive papers into four reporting categories (Wall-clock, Throughput, Relative Performance, Runtime Scaling) plus **Unspecified Runtime** when evidence is too vague to subtype. Papers may contribute to more than one category, so category totals may exceed the number of Runtime-positive papers. Interaction mirrors the main metrics page: browse all Runtime-positive papers by default, click a sub-metric bar to focus contributing papers, click the title for Overview / By paper reporting detail, and use **All papers** (or empty chart click) to return. A separate **Runtime Measurement Context** panel counts reporting completeness for Hardware / Parallelism / Software / Numerical Configuration / Workload — execution context is not itself a Runtime metric. Taxonomy config lives in `runtime-taxonomy.js`; structured entries are `runtime_details` on each paper in `papers-data.json` (mirror: `data/runtime-details.json`). Top-level `runtime: 0|1` flags are unchanged. The same shell (filters → category graph → paper detail → context) can be copied for other metrics later.

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

Needs a local HTTP server (not `file://`) so the page can load `papers-data.json` and `metrics/*.md`. If port 8000 is taken, pick another and match the URL, e.g. `python3 -m http.server 8765` → `http://127.0.0.1:8765/`.

### Metric overviews

Cross-paper syntheses of how each canonical metric is used live in `metrics/` (e.g. `metrics/runtime.md`, `metrics/compute.md`). The webpage “How papers report …” panel can toggle between the per-paper note list and these overviews.

## Bibliography review before extraction (gate)

`PAPERS.md` lists candidate papers per method family with stable landing-page links (ADS/DOI/arXiv/publisher), status `pending captain approval`.

**No candidate paper or PDF listed in `PAPERS.md` may be opened, downloaded, or have content/metrics extracted from it until the captain has reviewed and approved the candidate list.** Only the already-complete `cohorts/r2d2-citing/` material and the R2D2 source paper's existing published metadata are exempt, since they were preserved from prior completed work, not newly extracted here. See `AGENTS.md` for the durable version of this rule.
