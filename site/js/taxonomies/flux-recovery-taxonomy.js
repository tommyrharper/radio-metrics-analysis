/**
 * Flux Recovery sub-metric taxonomy — shared config for flux-recovery.html.
 *
 * Parallel to rms-taxonomy.js / runtime-taxonomy.js / dr-taxonomy.js.
 * Binary metrics.flux_recovery is unchanged; this only subtypes papers that
 * already have flux_recovery: 1.
 *
 * Categories below are Flux reporting types (NOT Flux Context).
 * Flux Context (units, aperture, reference type, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * Flux = quantitative recovered flux vs reference/model/catalogue (or explicit
 * cross-method recovered-flux comparison). Observational flux context, peak
 * brightness alone, DR/RMS, or qualitative morphology → not Flux.
 */
(function (global) {
  const FLUX_RECOVERY_TAXONOMY = {
    truth_based_flux: {
      id: "truth_based_flux",
      label: "Truth-based Flux Recovery",
      short: "Truth",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Recovered flux, fraction, peak bias, relative error, or catalogue flux error against known model/truth.",
      submetrics: {
        integrated_vs_true: {
          id: "integrated_vs_true",
          label: "Integrated flux vs true model",
          short: "Integ vs true",
          description:
            "Absolute recovered integrated flux compared with known model/reference flux (Jy or arbitrary model units).",
        },
        recovery_fraction: {
          id: "recovery_fraction",
          label: "Recovered-flux fraction / percentage",
          short: "Fraction",
          description:
            "Fraction or percentage of true/reference flux recovered (including missing-flux statements as 1 − fraction).",
        },
        peak_flux_bias: {
          id: "peak_flux_bias",
          label: "Peak / core intensity bias vs truth",
          short: "Peak bias",
          description:
            "Peak-flux or core specific-intensity error/bias relative to known truth (relative % or fractional error).",
        },
        relative_flux_density_error: {
          id: "relative_flux_density_error",
          label: "Relative flux-density error",
          short: "Rel dens.",
          description:
            "Relative flux-density error (Ŝ−S)/S (e.g. vs beam radius or direction-dependent effects).",
        },
        catalogue_flux_error: {
          id: "catalogue_flux_error",
          label: "Catalogue / source-finder flux error",
          short: "Catalogue",
          description:
            "Source-finder or catalogue photometric error vs truth (standard error %, RMSE in Jy or Jy/pixel).",
        },
      },
    },
    cross_method_flux: {
      id: "cross_method_flux",
      label: "Cross-method / Comparative Flux",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Integrated-flux tables or numerical recovered-flux comparisons across algorithms (often real data, no sky truth).",
      submetrics: {
        cross_method_integrated: {
          id: "cross_method_integrated",
          label: "Cross-method integrated-flux tables",
          short: "Cross tbl",
          description:
            "Tabulated integrated fluxes in matching apertures across methods (consistency / photometry check, not truth error).",
        },
        comparative_recovered_flux: {
          id: "comparative_recovered_flux",
          label: "Comparative recovered flux vs baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method recovers more/less flux or lower/higher flux error than a named baseline.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Flux Recovery",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Flux-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague flux-preservation mentions already flagged flux_recovery=1 but not subtypeable as truth-based or comparative Flux.",
        },
      },
    },
  };

  const FLUX_RECOVERY_CATEGORY_ORDER = [
    "truth_based_flux",
    "cross_method_flux",
    "unspecified",
  ];

  const FLUX_RECOVERY_CONTEXT_FIELDS = [
    { id: "units", label: "Units" },
    { id: "aperture_region", label: "Aperture / region" },
    { id: "reference_type", label: "Reference type" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.FLUX_RECOVERY_TAXONOMY = FLUX_RECOVERY_TAXONOMY;
  global.FLUX_RECOVERY_CATEGORY_ORDER = FLUX_RECOVERY_CATEGORY_ORDER;
  global.FLUX_RECOVERY_CONTEXT_FIELDS = FLUX_RECOVERY_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
