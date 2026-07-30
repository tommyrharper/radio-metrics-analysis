# SNR

## What this metric means here
In this review, **SNR** marks papers that report a signal-to-noise ratio as a quantitative fidelity or operating-condition measure anywhere in the imaging pipeline (visibilities → gridding → iFFT → deconvolution). Our column is intentionally broad: it covers image-domain reconstruction SNR against known truth, input visibility SNR used to set noise in simulations, and classic image-plane SNR definitions tied to deconvolution behaviour—not a single enforced formula.

## How papers use it
**Ground-truth reconstruction SNR (dominant in ML and sparse-imaging papers).** The most common pattern is an L₂ image error expressed in decibels: `20·log₁₀(‖x‖₂ / ‖x − x̂‖₂)` (or equivalent with σ-based denominators in early SARA work). Classic sparse-imaging papers (SARA 2012, PURIFY 2014) sweep variable-density Fourier coverage and Monte Carlo noise, reporting mean reconstruction SNR over tens to hundreds of trials. The R2D2-citing cohort treats this as the primary headline metric: R2D2, AIRI, uSARA, QuantifAI, ISCAD, GMCP, HyperAIRI, and related methods report SNR in tables, per-iteration curves, and noise-robustness sweeps (typically input SNR 15–55 dB, 100 Monte Carlo runs). Reported reconstruction SNR spans roughly 5–40 dB depending on method, source, and coverage; learned series methods (R2D2, R3D3) commonly lead optimization baselines by ≈2–4 dB on matched simulated tests.

**Input vs output SNR.** Several papers explicitly separate visibility input SNR (`20·log₁₀(‖y₀‖₂/‖n‖₂)` or per-visibility noise std) from reconstruction SNR. PURIFY and SARA fix input SNR (e.g. 30 dB) and measure recovery SNR as a function of coverage ratio M/N. Noise-robustness experiments plot reconstruction SNR vs swept input SNR to show method stability rather than single-point rankings.

**Classic deconvolution and operating limits.** In the classic cohort, SNR often describes the *observing* or *simulation* regime rather than a truth-based score. Multiscale CLEAN (2008) defines theoretical image-plane SNR as clean-beam-convolved model peak divided by image-plane noise and studies flux-recovery thresholds vs SNR. Faceting for direction-dependent deconvolution discusses sparsification reducing effective SNR by 10× while keeping early CLEAN cycles above the noise floor—an operational trade-off, not a measured end-to-end benchmark.

**Real-data and non-standard uses.** QuantifAI reports reconstruction SNR rising with MeerKAT synthesis time (25–34 dB over 1–8 h). Lens-discoverability work cites literature thresholds on combined lensed-image SNR (≥ 20). One diffusion paper (DDRM 2026) uses a different definition: `SNR = 10·log₁₀[(1/N)Σx⁽ʲ⁾ / MSE]`. POLISH is described qualitatively as giving ≈3 dB SNR gain over CLEAN dirty images in a review paper. Residual-map flatness is sometimes discussed alongside SNR but explicitly rejected as an adequate substitute (PURIFY, SARA).

## Popular measurement variants
- **L₂ ratio in dB (20·log₁₀):** `‖x‖₂ / ‖x − x̂‖₂` — standard in R2D2, AIRI, QuantifAI, MROP, and most r2d2-citing benchmarks.
- **Standard-deviation form (20·log₁₀):** `σ_x / σ_{x−x̂}` — used in SARA (2012) as ground-truth image-domain error score.
- **Input visibility SNR:** same dB form on visibilities or noise std, fixed to define simulation noise (commonly 30–35 dB).
- **Image-plane / theoretical SNR:** peak of beam-convolved model over image noise (Multiscale CLEAN noise sweeps).
- **Alternate 10·log₁₀ SNR from mean flux and MSE:** reported in DDRM alongside PSNR.
- **Per-iteration / per-cycle tracking:** SNR vs R2D2 iteration, AIRI observation time, or decentralized imaging major cycles.
- **Hyperspectral Frobenius SNR:** `20·log₁₀(‖X̄‖_F / ‖X̄ − X‖_F)` in HyperAIRI (distinct from monochromatic use).

## Gaps and caveats
- **Formula heterogeneity:** Most papers use 20·log₁₀ on L₂ norms, but DDRM uses 10·log₁₀ with MSE; comparing SNR values across papers requires checking the definition.
- **Truth availability:** High SNR scores are almost always simulation-only; real-data validations (QuantifAI MeerKAT, R2D2 Cygnus A case studies) are exceptions and may use partial or proxy truth.
- **SNR vs data fidelity:** R2D2 papers emphasize that high reconstruction SNR can coexist with worse residual-to-dirty ratios (RDR); the metrics measure different things.
- **Residual flatness misleading:** Papers warn that flat dirty residuals do not imply good truth-based SNR (PURIFY 30 Doradus example; SARA residual discussion).
- **Classification without detail:** Some SNR-flagged papers (e.g. lens-discoverability thresholds, decentralized framework) contribute contextual SNR use rather than full benchmark tables; a few r2d2-citing rows may lack dedicated extraction bullets beyond the column flag.
