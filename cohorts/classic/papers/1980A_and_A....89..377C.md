# An Efficient Implementation of the Algorithm "CLEAN"

**Bibcode:** 1980A&A....89..377C
**Authors:** B. G. Clark
**Journal:** Astronomy and Astrophysics 89, 377-378 (1980)
**ADS:** https://ui.adsabs.harvard.edu/abs/1980A&A....89..377C/abstract
**Full text:** https://articles.adsabs.harvard.edu/pdf/1980A%26A....89..377C

## One-line summary
Clark accelerates Högbom CLEAN by choosing many approximate components in fast minor cycles using only high residual-map points and a truncated central beam patch, then applying their full point-source-response convolution together in a Fourier-domain major cycle.

## Method
The paper separates CLEAN's nonlinear component-location step from its convolution and subtraction step. Within each major cycle, it scans the residual map, constructs a value histogram, and measures the largest point-source-response sidelobe outside centered squares of candidate sizes. It then selects a limiting residual value, \(S_{\mathrm{lim}}\), and a central beam patch so that the largest excluded map value has the same fraction of the map peak as the largest beam value outside the patch, while the retained map points and patch fit in main memory. Beam symmetry permits storage of a rectangular patch with a 2:1 side ratio.

A minor cycle repeatedly finds the largest retained residual value and subtracts, from retained points within one patch width, the CLEAN gain times the component flux times the beam-patch value. The implementation therefore ignores lower residual points and treats the point-source response as zero outside the patch during approximate component selection.

A major cycle restores accuracy by transforming all components selected since the cycle began, multiplying by the stored Fourier transform of the full point-source response, inverse-transforming the result, and subtracting that full convolution from the original map to produce a new residual map. The component transform uses a direct discrete transform in the Y direction followed by an FFT in X, avoiding a long transpose. The same component transform can also be multiplied by the transform of the Gaussian clean beam for restoration.

The implemented major-cycle stopping rule ends minor iteration \(N\) when its map maximum falls below \(S_{\mathrm{lim}} F(M,N)\), where \(M\) is the first minor-iteration index of the major cycle and \(F(M,N)=1+\sum_{n=M}^{N}1/n\). Clark describes this logarithmically increasing guard as conservative and explicitly notes that the patch adaptation and stopping decisions are empirical rather than proven optimal.

## Performance / fidelity metrics used
- Runtime throughput: on a PDP-11/70 with an attached FPS AP-120B array processor, the minor cycle processed about 15 components per second. This is an implementation throughput, not an end-to-end image-runtime measurement.
- Relative computation time: for typical VLA use, the implementation saved a factor of 2 to 10 relative to a conventional CLEAN implementation. The paper does not provide individual timing tables, test-image identifiers, or uncertainty estimates; it states that the ratio depends strongly on map size, CLEAN gain, map complexity, and point-source-response sidelobe level.
- Workload context: the implementation had been used routinely for several months on VLA images of complex objects. Common square image sizes were 256 to 1024 pixels per side. The mention of future images up to 8192 pixels per side is a projected requirement, not a tested benchmark.
- Memory and patch context: the machine had 32 kwords of main memory, and the beam patch was constrained between 21 x 41 and 64 x 127 elements. These are implementation constraints, not reconstruction-quality scores.
- Cycle behavior: the empirical stopping rule usually removed 5 or 6 components in the first major cycle and increased toward a map- and gain-dependent limit, described as typically perhaps 250 components at gain 0.5. "Perhaps" makes this an approximate operational observation rather than a controlled benchmark.
- Restoration fidelity: reusing the component transform means that the effective clean beam is the requested Gaussian convolved with the field-of-view sinc function. Clark says the difference is negligible when sampling at 4 points per beam, but supplies no numerical error, residual, dynamic-range, or image-fidelity metric.
- The paper reports no named sky dataset, visibility count, residual RMS, flux-recovery error, dynamic range, or quantitative comparison of reconstructed image fidelity against conventional CLEAN.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
This paper addresses the deconvolution stage after gridding and the initial inverse FFT. Its major/minor-cycle split is directly relevant to hybrid ML designs: a fast learned component proposer or approximate residual updater could operate in minor cycles, while periodic full point-source-response convolution supplies a physics-based correction and limits accumulated approximation error. The paper also identifies end-to-end measurements that matter for an ML replacement, including component throughput and total speedup under fixed hardware, while exposing missing evaluation dimensions such as residual RMS, recovered flux, dynamic range, and controlled fidelity comparisons. It does not modify visibility weighting, gridding, or the initial image-forming iFFT.
