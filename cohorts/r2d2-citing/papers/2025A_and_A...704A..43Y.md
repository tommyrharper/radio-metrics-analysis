# Non-convex sparse regularisation for radio interferometric imaging via smoothly clipped absolute deviation

**Bibcode:** 2025A&A...704A..43Y
**Authors:** Xiaocheng Yang, Huangfeng Cheng, Lin Wu, Jingye Yan, Mingfeng Jiang, Xu Yang
**ADS:** https://ui.adsabs.harvard.edu/abs/2025A%26A...704A..43Y/abstract
**arXiv:** not found (no preprint located via arXiv/ADS search; publisher HTML full text used instead: https://www.aanda.org/articles/aa/full_html/2025/12/aa55737-25/aa55737-25.html)

## One-line summary
The authors propose ISCAD, a non-convex sparse-regularisation method for radio-interferometric image reconstruction that replaces the biased L1-norm surrogate with a smoothly clipped absolute deviation (SCAD) penalty, solved via an accelerated (restarted, adaptive-step-size) proximal gradient algorithm, and show it beats SARA, AIRI, and an Lq-norm (LPG) baseline in both reconstruction fidelity and speed.

## Method
The imaging problem is posed as least-squares data fidelity plus a sparsity-promoting penalty on wavelet coefficients: minimize ||y − Φx||²₂ + P_λ(Ψ†x). Instead of the convex L1 relaxation of the L0 "norm" (which biases large coefficients), ISCAD uses the SCAD penalty, which is asymptotically unbiased for large coefficients while still convex-ish/continuous near zero. This non-convex problem is solved with an improved proximal-gradient algorithm featuring: (1) a gradient restart strategy, (2) an adaptive non-monotonic step-size (ANMS) strategy to accelerate convergence, and (3) an adaptively updated regularisation parameter based on prior image information. Complexity is O(nN log nN) + O(N) per iteration. Baselines compared: SARA (Carrillo et al. 2012, reweighted-L1 convex sparsity averaging, solved via PPD), AIRI (Terris et al. 2023, DNN denoiser replacing the proximal operator in unconstrained SARA/uSARA), and LPG (non-convex Lq-norm proximal gradient, q≈0.8). Tests used simulated VLA (30 Doradus test image, 256×256) and simulated SKA (W28 supernova remnant, 1024×1024; Messier 106, 512×512) visibility coverages generated with CASA/CASACORE, with Gaussian noise added (default input S/N = 35 dB; also swept 15–55 dB).

## Performance / fidelity metrics used
- **S/N (signal-to-noise ratio, dB):** S/N = 20·log10(‖x‖₂ / ‖x − x̃‖₂), where x is the ground-truth image and x̃ the reconstruction. Standard linear-scale fidelity metric.
- **S/N_log (log-scale S/N, dB):** S/N_log = 20·log10( ‖log10(x/ε + I_N)‖₂ / ‖log10(x/ε + I_N) − log10(x̃/ε + I_N)‖₂ ), i.e. S/N computed after a log10 stretch of pixel intensities — used specifically to assess dynamic-range/faint-structure fidelity, since linear S/N is dominated by bright pixels.
- **Running time (s)** and **iteration count** — used as computational-efficiency/convergence-speed metrics, reported alongside fidelity.
- **Qualitative residual/error-map inspection** — visual comparison of reconstructed images, linear-scale error images (Δx = x − x̃), and real part of residual visibility images, to assess artefacts/residual structure (e.g. SARA showing large residuals/artefacts near bright sources; ISCAD showing "scarcely perceptible errors and artefacts").
- **Noise-robustness curves:** S/N and S/N_log vs. input S/N (15–55 dB), each point averaged over 100 Monte Carlo realisations, to test robustness rather than a single-point comparison.

Reported values (input S/N = 35 dB), method: S/N (dB) / S/N_log (dB) / time (s):
- **30 Doradus (VLA, 256×256):** SARA 30.84/19.41/165.67; AIRI 32.57/20.68/105.24; LPG 33.65/21.05/128.46; **ISCAD 33.88/21.23/89.13**.
- **W28 (SKA, 1024×1024):** SARA 32.82/21.05/450.84; AIRI 33.78/21.84/295.36; LPG 35.22/22.36/318.64; **ISCAD 35.53/22.43/240.33**.
- **Messier 106 (SKA, 512×512):** SARA 31.95/20.14/321.06; AIRI 33.12/21.23/127.34; LPG 34.40/21.75/156.78; **ISCAD 34.63/21.97/107.11**.

Across all three test cases ISCAD attains the highest S/N and S/N_log and the lowest runtime of the four methods; it also converges in fewer iterations than LPG and shows greater robustness (consistently higher S/N/S/N_log) across the swept 15–55 dB noise range in the Monte Carlo experiment.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
This is a classical (non-ML) compressed-sensing/proximal-optimisation deconvolution method, but AIRI (a learned DNN-denoiser-in-the-loop baseline) is directly benchmarked against it using the same S/N and S/N_log metrics — giving a useful, consistently-defined fidelity/speed comparison point for evaluating any new ML-based deconvolution/regularisation module in the visibility→image pipeline.
