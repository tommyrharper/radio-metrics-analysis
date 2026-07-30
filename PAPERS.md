# Candidate Bibliography

**Status: captain-approved extraction complete for all accessible remaining candidates.** The discovery-time PDF notes below are retained as provenance for the pre-approval bibliography. Full-text extraction outcomes are recorded in each entry's status.

The remaining candidates were explicitly approved before extraction. One identifiable paper, SMURFIT, remains blocked by authoritative full-text access; Focused CLEAN remains unresolved because no paper was identified.

Entries already preserved in the completed `cohorts/r2d2-citing/` corpus are cross-referenced by bibcode rather than duplicated.

**2026-07-30 follow-up:** added a "CLEAN-family algorithmic variants" subsection (Högbom, Clark, Cotton-Schwab, Steer-Dewdney-Ito, Asp-Clean, Multi-Resolution CLEAN, joined-channel/wideband CLEAN, plus MS-MFS/MT-MFS naming clarification) per captain-approved scope extension. Same bibliography-only rules applied; see ambiguity notes 8–11.

---

## Classic / current-practice

### WSClean
- **Primary paper:** "WSClean: an implementation of a fast, generic wide-field imager for radio astronomy"
- **Authors/year:** A. R. Offringa, B. McKinley, N. Hurley-Walker, et al., 2014
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2014MNRAS.444..606O/abstract
- **PDF:** not directly exposed in search metadata
- **Cohort / stage:** classic; gridding / imaging (wide-field imager; introduces w-stacking)
- **Reason:** title/abstract explicitly describe it as "a fast, generic wide-field imager for radio astronomy"; the standard modern imager.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2014MNRAS.444..606O.md`

### IDG (Image Domain Gridding)
- **Primary paper:** "Image Domain Gridding: a fast method for convolutional resampling of visibilities"
- **Authors/year:** S. van der Tol, B. Veenboer, A. R. Offringa, 2018
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2018A&A...616A..27V/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/1909.07226 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; gridding
- **Reason:** abstract describes a new gridding/degridding method computing visibility contributions in image space, as an alternative to AW/W-projection gridding.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2018A_and_A...616A..27V.md`

### CASA (Common Astronomy Software Applications)
- **Primary paper:** "CASA Architecture and Applications" (foundational citation; note a newer overview, "CASA, the Common Astronomy Software Applications for Radio Astronomy," PASP 2022, also exists)
- **Authors/year:** J. P. McMullin, B. Waters, D. Schiebel, W. Young, K. Golap, 2007
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2007ASPC..376..127M/abstract
- **PDF:** not directly exposed
- **Cohort / stage:** classic; end-to-end calibration/imaging software package
- **Reason:** canonical citation for CASA, the primary reduction/imaging package for ALMA/VLA.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2007ASPC..376..127M.md`

### AIPS (Astronomical Image Processing System)
- **Primary paper:** "NRAO's Astronomical Image Processing System (AIPS)"
- **Authors/year:** D. C. Wells, 1985
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1985daa..conf..195W/abstract (DOI https://doi.org/10.1007/978-1-4615-9433-8_18)
- **PDF:** not directly exposed
- **Cohort / stage:** classic; end-to-end calibration/imaging software (deconvolution/analysis)
- **Reason:** original description of AIPS as the main NRAO system for production, deconvolution and analysis of radio images.
- **Status:** captain approved; extraction outcome recorded in `cohorts/classic/papers/1985daa..conf..195W.md` (full-text methods and metrics remain blocked by source access)

### MIRIAD
- **Primary paper:** "A Retrospective View of Miriad"
- **Authors/year:** R. J. Sault, P. J. Teuben, M. C. H. Wright, 1995
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1995ASPC...77..433S/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/astro-ph/0612759 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; end-to-end reduction/imaging software
- **Reason:** canonical citation for MIRIAD, "a radio interferometry data-reduction package, designed for taking raw data through to the image analysis stage."
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1995ASPC...77..433S.md`

