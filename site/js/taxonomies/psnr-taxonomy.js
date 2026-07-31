/**
 * PSNR sub-metric taxonomy — shared config for psnr.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.psnr is unchanged; this only subtypes papers that already
 * have psnr: 1.
 *
 * Categories below are PSNR reporting types (NOT PSNR Context).
 * PSNR Context (formulation, MAX definition, image domain, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * PSNR = peak signal-to-noise ratio as a pixel-wise reconstruction fidelity
 * score against known truth / reference (dB). Do not invent subtypes from
 * qualitative visual comparisons alone. SNR/logSNR are separate columns.
 */
(function (global) {
  const PSNR_TAXONOMY = {
    absolute_psnr: {
      id: "absolute_psnr",
      label: "Measured PSNR (Absolute)",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Tabulated or quoted PSNR in dB against known truth / reference images.",
      submetrics: {
        ten_log10_psnr: {
          id: "ten_log10_psnr",
          label: "10·log₁₀ PSNR",
          short: "10 log₁₀",
          description:
            "PSNR via 10·log₁₀(MAX/MSE), 10·log₁₀(I_max²/MSE), or magnitude L₂ form 10·log₁₀(NM²/‖·‖₂²).",
        },
        twenty_log10_linear_psnr: {
          id: "twenty_log10_linear_psnr",
          label: "20·log₁₀ linear PSNR",
          short: "20 log₁₀",
          description:
            "Linear-image PSNR = 20·log₁₀(max(I) / reconstruction error), e.g. CG-CLEAN.",
        },
        log_domain_psnr: {
          id: "log_domain_psnr",
          label: "Log-domain PSNR (PSNR_log)",
          short: "PSNR_log",
          description:
            "PSNR on log-scaled images (faint/diffuse emphasis); not the separate logSNR column.",
        },
      },
    },
    comparative_psnr: {
      id: "comparative_psnr",
      label: "Comparative PSNR",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower PSNR than a named baseline, or an explicit dB gain/delta.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower PSNR than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches higher or lower PSNR than a named baseline.",
        },
        psnr_gain_db: {
          id: "psnr_gain_db",
          label: "PSNR gain / delta (dB)",
          short: "Δ dB",
          description: "Explicit PSNR improvement (or drop) in decibels relative to a baseline.",
        },
      },
    },
    parameter_sweep_psnr: {
      id: "parameter_sweep_psnr",
      label: "PSNR vs Parameter / Ablation",
      short: "Sweep",
      color: "#0369a1",
      borderStyle: "dashed",
      note: "PSNR tracked across a hyperparameter, perturbation, or training schedule.",
      submetrics: {
        vs_hyperparameter: {
          id: "vs_hyperparameter",
          label: "PSNR vs hyperparameter / perturbation",
          short: "Vs param",
          description:
            "PSNR swept vs sampling steps, PSF-warp γ, or similar controlled parameter.",
        },
        checkpoint_selection: {
          id: "checkpoint_selection",
          label: "Training / fine-tuning peak PSNR",
          short: "Peak epoch",
          description:
            "Validation or fine-tuning PSNR used to select checkpoints or report convergence epochs.",
        },
      },
    },
    framework_defined: {
      id: "framework_defined",
      label: "Framework / Defined PSNR",
      short: "Framework",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Named core quality metric without tabulated reconstruction PSNR values.",
      submetrics: {
        named_core_quality_metric: {
          id: "named_core_quality_metric",
          label: "Named core quality metric",
          short: "Named",
          description:
            "PSNR defined as a core framework/benchmark quality metric without Section-style tabulated run values.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified PSNR",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "PSNR-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague PSNR mentions already flagged psnr=1 but not subtypeable as absolute, comparative, sweep, or framework.",
        },
      },
    },
  };

  const PSNR_CATEGORY_ORDER = [
    "absolute_psnr",
    "comparative_psnr",
    "parameter_sweep_psnr",
    "framework_defined",
    "unspecified",
  ];

  const PSNR_CONTEXT_FIELDS = [
    { id: "formulation", label: "Formulation" },
    { id: "max_definition", label: "MAX / peak definition" },
    { id: "image_domain", label: "Image domain / normalisation" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.PSNR_TAXONOMY = PSNR_TAXONOMY;
  global.PSNR_CATEGORY_ORDER = PSNR_CATEGORY_ORDER;
  global.PSNR_CONTEXT_FIELDS = PSNR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
