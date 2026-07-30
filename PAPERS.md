# Candidate Bibliography

**Status: pending captain approval.** Every entry below was identified using bibliographic/abstract-index metadata only — ADS, arXiv abstract pages, Crossref, and official software documentation. **No candidate PDF was opened or downloaded, and no methods/results/metrics were extracted from any candidate.** Direct PDF links are recorded only where they were exposed directly alongside the metadata (e.g. an arXiv `/pdf/` link next to the `/abs/` page); they were not followed.

Per `AGENTS.md`, no link below may be opened and no candidate may be extracted into `cohorts/classic/` or `cohorts/emerging-ml/` until the captain approves it here.

Entries already preserved in the completed `cohorts/r2d2-citing/` corpus are cross-referenced by bibcode rather than duplicated.

---

## Classic / current-practice

### WSClean
- **Primary paper:** "WSClean: an implementation of a fast, generic wide-field imager for radio astronomy"
- **Authors/year:** A. R. Offringa, B. McKinley, N. Hurley-Walker, et al., 2014
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..606O/abstract
- **PDF:** not directly exposed in search metadata
- **Cohort / stage:** classic; gridding / imaging (wide-field imager; introduces w-stacking)
- **Reason:** title/abstract explicitly describe it as "a fast, generic wide-field imager for radio astronomy"; the standard modern imager.
- **Status:** pending captain approval

### IDG (Image Domain Gridding)
- **Primary paper:** "Image Domain Gridding: a fast method for convolutional resampling of visibilities"
- **Authors/year:** S. van der Tol, B. Veenboer, A. R. Offringa, 2018
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2018A&A...616A..27V/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/1909.07226 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; gridding
- **Reason:** abstract describes a new gridding/degridding method computing visibility contributions in image space, as an alternative to AW/W-projection gridding.
- **Status:** pending captain approval

### CASA (Common Astronomy Software Applications)
- **Primary paper:** "CASA Architecture and Applications" (foundational citation; note a newer overview, "CASA, the Common Astronomy Software Applications for Radio Astronomy," PASP 2022, also exists)
- **Authors/year:** J. P. McMullin, B. Waters, D. Schiebel, W. Young, K. Golap, 2007
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2007ASPC..376..127M/abstract
- **PDF:** not directly exposed
- **Cohort / stage:** classic; end-to-end calibration/imaging software package
- **Reason:** canonical citation for CASA, the primary reduction/imaging package for ALMA/VLA.
- **Status:** pending captain approval

