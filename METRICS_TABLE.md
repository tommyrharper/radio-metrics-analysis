# Performance/Fidelity Metrics Table — root aggregate

Aggregates the three cohort tables. **This root table currently reflects only completed data**: the `cohorts/r2d2-citing/` cohort (33/33 papers). The `classic` and `emerging-ml` cohorts have no completed rows yet — see their own `METRICS_TABLE.md` files, and `PAPERS.md` for the candidates awaiting captain approval.

| Cohort | Status | Papers classified | Table |
|---|---|---|---|
| R2D2-citing | complete | 33 / 33 | `cohorts/r2d2-citing/METRICS_TABLE.md` |
| Classic / current-practice | awaiting approved-paper extraction | 0 | `cohorts/classic/METRICS_TABLE.md` |
| ML / emerging | awaiting approved-paper extraction | 0 | `cohorts/emerging-ml/METRICS_TABLE.md` |

## R2D2-citing cohort (complete — copied verbatim from `cohorts/r2d2-citing/METRICS_TABLE.md`)

| Bibcode | Title | SNR | logSNR | PSNR | SSIM | DR | RDR/Resid | NMSE | MAE | Runtime | Iters | CredInt | UncCorr | Wasser | Class | Text | Compute | #Other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026arXiv260702110D | Black Boxes in Black Hole Imaging | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2026arXiv260628493D | The Role of Artificial Intelligence in the... | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |
| 2026arXiv260526347D | A distributed resource-adaptive implementa... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| 2026arXiv260309162W | POLISH'ing the Sky: Wide-Field and High-Dy... | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2026arXiv260115844M | Radio-Interferometric Image Reconstruction... | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2026ApJS..283....9T | HyperAIRI: A Plug-and-play Algorithm for P... | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2026AJ....171..220Y | An Imaging Algorithm Based on Generalized ... | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026AJ....171...44Y | A Radio-interferometric Imaging Method Bas... | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026A&A...706A..77M | Accelerating the CLEAN algorithm of radio ... | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2025arXiv251208444H | Learned iterative networks: An operator le... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2025arXiv250915176M | To CLEAN or not to CLEAN: Data Processing ... | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025arXiv250721270M | Generative imaging for radio interferometr... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2025arXiv250309559C | Interlaced R2D2 DNN Series for Scalable No... | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025arXiv250102473D | IRIS: A Bayesian Approach for Image Recons... | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025RASTI...4..25M | Learned Radio Interferometric Imaging for ... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025MNRAS.543.1727L | MROP: modulated rank-one projections for c... | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2025MNRAS.542.2494M | Strong gravitational lensing with upcoming... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 2025MNRAS.542..426T | S-R2D2: a spherical extension of the R2D2 ... | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025MNRAS.537.1608T | The AIRI plug-and-play algorithm for image... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2025MLS&T...6d5005Z | Unveiling the power of multimodal large la... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 2025ChJSS..45.1597F | Imaging Method of Synthetic Aperture Radio... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2025ApJS..280...63A | Toward a Robust R2D2 Paradigm for Radio-in... | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2025ApJ...984...86P | Theoretical Foundation of Black Hole Image... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| 2025AJ....169..289W | A Decentralized Framework for Radio-interf... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 2025A&A...704A..43Y | Non-convex sparse regularisation for radio... | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2025A&A...698A.176M | How to make CLEAN variants faster using cl... | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025A&A...698A..61J | Deep learning inference with the Event Hor... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2024arXiv241023178C | Uncertainty Quantification for Fast Recons... | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2024arXiv240318052A | R2D2 Image Reconstruction with Model Uncer... | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2024arXiv240317905C | Scalable Non-Cartesian Magnetic Resonance ... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 2024RASTI...3..505L | Scalable Bayesian uncertainty quantificati... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2024ApJ...966L..34D | CLEANing Cygnus A Deep and Fast with R2D2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2024A&A...690A.387R | fast-resolve: Fast Bayesian Radio Interfer... | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| **TOTAL** |  | **18** | **10** | **4** | **2** | **11** | **12** | **3** | **1** | **25** | **16** | **4** | **1** | **1** | **5** | **1** | **16** | **42** |

## Column key

Same canonical metric list as `cohorts/r2d2-citing/METRICS_TABLE.md`: SNR (`snr`), logSNR (`logsnr`), PSNR (`psnr`), SSIM (`ssim`), DR (`dynamic_range`), RDR/Resid (`rdr_residual`), NMSE (`nmse_nrmse`), MAE (`mae`), Runtime (`runtime`), Iters (`iterations`), CredInt (`credible_interval`), UncCorr (`uncertainty_correlation`), Wasser (`wasserstein`), Class (`classification_metrics`), Text (`text_metrics`), Compute (`compute_cost`).
