/**
 * RMS sub-metric taxonomy — shared config for rms.html.
 *
 * Parallel to runtime-taxonomy.js / compute-taxonomy.js / iterations-taxonomy.js / dr-taxonomy.js.
 * Binary metrics.rms is unchanged; this only subtypes papers that already have rms: 1.
 *
 * Categories below are RMS reporting types (NOT RMS Context).
 * RMS Context (units, image region, residual vs dirty, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * RMS = absolute residual/dirty/off-source RMS as a reported score (not merely
 * DR’s denominator). Do not treat RDR (‖r̂‖₂/‖x_dirty‖₂) as RMS. Qualitative
 * residuals alone should not invent subtypes.
 */
(function (global) {
  const RMS_TAXONOMY = {
    absolute_rms: {
      id: "absolute_rms",
      label: "Residual / Image RMS (Absolute)",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Absolute residual, dirty, or off-source RMS (or equivalent std) reported as a fidelity/noise score.",
      submetrics: {
        residual_image_rms: {
          id: "residual_image_rms",
          label: "Residual-image RMS",
          short: "Resid img",
          description:
            "RMS (or std) of the residual image in physical units (Jy/beam, mJy/beam, μJy/PSF, etc.).",
        },
        off_source_blank_rms: {
          id: "off_source_blank_rms",
          label: "Off-source / blank-region RMS",
          short: "Off-src",
          description:
            "RMS measured in blank / off-source regions of the residual or restored image.",
        },
        dirty_image_rms: {
          id: "dirty_image_rms",
          label: "Dirty-image RMS",
          short: "Dirty",
          description:
            "RMS of the dirty image (σ_dirty or equivalent), reported as a noise/artefact score.",
        },
        residual_map_sigma: {
          id: "residual_map_sigma",
          label: "Residual-map σ / std",
          short: "σ / std",
          description:
            "Residual-map standard deviation (or σ) reported as a data-fidelity score, including residual-dirty std tables.",
        },
        other_absolute_rms: {
          id: "other_absolute_rms",
          label: "Other absolute RMS variants",
          short: "Other",
          description:
            "Other absolute RMS-style scores (e.g. image-domain RMS error vs smoothed truth) that are not residual/dirty/off-source labels above.",
        },
      },
    },
    comparative_rms: {
      id: "comparative_rms",
      label: "Comparative RMS",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Lower/higher residual RMS than a baseline, reduction factors, or percentage change.",
      submetrics: {
        lower_higher_than_baseline: {
          id: "lower_higher_than_baseline",
          label: "Lower / higher RMS than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches lower or higher residual/image RMS than a named baseline.",
        },
        rms_reduction_factor: {
          id: "rms_reduction_factor",
          label: "RMS reduction factor / ratio",
          short: "Factor",
          description:
            "Numerical factor by which residual RMS is lower than a baseline (including residual vs dirty RMS factors that are not R2D2-style ‖r̂‖₂/‖x_dirty‖₂ RDR).",
        },
        percentage_rms_change: {
          id: "percentage_rms_change",
          label: "Percentage RMS change",
          short: "%Δ",
          description: "Percentage increase or decrease in residual/image RMS relative to a baseline.",
        },
      },
    },
    framework_defined: {
      id: "framework_defined",
      label: "Framework / Defined RMS",
      short: "Framework",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Named core quality metric (e.g. framework dirty-image RMS) without tabulated run values.",
      submetrics: {
        named_core_quality_metric: {
          id: "named_core_quality_metric",
          label: "Named core quality metric",
          short: "Named",
          description:
            "RMS defined as a core framework/benchmark quality metric without Section-style tabulated reconstruction values.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified RMS",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "RMS-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague residual-noise mentions already flagged rms=1 but not subtypeable as absolute, comparative, or framework RMS.",
        },
      },
    },
  };

  const RMS_CATEGORY_ORDER = [
    "absolute_rms",
    "comparative_rms",
    "framework_defined",
    "unspecified",
  ];

  const RMS_CONTEXT_FIELDS = [
    { id: "units", label: "Units" },
    { id: "image_region", label: "Image region" },
    { id: "residual_vs_dirty", label: "Residual vs dirty" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.RMS_TAXONOMY = RMS_TAXONOMY;
  global.RMS_CATEGORY_ORDER = RMS_CATEGORY_ORDER;
  global.RMS_CONTEXT_FIELDS = RMS_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
