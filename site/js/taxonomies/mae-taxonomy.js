/**
 * MAE sub-metric taxonomy — shared config for mae.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.mae is unchanged; this only subtypes papers that already have mae: 1.
 *
 * Categories below are MAE reporting types (NOT MAE Context).
 * MAE Context (target parameters, train vs validation, domain, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * MAE here is any reported mean absolute error tied to the imaging or inference
 * workflow — not restricted to pixel-wise restored-image MAE vs sky truth.
 */
(function (global) {
  const MAE_TAXONOMY = {
    parameter_regression: {
      id: "parameter_regression",
      label: "Parameter-Regression MAE",
      short: "Param",
      color: "#0f766e",
      borderStyle: "solid",
      note: "MAE on inferred physical or model parameters (not image-pixel fidelity).",
      submetrics: {
        physical_parameter_mae: {
          id: "physical_parameter_mae",
          label: "Physical-parameter MAE",
          short: "Phys param",
          description:
            "Mean absolute error on inferred physical parameters (e.g. spin, R_high, inclination, position angle), including train/validation curves without a single summary scalar.",
        },
        other_parameter_mae: {
          id: "other_parameter_mae",
          label: "Other parameter-regression MAE",
          short: "Other param",
          description:
            "MAE on other regressed quantities (calibration, model coefficients, etc.) that are not the named physical-parameter set above.",
        },
      },
    },
    image_domain: {
      id: "image_domain",
      label: "Image-Domain MAE",
      short: "Image",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Pixel-wise or image-region MAE against truth / reference brightness maps.",
      submetrics: {
        pixel_mae_vs_truth: {
          id: "pixel_mae_vs_truth",
          label: "Pixel MAE vs ground truth",
          short: "Pixel vs truth",
          description:
            "Mean absolute error between reconstructed and true / reference sky brightness maps (image-domain fidelity).",
        },
        other_image_mae: {
          id: "other_image_mae",
          label: "Other image-domain MAE",
          short: "Other img",
          description:
            "Other image-space MAE variants (e.g. masked region, residual-image MAE) that are not full-map pixel MAE vs truth.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified MAE",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "MAE-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague MAE mentions already flagged mae=1 but not subtypeable as parameter-regression or image-domain MAE.",
        },
      },
    },
  };

  const MAE_CATEGORY_ORDER = [
    "parameter_regression",
    "image_domain",
    "unspecified",
  ];

  const MAE_CONTEXT_FIELDS = [
    { id: "target_parameters", label: "Target parameters" },
    { id: "train_vs_validation", label: "Train vs validation" },
    { id: "domain", label: "Domain" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.MAE_TAXONOMY = MAE_TAXONOMY;
  global.MAE_CATEGORY_ORDER = MAE_CATEGORY_ORDER;
  global.MAE_CONTEXT_FIELDS = MAE_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
