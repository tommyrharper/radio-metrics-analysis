# Flux Recovery

## What this metric means here
**Flux Recovery** (`flux_recovery`) flags papers that report a **quantitative** measure of how accurately reconstructed source flux is preserved relative to a reference, model, catalogue, or expected value. Table/chart label: **Flux**.

Included reporting forms: recovered flux / true flux; integrated-flux recovery fraction; percentage recovered flux; integrated-flux error or bias; peak-flux recovery or bias; missing-flux fraction; total recovered emission; photometric accuracy when explicitly based on reconstructed flux; numerical comparative statements (e.g. method A recovers ~2× the total flux of CLEAN).

**Not** classified from: a source’s measured flux quoted only as observational context; image peak brightness alone; contour levels; dynamic range; qualitative “more extended emission is visible”; component counts; residual RMS; spectral-index accuracy without an associated flux-recovery measurement; purely qualitative descriptions; or explicit statements that flux recovery was **not** reported.

Cohort totals: classic **5**, emerging-ml **4**, r2d2-citing **1** (grand total **10** / 63).

## How papers use it
**Truth-based integrated / peak flux (classic).** Multi-Resolution CLEAN reports recovered integrated flux vs known model flux (e.g. MRC 962 of 1002 vs CLEAN 563; 93.6% of 10,000 on a realistic model). Multiscale CLEAN tabulates total recovered flux vs a 1,495 Jy reference and recovered-flux fraction across source-size/noise sweeps. MS-MFS reports reference-frequency peak-flux error (~1 part in 10³) on a noise-free Taylor-order test. WSClean quotes AEGEAN source-flux standard error (~1.3%) on a 100×1 Jy MWA simulation. DDFacet plots relative flux-density error `(Ŝ−S)/S` vs beam radius.

**Cross-method photometry on real data (emerging-ml).** AIRI on MeerKAT (ESO 137-006) and uSARA/AIRI ASKAP papers compare AGN or diffuse-source integrated fluxes in mJy across algorithms (no known sky truth)—treated here as comparative flux recovery/consistency checks. Radionets reports core specific-intensity (peak-flux) relative deviation vs synthetic Gaussian truth.

**Catalogue flux RMSE (r2d2-citing).** POLISH’ing the Sky reports SEP-extracted source flux RMSE vs ground truth on true-positive detections (CLEAN best; learned variants worse)—the sole r2d2-citing positive.

## Popular measurement variants
- **Integrated flux vs true model flux** (recovery fraction or absolute Jy).
- **Peak-flux / core specific-intensity bias** relative to truth.
- **Catalogue / source-finder flux error** (standard error %, RMSE in Jy or Jy/pixel).
- **Relative flux-density error** vs radius or direction-dependent effects.
- **Cross-method integrated-flux tables** on real data (consistency, not truth error).

## Distinctions
- **Integrated vs peak:** Integrated recovery tests total emission (extended structure, missing short spacings); peak/core intensity tests bright-component photometry. Both score as Flux when quantitative.
- **vs DR / RMS:** Dynamic range and residual RMS do not measure recovered flux vs a reference; low residuals can coexist with wrong total flux.
- **vs morphology / brightness reporting:** “More filamentary structure” or quoting an observed source flux as context is not Flux Recovery.
- **vs SNR / NMSE / pixel MSE:** Global image-error metrics can *imply* flux error but are not classified as Flux unless an explicit flux-preservation statistic is reported.

## Gaps and caveats
- **Incomparable apertures and products:** Real-data comparisons often use manually drawn regions, CLEAN restoring-beam–convolved models vs unconvolved ML models, or unequal resolution—agreement is not known-truth accuracy.
- **Over-recovery:** Recovered flux can exceed truth at low SNR (MRC); fraction alone is not an unbiased error.
- **Sparse in ML / R2D2 literature:** Most R2D2-family papers score SNR/logSNR/RDR and omit explicit flux photometry; only one of 33 citing papers reports flux RMSE.
- **Framework-only mentions:** Named “photometric error” in a benchmark design without measured values → Flux=0 (e.g. astroCAMP experimental release).
