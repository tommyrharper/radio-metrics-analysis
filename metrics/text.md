# Text

## What this metric means here
Natural-language evaluation of model outputs about radio-astronomical images—semantic similarity between generated and reference answers in visual question answering (VQA) or free-text description tasks, sitting outside classical pixel fidelity for the visibility → gridding → iFFT → deconvolution pipeline. In this review, **Text** marks BLEU, ROUGE, chrF, or comparable text-overlap metrics applied to radio-image understanding systems.

Root total: **1** Text-positive paper (r2d2-citing). Binary `text_metrics: 0|1` flags are unchanged by the drill-down; subtype detail lives in `text_details` ([`site/detail/text.html`](../site/detail/text.html)).

## How papers use it
One paper is tagged (Unveiling the power of multimodal large language models for radio astronomical image understanding and question answering, 2025MLS&T...6d5005Z). For VQA and free-text tasks, the authors report **BLEU**, **ROUGE**, and **chrF** as semantic-similarity scores between generated and reference answers. The same paper also uses classification metrics (accuracy, precision, recall, F1, TPR, FPR, missed-detection counts) on discrete tasks; those fall under **Class**, not **Text**.

## Drill-down taxonomy (second-level page)
See [`site/detail/text.html`](../site/detail/text.html) / `site/js/taxonomies/text-taxonomy.js`. Categories (papers may hit more than one):

| Category | Sub-metrics |
|---|---|
| Semantic Similarity / Text Overlap | BLEU; ROUGE; chrF; Other text-overlap metric |
| Comparative Text Scores | Higher / lower than baseline; Score delta / percentage change |
| Unspecified Text | Vague VQA/free-text mentions already flagged text_metrics=1 but not subtypeable |

**Text Context** (task, dataset, models, reference type, domain) is reporting completeness only — not itself a Text metric.

## Popular measurement variants
- **BLEU** for n-gram overlap between generated and reference answers.
- **ROUGE** for recall-oriented n-gram and sequence overlap.
- **chrF** for character n-gram F-score similarity.

## Gaps and caveats
- Sample size is 1 paper; no cross-study convention for prompt sets, reference phrasing, or acceptable score ranges.
- Text metrics judge answer wording, not reconstruction fidelity—links to interferometric image quality are indirect.
- The tagged paper combines text and classification evaluations; **Text** applies only to the VQA/free-text subset in the notes.
- Do not count classification accuracy / F1 / TPR / FPR as Text — those are **Class**.