### GILDAS/GREG
- **Naming note:** the brief's source wording "GILDA/GREG" is almost certainly a typo for **GILDAS** (Grenoble Image and Line Data Analysis Software), the umbrella package; **GREG** is GILDAS's plotting/graphics sub-tool, not a standalone citable package (see ambiguity note below).
- **Primary paper:** "Successes of and Challenges to GILDAS, a State-of-the-Art Radioastronomy Toolkit"
- **Authors/year:** J. Pety, 2005
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2005sf2a.conf..721P/abstract (SF2A-2005 conference proceedings); official software page https://www.iram.fr/IRAMFR/GILDAS/
- **PDF:** not directly exposed
- **Cohort / stage:** classic; calibration/imaging/analysis software suite (single-dish + interferometer)
- **Reason:** conventional citation for GILDAS in the literature; no dedicated standalone GREG paper exists.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2005sf2a.conf..721P.md`

### DDFacet
- **Primary paper:** "Faceting for direction-dependent spectral deconvolution"
- **Authors/year:** C. Tasse, B. Hugo, M. Mirmont, O. Smirnov, et al., 2018
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2018A&A...611A..87T/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/1712.02078 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; imaging/deconvolution (direction-dependent, wideband faceted deconvolution)
- **Reason:** the DDFacet method paper: "wideband wide-field spectral deconvolution framework... based on image plane faceting."
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2018A_and_A...611A..87T.md`

