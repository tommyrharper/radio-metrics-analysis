# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Approval gate on `PAPERS.md` candidates

`PAPERS.md` lists candidate papers with status `pending captain approval`. **Do not open, fetch, or download any candidate paper/PDF link from `PAPERS.md`, and do not extract metrics/methods/results from a candidate, until the captain has explicitly approved that entry.** This applies regardless of how confident the link resolution looks. The only exempt material is what is already preserved under `cohorts/r2d2-citing/` (copied from a prior completed review, see `cohorts/r2d2-citing/PROVENANCE.md`) and the R2D2 source paper's own published bibliographic metadata.

## Repo structure

- Three cohorts under `cohorts/`: `r2d2-citing` (complete), `classic`, `emerging-ml` (both extracted). Root `METRICS_TABLE.md` merges all three. Metrics webpage: see README “Metrics webpage” (`python3 -m http.server 8765` → http://127.0.0.1:8765/).
- This repo has no dependency on the separate PDF-extractor project.
- When a candidate is approved and extracted, follow the existing `cohorts/r2d2-citing/` layout as the template: `papers/<id>.md` summary + `metrics_table/rows/<id>.json` classification row, then regenerate that cohort's `METRICS_TABLE.md` and the root aggregate.

## RMS / RDR schema (in progress)

Former combined column `RDR/Resid` (`rdr_residual`) is splitting into **RMS** (`rms`) and **RDR** (`rdr`). **Classic is done** (see `cohorts/classic/METRICS_TABLE.md`). Emerging-ml and r2d2-citing row JSONs / cohort tables still use `rdr_residual`. Site data (`papers-data.json`, `index.html`) already uses `rms`/`rdr`; non-classic entries are temporary placeholders (`rms:0`, `rdr:<old rdr_residual>`). Do not regenerate the root aggregate until those cohorts are split. Classification: RMS = absolute residual/dirty/off-source RMS as a reported score (not merely DR’s denominator); RDR = residual-to-dirty ratio only; qualitative residuals alone → both 0.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
