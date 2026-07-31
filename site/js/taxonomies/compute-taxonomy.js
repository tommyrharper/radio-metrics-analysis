/**
 * Compute sub-metric taxonomy — shared config for compute.html.
 *
 * Parallel to runtime-taxonomy.js. Binary metrics.compute_cost is unchanged;
 * this only subtypes papers that already have compute_cost: 1.
 *
 * Categories below are Compute reporting types (NOT measurement context).
 * Measurement context (hardware, parallelism, software, numerical config, workload)
 * is summarized separately on the Compute page.
 *
 * Do not mix pure wall-clock Runtime into these subtypes unless the paper frames
 * the result as resource cost (CPU/GPU-hours, energy, memory, FLOPs, etc.).
 */
(function (global) {
  const COMPUTE_TAXONOMY = {
    resource_usage: {
      id: "resource_usage",
      label: "Resource Usage (Absolute)",
      short: "Abs",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Absolute resource totals: core-hours, energy, memory, FLOPs, or other measured resource quantities.",
      submetrics: {
        cpu_gpu_hours: {
          id: "cpu_gpu_hours",
          label: "CPU / GPU hours",
          short: "Core-h",
          description:
            "CPU core-hours, GPU-hours, or GPU-years for training, precomputation, or imaging (not plain wall-clock alone).",
        },
        energy: {
          id: "energy",
          label: "Energy",
          short: "Energy",
          description: "Energy-to-solution or job energy (J, kWh), including static vs dynamic energy splits when reported.",
        },
        peak_memory: {
          id: "peak_memory",
          label: "Peak memory / footprint",
          short: "Mem",
          description:
            "Peak working memory, operator/matrix storage, beam-patch footprint, or similar absolute memory cost.",
        },
        flops: {
          id: "flops",
          label: "FLOPs / arithmetic intensity",
          short: "FLOP",
          description:
            "FLOP counts, sustained Gflop/s, arithmetic intensity (flop/byte), or facility-scale FLOP/s budgets framed as compute cost.",
        },
        other_absolute: {
          id: "other_absolute",
          label: "Other absolute resource",
          short: "Other",
          description:
            "Other absolute resource scores (e.g. device utilisation, carbon-to-solution, model parameter count as resource size).",
        },
      },
    },
    efficiency_intensity: {
      id: "efficiency_intensity",
      label: "Efficiency / Intensity",
      short: "Eff",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Resource efficiency ratios (work per joule, per watt, per byte of energy, etc.), not raw totals alone.",
      submetrics: {
        energy_efficiency: {
          id: "energy_efficiency",
          label: "Energy efficiency",
          short: "η_E",
          description: "Work per unit energy (e.g. visibilities/J) or related energy-efficiency scores.",
        },
        performance_per_watt: {
          id: "performance_per_watt",
          label: "Performance per watt",
          short: "Perf/W",
          description: "Throughput or performance normalized by power draw.",
        },
        memory_efficiency: {
          id: "memory_efficiency",
          label: "Memory efficiency",
          short: "η_mem",
          description: "Bytes processed per joule, or similar memory-efficiency ratios.",
        },
        other_efficiency: {
          id: "other_efficiency",
          label: "Other efficiency ratio",
          short: "Eff*",
          description: "Other efficiency or intensity ratios framed as compute cost (e.g. cost efficiency, carbon efficiency).",
        },
      },
    },
    relative_compute: {
      id: "relative_compute",
      label: "Relative Compute",
      short: "Rel",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Resource use vs a baseline: FLOP/resource speedups, percentage reductions, or cost ratios between methods.",
      submetrics: {
        resource_speedup: {
          id: "resource_speedup",
          label: "Resource speedup",
          short: "Speedup",
          description: "Speedup in FLOPs, core-hours, or other resource use vs a named baseline (not wall-clock alone).",
        },
        resource_reduction_pct: {
          id: "resource_reduction_pct",
          label: "% resource reduction",
          short: "%↓",
          description: "Percentage reduction in memory, energy, operations, or other resource vs a baseline.",
        },
        cost_ratio: {
          id: "cost_ratio",
          label: "Cost ratio",
          short: "Ratio",
          description:
            "Direct compute-cost ratio between methods or configurations (e.g. ×N CPU-hours, operation-count ratios).",
        },
      },
    },
    scaling_complexity: {
      id: "scaling_complexity",
      label: "Scaling / Complexity",
      short: "Scale",
      color: "#2563eb",
      borderStyle: "dashed",
      note: "How compute/work scales with problem size, asymptotic complexity, or hardware when framed as cost/work.",
      submetrics: {
        problem_size_scaling: {
          id: "problem_size_scaling",
          label: "Problem-size scaling",
          short: "N-scale",
          description:
            "Compute or work dependence on image size, visibility count, channels, coils, or similar problem dimensions.",
        },
        asymptotic_complexity: {
          id: "asymptotic_complexity",
          label: "Asymptotic complexity",
          short: "O(·)",
          description: "Stated big-O or analytic operation-count models framed as computational cost.",
        },
        hardware_scaling: {
          id: "hardware_scaling",
          label: "Hardware scaling",
          short: "HW",
          description:
            "How compute/work or capacity scales with cores, GPUs, or nodes (cost/work framing, not wall-clock alone).",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Compute",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Compute-positive papers whose evidence is too vague to subtype, or only wall-clock already covered by Runtime. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Compute mentioned without enough detail to assign an absolute, efficiency, relative, or scaling subtype (often qualitative cost claims or wall-clock labelled as compute).",
        },
      },
    },
  };

  const COMPUTE_CATEGORY_ORDER = [
    "resource_usage",
    "efficiency_intensity",
    "relative_compute",
    "scaling_complexity",
    "unspecified",
  ];

  const COMPUTE_CONTEXT_FIELDS = [
    { id: "hardware", label: "Hardware" },
    { id: "parallelism", label: "Parallelism" },
    { id: "software", label: "Software" },
    { id: "numerical_configuration", label: "Numerical Configuration" },
    { id: "workload", label: "Workload" },
  ];

  global.COMPUTE_TAXONOMY = COMPUTE_TAXONOMY;
  global.COMPUTE_CATEGORY_ORDER = COMPUTE_CATEGORY_ORDER;
  global.COMPUTE_CONTEXT_FIELDS = COMPUTE_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
