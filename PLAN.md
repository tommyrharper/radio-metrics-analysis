# Plan

Fast-path milestones. This repo has no dependency on the separate PDF-extractor project.

- [x] **Stage 0 — Bootstrap (this task).** Repo scaffold, durable agent instructions, preserved R2D2-citing cohort (33/33), four `METRICS_TABLE.md` surfaces, candidate bibliography (`PAPERS.md`) with stable links, all pending captain approval.
- [ ] **Stage 1 — Captain review of `PAPERS.md`.** Captain approves, trims, or amends the candidate list (canonical names, cohort/stage assignments, ambiguous entries flagged in `PAPERS.md`). No extraction happens before this.
- [x] **Stage 2 — Classic cohort extraction.** For each approved classic-cohort candidate: read the approved paper, write `cohorts/classic/papers/<id>.md`, add a row to `cohorts/classic/metrics_table/rows/<id>.json`, update `cohorts/classic/METRICS_TABLE.md`.
- [x] **Stage 3 — Emerging-ML cohort extraction.** Same process as Stage 2 for `cohorts/emerging-ml/`, including the R2D2 source paper itself.
- [x] **Stage 4 — Root aggregate refresh.** Regenerate the root `METRICS_TABLE.md` across all three cohorts once Stage 2 and Stage 3 have any completed rows.
- [ ] **Stage 5 — Cross-cohort synthesis.** Compare metric conventions and reported baselines across classic vs. ML methods and against the R2D2-citing cohort's findings.
