# Performance/Fidelity Metrics Table - ML / emerging cohort

Extracted from the 7 paper summaries in `papers/*.md` by classifying against the fixed canonical metric list used by the completed R2D2-citing cohort. 1 = metric used/reported in that paper's summary, 0 = not used. See `other_metrics` notes below the table for metrics outside this canonical set.

> Note: Former `RDR/Resid` (`rdr_residual`) is split into **RMS** and **RDR** across all cohorts and the root aggregate. **Flux** (`flux_recovery`) and **Astrometry** (`astrometric_accuracy`) are first-class canonical columns (after MAE / after Flux).

| Bibcode | Title | SNR | logSNR | PSNR | SSIM | DR | RMS | RDR | NMSE | MAE | Flux | Astrometry | Runtime | Iters | CredInt | UncCorr | Wasser | Class | Text | Compute | #Other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024ApJS..273....3A | The R2D2 Deep Neural Network Series Paradigm for Fast Precision Imaging in Radio Astronomy | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2023MNRAS.522.5576W | Scalable precision wide-field imaging in radio interferometry: II. AIRI validated on ASKAP data | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 2023MNRAS.522.5558W | Scalable precision wide-field imaging in radio interferometry: I. uSARA validated on ASKAP data | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| 2023ApJ...943..144M | Principal-Component Interferometric Modeling (PRIMO), an Algorithm for EHT Data I: Reconstructing Images from Simulated EHT Observations | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2022MNRAS.514.2614C | Deep radio-interferometric imaging with POLISH: DSA-2000 and weak lensing | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 |
| 2022ApJ...939L...4D | First AI for Deep Super-resolution Wide-field Imaging in Radio Astronomy: Unveiling Structure in ESO 137-006 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| 2022A&A...664A.134S | Deep learning-based imaging in radio interferometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| **TOTAL** |  | **1** | **1** | **1** | **1** | **3** | **1** | **1** | **0** | **0** | **4** | **0** | **5** | **5** | **1** | **0** | **0** | **1** | **0** | **6** | **18** |

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

- **2023MNRAS.522.5576W**: spectral index; pixelwise reconstruction variation
- **2023MNRAS.522.5558W**: spectral index; contour level; operator storage
- **2023ApJ...943..144M**: PCA variance explained; fractional complex visibility error; fractional visibility-amplitude error; visibility-phase error
- **2022MNRAS.514.2614C**: false-positive incidence; source size; effective source density
- **2022ApJ...939L...4D**: super-resolution factor; spectral index; measurement-operator storage; filament intensity
- **2022A&A...664A.134S**: jet-angle error; thresholded source-area ratio
