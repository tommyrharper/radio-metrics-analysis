/**
 * RDR sub-metric taxonomy — shared config for rdr.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.rdr is unchanged; this only subtypes papers that already have rdr: 1.
 *
 * Categories below are RDR reporting types (NOT RDR Context).
 * RDR Context (domain, norm, reporting scale, simulation vs real,
 * frequency, array) is summarized separately.
 *
 * RDR = residual-to-dirty ratio ‖r̂‖₂/‖x_dirty‖₂ (or Frobenius / sphere /
 * back-projected analogues). Do NOT treat absolute residual RMS (Jy/beam)
 * as RDR. Qualitative residuals alone should not invent subtypes.
 */
(function (global) {
  const RDR_TAXONOMY = {
    reported_rdr: {
      id: "reported_rdr",
      label: "Reported / Measured RDR",
      short: "Reported",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Tabulated or quoted residual-to-dirty ratio (or named image-domain data-fidelity σ of the same form).",
      submetrics: {
        planar_l2_rdr: {
          id: "planar_l2_rdr",
          label: "Planar ℓ₂ RDR / data-fidelity σ",
          short: "Planar ℓ₂",
          description:
            "‖r̂‖₂/‖x_dirty‖₂ on planar images (including Aghabiglou-style image-domain data fidelity σ).",
        },
        frobenius_cube_rdr: {
          id: "frobenius_cube_rdr",
          label: "Frobenius hyperspectral RDR",
          short: "Frobenius",
          description:
            "RDR = ‖X^res‖_F / ‖X^dirty‖_F on hyperspectral cubes (e.g. HyperAIRI).",
        },
        spherical_rdr: {
          id: "spherical_rdr",
          label: "Spherical RDR",
          short: "Sphere",
          description:
            "RDR(r, x^d) = ‖r‖₂/‖x^d‖₂ with residual and dirty image on the sphere (e.g. S-R2D2).",
        },
        backprojected_mri_rdr: {
          id: "backprojected_mri_rdr",
          label: "Back-projected residual ratio (MRI)",
          short: "MRI RDR",
          description:
            "RDR = ‖r‖₂/‖x_b‖₂ for back-projected data residual vs dirty-like image (e.g. iR2D2 MRI).",
        },
      },
    },
    comparative_rdr: {
      id: "comparative_rdr",
      label: "Comparative RDR",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Lower/higher RDR than a baseline, or order-of-magnitude / factor claims.",
      submetrics: {
        lower_higher_than_baseline: {
          id: "lower_higher_than_baseline",
          label: "Lower / higher RDR than baseline",
          short: "Vs base",
          description:
            "Clear numerical statement that a method reaches lower or higher RDR than a named baseline.",
        },
        rdr_factor_vs_baseline: {
          id: "rdr_factor_vs_baseline",
          label: "RDR factor / order-of-magnitude vs baseline",
          short: "Factor",
          description:
            "Numerical factor or order-of-magnitude by which RDR differs from a baseline.",
        },
      },
    },
    framework_operational: {
      id: "framework_operational",
      label: "Framework / Operational RDR",
      short: "Framework",
      color: "#a16207",
      borderStyle: "dotted",
      note: "RDR named as a core fidelity metric or used operationally (e.g. adaptive stopping).",
      submetrics: {
        named_data_fidelity_metric: {
          id: "named_data_fidelity_metric",
          label: "Named core data-fidelity metric",
          short: "Named",
          description:
            "RDR (or σ) defined as a primary evaluation / data-fidelity metric in the paper’s framework.",
        },
        adaptive_stopping_criterion: {
          id: "adaptive_stopping_criterion",
          label: "Adaptive stopping via RDR",
          short: "Stopping",
          description:
            "RDR (or residual-energy descent) used to drive adaptive series length / stopping.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified RDR",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "RDR-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague residual-ratio mentions already flagged rdr=1 but not subtypeable as reported, comparative, or framework RDR.",
        },
      },
    },
  };

  const RDR_CATEGORY_ORDER = [
    "reported_rdr",
    "comparative_rdr",
    "framework_operational",
    "unspecified",
  ];

  const RDR_CONTEXT_FIELDS = [
    { id: "domain", label: "Domain" },
    { id: "norm", label: "Norm" },
    { id: "reporting_scale", label: "Reporting scale" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.RDR_TAXONOMY = RDR_TAXONOMY;
  global.RDR_CATEGORY_ORDER = RDR_CATEGORY_ORDER;
  global.RDR_CONTEXT_FIELDS = RDR_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
