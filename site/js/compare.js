/**
 * Comparison mode: overview (binary metrics) + detailed (structured subtypes).
 */
(function () {
  const store = window.ComparisonStore;
  const root = document.getElementById("compareRoot");
  const VIEW_KEY = "radio-metrics-compare-view";

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

  function loadView() {
    const q = new URLSearchParams(location.search).get("view");
    if (q === "overview" || q === "detailed") return q;
    try {
      const s = localStorage.getItem(VIEW_KEY);
      if (s === "overview" || s === "detailed") return s;
    } catch { /* ignore */ }
    return "overview";
  }

  function saveView(view) {
    try {
      localStorage.setItem(VIEW_KEY, view);
    } catch { /* ignore */ }
    const url = new URL(location.href);
    url.searchParams.set("view", view);
    history.replaceState(null, "", url);
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

  function paperTitle(paper, maxLen) {
    const t = (paper && paper.title) || paper.bibcode || "Untitled";
    if (!maxLen || t.length <= maxLen) return t;
    return `${t.slice(0, maxLen - 1).trim()}…`;
  }

  function categoryCounts(paper) {
    const cats = window.METRIC_CATEGORIES || {};
    const order = window.METRIC_CATEGORY_ORDER || [];
    const out = {};
    order.forEach((cid) => {
      const keys = (cats[cid] && cats[cid].metrics) || [];
      out[cid] = keys.filter((k) => paper.metrics && paper.metrics[k] === 1).length;
    });
    return out;
  }

  function flaggedMetrics(paper) {
    return (window.METRIC_REGISTRY || []).filter(
      (m) => paper.metrics && paper.metrics[m.binaryKey] === 1
    );
  }

  function headerCell(paper) {
    const th = document.createElement("th");
    th.title = `${paper.title || ""}\n${paper.bibcode || ""}`;
    const name = document.createElement("div");
    name.className = "th-title";
    name.textContent = paperTitle(paper, 48);
    th.append(name);
    return th;
  }

  function renderOverview(papers) {
    const wrap = document.createElement("div");
    wrap.className = "overview-wrap";

    const catOrder =
      (window.METRIC_CATEGORY_ORDER && window.METRIC_CATEGORY_ORDER.length
        ? window.METRIC_CATEGORY_ORDER
        : ["observational", "computational", "fidelity", "uncertainty", "scientific"]);
    const cats = window.METRIC_CATEGORIES || {};
    const registry = window.METRIC_REGISTRY || [];
    const toCategory = window.metricToCategory || {};

    // Category counts table
    const catSection = document.createElement("section");
    catSection.className = "compare-section";
    const catH = document.createElement("h2");
    catH.textContent = "Counts by category";
    const catNote = document.createElement("p");
    catNote.className = "full-name";
    catNote.textContent =
      "Number of high-level metrics each paper reports in each group (same taxonomy as the main chart).";
    catSection.append(catH, catNote);

    const catTable = document.createElement("table");
    catTable.className = "overview-table";
    const catHead = document.createElement("thead");
    const catHeadRow = document.createElement("tr");
    const th0 = document.createElement("th");
    th0.textContent = "Category";
    catHeadRow.append(th0);
    papers.forEach((p) => catHeadRow.append(headerCell(p)));
    catHead.append(catHeadRow);
    const catBody = document.createElement("tbody");

    catOrder.forEach((cid) => {
      const cat = cats[cid];
      if (!cat) return;
      const tr = document.createElement("tr");
      const label = document.createElement("th");
      label.scope = "row";
      const dot = document.createElement("span");
      dot.className = "cat-dot";
      dot.style.background = cat.color;
      label.append(dot, document.createTextNode(cat.label));
      tr.append(label);
      papers.forEach((p) => {
        const td = document.createElement("td");
        td.className = "count-cell";
        const n = categoryCounts(p)[cid] || 0;
        td.textContent = String(n);
        if (n > 0) td.classList.add("has-count");
        tr.append(td);
      });
      catBody.append(tr);
    });

    const totRow = document.createElement("tr");
    totRow.className = "total-row";
    const totLabel = document.createElement("th");
    totLabel.scope = "row";
    totLabel.textContent = "Total metrics";
    totRow.append(totLabel);
    papers.forEach((p) => {
      const td = document.createElement("td");
      td.className = "count-cell";
      td.textContent = String(flaggedMetrics(p).length);
      totRow.append(td);
    });
    catBody.append(totRow);
    catTable.append(catHead, catBody);
    catSection.append(catTable);
    wrap.append(catSection);

    // Presence matrix
    const matrixSection = document.createElement("section");
    matrixSection.className = "compare-section";
    const mH = document.createElement("h2");
    mH.textContent = "Which metrics each paper reports";
    const mNote = document.createElement("p");
    mNote.className = "full-name";
    mNote.textContent =
      "✓ = reported on the main chart · — = not reported. Grouped by category.";
    matrixSection.append(mH, mNote);

    const matrix = document.createElement("table");
    matrix.className = "overview-table presence-table";
    const mHead = document.createElement("thead");
    const mHeadRow = document.createElement("tr");
    const metricTh = document.createElement("th");
    metricTh.textContent = "Metric";
    mHeadRow.append(metricTh);
    papers.forEach((p) => mHeadRow.append(headerCell(p)));
    mHead.append(mHeadRow);
    const mBody = document.createElement("tbody");

    let rowsAdded = 0;
    catOrder.forEach((cid) => {
      const cat = cats[cid];
      if (!cat) return;
      const groupMetrics = registry.filter((m) => toCategory[m.binaryKey] === cid);
      const used = groupMetrics.filter((m) =>
        papers.some((p) => p.metrics && p.metrics[m.binaryKey] === 1)
      );
      if (!used.length) return;

      const groupRow = document.createElement("tr");
      groupRow.className = "group-row";
      const groupTh = document.createElement("th");
      groupTh.colSpan = papers.length + 1;
      const gDot = document.createElement("span");
      gDot.className = "cat-dot";
      gDot.style.background = cat.color;
      groupTh.append(gDot, document.createTextNode(`${cat.label} metrics`));
      groupRow.append(groupTh);
      mBody.append(groupRow);

      used.forEach((m) => {
        const tr = document.createElement("tr");
        const label = document.createElement("th");
        label.scope = "row";
        const short = document.createElement("div");
        short.className = "metric-short";
        short.textContent = m.shortLabel;
        const full = document.createElement("div");
        full.className = "metric-full";
        full.textContent = m.fullName;
        label.append(short, full);
        tr.append(label);
        papers.forEach((p) => {
          const td = document.createElement("td");
          const on = p.metrics && p.metrics[m.binaryKey] === 1;
          td.className = on ? "present" : "absent";
          td.textContent = on ? "✓" : "—";
          td.title = on
            ? `${p.title}: reports ${m.fullName}`
            : `${p.title}: does not report ${m.fullName}`;
          tr.append(td);
        });
        mBody.append(tr);
        rowsAdded += 1;
      });
    });

    if (!rowsAdded) {
      const empty = document.createElement("tr");
      const td = document.createElement("td");
      td.colSpan = papers.length + 1;
      td.className = "entry-empty";
      td.textContent = "No flagged metrics among these papers.";
      empty.append(td);
      mBody.append(empty);
    }

    matrix.append(mHead, mBody);
    matrixSection.append(matrix);
    wrap.append(matrixSection);
    return wrap;
  }

  function renderDetailed(papers) {
    const wrap = document.createElement("div");
    wrap.className = "detailed-wrap";

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

    wrap.append(nav, sectionsHost);
    apply();
    return wrap;
  }

  function showMessage(cls, text) {
    root.replaceChildren();
    const p = document.createElement("p");
    p.className = cls;
    p.textContent = text;
    root.append(p);
  }

  function makePill(paper) {
    const pill = document.createElement("div");
    pill.className = "paper-pill";
    const sw = document.createElement("span");
    sw.className = `swatch ${cohortClass(paper.cohort)}`;
    const title = document.createElement("span");
    title.className = "title";
    title.textContent = paperTitle(paper, 56);
    title.title = paper.bibcode || "";
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "remove";
    remove.setAttribute("aria-label", `Remove ${paper.title || paper.bibcode}`);
    remove.textContent = "×";
    remove.addEventListener("click", () => {
      store.remove(paper.bibcode);
    });
    pill.append(sw, title, remove);
    return pill;
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

    const pills = document.createElement("div");
    pills.className = "paper-pills";
    papers.forEach((p) => pills.append(makePill(p)));
    root.append(pills);

    let view = loadView();
    const viewToggle = document.createElement("div");
    viewToggle.className = "view-toggle";
    viewToggle.setAttribute("role", "tablist");
    viewToggle.setAttribute("aria-label", "Comparison view");

    const overviewBtn = document.createElement("button");
    overviewBtn.type = "button";
    overviewBtn.className = "view-btn";
    overviewBtn.textContent = "Overview";
    overviewBtn.setAttribute("role", "tab");

    const detailedBtn = document.createElement("button");
    detailedBtn.type = "button";
    detailedBtn.className = "view-btn";
    detailedBtn.textContent = "Detailed";
    detailedBtn.setAttribute("role", "tab");

    viewToggle.append(overviewBtn, detailedBtn);
    root.append(viewToggle);

    const body = document.createElement("div");
    body.className = "compare-body";
    root.append(body);

    function paint() {
      overviewBtn.classList.toggle("active", view === "overview");
      detailedBtn.classList.toggle("active", view === "detailed");
      overviewBtn.setAttribute("aria-selected", String(view === "overview"));
      detailedBtn.setAttribute("aria-selected", String(view === "detailed"));
      lede.textContent =
        view === "overview"
          ? `High-level metric coverage for ${papers.length} papers — category counts and which metrics each paper reports.`
          : `Side-by-side structured metric details for ${papers.length} papers. Select a metric to focus, or All.`;
      body.replaceChildren(
        view === "overview" ? renderOverview(papers) : renderDetailed(papers)
      );
      saveView(view);
    }

    overviewBtn.addEventListener("click", () => {
      view = "overview";
      paint();
    });
    detailedBtn.addEventListener("click", () => {
      view = "detailed";
      paint();
    });

    paint();
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
