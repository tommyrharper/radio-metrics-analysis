# Astrometric Accuracy

## What this metric means here
**Astrometric Accuracy** (`astrometric_accuracy`) flags papers that report a **quantitative** measure of how accurately a reconstructed source’s position is recovered relative to a reference position, catalogue, simulation truth, or known sky coordinate. Table/chart label: **Astrometry**.

Included reporting forms: angular or pixel distance of a reconstructed source from a reference; RA or Dec error; centroid displacement; mean/median/RMS/max positional error; astrometric bias; fraction of sources localised within a stated positional tolerance; numerical comparative statements that one method recovers more accurate positions than another.

**Not** classified from: quoted coordinates as observational context only; image resolution or beam size alone; source detection completeness/purity without a positional-error statistic; morphology or shape accuracy (including jet-angle or ring orientation); qualitative “well aligned” or visual contour agreement; PSNR/SSIM (even when a paper notes PSNR is sensitive to shifts); a matching radius used only as a pipeline/association setting; or framework-named “astrometric error” without measured results.

Cohort totals: classic **0**, emerging-ml **0**, r2d2-citing **0** (grand total **0** / 63).

## How papers use it
**No measured positives in this review.** Across all three cohorts, summaries either omit source-position error, explicitly state that astrometric error was not reported, or name it only as a desirable / framework metric.

Closest non-scoring patterns (kept at 0 under the rules above):
- **astroCAMP (classic)** lists catalogue position offsets among algorithmic-quality metrics but excludes them from the current experimental release — same treatment as photometric error for Flux.
- **WSClean / POLISH’ing the Sky** run source finders (AEGEAN, SEP) and report flux or shape RMSE on matches; matching thresholds define true positives, not achieved position accuracy.
- **radionets** reports jet-angle (orientation) error vs synthetic truth and states these are not astrometric tests; the summary also notes no real-data astrometric error.
- **POLISH (emerging-ml)** notes that PSNR is sensitive to astrometric shifts and recommends measuring astrometric error in production evaluations — sensitivity/recommendation only.

## Popular measurement variants
(Expected forms when papers do report the metric; none scored here.)
- **Angular / pixel offset** of centroid or peak vs truth or catalogue.
- **RA / Dec or radial position error** (mean, median, RMS, max), sometimes in arcsec, mas, pixels, or beam fractions.
- **Fraction within tolerance** (e.g. % of sources within N arcsec or N×beam).
- **Astrometric bias** (systematic shift) separate from scatter.
- **Comparative position accuracy** across methods without a named scalar.

## Distinctions
- **Absolute vs relative:** Absolute error vs catalogue/truth is the core include; quantitative registration/offset between two reconstructions can also score when reported as a position-accuracy measure.
- **Centroid / coordinate bias vs matching tolerance:** Achieved offset or bias scores; an association radius used only to define matches does not.
- **vs resolution / beam:** Beam or pixel scale as imaging context is not Astrometry; normalising a reported positional error by the beam can still score if the error itself is reported.
- **vs detection (Class):** Precision/recall/completeness without position-error analysis → Class only.
- **vs morphology / size / jet angle:** Shape, size, orientation, and ring parameters are not source-position recovery.
- **vs PSNR / SSIM / NMSE:** Global image-similarity metrics may be shift-sensitive but are not classified as Astrometry unless an explicit position-error statistic is reported.

## Gaps and caveats
- **Absent in this corpus:** Zero of 63 papers report a measured source-position error under the include rules — a notable evaluation gap relative to Flux (10/63).
- **Framework-only naming:** Keeping `astrometric error` in `other_metrics` (e.g. astroCAMP) while scoring the canonical field 0 avoids false positives when the metric is defined but not measured.
- **Source-finder confusion:** Catalogue extraction often yields flux/shape statistics; do not infer position accuracy from the mere use of AEGEAN/SEP unless offsets are reported.
- **Name collisions:** “Position angle,” “peak location” in morphological cross-sections, antenna pointing-error corrections, and lens image-separation Δθ are not reconstructed-source astrometry vs reference.
