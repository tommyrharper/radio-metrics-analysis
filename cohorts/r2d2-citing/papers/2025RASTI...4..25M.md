# Learned Radio Interferometric Imaging for Varying Visibility Coverage

**Bibcode:** 2025RASTI...4..25M
**Authors:** Matthijs Mars, Marta M. Betcke, Jason D. McEwen
**ADS:** https://ui.adsabs.harvard.edu/abs/2025RASTI...4..25M/abstract
**arXiv:** https://arxiv.org/abs/2405.08958

## One-line summary
The paper develops learned post-processing (U-Net) and learned unrolled iterative (GU-Net) reconstruction methods for radio interferometric imaging, and proposes training strategies (single random coverage, distribution-of-coverages, transfer learning) that make these networks generalize to unseen visibility/uv-coverages without full retraining.

## Method
Two learned architectures are compared: a **U-Net** post-processor, which takes a dirty-image-type reconstruction as input and removes artefacts as a pure image-to-image network decoupled from the measurement process; and a **GU-Net** (gradient U-Net), an unrolled iterative method that embeds the telescope measurement operator directly inside a multi-scale network via gradient-descent-like data-consistency steps and sub-sampled dirty images at each scale. To make these networks robust to coverage that differs from training, four training strategies are tested: (i) "true coverage" (oracle, fully retrained per observation), (ii) training on a single fixed alternate coverage, (iii) training on a distribution of randomly drawn Gaussian uv-coverages (new coverage sampled per batch), and (iv) transfer learning — fine-tuning a pre-trained (single- or distribution-trained) model on the true coverage for 50–100 epochs. Training data: 2000 IllustrisTNG-derived 256×256 images (1000 test images), 32,768 measurements per observation, input SNR (ISNR) of 30 dB. Generalization is tested on Gaussian random coverages, a real MeerKAT coverage (241,920 visibilities, ~7.4× more than the Gaussian case), and an out-of-distribution 30 Doradus image with dynamic range ~600 (well above training dynamic range).

## Performance / fidelity metrics used
- **SNR (signal-to-noise ratio, dB):** defined as SNR(x_true, x_pred) = 20·log10(‖x_true‖ / ‖x_pred − x_true‖). Used as the primary reconstruction-fidelity metric, reported mainly via box-plots (Figures 5, 8, 9) rather than in-text tables.
- **logSNR:** SNR computed on the log10 of the true and predicted images (logSNR = SNR(log10(x_true), log10(x_pred))), used to better capture fidelity in faint/high-dynamic-range regions.
- **Reconstruction time (ms)**, Table 1: Pseudo-inverse 13.0±0.4 ms (1 operator evaluation); U-Net 54.9±1.6 ms (1 op. eval.); GU-Net 85.7±1.5 ms (7 op. evals, dominated by finest-scale evaluations). On MeerKAT's larger coverage, reconstruction time rose to 194.6±3.1 ms (~2.3× longer than for Gaussian coverage).
- **Training/fine-tuning time:** full training ~28 h (U-Net) and ~51 h (GU-Net) vs. transfer-learning fine-tuning of only 0.3 h (U-Net) and 2.7 h (GU-Net); for the MeerKAT/30 Doradus case, data creation ~2 h and fine-tuning ~5 h.
- **Qualitative dynamic-range robustness:** GU-Net successfully reconstructed the ~600 dynamic-range 30 Doradus image despite training on lower-dynamic-range data, while U-Net "struggled" to reconstruct the higher dynamic range.
- **Baseline comparisons:** CLEAN and multi-scale CLEAN variants are discussed only qualitatively/historically (described as computationally costly and giving suboptimal reconstruction quality); no numeric SNR values against CLEAN/MS-CLEAN are reported in the text — comparisons are between the paper's own U-Net vs. GU-Net variants under different coverage-training strategies.
- **Generalization across coverage-training strategies:** GU-Net consistently outperformed U-Net across all coverage strategies; under the distribution-of-coverages strategy GU-Net showed only a small reconstruction-quality loss relative to the fully-retrained (oracle, true-coverage) model; transfer learning restored GU-Net performance close to the oracle; U-Net performed "significantly worse" and showed overfitting tendencies when coverage varied.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Directly relevant: GU-Net embeds the interferometric measurement/gridding operator inside an unrolled deep network to replace/augment CLEAN-style deconvolution, and demonstrates (via SNR/logSNR and dynamic-range robustness) that measurement-operator-aware unrolled learning generalizes far better across varying uv-coverage than a decoupled post-processing (U-Net) network — a key consideration for any ML replacement of the gridding→iFFT→deconvolution stages that must handle instrument- and observation-dependent visibility sampling.
