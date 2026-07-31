/**
 * SSIM sub-metric taxonomy — shared config for ssim.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.ssim is unchanged; this only subtypes papers that already
 * have ssim: 1.
 *
 * Categories below are SSIM reporting types (NOT SSIM Context).
 * SSIM Context (aggregation, image domain, normalization, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * SSIM = structural similarity index as a reconstruction fidelity score
 * (typically vs ground truth; 1 = perfect). Qualitative “looks similar”
 * claims alone should not invent subtypes.
 */
(function (global) {
  const SSIM_TAXONOMY = {
    absolute_ssim: {
      id: "absolute_ssim",
      label: "Reported SSIM (Absolute)",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Numerical SSIM (mean, median, or magnitude-image) reported as a fidelity score.",
      submetrics: {
        mean_image_ssim: {
          id: "mean_image_ssim",
          label: "Mean image SSIM",
          short: "Mean",
          description:
            "Mean SSIM over an image or validation set (often ± std), typically on intensity / normalized images.",
        },
        median_ssim: {
          id: "median_ssim",
          label: "Median SSIM",
          short: "Median",
          description:
            "Median SSIM aggregation over a test set (e.g. table medians rather than means).",
        },
        magnitude_image_ssim: {
          id: "magnitude_image_ssim",
          label: "Magnitude-image SSIM",
          short: "Magnitude",
          description:
            "SSIM computed on magnitude reconstructions (|x⋆| vs |x̂|), as in non-Cartesian MRI transfer benchmarks.",
        },
      },
    },
    comparative_ssim: {
      id: "comparative_ssim",
      label: "Comparative SSIM",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower SSIM than a baseline, or a stated SSIM delta / improvement.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower SSIM than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches higher or lower SSIM than a named baseline.",
        },
        ssim_delta: {
          id: "ssim_delta",
          label: "SSIM delta / improvement",
          short: "Δ",
          description:
            "Absolute SSIM difference or mean improvement vs a baseline (e.g. +0.009).",
        },
      },
    },
    framework_defined: {
      id: "framework_defined",
      label: "Framework / Defined SSIM",
      short: "Framework",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Named core quality metric (e.g. framework PSNR/SSIM pair) without tabulated run values.",
      submetrics: {
        named_core_quality_metric: {
          id: "named_core_quality_metric",
          label: "Named core quality metric",
          short: "Named",
          description:
            "SSIM defined as a core framework/benchmark quality metric without Section-style tabulated reconstruction values.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified SSIM",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "SSIM-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague structural-similarity mentions already flagged ssim=1 but not subtypeable as absolute, comparative, or framework SSIM.",
        },
      },
    },
  };

  const SSIM_CATEGORY_ORDER = [
    "absolute_ssim",
    "comparative_ssim",
    "framework_defined",
    "unspecified",
  ];

  const SSIM_CONTEXT_FIELDS = [
    { id: "aggregation", label: "Aggregation" },
    { id: "image_domain", label: "Image domain" },
    { id: "normalization", label: "Normalization" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.SSIM_TAXONOMY = SSIM_TAXONOMY;
  global.SSIM_CATEGORY_ORDER = SSIM_CATEGORY_ORDER;
  global.SSIM_CONTEXT_FIELDS = SSIM_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
