# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Approval gate on `PAPERS.md` candidates

`PAPERS.md` lists candidate papers with status `pending captain approval`. **Do not open, fetch, or download any candidate paper/PDF link from `PAPERS.md`, and do not extract metrics/methods/results from a candidate, until the captain has explicitly approved that entry.** This applies regardless of how confident the link resolution looks. The only exempt material is what is already preserved under `cohorts/r2d2-citing/` (copied from a prior completed review, see `cohorts/r2d2-citing/PROVENANCE.md`) and the R2D2 source paper's own published bibliographic metadata.

## Repo structure

- Three cohorts under `cohorts/`: `r2d2-citing` (complete), `classic`, `emerging-ml` (both extracted). Root `METRICS_TABLE.md` merges all three. Metrics webpage: serve from repo root (`python3 -m http.server` → http://127.0.0.1:8000/).
- Site assets under `site/` (detail pages, shared CSS/JS, taxonomies); site data under `data/` (`papers-data.json`, `*-details.json` mirrors); overview markdown under `metrics/`; injectors under `scripts/`.
- This repo has no dependency on the separate PDF-extractor project.
- When a candidate is approved and extracted, follow the existing `cohorts/r2d2-citing/` layout as the template: `papers/<id>.md` summary + `metrics_table/rows/<id>.json` classification row, then regenerate that cohort's `METRICS_TABLE.md` and the root aggregate.

## Metric detail pages

All chart metrics have second-level pages under `site/detail/` (19 stubs). Shared shell: `site/css/metric-detail.css` + `site/js/metric-detail.js`. Each stub only sets `window.METRIC_DETAIL` (taxonomy from `site/js/taxonomies/`, binary/details keys, page copy) then loads the shared script. Main chart Explore links: `METRIC_DRILLDOWNS` in `index.html`. Do not copy-paste a full detail page for new metrics — add taxonomy + stub + `*_details` in `data/papers-data.json` + one Explore link.

Paper-centric view: `site/paper.html?bib=<bibcode>` (registry `site/js/metric-registry.js`) lists every flagged metric for one paper with structured `*_details` cards. Linked from paper rows via **Details** (home and metric-detail pages); external source uses a link icon.

Comparison: **Compare** toggles papers into a shared selection (`site/js/comparison-store.js`, max 5). Sticky tray → `site/compare.html` for side-by-side metric details.

## RMS / RDR schema

Former combined column `RDR/Resid` (`rdr_residual`) is split into **RMS** (`rms`) and **RDR** (`rdr`). **All three cohorts and the root aggregate** use this schema (see each `METRICS_TABLE.md` and the website). Classification: RMS = absolute residual/dirty/off-source RMS as a reported score (not merely DR’s denominator); RDR = residual-to-dirty ratio only; qualitative residuals alone → both 0.

## Flux Recovery

Canonical key `flux_recovery` (table label **Flux**, after MAE): quantitative recovered flux vs reference/model/catalogue (or explicit cross-method recovered-flux comparison). Observational flux context, peak brightness alone, DR/RMS, or qualitative morphology → 0. See `metrics/flux-recovery.md`.

## Astrometric Accuracy

Canonical key `astrometric_accuracy` (table label **Astrometry**, after Flux): quantitative reconstructed-source position vs reference/catalogue/truth (centroid/RA–Dec/positional error, localisation within tolerance, or comparative position accuracy). Resolution/beam alone, detection without position error, morphology/jet-angle, PSNR/SSIM, matching radius as setting only, or framework-named without measured results → 0. See `metrics/astrometric-accuracy.md`.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
