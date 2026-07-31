/**
 * Text-metrics sub-metric taxonomy — shared config for text.html.
 *
 * Parallel to rms-taxonomy.js / runtime-taxonomy.js / compute-taxonomy.js.
 * Binary metrics.text_metrics is unchanged; this only subtypes papers that
 * already have text_metrics: 1.
 *
 * Categories below are Text reporting types (NOT Text Context).
 * Text Context (task, dataset, models, reference type, domain) is summarized
 * separately.
 *
 * Text = BLEU / ROUGE / chrF (or comparable text-overlap) on VQA or free-text
 * answers about radio images. Classification accuracy / F1 / TPR / FPR belong
 * under Class, not Text. Pixel fidelity (SNR, DR, RMS, …) is not Text.
 */
(function (global) {
  const TEXT_TAXONOMY = {
    semantic_similarity: {
      id: "semantic_similarity",
      label: "Semantic Similarity / Text Overlap",
      short: "Overlap",
      color: "#0f766e",
      borderStyle: "solid",
      note: "BLEU, ROUGE, chrF, or comparable overlap scores between generated and reference answers.",
      submetrics: {
        bleu: {
          id: "bleu",
          label: "BLEU",
          short: "BLEU",
          description:
            "BLEU n-gram precision/overlap between generated and reference VQA or free-text answers.",
        },
        rouge: {
          id: "rouge",
          label: "ROUGE",
          short: "ROUGE",
          description:
            "ROUGE recall-oriented n-gram / sequence overlap between generated and reference answers.",
        },
        chrf: {
          id: "chrf",
          label: "chrF",
          short: "chrF",
          description:
            "Character n-gram F-score (chrF) similarity between generated and reference answers.",
        },
        other_text_overlap: {
          id: "other_text_overlap",
          label: "Other text-overlap metric",
          short: "Other",
          description:
            "Other named text-overlap or semantic-similarity scores on generated answers that are not BLEU/ROUGE/chrF.",
        },
      },
    },
    comparative_text: {
      id: "comparative_text",
      label: "Comparative Text Scores",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower BLEU/ROUGE/chrF than a named baseline, or explicit score deltas.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches higher or lower text-overlap scores than a named baseline.",
        },
        score_delta: {
          id: "score_delta",
          label: "Score delta / percentage change",
          short: "Δ",
          description: "Absolute or percentage change in BLEU/ROUGE/chrF relative to a baseline.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Text",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Text-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague VQA/free-text evaluation mentions already flagged text_metrics=1 but not subtypeable as BLEU/ROUGE/chrF or comparative.",
        },
      },
    },
  };

  const TEXT_CATEGORY_ORDER = [
    "semantic_similarity",
    "comparative_text",
    "unspecified",
  ];

  const TEXT_CONTEXT_FIELDS = [
    { id: "task", label: "Task" },
    { id: "dataset", label: "Dataset" },
    { id: "models", label: "Models" },
    { id: "reference_type", label: "Reference type" },
    { id: "domain", label: "Domain" },
  ];

  global.TEXT_TAXONOMY = TEXT_TAXONOMY;
  global.TEXT_CATEGORY_ORDER = TEXT_CATEGORY_ORDER;
  global.TEXT_CONTEXT_FIELDS = TEXT_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
