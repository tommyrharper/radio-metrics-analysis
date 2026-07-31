# Compute

## What this metric means here

**Compute** captures resource cost beyond plain wall-clock time: CPU or GPU core-hours, accelerator memory footprint and bandwidth, energy and carbon, throughput and arithmetic intensity, device utilisation, and amortized training or operator-precomputation cost across the imaging pipeline (visibilities → gridding → iFFT → deconvolution). Papers rarely report all dimensions; this column aggregates whichever resource metrics authors actually measure or model.

## How papers use it

### Formal benchmark metrics (astroCAMP)

astroCAMP (2025) defines the richest compute taxonomy in the corpus. Core quantities include **energy-to-solution** `E_c = ∫P(t)dt` (J, from PDU/RAPL/NVML), **throughput** `Θ = N/T_c` (visibilities/s), **energy efficiency** `η_E = N/E_c` (visibilities/J), **device utilisation** `U = t_active/t_total`, **memory bandwidth** `B_mem = Bytes/T_c` (GB/s), **memory efficiency** `η_mem = Bytes/E_c` (GB/J), **peak memory** `M_peak` (GB), **carbon-to-solution** `C_c = E_c·κ(t,r)` (gCO₂e), and **cost** metrics (`C_E`, TCO, visibilities per euro). Measured findings: GPU/IDG-device layers contribute ≈60–90% of active-compute energy at 32,768² pixels; static (idle) energy is ≈80–85% of total; CPU end-to-end utilisation rises only ≈2% (1 thread) to ≈18% (64 threads) while gridding kernels reach higher intra-stage scaling; roofline analysis attributes limits to orchestration and host–device supply more than single-kernel peaks.

### Gridding throughput and capacity modeling (classic)

SKA-MEMO-132 reports **grid-point throughput** (Mpoints/s): Tesla C2070 CUDA 3413.5 Mpoints/s vs dual Xeon X5570 1408.9 Mpoints/s for 4096² grid, 129-pixel support. Arithmetic intensity ≈0.3 SP flop/byte; achieved ≈6% of Xeon FP peak and ≈2.7% of C2070 peak, with memory bandwidth as the binding limit. ASKAP pipeline capacity estimates (820–3404 nodes, 76–319 DP Tflop/s peak) are derived from measured throughput, not end-to-end runtimes. IDG (2018) adds visibility/s throughput and notes GPU kernel launch overhead (17,417 launches for 160,000 samples). W-projection (2008) documents kernel memory (512×512 complex w-plane kernels at 2 MB) and hardware (dual 3.06 GHz Xeon, 3 GB RAM).

### CPU/GPU core-hours and memory on HPC (emerging-ml)

