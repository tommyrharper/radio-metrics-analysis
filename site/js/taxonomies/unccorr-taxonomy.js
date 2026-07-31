/**
 * Uncertainty correlation (UncCorr) sub-metric taxonomy — shared config for unccorr.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.uncertainty_correlation is unchanged; this only subtypes papers
 * that already have uncertainty_correlation: 1.
 *
 * Categories below are UncCorr reporting types (NOT UncCorr Context).
 * UncCorr Context (statistic, uncertainty source, error reference, sample count,
 * simulation vs real, array) is summarized separately.
 *
 * UncCorr = correlation-style checks on whether predicted/bootstrap uncertainty
 * aligns with empirical error or another uncertainty estimate. Distinct from
 * credible_interval (which reports the uncertainty itself).
 */
(function (global) {
  const UNCCORR_TAXONOMY = {
    uncertainty_error_correlation: {
      id: "uncertainty_error_correlation",
      label: "Uncertainty–Error Correlation",
      short: "Err corr",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Correlation (or closely related agreement) between predicted uncertainty and reconstruction error.",
      submetrics: {
        pearson_uncertainty_vs_abs_error: {
          id: "pearson_uncertainty_vs_abs_error",
          label: "Pearson uncertainty vs |error|",
          short: "Pearson",
          description:
            "Pearson correlation between predicted per-pixel (or aggregated) uncertainty and absolute reconstruction error vs truth.",
        },
        other_uncertainty_error_agreement: {
          id: "other_uncertainty_error_agreement",
          label: "Other uncertainty–error agreement",
          short: "Other err",
          description:
            "Spearman, mutual information, or other explicit uncertainty-vs-error agreement scores that are not Pearson.",
        },
      },
    },
    inter_estimate_correlation: {
      id: "inter_estimate_correlation",
      label: "Inter-Estimate Correlation",
      short: "Inter-UQ",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Agreement between two uncertainty estimates (e.g. bootstrap vs posterior, method A vs B maps).",
      submetrics: {
        pairwise_uncertainty_map_correlation: {
          id: "pairwise_uncertainty_map_correlation",
          label: "Pairwise uncertainty-map correlation",
          short: "Map×map",
          description:
            "Correlation between two uncertainty fields or UQ methods without requiring ground-truth error.",
        },
      },
    },
    comparative_unccorr: {
      id: "comparative_unccorr",
      label: "Comparative UncCorr",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower correlation than a baseline, or correlation vs sample-count / hyperparameter ablations.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower correlation than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches higher or lower uncertainty–error (or inter-UQ) correlation than a named baseline.",
        },
        correlation_vs_sample_count: {
          id: "correlation_vs_sample_count",
          label: "Correlation vs sample count",
          short: "N-samp",
          description:
            "Uncertainty–error correlation reported as a function of posterior/bootstrap sample count (ablation / plateau).",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified UncCorr",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "UncCorr-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague UQ-calibration mentions already flagged uncertainty_correlation=1 but not subtypeable as error, inter-estimate, or comparative UncCorr.",
        },
      },
    },
  };

  const UNCCORR_CATEGORY_ORDER = [
    "uncertainty_error_correlation",
    "inter_estimate_correlation",
    "comparative_unccorr",
    "unspecified",
  ];

  const UNCCORR_CONTEXT_FIELDS = [
    { id: "correlation_statistic", label: "Correlation statistic" },
    { id: "uncertainty_source", label: "Uncertainty source" },
    { id: "error_reference", label: "Error reference" },
    { id: "sample_count", label: "Sample count" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "array", label: "Array" },
  ];

  global.UNCCORR_TAXONOMY = UNCCORR_TAXONOMY;
  global.UNCCORR_CATEGORY_ORDER = UNCCORR_CATEGORY_ORDER;
  global.UNCCORR_CONTEXT_FIELDS = UNCCORR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
