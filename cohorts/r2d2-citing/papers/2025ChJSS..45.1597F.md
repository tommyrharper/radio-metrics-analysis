# Imaging Method of Synthetic Aperture Radio Telescope Based on Minimax Concave Penalty

**Bibcode:** 2025ChJSS..45.1597F
**Authors:** Fan Xiaoyi, Yang Xiaocheng, Wu Lin, Yan Jingye, Xu Lu (School of Computer Science and Technology, Zhejiang Sci-Tech University, Hangzhou; State Key Laboratory of Solar Activity and Space Weather, Chinese Academy of Sciences, Beijing)
**ADS:** https://ui.adsabs.harvard.edu/abs/2025ChJSS..45.1597F/abstract
**arXiv:** not found (no preprint located; paper appears to be published only in Chinese Journal of Space Science, 2025, 45(6): 1597–1606, DOI: 10.11728/cjss2025.06.2024-0186)

## One-line summary
Proposes a compressed-sensing radio-interferometric imaging method that replaces the usual L1-norm sparsity penalty with a minimax concave penalty (MCP, a closer approximation to the L0 norm), solved via a proximal gradient algorithm with adaptive/restart strategies and maximum-likelihood-based regularization parameter selection, and shows it outperforms SARA and the deep-learning method AIRI on reconstruction quality and speed.

## Method
The paper treats image reconstruction from undersampled interferometric visibility data as an ill-posed inverse problem. Instead of the biased L1-norm minimization used in standard compressed-sensing approaches, they use a nonconvex minimax concave penalty (MCP) to more closely approximate L0-norm sparsity, solving the resulting nonconvex minimization with a proximal gradient algorithm. They add maximum likelihood estimation for adaptive selection of the regularization parameter and use restart/adaptive step-size strategies to improve convergence speed and stability. Results are demonstrated on simulated data across different visibility undersampling rates and on an SKA-configuration array.

## Performance / fidelity metrics used
Full text (via SciEngine/CJSS) was accessible and metrics were extracted directly from reported tables:

- **SNR (dB)** — primary reconstruction-quality metric, computed at 10% and 50% visibility undersampling rates, and on a simulated SKA array.
- **Fidelity Index** — a secondary image-fidelity score reported alongside SNR for each condition.
- **Runtime (seconds)** — wall-clock reconstruction time, compared across methods.
- **Baseline comparisons:** SARA (sparsity-averaging compressed-sensing algorithm) and AIRI (a deep-learning/plug-and-play imaging method related to the R2D2 family) used as competing baselines; their proposed MCP method (labeled "MCP" in tables) is compared directly against both.

Reported results (from Table 1, 10%/50% undersampling; Table 2, SKA array):
- 10% undersampling: SARA SNR 16.37 dB / Fidelity 2.89 / 43.27 s; AIRI SNR 22.39 dB / Fidelity 3.39 / 21.76 s; MCP (proposed) SNR 24.16 dB / Fidelity 5.55 / 25.07 s.
- 50% undersampling: SARA SNR 24.27 dB / Fidelity 10.27 / 44.03 s; AIRI SNR 27.21 dB / Fidelity 13.81 / 24.21 s; MCP SNR 27.78 dB / Fidelity 15.93 / 26.11 s.
- SKA array: SARA SNR 32.83 dB / Fidelity 0.85 / 342.75 s; AIRI SNR 34.52 dB / Fidelity 0.97 / 175.32 s; MCP SNR 35.73 dB / Fidelity 1.09 / 189.62 s.

The paper reports the proposed MCP method achieves the highest SNR and fidelity index in every tested condition, is substantially faster than SARA, and is only marginally slower than AIRI while improving reconstruction quality. It also reports enhanced noise robustness versus competing approaches (via convergence/noise-performance figures), though exact noise-robustness metric definitions were not captured beyond what is summarized above.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Directly relevant: this is a deconvolution/image-reconstruction algorithm competing with the AIRI deep-learning method (closely related to the R2D2 paradigm) on the same visibility-to-image inverse problem, giving a useful non-ML (nonconvex sparse optimization) baseline with quantitative SNR/fidelity/runtime comparisons against a deep-learning approach.
