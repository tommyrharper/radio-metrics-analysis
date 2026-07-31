/**
 * Dynamic Range (DR) sub-metric taxonomy — shared config for dr.html.
 *
 * Parallel to runtime-taxonomy.js / compute-taxonomy.js / iterations-taxonomy.js.
 * Binary metrics.dynamic_range is unchanged; this only subtypes papers that
 * already have dynamic_range: 1.
 *
 * Categories below are DR reporting types (NOT DR Context).
 * DR Context (definition, noise estimator, image region, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * Do not count residual RMS alone as DR (that is RMS). Do not treat SNR as DR.
 */
(function (global) {
  const DR_TAXONOMY = {
    reported_achieved: {
      id: "reported_achieved",
      label: "Reported / Achieved DR",
      short: "Achieved",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Measured or quoted dynamic-range scores from reconstructed images (formula-specific or scalar).",
      submetrics: {
        peak_rms_dr: {
          id: "peak_rms_dr",
          label: "Peak / RMS (or off-source noise)",
          short: "Peak/RMS",
          description:
            "DR as peak brightness divided by RMS or off-source noise (including framework definitions of this form).",
        },
        peak_mad_dr: {
          id: "peak_mad_dr",
          label: "Peak / MAD (robust noise)",
          short: "Peak/MAD",
          description:
            "DR as peak brightness divided by median absolute deviation or another robust noise estimator (e.g. W-projection DR1).",
        },
        peak_peak_residual_dr: {
          id: "peak_peak_residual_dr",
          label: "Peak / peak-residual DR",
          short: "Peak/resid",
          description:
            "DR as peak brightness divided by the strongest residual peak (peak-to-peak-residual dynamic range).",
        },
        tabulated_scalar_dr: {
          id: "tabulated_scalar_dr",
          label: "Tabulated scalar achieved DR",
          short: "Scalar",
          description:
            "A quoted or tabulated achieved/operating DR number without a fully specified alternate formula subtype.",
        },
        other_measured_dr_formula: {
          id: "other_measured_dr_formula",
          label: "Other measured DR formula",
          short: "Other",
          description:
            "Other explicit measured DR definitions (e.g. peak / strongest nearby negative feature).",
        },
      },
    },
    target_configured: {
      id: "target_configured",
      label: "Target / Configured DR",
      short: "Target",
      color: "#a16207",
      borderStyle: "dotted",
      note: "DR used as a simulation parameter, regularisation estimate, or capability claim — not necessarily a measured score.",
      submetrics: {
        simulation_draw_parameter: {
          id: "simulation_draw_parameter",
          label: "Simulation draw / configured target DR",
          short: "Sim target",
          description:
            "Ground-truth or observation DR drawn or configured for synthetic tests (ranges such as 10³–10⁵).",
        },
        dirty_peak_noise_estimate: {
          id: "dirty_peak_noise_estimate",
          label: "Dirty-peak / noise estimate",
          short: "Dirty est.",
          description:
            "Nominal DR from dirty-image peak over estimated noise, typically for regularisation or denoiser selection.",
        },
        capability_table_max_dr: {
          id: "capability_table_max_dr",
          label: "Capability-table max DR",
          short: "Capability",
          description:
            "Quantitative max-DR claims in capability/comparison tables (not shared-benchmark measured scores).",
        },
      },
    },
    comparative_dr: {
      id: "comparative_dr",
      label: "Comparative DR",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "DR higher/lower than a named baseline, improvement factors, or percentage change.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower DR than baseline",
          short: "Vs base",
          description:
            "Clear statement that a method reaches higher or lower DR than a named baseline (with or without a shared scalar).",
        },
        dr_improvement_factor: {
          id: "dr_improvement_factor",
          label: "DR improvement factor / ratio",
          short: "Factor",
          description: "Numerical factor or order-of-magnitude DR improvement vs a baseline or prior configuration.",
        },
        percentage_dr_change: {
          id: "percentage_dr_change",
          label: "Percentage DR change",
          short: "%Δ",
          description: "Percentage increase or decrease in dynamic range relative to a baseline.",
        },
      },
    },
    dr_limits: {
      id: "dr_limits",
      label: "DR Limits / System Effects",
      short: "Limits",
      color: "#2563eb",
      borderStyle: "dashed",
      note: "Quantitative DR ceilings from calibration, physics, or algorithm divergence — not achieved reconstruction scores.",
      submetrics: {
        dd_calibration_leakage_ceilings: {
          id: "dd_calibration_leakage_ceilings",
          label: "DD / calibration / leakage ceilings",
          short: "Calib",
          description:
            "Direction-dependent, primary-beam, pointing, or leakage effects that impose numerical DR ceilings.",
        },
        algorithm_divergence_limits: {
          id: "algorithm_divergence_limits",
          label: "Algorithm divergence / practical limits",
          short: "Diverge",
          description:
            "Practical DR limits from algorithm divergence or failure modes (e.g. Högbom loop divergence).",
        },
        other_dr_limiting_physics: {
          id: "other_dr_limiting_physics",
          label: "Other DR-limiting physics / systematics",
          short: "Physics",
          description: "Other quantitative DR-limiting systematics not covered by calibration or divergence subtypes.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified DR",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "DR-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "DR is discussed qualitatively (e.g. “high DR”, “competitive DR”) without subtypeable measured, configured, comparative, or limit evidence.",
        },
      },
    },
  };

  const DR_CATEGORY_ORDER = [
    "reported_achieved",
    "target_configured",
    "comparative_dr",
    "dr_limits",
    "unspecified",
  ];

  const DR_CONTEXT_FIELDS = [
    { id: "definition_used", label: "Definition used" },
    { id: "noise_estimator", label: "Noise estimator" },
    { id: "image_region", label: "Image region" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.DR_TAXONOMY = DR_TAXONOMY;
  global.DR_CATEGORY_ORDER = DR_CATEGORY_ORDER;
  global.DR_CONTEXT_FIELDS = DR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
