# CredInt

## What this metric means here
Bayesian credible intervals and Highest Posterior Density (HPD) regions on reconstructed radio images or image structures—per-pixel error bars, regional uncertainty envelopes, or isocontours derived from a posterior or MAP potential after the visibility → gridding → iFFT → deconvolution chain. In this review, **CredInt** marks any use of credible levels, HPD boundaries, or local credible interval (LCI) widths to quantify reconstruction uncertainty rather than point-estimate fidelity alone.

**Taxonomy:** **Uncertainty** — describes reported posterior or inferential uncertainty (distinct from `uncertainty_correlation`, which evaluates whether estimated uncertainty tracks actual error).

## How papers use it
Five papers are tagged, but only one (QuantifAI, 2024RASTI...3..505L) reports concrete credible-interval machinery in the notes. That work defines HPD credible regions at level 100(1−α)% (approximated analytically from the MAP potential), uses a 99% HPD isocontour (α=0.01) for hypothesis tests on inpainted or blurred surrogate images, and reports per–16×16-superpixel Local Credible Intervals l_i = ξ+,Ωi − ξ−,Ωi with mean values 0.20, 0.08, 0.24, and 0.07 across four test images. The other four tagged papers (PRIMO, fast-resolve, equivariant-bootstrap UQ, IRIS) are classified from their overall Bayesian/UQ framing but carry no dedicated credible-interval bullets in the extracted notes.

## Popular measurement variants
- **HPD credible regions** at a stated level 100(1−α)%, often approximated without MCMC from a MAP potential.
- **Hypothesis testing via HPD isocontours**—compare a surrogate image’s potential to a fixed-level HPD boundary (e.g. 99%) to accept or reject structural hypotheses.
- **Local Credible Intervals (LCIs)**—superpixel-scale Bayesian error-bar widths from root-finding on HPD boundaries, summarized by mean LCI per image.
- **Qualitative validation** of analytic intervals against posterior-sample standard deviation (mentioned for LCIs).

## Gaps and caveats
- Sample is small (5 papers) and heavily dominated by one detailed source; four entries lack metric-specific extraction detail.
- Credible level, spatial aggregation (pixel vs superpixel vs region), and whether intervals are on flux, potential, or structure differ across methods and are not harmonized in the notes.
- Classification for several papers rests on overall UQ content, not a standardized reporting template—cross-paper comparison of CredInt numbers is not yet meaningful.
