# Class

## What this metric means here
Classification and catalog-level detection metrics applied to reconstructed radio images or downstream science products—accuracy, precision, recall, F1, true/false positive rates, and related counts—rather than pixel-wise image fidelity in the core visibility → gridding → iFFT → deconvolution chain. In this review, **Class** covers any discrete label, source-detection, or lens-finding evaluation built on interferometric reconstructions.

## How papers use it
Six papers span three distinct evaluation cultures. **Source detection on simulated wide-field images** (POLISH’ing the Sky, 2026arXiv260309162W) is the most fully specified: SEP-based matching with size-dependent pixel thresholds yields precision/recall/F1 (e.g. POLISH++ 0.8433 / 0.6142 / 0.7107 vs CLEAN 0.3612 / 0.2220 / 0.2750 in Table 3), plus RMSE on matched detections for major-axis FWHM, minor-axis FWHM, and flux; performance is also tracked vs SNR threshold (3–300,000). **Approximate false-detection rates** appear in the earlier POLISH weak-lensing paper (~5% false positives per galaxy for CLEAN vs ~2% for POLISH) without full catalog benchmark specification. **Strong-lens finding** uses CNN finders with TPR at fixed FPR (e.g. FPR=10⁻³ vs Einstein radius in POLISH’ing the Sky; cited >90% recovery at 0.008% FPR for ILT simulations in Rezaei et al. 2022, echoed in SKA-era survey commentary). **Non-imaging classification** includes near-perfect MAD/SANE magnetic-state accuracy for EHT ZINGULARITY (2025A&A...698A..61J) and multimodal LLM radio-image tasks reporting accuracy, precision, recall, F1, TPR, FPR, and missed-detection counts (2025MLS&T...6d5005Z).

## Popular measurement variants
- **Precision / recall / F1** on source detections with explicit TP definition (ground-truth match within a size-dependent pixel radius).
- **False-positive incidence or rate** from source finders (sometimes approximate, e.g. false galaxies per N simulated galaxies).
- **TPR at fixed FPR** for CNN lens finders, often plotted vs Einstein radius or image separation relative to the PSF.
- **Classification accuracy** for discrete physical labels (e.g. EHT magnetic-state classes).
- **RMSE on true-positive subsets** for estimated shape and flux parameters (adjacent to detection matching, reported alongside Class in POLISH++).
- **Multimodal LLM benchmarks** combining standard classification rates with missed-detection counts.

## Gaps and caveats
- Tasks mix simulated catalogs, real-survey lens finding, EHT morphology classes, and VQA-style LLM evaluation—**Class** is a broad bucket, not one comparable score.
- Several entries cite external benchmarks (Rezaei et al. 2022) or give order-of-magnitude yield claims without full precision–recall curves in the notes.
- Early POLISH false-detection figures lack completeness, threshold settings, and uncertainty intervals; POLISH++ is the only source with full Table 3 numbers in the notes.
- Shape/flux RMSE and lens TPR curves are science-pipeline metrics downstream of reconstruction quality; they depend on finder training data matched (or not) to each image type.
