# radio-metrics-analysis

## Purpose

A literature-review repository tracking how radio-interferometric imaging methods — classic/current-practice pipelines (CLEAN-family, gridding, deconvolution) and ML/emerging methods — are evaluated: which reconstruction **performance and fidelity metrics** (SNR, PSNR, SSIM, dynamic range, runtime, etc.) each paper reports, and how methods compare against one another.

This feeds the Cavendish Astrophysics UROP project on the visibility-data -> gridding -> iFFT -> deconvolution imaging pipeline, improved with ML. It is a standalone literature-tracking repo with **no dependency** on the separate PDF-extractor project.

## Status

**Stage 0 (this bootstrap): scaffold only.** See `PLAN.md`.

- `cohorts/r2d2-citing/` is **complete** — 33/33 papers summarized and classified.
- `cohorts/classic/` and `cohorts/emerging-ml/` are **awaiting captain-approved candidate papers** — no extraction has happened yet.
- `PAPERS.md` is the candidate bibliography awaiting captain review before any candidate link is opened or any new metric is extracted.

## Cohorts

1. **`cohorts/r2d2-citing/`** — papers that cite the R2D2 source paper (Aghabiglou et al. 2024, ApJS 273, 3). Complete: 33 paper summaries + 33 classified metric rows.
2. **`cohorts/classic/`** — classic / current-practice imaging methods and software (WSClean, CASA, AIPS, MIRIAD, CLEAN-family, w-projection/w-stacking, SARA/PURIFY, etc.). Candidates only; no extraction yet.
3. **`cohorts/emerging-ml/`** — ML / emerging imaging methods (uSARA, AIRI/HyperAIRI, R2D2 itself, POLISH, PRIMO, and related). Candidates only; no extraction yet.

## Four-table model

Each cohort has its own `METRICS_TABLE.md`, plus one root aggregate:

1. `METRICS_TABLE.md` (root) — aggregate view; currently reflects only completed data (the R2D2-citing cohort).
2. `cohorts/r2d2-citing/METRICS_TABLE.md` — complete, copied from the source review repo.
3. `cohorts/classic/METRICS_TABLE.md` — awaiting approved-paper extraction.
4. `cohorts/emerging-ml/METRICS_TABLE.md` — awaiting approved-paper extraction.

## Bibliography review before extraction (gate)

`PAPERS.md` lists candidate papers per method family with stable landing-page links (ADS/DOI/arXiv/publisher), status `pending captain approval`.

**No candidate paper or PDF listed in `PAPERS.md` may be opened, downloaded, or have content/metrics extracted from it until the captain has reviewed and approved the candidate list.** Only the already-complete `cohorts/r2d2-citing/` material and the R2D2 source paper's existing published metadata are exempt, since they were preserved from prior completed work, not newly extracted here. See `AGENTS.md` for the durable version of this rule.
