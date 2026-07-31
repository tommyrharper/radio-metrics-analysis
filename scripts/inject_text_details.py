#!/usr/bin/env python3
"""Inject text_details into data/papers-data.json for Text-positive papers.

Run from repo root: python3 scripts/inject_text_details.py
Does not change top-level metrics.text_metrics flags.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DATA = ROOT / "data" / "papers-data.json"
MIRROR = ROOT / "data" / "text-details.json"


def ctx(
    task=None,
    dataset=None,
    models=None,
    reference_type=None,
    domain=None,
):
    return {
        "task": task,
        "dataset": dataset,
        "models": models,
        "reference_type": reference_type,
        "domain": domain,
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


_RADIOASTRO_CTX = ctx(
    task="VQA / free-text (RadioAstroVQA)",
    dataset="RadioAstroVQA (FAST, HTRU Medlat, Spectrumcls, Radio Galaxy)",
    models="DeepSeek-VL-7B, InternVL2-40B (LoRA fine-tuned); vs ML/DL and general MLLM baselines",
    reference_type="Reference answers in VQA-format examples",
    domain="Radio astronomical image understanding / question answering",
)

# bibcode -> list of text_details entries
CLASSIFICATIONS: dict[str, list[dict]] = {
    # --- r2d2-citing ---
    "2025MLS&T...6d5005Z": [
        entry(
            "semantic_similarity",
            "bleu",
            value=None,
            unit=None,
            scope="Open-ended VQA / free-text tasks on RadioAstroVQA",
            empirical=True,
            execution_context=_RADIOASTRO_CTX,
            evidence=(
                "VQA / free-text tasks report BLEU as a semantic-similarity score between "
                "generated and reference answers. Classification metrics on discrete tasks "
                "are scored under Class, not Text."
            ),
        ),
        entry(
            "semantic_similarity",
            "rouge",
            value=None,
            unit=None,
            scope="Open-ended VQA / free-text tasks on RadioAstroVQA",
            empirical=True,
            execution_context=_RADIOASTRO_CTX,
            evidence=(
                "VQA / free-text tasks report ROUGE as a recall-oriented n-gram / sequence "
                "overlap score between generated and reference answers."
            ),
        ),
        entry(
            "semantic_similarity",
            "chrf",
            value=None,
            unit=None,
            scope="Open-ended VQA / free-text tasks on RadioAstroVQA",
            empirical=True,
            execution_context=_RADIOASTRO_CTX,
            evidence=(
                "VQA / free-text tasks report chrF (character n-gram F-score) as a "
                "semantic-similarity score between generated and reference answers."
            ),
        ),
    ],
}


def main():
    data = json.loads(PAPERS_DATA.read_text())
    papers = data["papers"]
    text_papers = [p for p in papers if p["metrics"].get("text_metrics") == 1]
    missing = [p["bibcode"] for p in text_papers if p["bibcode"] not in CLASSIFICATIONS]
    extra = sorted(set(CLASSIFICATIONS) - {p["bibcode"] for p in text_papers})
    if missing:
        raise SystemExit(f"Missing classifications for: {missing}")
    if extra:
        raise SystemExit(f"Extra classifications not text_metrics=1: {extra}")

    for p in papers:
        p.pop("text_details", None)

    mirror = {
        "schema_note": (
            "text_details live primarily on each paper in papers-data.json. "
            "This mirror is bibcode -> entries for inspection/tools. "
            "Top-level metrics.text_metrics binary flags are unchanged."
        ),
        "papers": {},
    }

    for p in text_papers:
        details = CLASSIFICATIONS[p["bibcode"]]
        p["text_details"] = details
        mirror["papers"][p["bibcode"]] = {
            "cohort": p["cohort"],
            "title": p["title"],
            "text_details": details,
        }

    PAPERS_DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(mirror, indent=2, ensure_ascii=False) + "\n")

    from collections import defaultdict

    cat_papers = defaultdict(set)
    sub_papers = defaultdict(set)
    for p in text_papers:
        seen_cats = set()
        seen_subs = set()
        for d in p["text_details"]:
            seen_cats.add(d["category"])
            seen_subs.add((d["category"], d["submetric"]))
        for c in seen_cats:
            cat_papers[c].add(p["bibcode"])
        for s in seen_subs:
            sub_papers[s].add(p["bibcode"])

    print(f"Injected text_details for {len(text_papers)} papers.")
    print("Unique papers per category:")
    for c, bibs in sorted(cat_papers.items(), key=lambda x: -len(x[1])):
        print(f"  {c}: {len(bibs)} — {', '.join(sorted(bibs))}")
    print("Unique papers per submetric:")
    for s, bibs in sorted(sub_papers.items(), key=lambda x: (-len(x[1]), x[0])):
        print(f"  {s[0]}/{s[1]}: {len(bibs)} — {', '.join(sorted(bibs))}")
    unspecified = sorted(cat_papers.get("unspecified", []))
    print(f"Unspecified ({len(unspecified)}): {unspecified}")

    assert all(p["metrics"]["text_metrics"] == 1 for p in text_papers)
    assert sum(1 for p in papers if p["metrics"].get("text_metrics") == 1) == 1
    print(f"Wrote {PAPERS_DATA.relative_to(ROOT)} and {MIRROR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
