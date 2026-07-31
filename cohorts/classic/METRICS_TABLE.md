# Performance/Fidelity Metrics Table - Classic / current-practice cohort

Extracted from the 23 paper summaries in `papers/*.md` by classifying against the fixed canonical metric list used by the R2D2-citing cohort. 1 = metric used or reported in that paper's summary, 0 = not used. See `other_metrics` notes below the table for metrics outside this canonical set.

> Note: Former `RDR/Resid` (`rdr_residual`) is split into **RMS** and **RDR** across all cohorts and the root aggregate. **Flux** (`flux_recovery`) and **Astrometry** (`astrometric_accuracy`) are first-class canonical columns (after MAE / after Flux).

| Bibcode | Title | SNR | logSNR | PSNR | SSIM | DR | RMS | RDR | NMSE | MAE | Flux | Astrometry | Runtime | Iters | CredInt | UncCorr | Wasser | Class | Text | Compute | #Other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SKA-MEMO-132 | Analysis of Convolutional Resampling Algorithm Performance | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| 2025arXiv251213591C | astroCAMP: A Community Benchmark and Co-Design Framework for Sustainable SKA-Scale Radio Imaging | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 21 |
| 2023arXiv230606007K | HVOX: Scalable Interferometric Synthesis and Analysis of Spherical Sky Maps | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2018A&A...616A..27V | Image Domain Gridding: a fast method for convolutional resampling of visibilities | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| 2018A&A...611A..87T | Faceting for direction-dependent spectral deconvolution | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| 2017MNRAS.471..301O | An optimized algorithm for multi-scale wideband deconvolution of radio astronomical images | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| 2014MNRAS.444..606O | WSClean: an implementation of a fast, generic wide-field imager for radio astronomy | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 2014MNRAS.439.3591C | PURIFY: a new approach to radio-interferometric imaging | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2012MNRAS.426.1223C | Sparsity Averaging Reweighted Analysis (SARA): a novel algorithm for radio-interferometric imaging | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2011A&A...532A..71R | A multi-scale multi-frequency deconvolution algorithm for synthesis imaging in radio interferometry | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2008ISTSP...2..793C | Multiscale CLEAN Deconvolution of Radio Synthesis Images | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2008ISTSP...2..647C | The Noncoplanar Baselines Effect in Radio Interferometry: The W-Projection Algorithm | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2008A&A...487..419B | Correcting direction-dependent gains in the deconvolution of radio interferometric images | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2007ASPC..376..127M | CASA Architecture and Applications | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2005sf2a.conf..721P | Successes of and Challenges to GILDAS, a State-of-the-Art Radioastronomy Toolkit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| 2004A&A...426..747B | Scale sensitive deconvolution of interferometric images. I. Adaptive Scale Pixel (Asp) decomposition | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| 1995ASPC...77..433S | A Retrospective View of Miriad | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1994A&AS..108..585S | Multi-frequency synthesis techniques in radio interferometric imaging | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| 1988A&A...200..312W | The Multi-Resolution Clean and its application to the short-spacing problem in interferometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 1985daa..conf..195W | NRAO's Astronomical Image Processing System (AIPS) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1984A&A...137..159S | Enhancements to the deconvolution algorithm "CLEAN" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 1980A&A....89..377C | An Efficient Implementation of the Algorithm "CLEAN" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 1974A&AS...15..417H | Aperture Synthesis with a Non-Regular Distribution of Interferometer Baselines | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| **TOTAL** |  | **4** | **0** | **1** | **1** | **7** | **8** | **0** | **3** | **0** | **5** | **0** | **13** | **12** | **0** | **0** | **0** | **0** | **0** | **12** | **72** |

## Column key

- **SNR** (`snr`)
- **logSNR** (`logsnr`)
- **PSNR** (`psnr`)
- **SSIM** (`ssim`)
- **DR** (`dynamic_range`)
- **RMS** (`rms`)
- **RDR** (`rdr`)
- **NMSE** (`nmse_nrmse`)
- **MAE** (`mae`)
- **Flux** (`flux_recovery`) — Flux Recovery
- **Astrometry** (`astrometric_accuracy`) — Astrometric Accuracy
- **Runtime** (`runtime`)
- **Iters** (`iterations`)
- **CredInt** (`credible_interval`)
- **UncCorr** (`uncertainty_correlation`)
- **Wasser** (`wasserstein`)
- **Class** (`classification_metrics`)
- **Text** (`text_metrics`)
- **Compute** (`compute_cost`)

## Other metrics noted per paper (outside the canonical list)

- **SKA-MEMO-132**: grid-point throughput; power efficiency; arithmetic intensity; hardware utilization; memory traffic; kernel support; capacity/node estimate
- **2025arXiv251213591C**: energy-to-solution; throughput; energy efficiency; data locality; device utilisation; memory bandwidth; memory efficiency; peak memory; carbon-to-solution; carbon efficiency; total cost of ownership; cost per job; cost efficiency; astrometric error; photometric error; polarisation purity; rotation-measure recovery error; spectral-line fidelity; time-series accuracy; transient completeness; resource occupancy
- **2023arXiv230606007K**: memory footprint; visibility count; sparse-domain speedup
- **2018A&A...616A..27V**: aliasing error; PSF sidelobe RMS; out-of-field-source suppression
- **2018A&A...611A..87T**: spectral-index error; BDA compression ratio; facet gridding speedup
- **2017MNRAS.471..301O**: spectral-index error; system-noise estimate; minor-loop throughput
- **2014MNRAS.444..606O**: runtime-model fit error; cross-array speedup
- **2014MNRAS.439.3591C**: visibility coverage ratio; visibility constraint radius
- **2012MNRAS.426.1223C**: Fourier coverage fraction
- **2011A&A...532A..71R**: spectral-index error; spectral-curvature error; bandpass-calibration accuracy
- **2008ISTSP...2..793C**: source-size scale
- **2008ISTSP...2..647C**: w-projection kernel support
- **2008A&A...487..419B**: polarization leakage; pointing-error accuracy; beam-model error
- **2005sf2a.conf..721P**: survey yield; pipeline success rate; angular resolution; atmospheric phase noise; bandwidth
- **2004A&A...426..747B**: active-set size; component count; residual correlation scale
- **1994A&AS..108..585S**: spectral-index error; integrated flux density; thermal noise; flux-scale bias
- **1988A&A...200..312W**: peak brightness; component count
- **1984A&A...137..159S**: finite-precision subtraction error
- **1980A&A....89..377C**: memory footprint / beam-patch dimensions
- **1974A&AS...15..417H**: peak-significance heuristic; source-parameter count; wide-field validity bound
