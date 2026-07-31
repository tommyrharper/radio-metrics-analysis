/**
 * Runtime sub-metric taxonomy — shared config for site/detail/runtime.html.
 *
 * How to add another metric detail page later:
 * 1. Copy site/detail/runtime.html → site/detail/<metric>.html and this file → <metric>-taxonomy.js
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
        end_to_end: {
          id: "end_to_end",
          label: "End-to-end",
          short: "E2E",
          description: "Total elapsed time for a full imaging/reconstruction pipeline run.",
        },
        reconstruction_per_image: {
          id: "reconstruction_per_image",
          label: "Reconstruction / per image",
          short: "Recon",
          description: "Wall-clock time attributed to reconstructing one image (or equivalent unit).",
        },
        deconvolution: {
          id: "deconvolution",
          label: "Deconvolution",
          short: "Deconv",
          description: "Elapsed time for the deconvolution / cleaning stage alone.",
        },
        gridding: {
          id: "gridding",
          label: "Gridding",
          short: "Grid",
          description: "Elapsed time for gridding (or degridding) visibility data.",
        },
        fft_ifft: {
          id: "fft_ifft",
          label: "FFT / iFFT",
          short: "FFT",
          description: "Elapsed time for Fourier transform steps in the imaging pipeline.",
        },
        other_stage_specific: {
          id: "other_stage_specific",
          label: "Other stage-specific",
          short: "Stage",
          description: "Wall-clock time for another named pipeline stage not covered above.",
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
        images_per_second: {
          id: "images_per_second",
          label: "Images / s",
          short: "Img/s",
          description: "Imaging or reconstruction rate in images (or fields) per second.",
        },
        components_per_second: {
          id: "components_per_second",
          label: "Components / s",
          short: "Comp/s",
          description: "Rate of CLEAN components, sky-model components, or similar units per second.",
        },
        pixels_per_second: {
          id: "pixels_per_second",
          label: "Pixels / s",
          short: "Pix/s",
          description: "Pixel-processing or image-pixel throughput rate.",
        },
        visibilities_per_second: {
          id: "visibilities_per_second",
          label: "Visibilities / s",
          short: "Vis/s",
          description: "Visibility processing rate (ingest, gridding, or related).",
        },
        data_throughput: {
          id: "data_throughput",
          label: "Data throughput",
          short: "Data",
          description: "Data-volume throughput (e.g. GB/s) rather than item counts alone.",
        },
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
        speedup_factor: {
          id: "speedup_factor",
          label: "Speedup factor",
          short: "Speedup",
          description: "Reported speedup vs a named baseline (e.g. ×N faster).",
        },
        slowdown_factor: {
          id: "slowdown_factor",
          label: "Slowdown factor",
          short: "Slow",
          description: "Reported slowdown vs a named baseline.",
        },
        percentage_runtime_reduction: {
          id: "percentage_runtime_reduction",
          label: "% runtime reduction",
          short: "%↓",
          description: "Percentage reduction in runtime relative to a baseline.",
        },
        runtime_ratio: {
          id: "runtime_ratio",
          label: "Runtime ratio",
          short: "Ratio",
          description: "Direct runtime ratio between methods or configurations.",
        },
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
        image_size: {
          id: "image_size",
          label: "Image size",
          short: "Npix",
          description: "Runtime dependence on image pixel dimensions or FoV size.",
        },
        visibility_count: {
          id: "visibility_count",
          label: "Visibility count",
          short: "Nvis",
          description: "Runtime dependence on number of visibilities or baselines.",
        },
        iteration_count: {
          id: "iteration_count",
          label: "Iteration / step count",
          short: "Iters",
          description: "Runtime dependence on iteration, major-cycle, or step count.",
        },
        source_count: {
          id: "source_count",
          label: "Source count",
          short: "Src",
          description: "Runtime dependence on number of sources or sky-model components.",
        },
        channel_count: {
          id: "channel_count",
          label: "Channel count",
          short: "Chan",
          description: "Runtime dependence on frequency channels or spectral windows.",
        },
        asymptotic_complexity: {
          id: "asymptotic_complexity",
          label: "Asymptotic complexity",
          short: "O(·)",
          description: "Stated big-O or asymptotic scaling of runtime with problem size.",
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
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Runtime mentioned without enough detail to assign a wall-clock stage, throughput, relative, or scaling subtype.",
        },
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
