# Performance/Fidelity Metrics Table — R2D2-citing cohort

> **Provenance:** copied verbatim (no re-research) from `r2d2-citations-review/METRICS_TABLE.md` at `/Users/thomasharper/code/cambridge/UROP/r2d2-citations-review` on 2026-07-30. Git history was not merged. See `cohorts/r2d2-citing/PROVENANCE.md` for details.

Extracted from the 33 paper summaries in `papers/*.md` by one subagent per paper, classifying against a fixed canonical metric list. 1 = metric used/reported in that paper's summary, 0 = not used. See `other_metrics` notes below the table for metrics outside this canonical set.

> Note: Former `RDR/Resid` (`rdr_residual`) is split into **RMS** and **RDR** (same rules as classic / emerging-ml). All three cohorts and the root aggregate use this schema.

| Bibcode | Title | SNR | logSNR | PSNR | SSIM | DR | RMS | RDR | NMSE | MAE | Runtime | Iters | CredInt | UncCorr | Wasser | Class | Text | Compute | #Other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026arXiv260702110D | Black Boxes in Black Hole Imaging | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| 2026arXiv260628493D | The Role of Artificial Intelligence i... | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |
| 2026arXiv260526347D | A distributed resource-adaptive imple... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| 2026arXiv260309162W | POLISH'ing the Sky: Wide-Field and Hi... | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2026arXiv260115844M | Radio-Interferometric Image Reconstru... | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2026ApJS..283....9T | HyperAIRI: A Plug-and-play Algorithm... | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2026AJ....171..220Y | An Imaging Algorithm Based on General... | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026AJ....171...44Y | A Radio-interferometric Imaging Metho... | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2026A&A...706A..77M | Accelerating the CLEAN algorithm of r... | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2025arXiv251208444H | Learned iterative networks: An operat... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2025arXiv250915176M | To CLEAN or not to CLEAN: Data Proces... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025arXiv250721270M | Generative imaging for radio interfer... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2025arXiv250309559C | Interlaced R2D2 DNN Series for Scalab... | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025arXiv250102473D | IRIS: A Bayesian Approach for Image R... | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025RASTI...4..25M | Learned Radio Interferometric Imaging... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025MNRAS.543.1727L | MROP: modulated rank-one projections... | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 2025MNRAS.542.2494M | Strong gravitational lensing with upc... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 2025MNRAS.542..426T | S-R2D2: a spherical extension of the... | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025MNRAS.537.1608T | The AIRI plug-and-play algorithm for... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2025MLS&T...6d5005Z | Unveiling the power of multimodal lar... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 2025ChJSS..45.1597F | Imaging Method of Synthetic Aperture... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2025ApJS..280...63A | Toward a Robust R2D2 Paradigm for Rad... | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2025ApJ...984...86P | Theoretical Foundation of Black Hole... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| 2025AJ....169..289W | A Decentralized Framework for Radio-i... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| 2025A&A...704A..43Y | Non-convex sparse regularisation for... | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2025A&A...698A.176M | How to make CLEAN variants faster usi... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025A&A...698A..61J | Deep learning inference with the Even... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2024arXiv241023178C | Uncertainty Quantification for Fast R... | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2024arXiv240318052A | R2D2 Image Reconstruction with Model... | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2024arXiv240317905C | Scalable Non-Cartesian Magnetic Reson... | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 2024RASTI...3..505L | Scalable Bayesian uncertainty quantif... | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2024ApJ...966L..34D | CLEANing Cygnus A Deep and Fast with... | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2024A&A...690A.387R | fast-resolve: Fast Bayesian Radio Int... | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| **TOTAL** |  | **18** | **10** | **4** | **2** | **11** | **2** | **6** | **3** | **1** | **25** | **16** | **4** | **1** | **1** | **5** | **1** | **16** | **42** |

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
- **Runtime** (`runtime`)
- **Iters** (`iterations`)
- **CredInt** (`credible_interval`)
- **UncCorr** (`uncertainty_correlation`)
- **Wasser** (`wasserstein`)
- **Class** (`classification_metrics`)
- **Text** (`text_metrics`)
- **Compute** (`compute_cost`)

## Other metrics noted per paper (outside the canonical list)

- **2026arXiv260702110D**: cross-method convergence/robustness; bias propagation; algorithmic transparency/interpretability
- **2026arXiv260628493D**: Calibration error / accuracy
- **2026arXiv260526347D**: memory footprint (byte-cost formula); memory reduction factor; w-layer count; precomputation cost amortization; communication overhead; computational cost relative to CLEAN
- **2026arXiv260115844M**: SRE (Standardised Reconstruction Error)
- **2026ApJS..283....9T**: sSNR (spectral-index SNR)
- **2026A&A...706A..77M**: momentum-parameter-sensitivity
- **2025arXiv251208444H**: Lipschitz constant; contractiveness/contraction guarantee; convergence to fixed point; generalization/stability properties
- **2025MNRAS.543.1727L**: data-to-image ratio (D/N); data-to-visibility ratio (D/VB); relative error map; peak intensity
- **2025MNRAS.542.2494M**: image separation Δθ (relative to PSF)
- **2025MNRAS.537.1608T**: std(Sol) across K=15 independent denoiser realisations (epistemic uncertainty from training variability)
- **2025MLS&T...6d5005Z**: missed-detection counts
- **2025ChJSS..45.1597F**: Fidelity Index
- **2025ApJS..280...63A**: MRU (mean relative uncertainty)
- **2025ApJ...984...86P**: Fourier correlation length; Resolving baseline scale; Characteristic Fourier-space variation scales (us, vs); Azimuthal Fourier-plane coverage fraction; PCA eigenimage compactness; Fourier-plane residual percentage; Variance explained by eigenimages; Angular resolution limit formula; Independence/resolution element count
- **2024arXiv241023178C**: interval length (ℓ2 norm ratio); empirical coverage
- **2024arXiv240318052A**: relative epistemic uncertainty [σ/µ]
- **2024arXiv240317905C**: Acceleration Factor; Additional Acceleration Ratio
- **2024ApJ...966L..34D**: super-resolution factor
- **2024A&A...690A.387R**: residual mean-squared error (log-brightness)
