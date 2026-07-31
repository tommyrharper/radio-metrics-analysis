/**
 * SNR sub-metric taxonomy — shared config for snr.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.snr is unchanged; this only subtypes papers that already have snr: 1.
 *
 * Categories below are SNR reporting types (NOT SNR Context).
 * SNR Context (formula, simulation vs real, input-SNR setting, frequency, array)
 * is summarized separately.
 *
 * logSNR / S/N_log is a separate binary column — do not invent logSNR subtypes here.
 * Qualitative residuals alone are not SNR; residual flatness is not a substitute.
 */
(function (global) {
  const SNR_TAXONOMY = {
    reconstruction_snr: {
      id: "reconstruction_snr",
      label: "Reconstruction SNR (Absolute)",
      short: "Absolute",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Measured reconstruction fidelity SNR against known truth (image-domain L₂ / σ / Frobenius / alternate MSE forms).",
      submetrics: {
        l2_reconstruction_snr: {
          id: "l2_reconstruction_snr",
          label: "L₂ reconstruction SNR (20·log₁₀)",
          short: "L₂",
          description:
            "Standard image-domain SNR: 20·log₁₀(‖x‖₂ / ‖x − x̂‖₂) (or equivalent −20·log₁₀ form) vs ground truth.",
        },
        std_reconstruction_snr: {
          id: "std_reconstruction_snr",
          label: "Std-dev reconstruction SNR",
          short: "σ form",
          description:
            "Reconstruction SNR as 20·log₁₀(σ_x / σ_{x−x̂}) (SARA 2012-style standard-deviation form).",
        },
        frobenius_hyperspectral_snr: {
          id: "frobenius_hyperspectral_snr",
          label: "Frobenius / hyperspectral SNR",
          short: "Frobenius",
          description:
            "Hyperspectral cube SNR via Frobenius norms: 20·log₁₀(‖X̄‖_F / ‖X̄ − X‖_F).",
        },
        alternate_mse_snr: {
          id: "alternate_mse_snr",
          label: "Alternate MSE SNR (10·log₁₀)",
          short: "MSE SNR",
          description:
            "Non-standard SNR from mean flux and MSE, e.g. 10·log₁₀[(1/N)Σx / MSE] (DDRM).",
        },
        spectral_index_snr: {
          id: "spectral_index_snr",
          label: "Spectral-index SNR (sSNR)",
          short: "sSNR",
          description:
            "SNR between reconstructed and ground-truth spectral-index maps (hyperspectral setting).",
        },
      },
    },
    input_operating_snr: {
      id: "input_operating_snr",
      label: "Input / Operating SNR",
      short: "Input/Op",
      color: "#a16207",
      borderStyle: "dotted",
      note: "SNR as simulation noise setting, image-plane observing regime, discoverability threshold, or operational trade-off — not a reconstruction score.",
      submetrics: {
        input_visibility_snr: {
          id: "input_visibility_snr",
          label: "Input visibility SNR",
          short: "Input vis",
          description:
            "Fixed or swept visibility/input SNR used to set simulation noise (commonly 15–55 dB; often 30–35 dB).",
        },
        image_plane_theoretical_snr: {
          id: "image_plane_theoretical_snr",
          label: "Image-plane / theoretical SNR",
          short: "Img-plane",
          description:
            "Image-plane SNR as clean-beam-convolved model peak over image-plane noise (classic deconvolution noise sweeps).",
        },
        discoverability_threshold_snr: {
          id: "discoverability_threshold_snr",
          label: "Discoverability / threshold SNR",
          short: "Threshold",
          description:
            "Literature or adopted SNR thresholds for detection/discoverability (e.g. combined lensed-image SNR ≥ 20).",
        },
        operational_tradeoff_snr: {
          id: "operational_tradeoff_snr",
          label: "Operational SNR trade-off",
          short: "Trade-off",
          description:
            "Quantitative operational claim that a processing choice changes effective SNR (e.g. sparsification reducing SNR by 10×).",
        },
      },
    },
    comparative_snr: {
      id: "comparative_snr",
      label: "Comparative SNR",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Higher/lower reconstruction SNR than a named baseline, or explicit dB gain/loss.",
      submetrics: {
        higher_lower_than_baseline: {
          id: "higher_lower_than_baseline",
          label: "Higher / lower SNR than baseline",
          short: "Vs base",
          description:
            "Clear statement that a method reaches higher or lower reconstruction SNR than a named baseline.",
        },
        db_gain_vs_baseline: {
          id: "db_gain_vs_baseline",
          label: "dB gain / loss vs baseline",
          short: "dB Δ",
          description:
            "Numerical dB improvement or degradation relative to a named baseline or configuration.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified SNR",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "SNR-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague SNR mentions already flagged snr=1 but not subtypeable as reconstruction, input/operating, or comparative SNR.",
        },
      },
    },
  };

  const SNR_CATEGORY_ORDER = [
    "reconstruction_snr",
    "input_operating_snr",
    "comparative_snr",
    "unspecified",
  ];

  const SNR_CONTEXT_FIELDS = [
    { id: "formula", label: "Formula" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "input_snr_setting", label: "Input SNR setting" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.SNR_TAXONOMY = SNR_TAXONOMY;
  global.SNR_CATEGORY_ORDER = SNR_CATEGORY_ORDER;
  global.SNR_CONTEXT_FIELDS = SNR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
