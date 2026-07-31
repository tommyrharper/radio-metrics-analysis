/**
 * NMSE / NRMSE sub-metric taxonomy — shared config for nmse.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.nmse_nrmse is unchanged; this only subtypes papers that
 * already have nmse_nrmse: 1.
 *
 * Categories below are NMSE reporting types (NOT NMSE Context).
 * NMSE Context (domain, formula/scale, simulation vs real, frequency, array,
 * reference) is summarized separately.
 *
 * NMSE = normalised mean squared error (or its dB / NRMSE form) as a reported
 * fidelity score. Do not treat unnormalised MSE, residual RMS, or source-parameter
 * RMSE alone as NMSE subtypes when the paper never reports NMSE/NRMSE.
 */
(function (global) {
  const NMSE_TAXONOMY = {
    visibility_domain: {
      id: "visibility_domain",
      label: "Visibility-domain NMSE",
      short: "Vis",
      color: "#0f766e",
      borderStyle: "solid",
      note: "NMSE between predicted/measured visibilities and a direct-evaluation or reference visibility set (operator / gridding fidelity).",
      submetrics: {
        fractional_visibility_nmse: {
          id: "fractional_visibility_nmse",
          label: "Fractional visibility NMSE",
          short: "Frac vis",
          description:
            "Requested or achieved fractional NMSE on visibilities (e.g. vs direct point-source evaluation), including accuracy-target sweeps.",
        },
        other_visibility_nmse: {
          id: "other_visibility_nmse",
          label: "Other visibility NMSE",
          short: "Other vis",
          description:
            "Other explicit visibility-domain NMSE / NRMSE formulations not covered by the fractional target/achieved sweep subtype.",
        },
      },
    },
    image_domain: {
      id: "image_domain",
      label: "Image-domain NMSE",
      short: "Image",
      color: "#1d4ed8",
      borderStyle: "solid",
      note: "NMSE / NRMSE of the reconstructed image against ground truth or a reference sky model.",
      submetrics: {
        image_nmse_db: {
          id: "image_nmse_db",
          label: "Image NMSE in dB",
          short: "NMSE dB",
          description:
            "Image-domain NMSE reported in decibels (e.g. NMSE [−dB] = −20·log₁₀(‖x⋆−x̂‖₂/‖x⋆‖₂)), where larger dB is better.",
        },
        image_fractional_nmse: {
          id: "image_fractional_nmse",
          label: "Fractional / linear image NMSE",
          short: "Frac img",
          description:
            "Image-domain NMSE or NRMSE as a fractional or linear normalised error (not the dB form).",
        },
        other_image_nmse: {
          id: "other_image_nmse",
          label: "Other image NMSE",
          short: "Other img",
          description:
            "Other explicit image-domain NMSE / NRMSE definitions not covered above.",
        },
      },
    },
    comparative_nmse: {
      id: "comparative_nmse",
      label: "Comparative NMSE",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Lower/higher NMSE than a named baseline, or a numerical improvement between methods.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower NMSE than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches better or worse NMSE/NRMSE than a named baseline (including dB comparisons).",
        },
        nmse_improvement_factor: {
          id: "nmse_improvement_factor",
          label: "NMSE improvement factor / order",
          short: "Factor",
          description:
            "Order-of-magnitude or factor improvement in NMSE relative to a baseline or requested target.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified NMSE",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "NMSE-positive papers whose evidence is too vague to subtype, or that report related MSE/RMSE/RMS without an explicit NMSE/NRMSE score. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Flagged nmse_nrmse=1 but no subtypeable NMSE/NRMSE reporting (e.g. MSE/PSNR only, residual RMS, or parameter RMSE without NMSE label).",
        },
      },
    },
  };

  const NMSE_CATEGORY_ORDER = [
    "visibility_domain",
    "image_domain",
    "comparative_nmse",
    "unspecified",
  ];

  const NMSE_CONTEXT_FIELDS = [
    { id: "domain", label: "Domain" },
    { id: "formula_scale", label: "Formula / scale" },
    { id: "reference", label: "Reference / truth" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.NMSE_TAXONOMY = NMSE_TAXONOMY;
  global.NMSE_CATEGORY_ORDER = NMSE_CATEGORY_ORDER;
  global.NMSE_CONTEXT_FIELDS = NMSE_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
