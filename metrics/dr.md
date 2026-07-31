# DR

## What this metric means here
**DR (dynamic range)** in this review flags papers that quantify, target, or discuss the ratio between the brightest and faintest recoverable structure in a reconstructed radio image—whether as a measured score, a simulation parameter, an algorithm limit, or a qualitative capability claim across the visibility-to-image pipeline.

## How papers use it
**Classic measured definitions and algorithm benchmarks.** The classic cohort uses several operational definitions. W-projection (2008) defines DR1 = peak / MAD from median and DR2 = peak / strongest nearby negative sidelobe, reporting DR1 from ≈1,570 (2D FFT) to 50,888 (256 w-planes) with runtime trade-offs. Multiscale CLEAN uses peak / off-source RMS, flattening near 4 at low input SNR. Multi-frequency deconvolution (2011) reports peak-to-peak-residual DR up to ≈110,000 on noise-free 3C286 tests and ≈100,000 in Taylor-order numerical tests; primary-beam uncorrected DR limit ≈1,000. Direction-dependent gains paper discusses ≈10⁴–10⁵ imaging limits from leakage and pointing errors without tabulated achieved DR. WSClean notes ≈1:1000 DR simulations with no accuracy loss under reduced-resolution inversion.

**DR as simulation parameter (emerging-ml and r2d2-citing).** High-DR synthetic benchmarks drive method design: R2D2 tests DR from 10³ to 5×10⁵; MROP splits d ∈ [10³,10⁴] vs [10⁴,10⁵]; AIRI observations span DR ≈2.9×10³ (1 h) to 1.1×10⁴ (8 h). logSNR transforms parameterize on DR. R2D2 residual-to-dirty ratios worsen at DR ≈10⁵ while truth-based SNR may still rank methods differently. S-R2D2 tests DR ∈ [10³, 5×10⁵] on the sphere; planar R2D2 truth fidelity degrades when super-resolving at high Np.

**Qualitative and real-data DR claims.** Real-data papers often discuss DR without a scalar score: fast-resolve reports higher DR than classical resolve on VLA Cygnus A; R2D2 Cygnus A paper quotes ≈1.7×10⁵ target/achieved DR; CG-CLEAN claims higher DR in later major-loop iterations on narrowband real data; IRIS and SKA-era review papers frame DR qualitatively vs CLEAN/MPoL. POLISH++ capability table compares max DR (≈10⁶ for POLISH++ vs ≈5×10⁵ for R2D2) without shared-benchmark numbers. Deep wide-field imaging (2022ApJ) uses estimated dirty-peak/noise for regularization (≈10⁵–10⁶ nominal) but cautions reconstructed peaks are >10× lower—configuration estimates, not measured fidelity.

**Framework definitions.** astroCAMP defines `DR = I_max / σ_res` as a core Table 2 quality metric (peak over residual RMS) and pairs it with dirty-image RMS and PSNR/SSIM in the co-design quality set; the published WSClean+IDG runs do not tabulate achieved DR.

## Popular measurement variants
- **Peak / off-source RMS:** Multiscale CLEAN noise and source-size sweeps.
- **DR1 and DR2 (peak / MAD; peak / local negative):** W-projection comparison table.
- **Peak-to-peak-residual DR:** Multi-frequency MS-CLEAN on 3C286 and noise-free simulations.
- **max / σ_noise or max / faintest intensity:** R2D2 MRI analogue; MROP d = reciprocal of faintest ground-truth intensity.
- **Configured or estimated target DR:** simulation draw parameter (10³–10⁶), dirty-peak/noise estimates for regularization, literature capability tables.
- **Achieved DR on real fields:** quoted scalars (Cygnus A ≈1.7×10⁵) or qualitative “higher DR than resolve/CLEAN” without formula.
- **Operational DR limits:** leakage, primary beam, w-term, pointing, Högbom loop divergence (“several hundred” in POLISH++ table for CLEAN).

## DR details page

The main metrics graph keeps a single binary **DR** column. Drill-down lives at [`site/detail/dr.html`](../site/detail/dr.html) (linked as **Explore DR Details** when DR is selected on `index.html`).

Reporting categories (a paper may appear in more than one — category totals can exceed DR-positive paper counts):

| Category | Sub-metrics |
|---|---|
| Reported / Achieved DR | peak_rms_dr, peak_mad_dr, peak_peak_residual_dr, tabulated_scalar_dr, other_measured_dr_formula |
| Target / Configured DR | simulation_draw_parameter, dirty_peak_noise_estimate, capability_table_max_dr |
| Comparative DR | higher_lower_than_baseline, dr_improvement_factor, percentage_dr_change |
| DR Limits / System Effects | dd_calibration_leakage_ceilings, algorithm_divergence_limits, other_dr_limiting_physics |
| Unspecified DR | unspecified (extraction limitation; not silently overclassified) |

**DR Context** (separate panel): Definition used, Noise estimator, Image region, Simulation vs real data, Frequency, Array — reporting-completeness counts only. DR context describes how dynamic range was defined or measured; it is not itself a DR metric. Residual RMS alone is not DR; SNR is not DR.

Structured data: `dr_details` arrays on DR-positive papers in `data/papers-data.json` (optional mirror `data/dr-details.json`). Taxonomy: `site/js/taxonomies/dr-taxonomy.js`. Injector: `scripts/inject_dr_details.py`.

## Gaps and caveats
- **Definition multiplicity:** Peak/RMS, peak/MAD, peak/local-minimum, and configured DR are not interchangeable; classic and ML papers rarely align on one definition.
- **Measured vs intended:** Many high-DR numbers are simulation settings or dirty-image estimates, not validated reconstructed DR on real data.
- **Real-data scarcity:** ASKAP validations (AIRI, uSARA) explicitly omit calibrated DR benchmarks; fidelity is morphology and flux, not DR scores.
- **DR vs truth fidelity decoupling:** R2D2 can show good SNR at high DR with worse RDR/residual structure around bright features.
- **Qualitative-only flags:** Several DR=1 papers (IRIS, SKA review) contribute discussion without a unified quantitative DR metric and are left Unspecified on the details page.
- **Some classic DR classifications** (direction-dependent gains, faceting) emphasize limits or comparative claims rather than tabulated achieved DR.
