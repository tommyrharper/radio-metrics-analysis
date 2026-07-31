/**
 * Iterations sub-metric taxonomy — shared config for iterations.html.
 *
 * Parallel to runtime-taxonomy.js / compute-taxonomy.js. Binary metrics.iterations
 * is unchanged; this only subtypes papers that already have iterations: 1.
 *
 * Categories below are Iterations reporting types (NOT iteration context).
 * Iteration Context (stopping criterion, tolerance, max iters, optimiser, LR,
 * batch size, initialisation, regularisation) is summarized separately.
 *
 * Do not mix pure wall-clock Runtime into these subtypes.
 */
(function (global) {
  const ITERATIONS_TAXONOMY = {
    iteration_count: {
      id: "iteration_count",
      label: "Iteration Count",
      short: "Count",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Reported algorithmic iteration / cycle / epoch counts (absolute numbers, not only stopping config).",
      submetrics: {
        total_optimisation_iterations: {
          id: "total_optimisation_iterations",
          label: "Total optimisation iterations",
          short: "Total",
          description:
            "Total CLEAN components, proximal/PnP steps, or other overall optimisation iteration budgets or totals.",
        },
        outer_iterations: {
          id: "outer_iterations",
          label: "Outer iterations",
          short: "Outer",
          description:
            "Major cycles / major loops / outer series steps that wrap an inner solver (e.g. Cotton–Schwab major cycles, R2D2 outer residual steps).",
        },
        inner_iterations: {
          id: "inner_iterations",
          label: "Inner iterations",
          short: "Inner",
          description:
            "Minor cycles, subminor loops, or other nested inner-loop iteration counts within an outer cycle.",
        },
        epochs: {
          id: "epochs",
          label: "Epochs",
          short: "Epochs",
          description: "Training epochs for learning-based methods (dataset passes), distinct from inference series length.",
        },
        training_iterations: {
          id: "training_iterations",
          label: "Training iterations",
          short: "Train",
          description:
            "Optimizer steps, training-series slots, or other training-time iteration counts that are not framed as epochs.",
        },
        inference_iterations: {
          id: "inference_iterations",
          label: "Inference iterations",
          short: "Infer",
          description:
            "Test-time / reconstruction series length, diffusion sampling steps, or other inference-time iteration counts.",
        },
      },
    },
    convergence_behaviour: {
      id: "convergence_behaviour",
      label: "Convergence Behaviour",
      short: "Conv",
      color: "#a16207",
      borderStyle: "dotted",
      note: "How reconstruction progresses to (or fails to reach) a stopping or stability criterion.",
      submetrics: {
        iterations_to_convergence: {
          id: "iterations_to_convergence",
          label: "Iterations to convergence",
          short: "To conv.",
          description:
            "Count or series length at which a residual, χ², SNR, RDR, or similar criterion is met.",
        },
        convergence_rate: {
          id: "convergence_rate",
          label: "Convergence rate",
          short: "Rate",
          description:
            "How fast residuals or objectives improve with iteration (e.g. early vs late major-loop speedup, superlinear behaviour).",
        },
        early_stopping: {
          id: "early_stopping",
          label: "Early stopping",
          short: "Early stop",
          description: "Adaptive halt of training or inference before a fixed maximum when a plateau/criterion is reached.",
        },
        convergence_tolerance_reached: {
          id: "convergence_tolerance_reached",
          label: "Convergence tolerance reached",
          short: "Tol.",
          description: "Explicit statement that a numerical tolerance or threshold was attained.",
        },
        stable_solution_achieved: {
          id: "stable_solution_achieved",
          label: "Stable solution achieved",
          short: "Stable",
          description:
            "Solution or active set stabilizes (components leave active set, residual plateaus) without necessarily quoting a tolerance.",
        },
        divergence_failure: {
          id: "divergence_failure",
          label: "Divergence / failure to converge",
          short: "Diverge",
          description: "Reported divergence, failure to converge, or runaway component growth.",
        },
      },
    },
    comparative_iteration: {
      id: "comparative_iteration",
      label: "Comparative Iteration Performance",
      short: "Cmp",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Iteration counts or ratios relative to a named baseline method or configuration.",
      submetrics: {
        fewer_than_baseline: {
          id: "fewer_than_baseline",
          label: "Fewer iterations than baseline",
          short: "Fewer",
          description: "Method needs fewer iterations / major cycles than a named baseline at matched accuracy or residual.",
        },
        more_than_baseline: {
          id: "more_than_baseline",
          label: "More iterations than baseline",
          short: "More",
          description: "Method uses more iterations than a baseline (e.g. fixed PnP budget vs adaptive CLEAN major cycles).",
        },
        percentage_iteration_reduction: {
          id: "percentage_iteration_reduction",
          label: "Percentage iteration reduction",
          short: "%↓",
          description: "Percentage or order-of-magnitude reduction in iterations vs a baseline.",
        },
        iteration_ratio: {
          id: "iteration_ratio",
          label: "Iteration ratio",
          short: "Ratio",
          description: "Direct ratio of iteration counts between methods (e.g. ×N fewer major loops, epoch speedup).",
        },
      },
    },
    iteration_scaling: {
      id: "iteration_scaling",
      label: "Iteration Scaling",
      short: "Scale",
      color: "#2563eb",
      borderStyle: "dashed",
      note: "How iteration count or convergence behaviour scales with problem size or algorithm settings.",
      submetrics: {
        image_size: {
          id: "image_size",
          label: "Scaling with image size",
          short: "N_pix",
          description: "Iteration count or work-vs-iteration models that depend on image/pixel size.",
        },
        visibility_count: {
          id: "visibility_count",
          label: "Scaling with visibility count",
          short: "N_vis",
          description: "How iterations scale with number of visibilities or dataset size.",
        },
        source_count: {
          id: "source_count",
          label: "Scaling with source count",
          short: "N_src",
          description: "How iterations scale with number of sources or components.",
        },
        noise_level: {
          id: "noise_level",
          label: "Scaling with noise level",
          short: "Noise",
          description: "Iteration-to-convergence or series length across noise / input-SNR sweeps.",
        },
        stopping_tolerance: {
          id: "stopping_tolerance",
          label: "Scaling with stopping tolerance",
          short: "Tol-scale",
          description: "How required iterations change with tighter or looser stopping tolerances.",
        },
        algorithm_parameters: {
          id: "algorithm_parameters",
          label: "Scaling with algorithm parameters",
          short: "Params",
          description:
            "Iteration dependence on gain, scales, sampling steps K, series depth, or other algorithm knobs.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Iterations",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Iterations-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Method is iterative or iterations flagged, but the paper does not report countable iteration results that fit a subtype.",
        },
      },
    },
  };

  const ITERATIONS_CATEGORY_ORDER = [
    "iteration_count",
    "convergence_behaviour",
    "comparative_iteration",
    "iteration_scaling",
    "unspecified",
  ];

  const ITERATIONS_CONTEXT_FIELDS = [
    { id: "stopping_criterion", label: "Stopping criterion" },
    { id: "convergence_threshold", label: "Convergence threshold" },
    { id: "maximum_iterations", label: "Maximum iterations allowed" },
    { id: "optimiser", label: "Optimiser" },
    { id: "learning_rate", label: "Learning rate" },
    { id: "batch_size", label: "Batch size" },
    { id: "initialisation_method", label: "Initialisation method" },
    { id: "regularisation_parameters", label: "Regularisation parameters" },
  ];

  global.ITERATIONS_TAXONOMY = ITERATIONS_TAXONOMY;
  global.ITERATIONS_CATEGORY_ORDER = ITERATIONS_CATEGORY_ORDER;
  global.ITERATIONS_CONTEXT_FIELDS = ITERATIONS_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
