# Unveiling the power of multimodal large language models for radio astronomical image understanding and question answering

**Bibcode:** 2025MLS&T...6d5005Z
**Authors:** Fuyong Zhao, Yuyang Li, Zhenyu Liu, Panfeng Chen, Cunshi Wang, Jifeng Liu, Hui Li, Yanhao Wang
**ADS:** https://ui.adsabs.harvard.edu/abs/2025MLS%26T...6d5005Z/abstract
**arXiv:** not found (no preprint located via arXiv or web search; published version at https://iopscience.iop.org/article/10.1088/2632-2153/ae0c56)

## One-line summary
The paper constructs RadioAstroVQA, a visual-question-answering dataset built from existing radio astronomy image repositories, and fine-tunes two open-source multimodal LLMs (DeepSeek-VL-7B and InternVL2-40B) to perform classification and free-form Q&A on radio astronomical images.

## Method
The authors address the lack of multimodal training resources in radio astronomy by converting labeled images from four existing repositories (FAST, HTRU Medlat, Spectrumcls, and Radio Galaxy datasets) into VQA-format examples via a semi-automated, two-stage pipeline using prompt templates plus numerical features and domain rules. They then fine-tune two MLLMs of different scales (7B and 40B parameters) using LoRA and quantization techniques, and evaluate them on both classification tasks (e.g. pulsar/source classification, radio galaxy morphology) and open-ended VQA tasks, comparing against specialized ML/DL baselines and general-domain MLLMs.

## Performance / fidelity metrics used
- **Classification tasks:** Accuracy, Precision, Recall, F1-score, True Positive Rate (TPR), False Positive Rate (FPR), missed-detection counts.
- **VQA / free-text tasks:** BLEU, ROUGE, and chrF for semantic similarity between generated and reference answers.
- **No image-reconstruction fidelity metrics are discussed.** The paper does not mention SNR, dynamic range, or any CLEAN/R2D2/AIRI-style reconstruction-quality metrics. Its training images are drawn from pre-existing labeled repositories (FAST, HTRU, Spectrumcls, Radio Galaxy) rather than from a described imaging/deconvolution pipeline, and there is no discussion of visibility-to-image reconstruction or its fidelity.

## Relevance to visibility→gridding→iFFT→deconvolution ML pipeline
Low direct relevance: this is a downstream image-understanding/QA task on already-produced radio images, not a study of the imaging pipeline itself, and it does not engage with reconstruction fidelity metrics relevant to the R2D2/AIRI/CLEAN comparison being reviewed.
