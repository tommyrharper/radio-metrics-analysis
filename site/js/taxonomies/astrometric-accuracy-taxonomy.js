/**
 * Astrometric Accuracy sub-metric taxonomy — shared config for
 * astrometric-accuracy.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.astrometric_accuracy is unchanged; this only subtypes
 * papers that already have astrometric_accuracy: 1.
 *
 * Categories below are Astrometry reporting types (NOT Astrometry Context).
 * Astrometry Context (units, reference type, simulation vs real, frequency,
 * array) is summarized separately.
 *
 * Astrometric Accuracy = quantitative reconstructed-source position vs
 * reference/catalogue/truth. Resolution/beam alone, detection without
 * position error, morphology/jet-angle, PSNR/SSIM, matching radius as
 * setting only, or framework-named without measured results → not enough.
 */
(function (global) {
  const ASTROMETRIC_ACCURACY_TAXONOMY = {
    absolute_position_error: {
      id: "absolute_position_error",
      label: "Absolute Position Error",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Measured angular/pixel offset, RA/Dec or radial error, bias, or fraction localised within a stated tolerance.",
      submetrics: {
        angular_pixel_offset: {
          id: "angular_pixel_offset",
          label: "Angular / pixel offset",
          short: "Offset",
          description:
            "Centroid or peak distance from truth or catalogue in arcsec, mas, pixels, or beam fractions.",
        },
        ra_dec_radial_error: {
          id: "ra_dec_radial_error",
          label: "RA / Dec / radial position error",
          short: "RA/Dec",
          description:
            "Mean, median, RMS, or max RA/Dec or radial positional error reported as a score.",
        },
        fraction_within_tolerance: {
          id: "fraction_within_tolerance",
          label: "Fraction within tolerance",
          short: "Within tol.",
          description:
            "Fraction or percentage of sources localised within a stated positional tolerance (e.g. N arcsec or N×beam).",
        },
        astrometric_bias: {
          id: "astrometric_bias",
          label: "Astrometric bias",
          short: "Bias",
          description:
            "Systematic positional shift (bias) reported separately from scatter.",
        },
        other_absolute_position_error: {
          id: "other_absolute_position_error",
          label: "Other absolute position-error variants",
          short: "Other",
          description:
            "Other quantitative position-accuracy scores not covered by the subtypes above.",
        },
      },
    },
    comparative_astrometry: {
      id: "comparative_astrometry",
      label: "Comparative Astrometry",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "One method recovers more accurate positions than another, or reports improvement factors / percentage change.",
      submetrics: {
        more_accurate_than_baseline: {
          id: "more_accurate_than_baseline",
          label: "More / less accurate than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method recovers more (or less) accurate source positions than a named baseline.",
        },
        position_error_improvement_factor: {
          id: "position_error_improvement_factor",
          label: "Position-error improvement factor / ratio",
          short: "Factor",
          description:
            "Numerical factor by which positional error is lower (or higher) than a baseline.",
        },
        percentage_position_error_change: {
          id: "percentage_position_error_change",
          label: "Percentage position-error change",
          short: "%Δ",
          description:
            "Percentage increase or decrease in positional error relative to a baseline.",
        },
      },
    },
    framework_defined: {
      id: "framework_defined",
      label: "Framework / Defined Astrometry",
      short: "Framework",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Named core quality metric (e.g. framework astrometric error) without measured reconstruction values.",
      submetrics: {
        named_core_quality_metric: {
          id: "named_core_quality_metric",
          label: "Named core quality metric",
          short: "Named",
          description:
            "Astrometric error defined as a core framework/benchmark quality metric without tabulated run values.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Astrometry",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Astrometry-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague position-accuracy mentions already flagged astrometric_accuracy=1 but not subtypeable as absolute, comparative, or framework Astrometry.",
        },
      },
    },
  };

  const ASTROMETRIC_ACCURACY_CATEGORY_ORDER = [
    "absolute_position_error",
    "comparative_astrometry",
    "framework_defined",
    "unspecified",
  ];

  const ASTROMETRIC_ACCURACY_CONTEXT_FIELDS = [
    { id: "units", label: "Units" },
    { id: "reference_type", label: "Reference type" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.ASTROMETRIC_ACCURACY_TAXONOMY = ASTROMETRIC_ACCURACY_TAXONOMY;
  global.ASTROMETRIC_ACCURACY_CATEGORY_ORDER = ASTROMETRIC_ACCURACY_CATEGORY_ORDER;
  global.ASTROMETRIC_ACCURACY_CONTEXT_FIELDS = ASTROMETRIC_ACCURACY_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
