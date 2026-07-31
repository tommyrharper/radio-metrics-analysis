/**
 * Classification-metrics sub-metric taxonomy — shared config for class.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.classification_metrics is unchanged; this only subtypes
 * papers that already have classification_metrics: 1.
 *
 * Categories below are Class reporting types (NOT Class Context).
 * Class Context (task, finder, operating point, matching criterion,
 * simulation vs real, dataset) is summarized separately.
 *
 * Class = catalog / label / finder evaluation on reconstructed images or
 * downstream science products (precision/recall/F1, FP rates, TPR@FPR,
 * accuracy, etc.) — not pixel-wise image fidelity (PSNR/SSIM/RMS/DR).
 */
(function (global) {
  const CLASS_TAXONOMY = {
    catalog_rates: {
      id: "catalog_rates",
      label: "Catalog Detection Rates",
      short: "Catalog",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Precision/recall/F1, false-positive incidence, missed detections, or TP-subset parameter RMSE from source catalogs.",
      submetrics: {
        precision_recall_f1: {
          id: "precision_recall_f1",
          label: "Precision / recall / F1",
          short: "P/R/F1",
          description:
            "Precision, recall, and/or F1 on source detections with an explicit TP matching rule (e.g. size-dependent pixel radius).",
        },
        false_positive_incidence: {
          id: "false_positive_incidence",
          label: "False-positive incidence",
          short: "FP incid.",
          description:
            "Approximate false-positive counts or incidence from a source finder (e.g. false galaxies per N simulated galaxies), without a full precision–recall curve.",
        },
        missed_detection_counts: {
          id: "missed_detection_counts",
          label: "Missed-detection counts",
          short: "Missed",
          description: "Explicit missed-detection / false-negative counts in a classification or detection benchmark.",
        },
        shape_flux_rmse_on_tps: {
          id: "shape_flux_rmse_on_tps",
          label: "Shape / flux RMSE on true positives",
          short: "TP RMSE",
          description:
            "RMSE on SEP (or similar) shape/flux parameters restricted to true-positive detections — adjacent to catalog matching, reported alongside Class.",
        },
      },
    },
    operating_point: {
      id: "operating_point",
      label: "TPR / FPR Operating Point",
      short: "TPR@FPR",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "True-positive rate at a fixed false-positive rate (ROC-style finder curves).",
      submetrics: {
        tpr_at_fixed_fpr: {
          id: "tpr_at_fixed_fpr",
          label: "TPR at fixed FPR",
          short: "TPR@FPR",
          description:
            "True-positive rate reported at a fixed false-positive rate (e.g. FPR=10⁻³), often vs Einstein radius or image separation.",
        },
      },
    },
    label_accuracy: {
      id: "label_accuracy",
      label: "Label Classification",
      short: "Label",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Discrete physical or semantic label accuracy (e.g. MAD/SANE; multimodal LLM radio-image tasks).",
      submetrics: {
        classification_accuracy: {
          id: "classification_accuracy",
          label: "Classification accuracy",
          short: "Accuracy",
          description:
            "Fraction of correct discrete-label predictions (magnetic-state classes, multimodal radio-image labels, etc.).",
        },
      },
    },
    cited_benchmark: {
      id: "cited_benchmark",
      label: "Cited External Benchmark",
      short: "Cited",
      color: "#b45309",
      borderStyle: "dashed",
      note: "Classification-style TPR/FPR (or similar) quoted from an external paper, not a primary measurement in this work.",
      submetrics: {
        cited_external_tpr_fpr: {
          id: "cited_external_tpr_fpr",
          label: "Cited external TPR / FPR",
          short: "Cited TPR",
          description:
            "External lens/source-finder recovery rates cited for context (e.g. Rezaei et al. 2022 on ILT simulations).",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Class",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Class-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague classification/detection mentions already flagged classification_metrics=1 but not subtypeable.",
        },
      },
    },
  };

  const CLASS_CATEGORY_ORDER = [
    "catalog_rates",
    "operating_point",
    "label_accuracy",
    "cited_benchmark",
    "unspecified",
  ];

  const CLASS_CONTEXT_FIELDS = [
    { id: "task", label: "Task" },
    { id: "finder_method", label: "Finder / method" },
    { id: "operating_point", label: "Operating point" },
    { id: "matching_criterion", label: "Matching / TP rule" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "dataset_or_survey", label: "Dataset / survey" },
  ];

  global.CLASS_TAXONOMY = CLASS_TAXONOMY;
  global.CLASS_CATEGORY_ORDER = CLASS_CATEGORY_ORDER;
  global.CLASS_CONTEXT_FIELDS = CLASS_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