### w-stacking
- **Primary paper (two candidates, see ambiguity note):** "Analysis of Convolutional Resampling Algorithm Performance" (SKA Memo 132) — earliest dedicated treatment; also embedded/described in the WSClean paper above (Offringa et al. 2014).
- **Authors/year:** B. Humphreys, T. J. Cornwell, 2011
- **Landing page:** SKA Memo 132 landing (no ADS bibcode confirmed — see ambiguity note)
- **PDF:** SKA memo PDF exposed directly in search results (https://www.skatelescope.org/uploaded/59116_132_Memo_Humphreys.pdf) — recorded per instructions, not opened
- **Cohort / stage:** classic; gridding / wide-field imaging (non-coplanar-baseline correction)
- **Reason:** introduces/analyzes w-stacking as an alternative to w-projection for handling non-coplanar baselines.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/SKA-MEMO-132.md`

### w-projection
- **Primary paper:** "The Noncoplanar Baselines Effect in Radio Interferometry: The W-Projection Algorithm"
- **Authors/year:** T. J. Cornwell, K. Golap, S. Bhatnagar, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008ISTSP...2..647C/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/0807.4161 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; gridding / wide-field imaging
- **Reason:** the original W-projection algorithm paper, reinterpreting the non-coplanar-baselines effect via Fresnel diffraction.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2008ISTSP...2..647C.md`

### NUFFT / HVOX
- **HVOX primary paper:** "HVOX: Scalable Interferometric Synthesis and Analysis of Spherical Sky Maps"
- **Authors/year:** S. Kashani, A. Jarret, et al., 2023 (arXiv:2306.06007)
- **Landing page:** https://arxiv.org/abs/2306.06007
- **PDF:** not confirmed exposed in snippet, omitted
- **Cohort / stage:** classic; gridding (3D-NUFFT-based synthesis/analysis, spherical/HEALPix-mesh compatible)
- **Reason:** resolves the "HVOX" token — a specific 3D-NUFFT-based gridder/synthesis algorithm positioned as an alternative to w-gridding for SKA/LOFAR-scale imaging.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2023arXiv230606007K.md`
- **General NUFFT reference (see ambiguity note - no single canonical radio-interferometry-specific NUFFT paper was identified):** "A Parallel Nonuniform Fast Fourier Transform Library" (FINUFFT), A. H. Barnett, J. F. Magland, L. af Klinteberg, 2019. Landing page: https://ui.adsabs.harvard.edu/abs/2019SJSC...41C.479B/abstract. PDF: arXiv abstract page https://arxiv.org/abs/1808.06736 (not opened). Cohort/stage: classic; gridding (general-purpose, not radio-interferometry-specific). Reason: widely-cited general NUFFT library, included as the representative reference per the brief's request; flagged as not RI-specific. Status: skipped by the approved extraction brief because this is the secondary general reference bundled with HVOX.

### A-projection
- **Primary paper:** "Correcting direction-dependent gains in the deconvolution of radio interferometric images"
- **Authors/year:** S. Bhatnagar, T. J. Cornwell, K. Golap, J. M. Uson, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008A&A...487..419B/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/0805.0834 (PDF link present alongside abs, not opened)
- **Cohort / stage:** classic; calibration / imaging (direction-dependent primary-beam/antenna-aperture correction during deconvolution)
- **Reason:** the original A-projection paper — "an iterative deconvolution algorithm that corrects known direction-dependent errors due to antenna power patterns."
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2008A_and_A...487..419B.md`

### Metrics used in the astroCAMP paper
- **Primary paper:** "astroCAMP: A Community Benchmark and Co-Design Framework for Sustainable SKA-Scale Radio Imaging"
- **Authors/year:** author list not fully resolved beyond first-author initial "C." (part of the SEAMS project); 2025 (submitted December 2025)
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2025arXiv251213591C/abstract (https://arxiv.org/abs/2512.13591)
- **PDF:** not directly exposed
- **Cohort / stage:** classic (benchmarking/methodology paper spanning classic pipelines); metrics/benchmarking framework, not a single pipeline stage
- **Reason:** contributes "a unified metric suite spanning performance, utilisation, memory/data-movement, sustainability, economics, and scientific fidelity" for SKA-scale imaging pipelines — directly matches "metrics used in the astroCAMP paper."
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2025arXiv251213591C.md`

### CLEAN-family algorithmic variants (added per captain-approved follow-up, 2026-07-30)

Evaluated against the widely-recognized core CLEAN family per the follow-up brief. Each entry states explicitly whether it is an ALGORITHMIC variant, IMPLEMENTATION SOFTWARE, or an IMAGING FEATURE of existing software, per the follow-up's instruction to distinguish these.

#### Högbom CLEAN
- **Primary paper:** "Aperture Synthesis with a Non-Regular Distribution of Interferometer Baselines"
- **Authors/year:** J. A. Högbom, 1974
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1974A&AS...15..417H/abstract
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — the original, foundational CLEAN deconvolution algorithm (image-domain, iterative point-source subtraction).
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** the canonical original CLEAN paper; every other entry in this section is a variant of it.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1974A_and_AS...15..417H.md`

#### Clark CLEAN
- **Primary paper:** "An efficient implementation of the algorithm 'CLEAN'"
- **Authors/year:** B. G. Clark, 1980
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1980A&A....89..377C/abstract
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — FFT-accelerated, patch/beam-based minor-cycle variant of Högbom CLEAN that subtracts many components per major-cycle pass.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** canonical, widely-implemented speed-oriented CLEAN variant (e.g. AIPS `APCLN`, CASA's Clark-based minor cycle).
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1980A_and_A....89..377C.md`

#### Cotton-Schwab CLEAN
- **Primary paper:** "Relaxing the isoplanatism assumption in self-calibration; applications to low-frequency radio interferometry" — **the same paper already listed above as the citation-only Schwab 1984 entry.**
- **Authors/year:** F. R. Schwab, 1984
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1984AJ.....89.1076S/abstract (DOI 10.1086/113605)
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — a data-domain major/minor-cycle CLEAN variant (subtracting components from the ungridded visibility data each major cycle rather than the image), described in this paper alongside its self-calibration content.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** verified as the correct primary reference via a standard NRAO deconvolution reference (Bridle, "Deconvolution Tutorial," cv.nrao.edu/~abridle/deconvol), which cites this exact 1984 AJ paper (as "Schwab 1984b") for the Cotton-Schwab algorithm. No separate, more specific Schwab paper describing Cotton-Schwab CLEAN was found.
- **Status:** captain approved; no separate summary created because the extraction brief explicitly excludes Schwab 1984 as a duplicate second file and retains its citation-only treatment

#### Steer-Dewdney-Ito CLEAN (SDI CLEAN)
- **Primary paper:** "Enhancements to the deconvolution algorithm 'CLEAN'"
- **Authors/year:** D. G. Steer, P. E. Dewdney, M. R. Ito, 1984
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1984A&A...137..159S/abstract
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — removes components in threshold-selected groups rather than individually, reducing "striping"/corrugation artifacts on extended emission and improving speed.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** a recognized core CLEAN enhancement (e.g. AIPS `SDCLN`), distinct in mechanism from Clark and Cotton-Schwab.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1984A_and_A...137..159S.md`

#### Multi-Scale CLEAN — already present, no new row
Already covered below by the existing "Multiscale CLEAN" entry (Cornwell 2008). Confirmed via independent search hits as the correct standard reference; cross-referenced only.

#### Multi-Term Multi-Frequency Synthesis (MT-MFS) — same algorithm as the existing MS-MFS entry
"MT-MFS" and "MS-MFS" are used interchangeably in current literature and software documentation (CASA `tclean`'s `mtmfs` deconvolver, WSClean docs) for the **same algorithm**: Rau & Cornwell 2011 (already listed below as "MS-MFS"). No new row is added for "MT-MFS" — it is the same entry under a different common name.

A genuinely distinct, earlier precursor was found and is flagged as an optional additional candidate rather than added outright:
- **Candidate primary paper:** "Multi-frequency synthesis techniques for radio interferometric imaging"
- **Authors/year:** R. J. Sault, M. H. Wieringa, 1994
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1994A&AS..108..585S/abstract
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — multi-frequency (Taylor-term) synthesis/deconvolution *without* the multi-scale component; a precursor that Rau & Cornwell 2011 explicitly extends.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** if the captain wants a citation for plain "multi-frequency synthesis" distinct from the combined multi-scale + multi-frequency algorithm, this is it. Not added as a required row — judgment call for the captain.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1994A_and_AS..108..585S.md`

#### Multi-Scale Multi-Frequency Synthesis "where distinct from MS-MFS" — confirmed not distinct
No separate paper under this exact name was found beyond Rau & Cornwell 2011 (the existing "MS-MFS" entry below). Confirmed same entry; no new row added, per the follow-up's instruction to avoid duplicating entries already present under another name.

#### Joined-channel / wideband CLEAN (WSClean)
- **Primary paper:** "An optimized algorithm for multi-scale wideband deconvolution of radio astronomical images"
- **Authors/year:** A. R. Offringa, O. Smirnov, 2017
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2017MNRAS.471..301O/abstract (DOI 10.1093/mnras/stx1547)
- **PDF:** arXiv abstract page https://arxiv.org/abs/1706.06786 (PDF link present alongside abs, not opened)
- **Variant type:** ALGORITHMIC paper describing an IMAGING FEATURE — this is WSClean's own cited reference for its `-join-channels` joined-channel deconvolution mode; distinct from the base WSClean 2014 software paper already listed above, and explicitly distinguished by WSClean's documentation from CASA's MS-MFS/MT-MFS approach.
- **Cohort / stage:** classic; deconvolution / CLEAN-family (wideband, multi-scale + multi-frequency joint minor-cycle optimization)
- **Reason:** the specific algorithmic reference for wideband/joined-channel CLEAN as implemented in a current major imager (WSClean), as opposed to the general WSClean software paper. CASA's side of wideband/joined-channel CLEAN is already covered by the existing MS-MFS entry (Rau & Cornwell 2011) — no separate CASA-side row added.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2017MNRAS.471..301O.md`

#### Adaptive Scale Pixel (Asp-Clean)
- **Primary paper:** "Scale sensitive deconvolution of interferometric images. I. Adaptive Scale Pixel (Asp) decomposition"
- **Authors/year:** S. Bhatnagar, T. J. Cornwell, 2004
- **Landing page:** https://www.aanda.org/articles/aa/abs/2004/41/aa0354-04/aa0354-04.html (A&A 426, 747; DOI 10.1051/0004-6361:20040354; also arXiv:astro-ph/0407225)
- **PDF:** publisher PDF exposed directly alongside the abstract in search results (aanda.org/articles/aa/pdf/2004/41/aa0354-04.pdf), not opened
- **Variant type:** ALGORITHMIC — models the sky as adaptive-scale pixels rather than a fixed set of Gaussian scales (contrast with multi-scale CLEAN), a distinct image-model approach in the CLEAN lineage.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** a recognized representative scale-sensitive CLEAN variant, structurally distinct from multi-scale CLEAN.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2004A_and_A...426..747B.md`

#### Multi-Resolution CLEAN (MRC / M-CLEAN) — additional mainstream variant
- **Primary paper:** "The Multi-Resolution CLEAN and its application to the short-spacing problem in interferometry"
- **Authors/year:** B. P. Wakker, U. J. Schwarz, 1988
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1988A&A...200..312W/abstract (bibcode constructed from consistent secondary-source citations — WebFetch could not directly render the ADS page for this entry; see ambiguity note)
- **PDF:** not directly exposed
- **Variant type:** ALGORITHMIC — builds a smoothed low-resolution map and a difference map, CLEANs each with a resolution-appropriate beam, then recombines; a historical precursor concept to multi-scale CLEAN.
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** explicitly named as a core member of the CLEAN-algorithm family ("HOGBOM, CLARK, MX, SDI, MRC, MULTI") in IRAM/GILDAS map-processing documentation, and discussed as a precursor in later multi-scale CLEAN literature; mainstream enough to include per the follow-up's "any other genuinely mainstream CLEAN variant" instruction.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/1988A_and_A...200..312W.md`

No other genuinely distinct mainstream CLEAN variant was identified beyond the entries above; "MX" and "MULTI" (seen in the GILDAS family listing) correspond to the AIPS program name for Cotton-Schwab CLEAN and to generic multi-scale/multi-field CLEAN respectively, not additional distinct algorithms.

### Focused CLEAN
- Could not confidently identify a specific paper or named algorithm variant called "focused CLEAN." Candidates considered and rejected as non-matches for this specific name: Clark CLEAN, Cotton-Schwab CLEAN (both now listed above as their own distinct entries), informal "boxed"/region-restricted CLEAN, DoB-CLEAN/DoG-HiT. **Status:** unresolved — pending captain clarification (see ambiguity note).

### Multiscale CLEAN
- **Primary paper:** "Multiscale CLEAN Deconvolution of Radio Synthesis Images"
- **Authors/year:** T. J. Cornwell, 2008
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2008ISTSP...2..793C/abstract
- **PDF:** arXiv:0806.2228 abstract page (PDF link exposed directly in search, not opened)
- **Cohort / stage:** classic; deconvolution / CLEAN-family
- **Reason:** the canonical multiscale CLEAN paper, improving CLEAN performance for extended objects.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2008ISTSP...2..793C.md`

### MS-MFS (multi-scale multi-frequency synthesis, a.k.a. MT-MFS)
- **Primary paper:** "A multi-scale multi-frequency deconvolution algorithm for synthesis imaging in radio interferometry"
- **Authors/year:** U. Rau, T. J. Cornwell, 2011
- **Landing page:** https://www.aanda.org/articles/aa/abs/2011/08/aa17104-11/aa17104-11.html (A&A 532, A71; ADS bibcode `2011A&A...532A..71R`, confirmed during extraction)
- **PDF:** arXiv abstract page https://arxiv.org/abs/1106.2745 (PDF link present alongside abs, not opened)
- **Naming note (follow-up):** this algorithm is referred to as both "MS-MFS" and "MT-MFS" interchangeably in CASA/WSClean documentation and the wider literature; see the "CLEAN-family algorithmic variants" subsection above for the distinct, earlier Sault & Wieringa 1994 multi-frequency-only precursor.
- **Cohort / stage:** classic; deconvolution / CLEAN-family (wideband extension)
- **Reason:** the canonical MS-MFS paper combining multi-scale and multi-frequency deconvolution.
- **Status:** captain approved; summary extracted to `cohorts/classic/papers/2011A_and_A...532A..71R.md`

### SARA / PURIFY
- **SARA primary paper:** "Sparsity Averaging Reweighted Analysis (SARA): a novel algorithm for radio-interferometric imaging"
  - Authors/year: R. E. Carrillo, J. D. McEwen, Y. Wiaux, 2012
  - Landing page: https://ui.adsabs.harvard.edu/abs/2012MNRAS.426.1223C/abstract (bibcode confirmed during extraction)
  - PDF: arXiv abstract page https://arxiv.org/abs/1205.3123 (PDF link present alongside abs, not opened)
  - Cohort/stage: classic; imaging/inverse-problem (compressed-sensing / convex optimization)
  - Reason: the original SARA algorithm — sparsity-averaging regularization across multiple wavelet bases for radio-interferometric imaging.
  - Status: captain approved; summary extracted to `cohorts/classic/papers/2012MNRAS.426.1223C.md`
- **PURIFY primary paper:** "PURIFY: a new approach to radio-interferometric imaging"
  - Authors/year: R. E. Carrillo, J. D. McEwen, Y. Wiaux, 2014
  - Landing page: https://ui.adsabs.harvard.edu/abs/2014MNRAS.439.3591C/abstract (bibcode confirmed during extraction)
  - PDF: arXiv abstract page https://arxiv.org/abs/1307.4370 (PDF link present alongside abs, not opened)
  - Cohort/stage: classic; imaging/inverse-problem (convex-optimization software implementing SARA-family priors)
  - Reason: the original PURIFY software/algorithm paper. A later companion, "Robust sparse image reconstruction of radio interferometric observations with PURIFY" (Pratley, McEwen, d'Avezac, Carrillo, Onose, Wiaux, 2018, MNRAS 473, 1038, arXiv:1610.02400), extends/validates it on real data — noted as a related follow-up, not proposed as a separate row.
  - Status: captain approved; summary extracted to `cohorts/classic/papers/2014MNRAS.439.3591C.md`

### Schwab 1984 (citation-only — no metric row)
- **Reference:** "Relaxing the isoplanatism assumption in self-calibration; applications to low-frequency radio interferometry"
- **Authors/year:** F. R. Schwab, 1984
- **Landing page:** https://ui.adsabs.harvard.edu/abs/1984AJ.....89.1076S/abstract (DOI 10.1086/113605)
- **PDF:** not directly exposed
- **Cohort / stage:** classic; calibration / CLEAN-family. **Citation-only per captain decision — no metrics-table row will be created for this entry.**
- **Reason:** canonical Schwab 1984 self-calibration/gridding reference cited throughout the literature.
- **Status:** citation-only, no extraction planned
- **Follow-up note (2026-07-30):** this same paper is also the verified primary reference for the algorithmic "Cotton-Schwab CLEAN" variant, added separately above in "CLEAN-family algorithmic variants." See ambiguity note 8 — the reuse is flagged, not resolved.

---

## ML / emerging

### uSARA (unconstrained SARA)
- **Primary paper:** "Scalable precision wide-field imaging in radio interferometry: I. uSARA validated on ASKAP data"
- **Authors/year:** A. G. Wilber, A. Dabbech, A. Jackson, Y. Wiaux, 2023
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2023MNRAS.522.5558W/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2302.14148 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; imaging/inverse-problem (optimization-based; precursor to the plug-and-play ML variant AIRI)
- **Reason:** uSARA is "a pure optimization variant leveraging a... proximal denoiser," extending SARA to unconstrained minimization, validated on real ASKAP data and outperforming CLEAN.
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2023MNRAS.522.5558W.md`

### SMURFIT
- **Naming note:** resolved to "Spatial-frequency Multi-class Radio Fourier Imaging Technique," but this could not be corroborated on ADS or arXiv (see ambiguity note) — treat authors/year/abstract detail as low-confidence.
- **Primary paper:** "SMURFIT: Spatial-frequency Multi-class Radio Fourier Imaging Technique"
- **Authors/year:** Sunrise Wang, Simon Prunet, Shan Mignot, Andre Ferrari; posted ~2026 (SSRN working paper)
- **Landing page:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6967740 (SSRN abstract page — direct fetch returned HTTP 403; metadata rests on search-engine snippet only)
- **PDF:** not directly exposed (SSRN gates PDF access)
- **Cohort / stage:** ML/emerging; imaging/inverse-problem, likely gridding/distributed-imaging ("transforms measured visibilities into images of the sky," extends a prior imaging framework "to multiple nodes" for scalability)
- **Reason:** direct title match to "SMURFIT" in a radio-imaging context; likely related to the same authors' 2025 arXiv paper "A Decentralized Framework for Radio-interferometric Image Reconstruction" (already in the R2D2-citing cohort, bibcode `2025AJ....169..289W`) — relationship unconfirmed.
- **Status:** captain approved; extraction blocked because the authoritative SSRN full text returned Cloudflare HTTP 403 through all allowed ordinary HTTP paths and no authoritative alternate full text was found

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
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2024ApJS..273....3A.md`

### AIRI precursor
- **Primary paper (see ambiguity note for an alternate candidate):** "First AI for Deep Super-resolution Wide-field Imaging in Radio Astronomy: Unveiling Structure in ESO 137-006"
- **Authors/year:** A. Dabbech, M. Terris, A. Jackson, M. Ramatsoku, O. M. Smirnov, Y. Wiaux, 2022
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2022ApJ...939L...4D/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2207.11336 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (plug-and-play DNN denoiser regularization — original AIRI, applied to real MeerKAT data)
- **Reason:** "the first AI-based framework for deep, super-resolution, wide-field radio-interferometric imaging" — the foundational AIRI paper, predating the "AIRI plug-and-play" follow-up already in the R2D2-citing cohort (`2025MNRAS.537.1608T`).
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2022ApJ...939L...4D.md`
- **Alternate candidate outcome:** the distinct ASKAP validation paper by Wilber, Dabbech, Terris, Jackson & Wiaux (2023), MNRAS 522, 5576, was also approved and extracted to `cohorts/emerging-ml/papers/2023MNRAS.522.5576W.md`

### POLISH
- **Primary paper:** "Deep radio-interferometric imaging with POLISH: DSA-2000 and weak lensing"
- **Authors/year:** Liam Connor, Katherine L. Bouman, Vikram Ravi, Gregg Hallinan, 2022
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2022MNRAS.514.2614C/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2111.03249 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (super-resolution/deconvolution CNN)
- **Reason:** "trained a high-dynamic range residual neural network to learn the mapping between the dirty image and the true radio sky, calling this procedure POLISH, in contrast to... CLEAN" — the original method, distinct from and predating "POLISH'ing the Sky..." (Wu, Connor, McCarty et al.), already in the R2D2-citing cohort at `2026arXiv260309162W`.
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2022MNRAS.514.2614C.md`

### PRIMO
- **Primary paper:** "Principal-Component Interferometric Modeling (PRIMO), an Algorithm for EHT Data I: Reconstructing Images from Simulated EHT Observations"
- **Authors/year:** Lia Medeiros, Dimitrios Psaltis, Tod R. Lauer, Feryal Özel, 2023
- **Landing page:** https://ui.adsabs.harvard.edu/abs/2023ApJ...943..144M/abstract
- **PDF:** arXiv abstract page https://arxiv.org/abs/2208.01667 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML/statistical reconstruction (PCA-based, trained on GRMHD simulations)
- **Reason:** the original PRIMO algorithm-introduction paper, distinct from both "The Image of the M87 Black Hole Reconstructed with PRIMO" (Medeiros et al. 2023, ApJL 947, L7) and "Theoretical Foundation of Black Hole Image Reconstruction Using PRIMO," already in the R2D2-citing cohort at `2025ApJ...984...86P`.
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2023ApJ...943..144M.md`

### Schmidt et al. direct-CNN paper
- **Primary paper:** "Deep learning-based imaging in radio interferometry"
- **Authors/year:** K. Schmidt, F. Geyer, S. Fröse, P.-S. Blomenkamp, M. Brüggen, F. de Gasperin, D. Elsässer, W. Rhode, 2022
- **Landing page:** https://www.aanda.org/articles/aa/full_html/2022/08/aa42113-21/aa42113-21.html (A&A 664, A134; ADS bibcode `2022A&A...664A.134S`, confirmed during extraction)
- **PDF:** arXiv abstract page https://arxiv.org/abs/2203.11757 (PDF link present alongside abs, not opened)
- **Cohort / stage:** ML/emerging; end-to-end ML reconstruction (direct CNN, Fourier-space inpainting rather than iterative deconvolution)
- **Reason:** a CNN (SRResNet-derived) that "reconstructs missing information directly in Fourier space... no iterative source model is formed" — matches the "direct CNN" description; part of the radionets project.
- **Status:** captain approved; summary extracted to `cohorts/emerging-ml/papers/2022A_and_A...664A.134S.md`

---

## Notes on ambiguity

1. **GILDAS/GREG:** the brief's "GILDA/GREG" wording is almost certainly a typo for GILDAS. No dedicated peer-reviewed GREG paper exists — GREG is documented only as a GILDAS plotting sub-module in IRAM memos/manuals.
2. **NUFFT/HVOX:** HVOX was clearly identified as a specific 3D-NUFFT-based radio-interferometric synthesis algorithm. No single canonical "NUFFT for radio interferometry" primary reference (distinct from general-purpose NUFFT papers) was confidently identified; several candidates exist (Duijndam & Schonewille 1997; Jackson et al. 1991; Fessler & Sutton 2003; Barnett, Magland & af Klinteberg 2019/FINUFFT). FINUFFT was used as the representative general reference and is flagged as not radio-interferometry-specific.
3. **Focused CLEAN:** no paper or named algorithm variant called "focused CLEAN" could be identified. Recommend the captain clarify whether this refers to a specific named technique or to informal region-restricted ("boxed") CLEAN.
4. **SMURFIT:** resolved to a specific SSRN working paper, but authoritative full text returned Cloudflare HTTP 403 through every allowed ordinary HTTP path, and no authoritative alternate copy was found. Metadata was corroborated through Crossref, but method and metric extraction remains blocked.
5. **w-stacking primary reference:** both distinct sources are now covered without duplication. SKA Memo 132 is extracted as the dedicated analysis, while the already-landed Offringa et al. 2014 summary covers WSClean's implementation.
6. **Previously constructed bibcodes:** SARA, PURIFY, MS-MFS, and Schmidt et al. identifiers were confirmed against authoritative full text and metadata during extraction.
7. **AIRI precursor - two candidates:** (a) Dabbech et al. 2022, ApJL 939, L4 (the first introduction of the AIRI concept), and (b) Wilber, Dabbech, Terris, Jackson & Wiaux 2023, MNRAS 522, 5576 ("AIRI validated on ASKAP data," arXiv:2302.14149, a companion/validation paper to the uSARA paper). Both distinct approved papers were extracted; no further candidate choice is required for this task.
8. **Schwab 1984 / Cotton-Schwab CLEAN reuse:** the paper remains citation-only and was not duplicated as a second summary, per the approved extraction brief.
9. **MS-MFS vs. MT-MFS terminology:** the names refer to Rau & Cornwell 2011. The distinct Sault & Wieringa 1994 multi-frequency-only precursor was also approved and extracted.
10. **Wakker & Schwarz 1988:** the ADS archival full text and metadata were verified during extraction.
11. **Joined-channel CLEAN vs. WSClean:** the distinct Offringa & Smirnov 2017 algorithm paper and Offringa et al. 2014 software paper are both covered as separate summaries.