ASKAP validation papers quantify **CPU core-hours**, **GPU-hours**, and **memory** on Cirrus UK Tier-2. uSARA (2023): operator precomputation 281 CPU-h, deconvolution 770 CPU-h (4.3 h wall) on 467 M visibilities; holographic encoding cuts normal-operator storage to 80 GB (≈5× vs de-gridding matrices; WSClean same field 58 CPU-h. AIRI (2023): 45–203 CPU-h and 1.1–2.9 h wall per sub-band/full-band; DNN backward step 10–30× faster than uSARA denoiser. ESO 137-006 (2022): operator construction 427–652 CPU-h; imaging 480–2377 CPU-h (uSARA) vs 112–236 CPU-h (WSClean) plus 5–6 GPU-h (AIRI); holographic matrices reduce storage 470→81 GB and 645→159 GB. Distributed measurement model (2026): holographic **H** matrix ≈7× memory reduction vs explicit **G** at ≈30% higher precomputation cost; fewer w-layers (e.g. 23 vs WSClean's 126) as efficiency proxy.

### Training compute (ML methods)

Training dominates total cost for learned imagers. R2D2 ApJS (2024): R2D2 ≈160 GPU-h + 4757 CPU-h; R3D3 ≈1276–1291 GPU-h + 2165–2244 CPU-h on Cirrus V100 nodes. Radionets (2022): ≈170 s/epoch, ≈14 h for 300 epochs on RTX 2080. POLISH (2022): ≈20 GPU-h/model, ≈300 GPU-h total on TITAN RTX. Robust R2D2 (2025): 231.6–420.9 GPU-h for series training; standalone U-Net/U-WDSR 85.6–165.7 GPU-h. NC-MRI R2D2 paper (2024): 48–315 h training depending on architecture and NUFFT backend. IRIS (2025): ≈0.72 A100 GPU-years for calibration/simulation testing; 250 posterior samples in ≈2.5 h on 10 V100s. ZINGULARITY/EHT (2025): ≈30 s/epoch on A100 for 600k samples; Horovod scaling to 128 GPUs.

### Inference vs precomputation trade-offs

Several papers treat **operator build cost** as amortizable: precomputation matched by application within "tens of iterations" and exceeded by ≈10× within a few hundred iterations (distributed measurement model). fast-resolve (2024): ≈2 CPU-h kernel precomputation plus ≈24 GPU-h for MeerKAT ESO 137-006 (≈400× larger than VLA case) vs 900–3000 CPU-h per band for prior convex/CLEAN-family work. R2D2 inference remains seconds on one GPU after training; AIRI PnP inference ≈616–4995 iterations at much higher per-step cost.

### Energy, carbon, and facility-scale modeling

Beyond astroCAMP, ngVLA review (2025) cites facility-scale needs (≈100 Tflop/s ALMA WSU, ≈50 Pflop/s ngVLA) with gridding as dominant cost. astroCAMP models location-dependent carbon (South Africa 0.672 vs Western Australia 0.321 kgCO₂/kWh) and scenario claims (up to 81% energy, 97% carbon reduction under improved-utilisation models—not measured optimisations). PREESM CPU/FPGA Pareto plots latency vs energy and occupancy without tabulated design points.

### Per-step and denoiser compute

AIRI variations (2025): GPU denoiser 0.05±0.02 s vs CPU 7.92±0.52 s vs SARA proximal 1.31±1.12 s vs BM3D 15.08±0.40 s per step (≈20× GPU speedup over SARA operators). S-R2D2 (2025): `t_tot = I×(t_reg + t_dat)` on Nvidia A40, ≈2–3 s total at I=10. QuantifAI (2024): MAP 0.64 s vs MCMC 6.44×10³ s vs fast pixel UQ 0.17 s on A100.

### Cohort tendencies

**Classic** papers emphasize gridding throughput, memory for convolution supports, and analytic operation-count ratios (2–3× multi-frequency synthesis vs Hogbom CLEAN; Asp ≈3× MS-Clean) with fewer absolute core-hour figures until astroCAMP. **Emerging-ml** introduces systematic CPU/GPU-hour accounting on HPC for uSARA/AIRI vs WSClean. **r2d2-citing** pairs low iteration-count GPU inference with large upfront training budgets and often reports parameter counts (millions) alongside GPU-hours.

## Popular measurement variants

- **CPU core-hours / GPU-hours**: total or split by precomputation, deconvolution, forward step, training (uSARA, AIRI, ESO 137-006, R2D2 training tables).
- **Energy-to-solution (`E_c`) and static vs dynamic energy**: integrated power over job duration; idle PDU fraction (astroCAMP).
- **Throughput**: Mpoints/s gridding (SKA-MEMO), visibilities/s (IDG, astroCAMP `Θ`), visibilities/J (`η_E`), visibilities/gCO₂e (`η_C`).
- **Peak and working memory**: operator storage GB (holographic vs de-gridding matrices), `M_peak`, output image GiB at 4096²–32768² scales, partition/chunk limits (HVOX 500 MB).
- **Memory bandwidth and arithmetic intensity**: GB/s sustained, flop/byte, % of roofline peak (SKA-MEMO, astroCAMP roofline).
- **Device utilisation (`U`)**: fraction of wall time with active kernels on CPU/GPU/FPGA (astroCAMP).
- **Training cost**: GPU-h, CPU-h, hours per epoch, total over dataset (R2D2, Radionets, POLISH, IRIS GPU-years).
- **Precomputation vs iteration amortization**: one-off operator build vs per-iteration apply cost crossover (distributed measurement model).
- **Parameter count / model size**: millions of trainable parameters tied to memory and training time (NC-MRI Table II).
- **Relative compute ratios**: AIRI ≈4× uSARA deconvolution, ≈5× WSClean; uSARA ≈20× WSClean on ASKAP; R2D2 ≈4 orders of magnitude faster inference than AIRI (NC-MRI).
- **Facility-scale FLOP/s requirements**: Tflop/s to Pflop/s estimates for ALMA WSU, ngVLA, SKA real-time (extrapolated, not job measurements).
- **Carbon and cost proxies**: gCO₂e, €/job, TCO-scenario modeling (astroCAMP).
- **Analytic operation-count models**: CLEAN work ∝ iterations×pixels; Autocorr-CLEAN scaling m·N·(8l/k); MRC-to-CLEAN operation ratios ≈0.25–0.6.
- **Stage-level compute breakdown**: degridding, gridding, FFT dominance; I/O misalignment diagnostics (decentralized framework, distributed implementation).

## Gaps and caveats

- **Wall time ≠ core-hours**: papers mix single-node wall clock with multi-core-hour totals; AIRI and uSARA often use different node types, breaking hardware-matched comparisons.
- **Training excluded from inference comparisons** is standard but makes "compute cost" incomplete for ML methods; amortization assumptions vary.
- **Scope limits**: gridding-only benchmarks (SKA-MEMO, parts of IDG) omit deconvolution fidelity and end-to-end energy; astroCAMP co-design savings are modeled scenarios, not shipped optimisations.
- **Memory vs time trade-offs** (chunked HVOX, holographic operators, reduced-resolution inversion) change both metrics; papers do not always report paired fidelity at the cheaper setting.
- **Carbon/cost metrics** depend strongly on grid intensity, tariff, and capex assumptions (Western Australia vs South Africa in astroCAMP).
- **Utilisation and roofline claims** are diagnostic: low CPU utilisation with high gridding kernel scaling indicates pipeline orchestration bottlenecks, not necessarily fixable by faster kernels alone.
- **Classic papers** often lack any absolute compute measurement (1984 Clark enhancements, 1994 multi-frequency synthesis give ratios or operation models only).
- **Classification overlap with Runtime**: many r2d2 papers report both seconds and GPU-hours; compute column emphasizes resource accounting beyond elapsed time. Pure wall-clock labelled as “computational cost” is kept on Runtime and typed **Unspecified Compute** on the detail page rather than silently remapped.

## Second-level Compute page

The main metrics graph keeps a single binary **Compute** column. Drill-down lives at [`compute.html`](../compute.html) (linked as **Explore Compute Details** when Compute is selected on `index.html`).

Reporting categories (a paper may appear in more than one — category totals can exceed Compute-positive paper counts):

| Category | Sub-metrics |
|---|---|
| Resource Usage (Absolute) | cpu_gpu_hours, energy, peak_memory, flops, other_absolute |
| Efficiency / Intensity | energy_efficiency, performance_per_watt, memory_efficiency, other_efficiency |
| Relative Compute | resource_speedup, resource_reduction_pct, cost_ratio |
| Scaling / Complexity | problem_size_scaling, asymptotic_complexity, hardware_scaling |
| Unspecified Compute | unspecified (extraction limitation; not silently overclassified) |

**Compute Measurement Context** (separate panel): Hardware, Parallelism, Software, Numerical Configuration, Workload — reporting-completeness counts only. Context is not itself a Compute sub-metric.

Structured data: `compute_details` arrays on Compute-positive papers in `papers-data.json` (optional mirror `data/compute-details.json`). Taxonomy: `compute-taxonomy.js`. Injector: `scripts/inject_compute_details.py`.