### AIPS (Astronomical Image Processing System)
- **Primary paper:** "NRAO's Astronomical Image Processing System (AIPS)"
- **Authors/year:** D. C. Wells, 1985
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1985daa..conf..195W/abstract (DOI https://doi.org/10.1007/978-1-4615-9433-8_18)
- **PDF:** not directly exposed
- **Cohort / stage:** classic; end-to-end calibration/imaging software (deconvolution/analysis)
- **Reason:** original description of AIPS as the main NRAO system for production, deconvolution and analysis of radio images.
- **Status:** pending captain approval

### MIRIAD
- **Primary paper:** "A Retrospective View of Miriad"
- **Authors/year:** R. J. Sault, P. J. Teuben, M. C. H. Wright, 1995
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1995ASPC...77..433S/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/astro-ph/0612759 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; end-to-end reduction/imaging software
- **Reason:** canonical citation for MIRIAD, "a radio interferometry data-reduction package, designed for taking raw data through to the image analysis stage."
- **Status:** pending captain approval

### GILDAS/GREG
- **Naming note:** the brief's source wording "GILDA/GREG" is almost certainly a typo for **GILDAS** (Grenoble Image and Line Data Analysis Software), the umbrella package; **GREG** is GILDAS's plotting/graphics sub-tool, not a standalone citable package (see ambiguity note below).
- **Primary paper:** "Successes of and Challenges to GILDAS, a State-of-the-Art Radioastronomy Toolkit"
- **Authors/year:** J. Pety, 2005
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2005sf2a.conf..721P/abstract (SF2A-2005 conference proceedings); official software page https://www.iram.fr/IRAMFR/GILDAS/
- **PDF:** not directly exposed
- **Cohort / stage:** classic; calibration/imaging/analysis software suite (single-dish + interferometer)
- **Reason:** conventional citation for GILDAS in the literature; no dedicated standalone GREG paper exists.
- **Status:** pending captain approval

### DDFacet
- **Primary paper:** "Faceting for direction-dependent spectral deconvolution"
- **Authors/year:** C. Tasse, B. Hugo, M. Mirmont, O. Smirnov, et al., 2018
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2018A&A...611A..87T/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/1712.02078 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; imaging/deconvolution (direction-dependent, wideband faceted deconvolution)
- **Reason:** the DDFacet method paper: "wideband wide-field spectral deconvolution framework... based on image plane faceting."
- **Status:** pending captain approval

### w-stacking
- **Primary paper (two candidates, see ambiguity note):** "Analysis of Convolutional Resampling Algorithm Performance" (SKA Memo 132) — earliest dedicated treatment; also embedded/described in the WSClean paper above (Offringa et al. 2014).
- **Authors/year:** R. A. Humphreys, T. J. Cornwell, 2011
- **Landing page:** SKA Memo 132 landing (no ADS bibcode confirmed — see ambiguity note)
- **PDF:** SKA memo PDF exposed directly in search results (https://www.skatelescope.org/uploaded/59116_132_Memo_Humphreys.pdf) — recorded per instructions, not opened
- **Cohort / stage:** classic; gridding / wide-field imaging (non-coplanar-baseline correction)
- **Reason:** introduces/analyzes w-stacking as an alternative to w-projection for handling non-coplanar baselines.
- **Status:** pending captain approval

### w-projection
- **Primary paper:** "The Noncoplanar Baselines Effect in Radio Interferometry: The W-Projection Algorithm"
- **Authors/year:** T. J. Cornwell, K. Golap, S. Bhatnagar, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008ISTSP...2..647C/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/0807.4161 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; gridding / wide-field imaging
- **Reason:** the original W-projection algorithm paper, reinterpreting the non-coplanar-baselines effect via Fresnel diffraction.
- **Status:** pending captain approval

### NUFFT / HVOX
- **HVOX primary paper:** "HVOX: Scalable Interferometric Synthesis and Analysis of Spherical Sky Maps"
- **Authors/year:** S. Kashani, A. Jarret, et al., 2023 (arXiv:2306.06007)
- **Landing page:** https://arxiv.org/abs/2306.06007
- **PDF:** not confirmed exposed in snippet, omitted
- **Cohort / stage:** classic; gridding (3D-NUFFT-based synthesis/analysis, spherical/HEALPix-mesh compatible)
- **Reason:** resolves the "HVOX" token — a specific 3D-NUFFT-based gridder/synthesis algorithm positioned as an alternative to w-gridding for SKA/LOFAR-scale imaging.
- **Status:** pending captain approval
- **General NUFFT reference (see ambiguity note — no single canonical radio-interferometry-specific NUFFT paper was identified):** "A Parallel Nonuniform Fast Fourier Transform Library" (FINUFFT), A. H. Barnett, J. F. Magland, L. af Klinteberg, 2019. Landing page: https://ui.adsabs.harvard.edu/abs/2019SJSC...41C.479B/abstract. PDF: arXiv abstract page https://arxiv.org/abs/1808.06736 (not opened). Cohort/stage: classic; gridding (general-purpose, not radio-interferometry-specific). Reason: widely-cited general NUFFT library, included as the representative reference per the brief's request; flagged as not RI-specific. Status: pending captain approval.

### A-projection
- **Primary paper:** "Correcting direction-dependent gains in the deconvolution of radio interferometric images"
- **Authors/year:** S. Bhatnagar, T. J. Cornwell, K. Golap, J. M. Uson, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008A&A...487..419B/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/0805.0834 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; calibration / imaging (direction-dependent primary-beam/antenna-aperture correction during deconvolution)
- **Reason:** the original A-projection paper — "an iterative deconvolution algorithm that corrects known direction-dependent errors due to antenna power patterns."
- **Status:** pending captain approval

### Metrics used in the astroCAMP paper
- **Primary paper:** "astroCAMP: A Community Benchmark and Co-Design Framework for Sustainable SKA-Scale Radio Imaging"
- **Authors/year:** author list not fully resolved beyond first-author initial "C." (part of the SEAMS project); 2025 (submitted December 2025)
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2025arXiv251213591C/abstract (https://arxiv.org/abs/2512.13591)
- **PDF:** not directly exposed
- **Cohort / stage:** classic (benchmarking/methodology paper spanning classic pipelines); metrics/benchmarking framework, not a single pipeline stage
- **Reason:** contributes "a unified metric suite spanning performance, utilisation, memory/data-movement, sustainability, economics, and scientific fidelity" for SKA-scale imaging pipelines — directly matches "metrics used in the astroCAMP paper."
- **Status:** pending captain approval

### Focused CLEAN
- Could not confidently identify a specific paper or named algorithm variant called "focused CLEAN." Candidates considered and rejected: Clark CLEAN, Cotton-Schwab CLEAN, informal "boxed"/region-restricted CLEAN, DoB-CLEAN/DoG-HiT. **Status:** unresolved — pending captain clarification (see ambiguity note).

### Multiscale CLEAN
- **Primary paper:** "Multiscale CLEAN Deconvolution of Radio Synthesis Images"
- **Authors/year:** T. J. Cornwell, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008ISTSP...2..793C/abstract
- **PDF:** arXiv:0806.2228 abstract page (PDF link exposed directly in search, not opened)
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** the canonical multiscale CLEAN paper, improving CLEAN performance for extended objects.
- **Status:** pending captain approval

### MS-MFS (multi-scale multi-frequency synthesis)
- **Primary paper:** "A multi-scale multi-frequency deconvolution algorithm for synthesis imaging in radio interferometry"
- **Authors/year:** U. Rau, T. J. Cornwell, 2011
- **Landing page:** https://www.aanda.org/articles/aa/abs/2011/08/aa17104-11/aa17104-11.html (A&A 532, A71; ADS bibcode likely `2011A&A...532A..71R`, not independently re-verified — see ambiguity note)
- **PDF:** arXiv abstract page https://arxiv.org/abs/1106.2745 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; deconvolution / CLEAN-family (wideband extension)
- **Reason:** the canonical MS-MFS paper combining multi-scale and multi-frequency deconvolution.
- **Status:** pending captain approval

### SARA / PURIFY
- **SARA primary paper:** "Sparsity Averaging Reweighted Analysis (SARA): a novel algorithm for radio-interferometric imaging"
  - Authors/year: R. E. Carrillo, J. D. McEwen, Y. Wiaux, 2012
  - Landing page: https://ui.adsabs.harvard.edu/abs/2012MNRAS.426.1223C/abstract (bibcode inferred from journal metadata, not independently re-verified — see ambiguity note)
  - PDF: arXiv abstract page https://arxiv.org/abs/1205.3123 (PDF link present alongside abs, not opened)
  - Cohort/stage: classic; imaging/inverse-problem (compressed-sensing / convex optimization)
  - Reason: the original SARA algorithm — sparsity-averaging regularization across multiple wavelet bases for radio-interferometric imaging.
  - Status: pending captain approval
- **PURIFY primary paper:** "PURIFY: a new approach to radio-interferometric imaging"
  - Authors/year: R. E. Carrillo, J. D. McEwen, Y. Wiaux, 2014
  - Landing page: https://ui.adsabs.harvard.edu/abs/2014MNRAS.439.3591C/abstract (bibcode inferred from journal metadata, not independently re-verified — see ambiguity note)
  - PDF: arXiv abstract page https://arxiv.org/abs/1307.4370 (PDF link present alongside abs, not opened)
  - Cohort/stage: classic; imaging/inverse-problem (convex-optimization software implementing SARA-family priors)
  - Reason: the original PURIFY software/algorithm paper. A later companion, "Robust sparse image reconstruction of radio interferometric observations with PURIFY" (Pratley, McEwen, d'Avezac, Carrillo, Onose, Wiaux, 2018, MNRAS 473, 1038, arXiv:1610.02400), extends/validates it on real data — noted as a related follow-up, not proposed as a separate row.
  - Status: pending captain approval

### Schwab 1984 (citation-only — no metric row)
- **Reference:** "Relaxing the isoplanatism assumption in self-calibration; applications to low-frequency radio interferometry"
- **Authors/year:** F. R. Schwab, 1984
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1984AJ.....89.1076S/abstract (DOI 10.1086/113605)
- **PDF:** not directly exposed
- **Cohort / stage:** classic; calibration / CLEAN-family. **Citation-only per captain decision — no metrics-table row will be created for this entry.**
- **Reason:** canonical Schwab 1984 self-calibration/gridding reference cited throughout the literature.
- **Status:** citation-only, no extraction planned

---

## ML / emerging

### uSARA (unconstrained SARA)
- **Primary paper:** "Scalable precision wide-field imaging in radio interferometry: I. uSARA validated on ASKAP data"
- **Authors/year:** A. G. Wilber, A. Dabbech, A. Jackson, Y. Wiaux, 2023
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2023MNRAS.522.5558W/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2302.14148 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; imaging/inverse-problem (optimization-based; precursor to the plug-and-play ML variant AIRI)
- **Reason:** uSARA is "a pure optimization variant leveraging a... proximal denoiser," extending SARA to unconstrained minimization, validated on real ASKAP data and outperforming CLEAN.
- **Status:** pending captain approval

### SMURFIT
- **Naming note:** resolved to "Spatial-frequency Multi-class Radio Fourier Imaging Technique," but this could not be corroborated on ADS or arXiv (see ambiguity note) — treat authors/year/abstract detail as low-confidence.
- **Primary paper:** "SMURFIT: Spatial-frequency Multi-class Radio Fourier Imaging Technique"
- **Authors/year:** Sunrise Wang, Simon Prunet, Shan Mignot, Andre Ferrari; posted ~2026 (SSRN working paper)
- **Landing page:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6967740 (SSRN abstract page — direct fetch returned HTTP 403; metadata rests on search-engine snippet only)
- **PDF:** not directly exposed (SSRN gates PDF access)
- **Cohort / stage:** ML/emerging; imaging/inverse-problem, likely gridding/distributed-imaging ("transforms measured visibilities into images of the sky," extends a prior imaging framework "to multiple nodes" for scalability)
- **Reason:** direct title match to "SMURFIT" in a radio-imaging context; likely related to the same authors' 2025 arXiv paper "A Decentralized Framework for Radio-interferometric Image Reconstruction" (already in the R2D2-citing cohort, bibcode `2025AJ....169..289W`) — relationship unconfirmed.
- **Status:** pending captain approval

### HyperAIRI — already preserved
- Already summarized and classified in the R2D2-citing cohort at bibcode `2026ApJS..283....9T` ("HyperAIRI: A Plug-and-play Algorithm for Precise Hyperspectral Image Reconstruction in Radio Interferometry," Tang, Dabbech, Jackson et al.). See `cohorts/r2d2-citing/papers/2026ApJS..283....9T.md`. Not proposed as a new candidate.

### Mars et al., "Learned Radio Interferometric Imaging for Varying Visibility Coverage" — already preserved
- Already summarized and classified in the R2D2-citing cohort at bibcode `2025RASTI...4..25M` (Mars, Betcke, McEwen). See `cohorts/r2d2-citing/papers/2025RASTI...4..25M.md`. Not proposed as a new candidate.

### R2D2 source paper
- **Primary paper:** "The R2D2 Deep Neural Network Series Paradigm for Fast Precision Imaging in Radio Astronomy"
- **Authors/year:** A. Aghabiglou, C. S. Chu, A. Jackson, A. Dabbech, Y. Wiaux, 2024
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2024ApJS..273....3A/abstract
- **PDF:** not directly exposed
- **Cohort / stage:** ML/emerging (per explicit captain decision); end-to-end ML reconstruction
- **Reason:** the R2D2 method's own introduction paper. It is not itself among the 33 papers that cite it, so per the captain's decision it is a genuine new candidate here.
- **Status:** pending captain approval

### AIRI precursor
- **Primary paper (see ambiguity note for an alternate candidate):** "First AI for Deep Super-resolution Wide-field Imaging in Radio Astronomy: Unveiling Structure in ESO 137-006"
- **Authors/year:** A. Dabbech, M. Terris, A. Jackson, M. Ramatsoku, O. M. Smirnov, Y. Wiaux, 2022
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2022ApJ...939L...4D/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2207.11336 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (plug-and-play DNN denoiser regularization — original AIRI, applied to real MeerKAT data)
- **Reason:** "the first AI-based framework for deep, super-resolution, wide-field radio-interferometric imaging" — the foundational AIRI paper, predating the "AIRI plug-and-play" follow-up already in the R2D2-citing cohort (`2025MNRAS.537.1608T`).
- **Status:** pending captain approval

### POLISH
- **Primary paper:** "Deep radio-interferometric imaging with POLISH: DSA-2000 and weak lensing"
- **Authors/year:** Liam Connor, Katherine L. Bouman, Vikram Ravi, Gregg Hallinan, 2022
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.2614C/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2111.03249 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (super-resolution/deconvolution CNN)
- **Reason:** "trained a high-dynamic range residual neural network to learn the mapping between the dirty image and the true radio sky, calling this procedure POLISH, in contrast to... CLEAN" — the original method, distinct from and predating "POLISH'ing the Sky..." (Wu, Connor, McCarty et al.), already in the R2D2-citing cohort at `2026arXiv260309162W`.
- **Status:** pending captain approval

### PRIMO
- **Primary paper:** "Principal-Component Interferometric Modeling (PRIMO), an Algorithm for EHT Data I: Reconstructing Images from Simulated EHT Observations"
- **Authors/year:** Lia Medeiros, Dimitrios Psaltis, Tod R. Lauer, Feryal Özel, 2023
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2023ApJ...943..144M/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2208.01667 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML/statistical reconstruction (PCA-based, trained on GRMHD simulations)
- **Reason:** the original PRIMO algorithm-introduction paper, distinct from both "The Image of the M87 Black Hole Reconstructed with PRIMO" (Medeiros et al. 2023, ApJL 947, L7) and "Theoretical Foundation of Black Hole Image Reconstruction Using PRIMO," already in the R2D2-citing cohort at `2025ApJ...984...86P`.
- **Status:** pending captain approval

### Schmidt et al. direct-CNN paper
- **Primary paper:** "Deep learning-based imaging in radio interferometry"
- **Authors/year:** K. Schmidt, F. Geyer, S. Fröse, P.-S. Blomenkamp, M. Brüggen, F. de Gasperin, D. Elsässer, W. Rhode, 2022
- **Landing page:** https://www.aanda.org/articles/aa/full_html/2022/08/aa42113-21/aa42113-21.html (A&A 664, A134; ADS bibcode likely `2022A&A...664A.134S`, not independently re-verified — see ambiguity note)
- **PDF:** arXiv abstract page https://arxiv.org/abs/2203.11757 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (direct CNN, Fourier-space inpainting rather than iterative deconvolution)
- **Reason:** a CNN (SRResNet-derived) that "reconstructs missing information directly in Fourier space... no iterative source model is formed" — matches the "direct CNN" description; part of the radionets project.
- **Status:** pending captain approval

---

## Notes on ambiguity

1. **GILDAS/GREG:** the brief's "GILDA/GREG" wording is almost certainly a typo for GILDAS. No dedicated peer-reviewed GREG paper exists — GREG is documented only as a GILDAS plotting sub-module in IRAM memos/manuals.
2. **NUFFT/HVOX:** HVOX was clearly identified as a specific 3D-NUFFT-based radio-interferometric synthesis algorithm. No single canonical "NUFFT for radio interferometry" primary reference (distinct from general-purpose NUFFT papers) was confidently identified; several candidates exist (Duijndam & Schonewille 1997; Jackson et al. 1991; Fessler & Sutton 2003; Barnett, Magland & af Klinteberg 2019/FINUFFT). FINUFFT was used as the representative general reference and is flagged as not radio-interferometry-specific.
3. **Focused CLEAN:** no paper or named algorithm variant called "focused CLEAN" could be identified. Recommend the captain clarify whether this refers to a specific named technique or to informal region-restricted ("boxed") CLEAN.
4. **SMURFIT:** resolved to a specific SSRN working paper, but this could not be corroborated on ADS or arXiv, and the SSRN page itself could not be fetched (HTTP 403). Treat the entry's authors/year/relationship-to-other-papers as low-confidence pending direct verification.
5. **w-stacking primary reference:** two candidate primary sources exist — Humphreys & Cornwell 2011 (SKA Memo 132, earliest dedicated analysis) and Offringa et al. 2014 (WSClean paper, most-cited description/implementation, also listed separately above). The captain should decide which is the primary citation for this row.
6. **Bibcodes constructed rather than directly confirmed:** for SARA, PURIFY, MS-MFS, and the Schmidt et al. paper, the ADS bibcode was inferred from journal/volume/page metadata in search snippets rather than confirmed via a direct ADS abstract-page fetch. The DOI and arXiv links for each were independently confirmed and are reliable; the bibcode strings themselves should be spot-checked before use as stable identifiers.
7. **AIRI precursor — two candidates:** (a) Dabbech et al. 2022, ApJL 939, L4 (the true first introduction of the AIRI concept, selected above), and (b) Wilber, Dabbech, Jackson & Wiaux 2023, MNRAS 522, 5576 ("AIRI validated on ASKAP data," arXiv:2302.14149, a companion/validation paper to the uSARA paper). The captain should confirm which paper is intended as "the" AIRI precursor.
