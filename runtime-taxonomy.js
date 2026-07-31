/**
 * Runtime sub-metric taxonomy — shared config for runtime.html (and future reuse).
 *
 * How to add another metric detail page later:
 * 1. Copy runtime.html → <metric>.html and this file → <metric>-taxonomy.js
 * 2. Replace RUNTIME_TAXONOMY / category keys with that metric’s subtypes
 * 3. Store structured details on each paper (e.g. psnr_details) without changing binary flags
 * 4. From index.html, show an “Explore … Details” link only when that metric is selected
 *
 * Categories below are Runtime reporting types (NOT execution context).
 * Execution context (hardware, parallelism, software, numerical config, workload)
 * is summarized separately on the Runtime page.
 */
(function (global) {
  const RUNTIME_TAXONOMY = {
    wall_clock: {
      id: "wall_clock",
      label: "Wall-clock Runtime",
      short: "Wall",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Elapsed wall-clock time for a stated imaging stage or full reconstruction.",
      submetrics: {
        end_to_end: { id: "end_to_end", label: "End-to-end", short: "E2E" },
        reconstruction_per_image: {
          id: "reconstruction_per_image",
          label: "Reconstruction / per image",
          short: "Recon",
        },
        deconvolution: { id: "deconvolution", label: "Deconvolution", short: "Deconv" },
        gridding: { id: "gridding", label: "Gridding", short: "Grid" },
        fft_ifft: { id: "fft_ifft", label: "FFT / iFFT", short: "FFT" },
        other_stage_specific: {
          id: "other_stage_specific",
          label: "Other stage-specific",
          short: "Stage",
        },
      },
    },
    throughput: {
      id: "throughput",
      label: "Throughput",
      short: "Thru",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Rate metrics (items processed per unit time), not raw elapsed seconds alone.",
      submetrics: {
        images_per_second: { id: "images_per_second", label: "Images / s", short: "Img/s" },
        components_per_second: {
          id: "components_per_second",
          label: "Components / s",
          short: "Comp/s",
        },
        pixels_per_second: { id: "pixels_per_second", label: "Pixels / s", short: "Pix/s" },
        visibilities_per_second: {
          id: "visibilities_per_second",
          label: "Visibilities / s",
          short: "Vis/s",
        },
        data_throughput: { id: "data_throughput", label: "Data throughput", short: "Data" },
      },
    },
    relative_performance: {
      id: "relative_performance",
      label: "Relative Performance",
      short: "Rel",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Speedups, slowdowns, ratios, or percentage runtime change vs a baseline.",
      submetrics: {
        speedup_factor: { id: "speedup_factor", label: "Speedup factor", short: "Speedup" },
        slowdown_factor: { id: "slowdown_factor", label: "Slowdown factor", short: "Slow" },
        percentage_runtime_reduction: {
          id: "percentage_runtime_reduction",
          label: "% runtime reduction",
          short: "%↓",
        },
        runtime_ratio: { id: "runtime_ratio", label: "Runtime ratio", short: "Ratio" },
      },
    },
    runtime_scaling: {
      id: "runtime_scaling",
      label: "Runtime Scaling",
      short: "Scale",
      color: "#2563eb",
      borderStyle: "dashed",
      note: "How runtime changes with problem size or algorithmic parameters (not hardware core counts).",
      submetrics: {
        image_size: { id: "image_size", label: "Image size", short: "Npix" },
        visibility_count: { id: "visibility_count", label: "Visibility count", short: "Nvis" },
        iteration_count: { id: "iteration_count", label: "Iteration / step count", short: "Iters" },
        source_count: { id: "source_count", label: "Source count", short: "Src" },
        channel_count: { id: "channel_count", label: "Channel count", short: "Chan" },
        asymptotic_complexity: {
          id: "asymptotic_complexity",
          label: "Asymptotic complexity",
          short: "O(·)",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified Runtime",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "Runtime-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently mapped to end-to-end.",
      submetrics: {
        unspecified: { id: "unspecified", label: "Unspecified", short: "Unsp" },
      },
    },
  };

  const RUNTIME_CATEGORY_ORDER = [
    "wall_clock",
    "throughput",
    "relative_performance",
    "runtime_scaling",
    "unspecified",
  ];

  const EXECUTION_CONTEXT_FIELDS = [
    { id: "hardware", label: "Hardware" },
    { id: "parallelism", label: "Parallelism" },
    { id: "software", label: "Software" },
    { id: "numerical_configuration", label: "Numerical Configuration" },
    { id: "workload", label: "Workload" },
  ];

  global.RUNTIME_TAXONOMY = RUNTIME_TAXONOMY;
  global.RUNTIME_CATEGORY_ORDER = RUNTIME_CATEGORY_ORDER;
  global.EXECUTION_CONTEXT_FIELDS = EXECUTION_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
