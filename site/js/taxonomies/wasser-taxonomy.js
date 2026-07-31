/**
 * Wasserstein sub-metric taxonomy — shared config for wasser.html.
 *
 * Parallel to rms-taxonomy.js / runtime-taxonomy.js / compute-taxonomy.js.
 * Binary metrics.wasserstein is unchanged; this only subtypes papers that
 * already have wasserstein: 1.
 *
 * Categories below are Wasserstein reporting types (NOT Wasserstein Context).
 * Wasserstein Context (window size, distance order, aggregation, simulation
 * vs real, frequency, array) is summarized separately.
 *
 * Wasser = earth-mover / Wasserstein distance on reconstructed intensity maps
 * as a fidelity or convergence proxy (especially when pixel-wise ground truth
 * is unavailable). Do not invent subtypes from GAN training losses alone.
 */
(function (global) {
  const WASSER_TAXONOMY = {
    windowed_distance: {
      id: "windowed_distance",
      label: "Windowed Wasserstein Distance",
      short: "Windowed",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Local / sliding-window Wasserstein distances on intensity maps, usually aggregated to a scalar.",
      submetrics: {
        w5_windowed_w1: {
          id: "w5_windowed_w1",
          label: "W₅ (5×5 windowed W₁ + L2)",
          short: "W₅",
          description:
            "L2 norm of per-pixel Wasserstein-1 distances in 5×5 sliding windows between reconstructions (W₅).",
        },
        other_windowed_wasserstein: {
          id: "other_windowed_wasserstein",
          label: "Other windowed Wasserstein",
          short: "Other win.",
          description:
            "Other local/windowed Wasserstein scores on reconstructed maps that are not the named W₅ construction.",
        },
      },
    },
    cross_iteration: {
      id: "cross_iteration",
      label: "Cross-Iteration Wasserstein",
      short: "X-iter",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Wasserstein between successive reconstructions used as a convergence / stability diagnostic.",
      submetrics: {
        successive_reconstruction: {
          id: "successive_reconstruction",
          label: "Successive-reconstruction distance",
          short: "Successive",
          description:
            "Wasserstein (e.g. W₅) between iteration-to-iteration reconstructions; typically decreases as iterations proceed.",
        },
      },
    },
    cross_method: {
      id: "cross_method",
      label: "Cross-Method Wasserstein",
      short: "X-method",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Wasserstein between outputs of different algorithms or implementations on the same data.",
      submetrics: {
        parallel_vs_serial: {
          id: "parallel_vs_serial",
          label: "Parallel vs serial similarity",
          short: "Par∥Ser",
          description:
            "Wasserstein between parallel and serial reconstructions arguing output similarity.",
        },
        other_method_comparison: {
          id: "other_method_comparison",
          label: "Other method / implementation comparison",
          short: "Vs method",
          description:
            "Wasserstein between named methods or implementations other than a parallel-vs-serial split.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Wasserstein",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Wasserstein-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague Wasserstein mentions already flagged wasserstein=1 but not subtypeable as windowed, cross-iteration, or cross-method.",
        },
      },
    },
  };

  const WASSER_CATEGORY_ORDER = [
    "windowed_distance",
    "cross_iteration",
    "cross_method",
    "unspecified",
  ];

  const WASSER_CONTEXT_FIELDS = [
    { id: "window_size", label: "Window size" },
    { id: "distance_order", label: "Distance order" },
    { id: "aggregation", label: "Aggregation" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.WASSER_TAXONOMY = WASSER_TAXONOMY;
  global.WASSER_CATEGORY_ORDER = WASSER_CATEGORY_ORDER;
  global.WASSER_CONTEXT_FIELDS = WASSER_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
