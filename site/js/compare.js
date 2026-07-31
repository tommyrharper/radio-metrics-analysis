/**
 * Comparison mode: side-by-side structured details for selected papers.
 */
(function () {
  const store = window.ComparisonStore;
  const root = document.getElementById("compareRoot");

  const cohorts = {
    classic: { label: "Classic" },
    emerging: { label: "Emerging-ML" },
    "emerging-ml": { label: "Emerging-ML" },
    r2d2: { label: "R2D2-citing" },
    "r2d2-citing": { label: "R2D2-citing" },
  };

  function cohortClass(id) {
    if (id === "emerging-ml" || id === "emerging") return "emerging";
    if (id === "r2d2-citing" || id === "r2d2") return "r2d2";
    return "classic";
  }

  function formatValue(d) {
    if (d.value === null || d.value === undefined) return "—";
    const v = typeof d.value === "number" ? String(d.value) : d.value;
    return d.unit ? `${v} ${d.unit}` : v;
  }

  function contextSummary(ec, fields) {
    if (!ec || !fields) return "—";
    const parts = fields
      .map((f) => ec[f.id])
      .filter(Boolean)
      .map((s) => (s.length > 100 ? `${s.slice(0, 97)}…` : s));
    return parts.length ? parts.join(" · ") : "—";
  }

  function entryCard(d, taxonomy, contextFields) {
    const cat = taxonomy?.[d.category];
    const sub = cat?.submetrics?.[d.submetric];
    const card = document.createElement("div");
    card.className = "entry-card" + (d.category === "unspecified" ? " unspecified" : "");
    const tags = document.createElement("div");
    tags.className = "tags";
    const b1 = document.createElement("span");
    b1.className = "badge";
    b1.style.color = cat?.color || "#475569";
    b1.textContent = cat?.label || d.category;
    const b2 = document.createElement("span");
    b2.className = "badge";
    b2.style.color = cat?.color || "#475569";
    b2.textContent = sub?.label || d.submetric;
    tags.append(b1, b2);
    const kv = (label, val) => {
      const div = document.createElement("div");
      div.className = "kv";
      const strong = document.createElement("strong");
      strong.textContent = `${label}: `;
      div.append(strong, document.createTextNode(val));
      return div;
    };
    const ev = document.createElement("p");
    ev.className = "evidence";
    ev.textContent = d.evidence || "";
    card.append(
      tags,
      kv("Value", formatValue(d)),
      kv("Baseline", d.baseline || "—"),
      kv("Scope", d.scope || "—"),
      kv("Context", contextSummary(d.execution_context, contextFields)),
      ev
    );
    return card;
  }

  function paperColumn(paper, meta) {
    const col = document.createElement("div");
    col.className = "compare-col";
    const head = document.createElement("div");
    head.className = "compare-col-head";
    const cohort = document.createElement("div");
    cohort.className = "cohort";
    const sw = document.createElement("span");
    sw.className = `swatch ${cohortClass(paper.cohort)}`;
    cohort.append(sw, document.createTextNode((cohorts[paper.cohort] || {}).label || paper.cohort));
    const bib = document.createElement("div");
    bib.className = "bib";
    bib.textContent = paper.bibcode;
    const title = document.createElement("div");
    title.className = "title";
    title.textContent = paper.title;
    const link = document.createElement("a");
    link.href = `paper.html?bib=${encodeURIComponent(paper.bibcode)}`;
    link.textContent = "Paper details";
    head.append(cohort, bib, title, link);
    col.append(head);

    const flagged = paper.metrics && paper.metrics[meta.binaryKey] === 1;
    const entries = paper[meta.detailsKey] || [];
    const cards = document.createElement("div");
    cards.className = "entry-cards";
    if (!flagged) {
      const empty = document.createElement("p");
      empty.className = "entry-empty";
      empty.textContent = `Not flagged for ${meta.shortLabel}.`;
      cards.append(empty);
    } else if (!entries.length) {
      const empty = document.createElement("p");
      empty.className = "entry-empty";
      empty.textContent = "Flagged, but no structured subtype entries.";
      cards.append(empty);
    } else {
      const taxonomy = globalThis[meta.taxonomyGlobal];
      const contextFields = globalThis[meta.contextFieldsGlobal];
      entries.forEach((d) => cards.append(entryCard(d, taxonomy, contextFields)));
    }
    col.append(cards);
    return col;
  }

  function renderMetricSection(papers, meta) {
    const section = document.createElement("section");
    section.className = "compare-section";
    const h2 = document.createElement("h2");
    h2.textContent = meta.shortLabel;
    const full = document.createElement("p");
    full.className = "full-name";
    full.textContent = meta.fullName;
    const grid = document.createElement("div");
    grid.className = "compare-grid";
    papers.forEach((p) => grid.append(paperColumn(p, meta)));
    section.append(h2, full, grid);
    return section;
  }

  function showMessage(cls, text) {
    root.replaceChildren();
    const p = document.createElement("p");
    p.className = cls;
    p.textContent = text;
    root.append(p);
  }

  function render(allPapers) {
    const bibs = store.list();
    const papers = bibs
      .map((b) => allPapers.find((p) => p.bibcode === b))
      .filter(Boolean);

    root.replaceChildren();

    const h1 = document.createElement("h1");
    h1.textContent = "Compare papers";
    const lede = document.createElement("p");
    lede.className = "lede";

    const actions = document.createElement("div");
    actions.className = "actions-row";
    const back = document.createElement("a");
    back.href = "../index.html";
    back.className = "primary";
    back.textContent = "← Back to all metrics";
    const clear = document.createElement("button");
    clear.type = "button";
    clear.textContent = "Clear comparison";
    clear.addEventListener("click", () => {
      store.clear();
      location.href = "../index.html";
    });
    actions.append(back, clear);

    root.append(h1, lede, actions);

    if (papers.length < 2) {
      lede.textContent =
        papers.length === 0
          ? "No papers selected. Add papers with Compare on the main list, then return here."
          : "Add at least one more paper to compare. Use Compare on the main list or a paper page.";
      if (papers.length === 1) {
        const pills = document.createElement("div");
        pills.className = "paper-pills";
        pills.append(makePill(papers[0]));
        root.append(pills);
      }
      return;
    }

    lede.textContent = `Side-by-side structured metric details for ${papers.length} papers. Select a metric to focus, or All.`;

    const pills = document.createElement("div");
    pills.className = "paper-pills";
    papers.forEach((p) => pills.append(makePill(p)));
    root.append(pills);

    const unionKeys = new Set();
    papers.forEach((p) => {
      (window.METRIC_REGISTRY || []).forEach((m) => {
        if (p.metrics && p.metrics[m.binaryKey] === 1) unionKeys.add(m.binaryKey);
      });
    });
    const metrics = (window.METRIC_REGISTRY || []).filter((m) => unionKeys.has(m.binaryKey));

    let selectedMetric = null;
    const sectionsHost = document.createElement("div");
    const nav = document.createElement("nav");
    nav.className = "metric-nav";
    nav.setAttribute("aria-label", "Metrics to compare");

    function makeChip(label, key, count) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "metric-chip";
      btn.dataset.metric = key == null ? "" : key;
      btn.append(document.createTextNode(label));
      if (count != null) {
        const span = document.createElement("span");
        span.className = "n";
        span.textContent = `(${count})`;
        btn.append(span);
      }
      return btn;
    }

    nav.append(makeChip("All", "", null));
    metrics.forEach((m) => {
      const n = papers.filter((p) => p.metrics && p.metrics[m.binaryKey] === 1).length;
      nav.append(makeChip(m.shortLabel, m.binaryKey, n));
    });

    function apply() {
      nav.querySelectorAll(".metric-chip").forEach((btn) => {
        const key = btn.dataset.metric || "";
        const active = selectedMetric ? key === selectedMetric : key === "";
        btn.classList.toggle("active", active);
      });
      sectionsHost.replaceChildren();
      const show = selectedMetric
        ? metrics.filter((m) => m.binaryKey === selectedMetric)
        : metrics;
      if (!show.length) {
        const empty = document.createElement("p");
        empty.className = "empty-state";
        empty.textContent = "These papers share no flagged chart metrics.";
        sectionsHost.append(empty);
        return;
      }
      show.forEach((m) => sectionsHost.append(renderMetricSection(papers, m)));
    }

    nav.addEventListener("click", (evt) => {
      const btn = evt.target.closest(".metric-chip");
      if (!btn) return;
      const key = btn.dataset.metric || "";
      if (!key) selectedMetric = null;
      else if (selectedMetric === key) selectedMetric = null;
      else selectedMetric = key;
      apply();
    });

    root.append(nav, sectionsHost);
    apply();
  }

  function makePill(paper) {
    const pill = document.createElement("div");
    pill.className = "paper-pill";
    const sw = document.createElement("span");
    sw.className = `swatch ${cohortClass(paper.cohort)}`;
    const bib = document.createElement("span");
    bib.className = "bib";
    bib.textContent = paper.bibcode;
    const title = document.createElement("span");
    title.className = "title";
    title.textContent = paper.title;
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "remove";
    remove.setAttribute("aria-label", `Remove ${paper.bibcode}`);
    remove.textContent = "×";
    remove.addEventListener("click", () => {
      store.remove(paper.bibcode);
    });
    pill.append(sw, bib, title, remove);
    return pill;
  }

  if (!store) {
    showMessage("error", "Comparison store failed to load.");
    return;
  }

  showMessage("loading", "Loading comparison…");

  fetch("../data/papers-data.json")
    .then((r) => {
      if (!r.ok) throw new Error(`Failed to load papers-data.json (${r.status})`);
      return r.json();
    })
    .then((data) => {
      const papers = data.papers || data;
      render(papers);
      store.subscribe(() => render(papers));
      window.ComparisonBar.mount({ compareHref: "compare.html" });
    })
    .catch((err) => showMessage("error", err.message || String(err)));
})();
