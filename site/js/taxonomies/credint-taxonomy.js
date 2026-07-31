/**
 * Credible interval (CredInt) sub-metric taxonomy — shared config for credint.html.
 *
 * Parallel to rms-taxonomy.js / dr-taxonomy.js / runtime-taxonomy.js.
 * Binary metrics.credible_interval is unchanged; this only subtypes papers that
 * already have credible_interval: 1.
 *
 * Categories below are CredInt reporting types (NOT CredInt Context).
 * CredInt Context (credible level, spatial aggregation, estimation method,
 * simulation vs real, frequency, array) is summarized separately.
 *
 * CredInt = Bayesian credible intervals / HPD regions, posterior percentile
 * ranges, or calibrated bootstrap/conformal image intervals used to quantify
 * reconstruction uncertainty. Distinct from uncertainty_correlation (whether
 * estimated uncertainty tracks actual error).
 */
(function (global) {
  const CREDINT_TAXONOMY = {
    hpd_local_credint: {
      id: "hpd_local_credint",
      label: "HPD / Local Credible Intervals",
      short: "HPD/LCI",
      color: "#0f766e",
      borderStyle: "solid",
      note: "Highest Posterior Density regions, local credible-interval widths, or HPD-based hypothesis tests.",
      submetrics: {
        hpd_credible_regions: {
          id: "hpd_credible_regions",
          label: "HPD credible regions",
          short: "HPD",
          description:
            "Highest Posterior Density credible regions at a stated level 100(1−α)%, often approximated from a MAP potential.",
        },
        local_credible_intervals: {
          id: "local_credible_intervals",
          label: "Local Credible Intervals (LCIs)",
          short: "LCI",
          description:
            "Pixel- or superpixel-scale Bayesian error-bar widths from HPD boundaries (e.g. mean LCI per image).",
        },
        hpd_hypothesis_testing: {
          id: "hpd_hypothesis_testing",
          label: "HPD hypothesis testing",
          short: "HPD test",
          description:
            "Surrogate-image potential compared to a fixed-level HPD isocontour to accept or reject structural hypotheses.",
        },
      },
    },
    posterior_sample_intervals: {
      id: "posterior_sample_intervals",
      label: "Posterior Sample Intervals",
      short: "Posterior",
      color: "#6d28d9",
      borderStyle: "dashed",
      note: "Intervals or uncertainty maps derived from posterior samples or variational posteriors (not HPD/LCI machinery).",
      submetrics: {
        pixel_percentile_ranges: {
          id: "pixel_percentile_ranges",
          label: "Pixel percentile ranges",
          short: "Percentile",
          description:
            "Per-pixel posterior percentile bands (e.g. 16th–84th) or equivalent sample-based credible ranges on the image.",
        },
        relative_posterior_uncertainty_maps: {
          id: "relative_posterior_uncertainty_maps",
          label: "Relative posterior uncertainty maps",
          short: "Rel. UQ",
          description:
            "Pixel-wise relative posterior uncertainty maps reported as Bayesian UQ (without tabulated HPD/LCI widths).",
        },
        parameter_posterior_intervals: {
          id: "parameter_posterior_intervals",
          label: "Parameter posterior intervals",
          short: "Param",
          description:
            "Posterior intervals on model/image-structure parameters (e.g. PCA amplitudes, ring geometry) from MCMC or similar.",
        },
      },
    },
    bootstrap_conformal_intervals: {
      id: "bootstrap_conformal_intervals",
      label: "Bootstrap / Conformal Intervals",
      short: "Bootstrap",
      color: "#a16207",
      borderStyle: "dotted",
      note: "Non-Bayesian or hybrid predictive intervals from bootstrap / conformal calibration on reconstructions.",
      submetrics: {
        pixel_confidence_intervals: {
          id: "pixel_confidence_intervals",
          label: "Pixel confidence intervals",
          short: "Pixel CI",
          description:
            "Pixel-wise confidence / predictive intervals from (equivariant) bootstrap and/or conformal calibration.",
        },
        interval_length_coverage: {
          id: "interval_length_coverage",
          label: "Interval length & empirical coverage",
          short: "Len/cov",
          description:
            "Reported interval-length scores (e.g. ℓ2 length ratio) and/or empirical coverage vs a target confidence level.",
        },
      },
    },
    unspecified: {
      id: "unspecified",
      label: "Unspecified CredInt",
      short: "Unsp",
      color: "#475569",
      borderStyle: "dashed",
      distinct: true,
      note:
        "CredInt-positive papers whose evidence is too vague to subtype. Extraction limitation — not silently overclassified.",
      submetrics: {
        unspecified: {
          id: "unspecified",
          label: "Unspecified",
          short: "Unsp",
          description:
            "Vague Bayesian/UQ framing already flagged credible_interval=1 but not subtypeable as HPD, posterior-sample, or bootstrap intervals.",
        },
      },
    },
  };

  const CREDINT_CATEGORY_ORDER = [
    "hpd_local_credint",
    "posterior_sample_intervals",
    "bootstrap_conformal_intervals",
    "unspecified",
  ];

  const CREDINT_CONTEXT_FIELDS = [
    { id: "credible_level", label: "Credible level" },
    { id: "spatial_aggregation", label: "Spatial aggregation" },
    { id: "estimation_method", label: "Estimation method" },
    { id: "simulation_vs_real", label: "Simulation vs real data" },
    { id: "frequency", label: "Frequency" },
    { id: "array", label: "Array" },
  ];

  global.CREDINT_TAXONOMY = CREDINT_TAXONOMY;
  global.CREDINT_CATEGORY_ORDER = CREDINT_CATEGORY_ORDER;
  global.CREDINT_CONTEXT_FIELDS = CREDINT_CONTEXT_FIELDS;
})(typeof window !== "undefined" ? window : globalThis);
