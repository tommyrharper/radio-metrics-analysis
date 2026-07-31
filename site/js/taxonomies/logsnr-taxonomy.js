/**
 * logSNR sub-metric taxonomy — shared config for logsnr.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.logsnr is unchanged; this only subtypes papers that already
 * have logsnr: 1.
 *
 * Categories below are logSNR reporting types (NOT logSNR Context).
 * logSNR Context (transform definition/parameter, pairing with linear SNR,
 * simulation vs real, array/domain, frequency) is summarized separately.
 *
 * logSNR = SNR after a logarithmic intensity remapping of reconstruction and
 * ground truth (faint / high-DR structure). Linear SNR alone is not logSNR.
 */
(function (global) {
  const LOGSNR_TAXONOMY = {
    absolute_logsnr: {
      id: "absolute_logsnr",
      label: "Reported / Absolute logSNR",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Numeric logSNR (or S/N_log / SNRlog) in dB from tables, means, or curves.",
      submetrics: {
        tabulated_mean_db: {
          id: "tabulated_mean_db",
          label: "Tabulated mean / scalar logSNR (dB)",
          short: "Tabulated",
          description:
            "Mean ± std or scalar logSNR values in a results table or summary (often paired with linear SNR).",
        },
        per_iteration_curve: {
          id: "per_iteration_curve",
          label: "Per-iteration / series logSNR curve",
          short: "Per-iter",
          description:
            "logSNR tracked across DNN-series iterations or optimisation steps (progression to a final value).",
        },
        parameter_sweep_logsnr: {
          id: "parameter_sweep_logsnr",
          label: "Parameter-sweep logSNR",
          short: "Sweep",
          description:
            "logSNR vs an experimental knob (Briggs ρ, acceleration factor, spherical Np, D/N, input noise, etc.).",
        },
      },
    },
    comparative_logsnr: {
      id: "comparative_logsnr",
      label: "Comparative logSNR",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower logSNR than a named baseline, or an explicit dB gain/loss.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower logSNR than baseline",
          short: "Vs base",
          description:
            "Clear statement that a method reaches higher or lower logSNR than CLEAN, AIRI, uSARA, planar R2D2, etc.",
        },
        logsnr_gain_db: {
          id: "logsnr_gain_db",
          label: "logSNR gain / loss (dB)",
          short: "Δ dB",
          description:
            "Numerical dB improvement or degradation in logSNR relative to a named baseline or setting.",
        },
      },
    },
    transform_family: {
      id: "transform_family",
      label: "Transform family (definition)",
      short: "Transform",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Which log remapping is used before SNR. Complements absolute/comparative scores.",
      submetrics: {
        r2d2_reversible_rlog: {
          id: "r2d2_reversible_rlog",
          label: "R2D2 reversible r_log (DR-param a)",
          short: "r_log",
          description:
            "r_log(x) = x_max·log_a(a·x/x_max + 1) (or close variant) with a tied to target/known DR, then L₂ SNR.",
        },
        log10_stretch_epsilon: {
          id: "log10_stretch_epsilon",
          label: "log₁₀ stretch with ε floor",
          short: "log₁₀+ε",
          description:
            "S/N_log or SNRlog via log₁₀(x/ε + I_N) (ISCAD / Thouvenin-style GMCP), emphasising faint emission.",
        },
        plain_log10: {
          id: "plain_log10",
          label: "Plain log₁₀ on truth & prediction",
          short: "log₁₀",
          description:
            "SNR(log₁₀(x_true), log₁₀(x_pred)) without a DR-parameterised reversible map.",
        },
        log_a_ax_plus_1: {
          id: "log_a_ax_plus_1",
          label: "log_a(a·x + 1) (DR = a)",
          short: "log_a",
          description:
            "Intensity map rlog(x) = log_a(a·x + 1) with a = image DR (MRI-transfer R2D2 analogue).",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified logSNR",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "logSNR-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague log-scale SNR mentions already flagged logsnr=1 but not subtypeable as absolute, comparative, or transform family.",
        },
      },
    },
  };

  const LOGSNR_CATEGORY_ORDER = [
    "absolute_logsnr",
    "comparative_logsnr",
    "transform_family",
    "unspecified",
  ];

  const LOGSNR_CONTEXT_FIELDS = [
    { id: "transform_definition", label: "Transform definition" },
    { id: "transform_parameter", label: "Transform parameter a / ε" },
    { id: "paired_with_linear_snr", label: "Paired with linear SNR" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "array_or_domain", label: "Array / domain" },
    { id: "frequency", label: "Frequency" },
  ];

  global.LOGSNR_TAXONOMY = LOGSNR_TAXONOMY;
  global.LOGSNR_CATEGORY_ORDER = LOGSNR_CATEGORY_ORDER;
  global.LOGSNR_CONTEXT_FIELDS = LOGSNR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
