#!/usr/bin/env python3
"""Inject class_details into data/papers-data.json for Class-positive papers.

Run from repo root: python3 scripts/inject_class_details.py
Does not change top-level metrics.classification_metrics flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "class-details.json"


def ctx(
    task=None,
    finder_method=None,
    operating_point=None,
    matching_criterion=None,
    simulation_vs_real=None,
    dataset_or_survey=None,
):
    return {
        "task": task,
        "finder_method": finder_method,
        "operating_point": operating_point,
        "matching_criterion": matching_criterion,
        "simulation_vs_real": simulation_vs_real,
        "dataset_or_survey": dataset_or_survey,
    }


def entry(
    category,
    submetric,
    *,
    value=None,
    unit=None,
    scope=None,
    baseline=None,
    empirical=True,
    execution_context=None,
    evidence=None,
):
    return {
        "category": category,
        "submetric": submetric,
        "value": value,
        "unit": unit,
        "scope": scope,
        "baseline": baseline,
        "empirical": empirical,
        "execution_context": execution_context or ctx(),
        "evidence": evidence,
    }


# bibcode -> list of class_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- emerging-ml ---
    "2022MNRAS.514.2614C": [
        entry(
            "catalog_rates",
            "false_positive_incidence",
            value=2,
            unit="% false-positive incidence (approx.)",
            scope="Source-Extractor false galaxies on simulated DSA-2000 skies (POLISH vs CLEAN)",
            baseline="CLEAN ≈5% (1 false per 20 galaxies)",
            empirical=True,
            execution_context=ctx(
                task="Source detection / false-galaxy incidence",
                finder_method="Source-Extractor",
                operating_point=None,
                matching_criterion="Approximate false galaxies per N simulated galaxies",
                simulation_vs_real="Simulation (DSA-2000)",
                dataset_or_survey="DSA-2000 simulated galaxies",
            ),
            evidence=(
                "Source-Extractor finds approximately one false-positive galaxy per 20 simulated "
                "galaxies in CLEAN and one per 50 in POLISH (≈5% vs ≈2% false-positive incidence). "
                "No underlying source counts, completeness, thresholds, or precision–recall curve."
            ),
        ),
    ],
    # --- r2d2-citing ---
    "2025A&A...698A..61J": [
        entry(
            "label_accuracy",
            "classification_accuracy",
            value=None,
            unit="fraction correct (qualitative: near-perfect)",
            scope="MAD/SANE magnetic-state classification on M87* fiducial model (ZINGULARITY)",
            empirical=True,
            execution_context=ctx(
                task="Discrete magnetic-state classification (MAD vs SANE)",
                finder_method="ZINGULARITY Bayesian DL inference",
                simulation_vs_real="Simulation / EHT inference (M87* fiducial)",
                dataset_or_survey="EHT M87*",
            ),
            evidence=(
                "Classification accuracy (correct predictions / total) for discrete MAD/SANE "
                "magnetic-state labels; reported as near-perfect for the M87* fiducial model."
            ),
        ),
    ],
    "2025MLS&T...6d5005Z": [
        entry(
            "label_accuracy",
            "classification_accuracy",
            value=None,
            unit=None,
            scope="Multimodal LLM radio-image understanding / classification tasks",
            empirical=True,
            execution_context=ctx(
                task="Multimodal LLM radio-image classification / VQA-style labels",
                finder_method="Multimodal large language models",
                simulation_vs_real=None,
                dataset_or_survey="Radio astronomical image understanding benchmark",
            ),
            evidence=(
                "Reports Accuracy among the classification-task metrics for multimodal LLM "
                "radio-image understanding."
            ),
        ),
        entry(
            "catalog_rates",
            "precision_recall_f1",
            value=None,
            unit=None,
            scope="Multimodal LLM classification tasks (Precision, Recall, F1)",
            empirical=True,
            execution_context=ctx(
                task="Multimodal LLM radio-image classification",
                finder_method="Multimodal large language models",
                dataset_or_survey="Radio astronomical image understanding benchmark",
            ),
            evidence=(
                "Classification-task suite includes Precision, Recall, and F1-score alongside "
                "accuracy and detection rates."
            ),
        ),
        entry(
            "operating_point",
            "tpr_at_fixed_fpr",
            value=None,
            unit=None,
            scope="Multimodal LLM tasks reporting TPR and FPR",
            empirical=True,
            execution_context=ctx(
                task="Multimodal LLM radio-image classification / detection",
                finder_method="Multimodal large language models",
                operating_point="TPR and FPR reported (operating point not fully specified in notes)",
                dataset_or_survey="Radio astronomical image understanding benchmark",
            ),
            evidence=(
                "True Positive Rate (TPR) and False Positive Rate (FPR) listed among "
                "classification-task metrics."
            ),
        ),
        entry(
            "catalog_rates",
            "missed_detection_counts",
            value=None,
            unit="counts",
            scope="Multimodal LLM missed-detection counts",
            empirical=True,
            execution_context=ctx(
                task="Multimodal LLM radio-image detection",
                finder_method="Multimodal large language models",
                dataset_or_survey="Radio astronomical image understanding benchmark",
            ),
            evidence="Missed-detection counts reported with the classification-task suite.",
        ),
    ],
    "2025MNRAS.542.2494M": [
        entry(
            "cited_benchmark",
            "cited_external_tpr_fpr",
            value=90,
            unit="% recovery (cited; at 0.008% FPR)",
            scope="Cited Rezaei et al. (2022) CNN lens finder on simulated ILT data",
            baseline=None,
            empirical=False,
            execution_context=ctx(
                task="Strong-lens finding (cited benchmark)",
                finder_method="CNN lens finder (Rezaei et al. 2022)",
                operating_point="0.008% FPR; 20σ detection; θE ≥ 3/2 beam size",
                matching_criterion="Galaxy-scale lens recovery on simulated ILT",
                simulation_vs_real="Simulation (ILT; cited)",
                dataset_or_survey="ILT simulations (Rezaei et al. 2022)",
            ),
            evidence=(
                "Cites Rezaei et al. (2022): >90% of galaxy-scale lenses recovered with a "
                "0.008% false-positive rate on simulated ILT data (20σ; θE ≥ 3/2 beam). "
                "Not an original measurement in this paper."
            ),
        ),
    ],
    "2026arXiv260309162W": [
        entry(
            "catalog_rates",
            "precision_recall_f1",
            value=0.7107,
            unit="F1 (POLISH++; Table 3 also lists P/R)",
            scope="SEP source detection on wide-field simulations (Table 3)",
            baseline="CLEAN 0.3612 / 0.2220 / 0.2750 (P/R/F1)",
            empirical=True,
            execution_context=ctx(
                task="Source detection catalog metrics",
                finder_method="SEP (Source Extraction and Photometry)",
                operating_point="Also tracked vs SNR threshold 3–300,000 (Fig. 4)",
                matching_criterion=(
                    "TP = ground-truth galaxy matched to a detection within a "
                    "size-dependent pixel threshold"
                ),
                simulation_vs_real="Simulation (wide-field / DSA-style)",
                dataset_or_survey="POLISH'ing the Sky wide-field simulations",
            ),
            evidence=(
                "Table 3 Precision/Recall/F1: CLEAN 0.3612/0.2220/0.2750; POLISH "
                "0.5560/0.4612/0.5042; POLISH+ 0.8744/0.5751/0.6938; POLISH++ "
                "0.8433/0.6142/0.7107. POLISH+/++ outperform CLEAN; largest gains at low SNR."
            ),
        ),
        entry(
            "catalog_rates",
            "shape_flux_rmse_on_tps",
            value=0.4654,
            unit="arcsec (θ_A RMSE, POLISH++; Table 3)",
            scope="SEP shape/flux RMSE on true-positive detections (Table 3; SNR>300 plots)",
            baseline="CLEAN θ_A 1.0046″ / θ_B 0.7862″ / flux 3.2625×10⁻⁴ Jy/px",
            empirical=True,
            execution_context=ctx(
                task="Shape & flux estimation on matched detections",
                finder_method="SEP parameter estimates on TPs",
                matching_criterion="True-positive subset from SEP matching",
                simulation_vs_real="Simulation",
                dataset_or_survey="POLISH'ing the Sky wide-field simulations",
            ),
            evidence=(
                "Table 3 TP RMSE: θ_A — CLEAN 1.0046″, POLISH++ 0.4654″; θ_B — CLEAN 0.7862″, "
                "POLISH++ 0.2056″; flux — CLEAN lowest (3.2625×10⁻⁴ Jy/px) vs POLISH++ "
                "3.1703×10⁻³ (CLEAN better absolute flux; learned methods super-resolve shapes)."
            ),
        ),
        entry(
            "operating_point",
            "tpr_at_fixed_fpr",
            value=None,
            unit="TPR vs Einstein radius at FPR=10⁻³",
            scope="CNN strong-lens finder per image type (Fig. 7)",
            baseline="CLEAN-trained finder; ~3×PSF-FWHM separation limit (Rezaei et al.)",
            empirical=True,
            execution_context=ctx(
                task="Strong-lens discovery",
                finder_method="CNN lens finder (Rezaei et al. 2022 architecture)",
                operating_point="FPR=10⁻³; TPR vs Einstein radius",
                matching_criterion="Lens finder trained/evaluated per reconstruction type",
                simulation_vs_real="Simulation",
                dataset_or_survey="DSA-discoverable galaxy–galaxy lenses (yield context)",
            ),
            evidence=(
                "TPR at fixed FPR=10⁻³ vs Einstein radius (Fig. 7). CLEAN-trained finder drops "
                "below ~3×PSF-FWHM separation; POLISH/++ recover near PSF FWHM (~10× estimated "
                "DSA lens-yield gain vs CLEAN). No absolute completeness/purity beyond the curve."
            ),
        ),
    ],
    "2026arXiv260628493D": [
        entry(
            "cited_benchmark",
            "cited_external_tpr_fpr",
            value=95.3,
            unit="% TPR (cited; at 0.008% FPR)",
            scope="Cited CNN lens/source-finding rates in SKA-era AI review",
            empirical=False,
            execution_context=ctx(
                task="CNN-based source / lens finding (cited)",
                finder_method="CNN source/lens finder (literature citation)",
                operating_point="0.008% FPR",
                simulation_vs_real=None,
                dataset_or_survey="SKA-era survey commentary (illustrative)",
            ),
            evidence=(
                "Cites 95.3% TPR at 0.008% FPR for CNN-based source (lens) finding as an "
                "illustrative classification-style metric in the broader pipeline — not an "
                "imaging-specific primary measurement in this review."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    class_papers = [p for p in papers if p["metrics"].get("classification_metrics") == 1]
    missing = [p["bibcode"] for p in class_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in class_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not classification_metrics=1: {extra}")

    for p in papers:
        p.pop("class_details", None)

    mirror = {
        "schema_note": (
            "class_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.classification_metrics binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in class_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["class_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "class_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in class_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["class_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected class_details for {len(class_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["classification_metrics"] == 1 for p in class_papers)
    assert sum(1 for p in papers if p["metrics"].get("classification_metrics") == 1) == 6
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
