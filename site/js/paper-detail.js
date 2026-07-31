/**
 * Paper-centric detail page: all structured *_details for one paper.
 * Expects METRIC_REGISTRY + all taxonomy globals loaded; URL ?bib=<bibcode>.
 */
(function () {
  const cohorts = {
    classic: { label: "Classic" },
    emerging: { label: "Emerging-ML" },
    "emerging-ml": { label: "Emerging-ML" },
    r2d2: { label: "R2D2-citing" },
    "r2d2-citing": { label: "R2D2-citing" },
  };

  const params = new URLSearchParams(window.location.search);
  const bibParam = params.get("bib") || params.get("bibcode") || "";
  const root = document.getElementById("paperRoot");

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
      .map((s) => (s.length > 120 ? `${s.slice(0, 117)}…` : s));
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

  function renderMetricSection(paper, meta) {
    const taxonomy = globalThis[meta.taxonomyGlobal];
    const contextFields = globalThis[meta.contextFieldsGlobal];
    const entries = paper[meta.detailsKey] || [];
    const notes = (paper.metric_details && paper.metric_details[meta.binaryKey]) || [];

    const panel = document.createElement("section");
    panel.className = "panel";
    panel.id = meta.binaryKey;

    const h2 = document.createElement("h2");
    h2.textContent = meta.shortLabel;
    const full = document.createElement("p");
    full.className = "full-name";
    full.textContent = meta.fullName;

    const links = document.createElement("p");
    links.className = "metric-links";
    const corp = document.createElement("a");
    corp.href = `detail/${meta.detailPage}`;
    corp.textContent = `Explore ${meta.shortLabel} Details (all papers)`;
    links.append(corp);

    panel.append(h2, full, links);

    if (notes.length) {
      const box = document.createElement("div");
      box.className = "notes";
      const nh = document.createElement("h3");
      nh.textContent = "How this paper uses " + meta.shortLabel;
      const ul = document.createElement("ul");
      notes.forEach((note) => {
        const li = document.createElement("li");
        li.textContent = note;
        ul.append(li);
      });
      box.append(nh, ul);
      panel.append(box);
    }

    const cards = document.createElement("div");
    cards.className = "entry-cards";
    if (entries.length) {
      entries.forEach((d) => cards.append(entryCard(d, taxonomy, contextFields)));
    } else {
      const empty = document.createElement("p");
      empty.className = "entry-empty";
      empty.textContent = notes.length
        ? "Flagged on the main graph; no structured subtype entries yet."
        : `${meta.shortLabel}-positive, but no structured subtype entries.`;
      cards.append(empty);
    }
    panel.append(cards);
    return panel;
  }

  function renderPaper(paper) {
    root.replaceChildren();

    const header = document.createElement("header");
    header.className = "paper-header";

    const tag = document.createElement("div");
    tag.className = "cohort-tag";
    const sw = document.createElement("span");
    sw.className = `swatch ${cohortClass(paper.cohort)}`;
    sw.setAttribute("aria-hidden", "true");
    tag.append(sw, document.createTextNode((cohorts[paper.cohort] || {}).label || paper.cohort));

    const bib = document.createElement("p");
    bib.className = "bib";
    bib.textContent = paper.bibcode;

    const h1 = document.createElement("h1");
    h1.textContent = paper.title;

    const actions = document.createElement("div");
    actions.className = "actions";
    if (paper.url) {
      const open = document.createElement("a");
      open.href = paper.url;
      open.target = "_blank";
      open.rel = "noopener noreferrer";
      open.textContent = "Open paper webpage";
      actions.append(open);
    }
    const back = document.createElement("a");
    back.href = "../index.html";
    back.className = "primary";
    back.textContent = "← Back to all metrics";
    actions.append(back);

    const used = (globalThis.METRIC_REGISTRY || []).filter(
      (m) => paper.metrics && paper.metrics[m.binaryKey] === 1
    );

    const lede = document.createElement("p");
    lede.className = "lede";
    if (!used.length) {
      lede.textContent = "No canonical metrics are flagged for this paper.";
    } else {
      const withDetails = used.filter((m) => (paper[m.detailsKey] || []).length).length;
      lede.textContent =
        `${used.length} metric${used.length === 1 ? "" : "s"} flagged` +
        (withDetails
          ? ` · ${withDetails} with structured subtype detail below.`
          : " · no structured subtype entries yet (overview notes shown when available).");
    }

    header.append(tag, bib, h1, actions, lede);
    root.append(header);

    if (used.length) {
      const nav = document.createElement("nav");
      nav.className = "metric-nav";
      nav.setAttribute("aria-label", "Metrics used by this paper");
      used.forEach((m) => {
        const a = document.createElement("a");
        a.href = `#${m.binaryKey}`;
        const n = (paper[m.detailsKey] || []).length;
        a.append(document.createTextNode(m.shortLabel));
        if (n) {
          const span = document.createElement("span");
          span.className = "n";
          span.textContent = `(${n})`;
          a.append(span);
        }
        nav.append(a);
      });
      root.append(nav);

      used.forEach((m) => root.append(renderMetricSection(paper, m)));
    }

    document.title = `${paper.bibcode} — paper metric details`;
  }

  function showError(msg) {
    root.replaceChildren();
    const p = document.createElement("p");
    p.className = "error";
    p.textContent = msg;
    root.append(p);
  }

  if (!bibParam) {
    showError("Missing paper id. Open this page from the main metrics list (Explore Paper Details).");
    return;
  }

  root.innerHTML = `<p class="loading">Loading paper…</p>`;

  fetch("../data/papers-data.json")
    .then((r) => {
      if (!r.ok) throw new Error(`Failed to load papers-data.json (${r.status})`);
      return r.json();
    })
    .then((data) => {
      const papers = data.papers || data;
      const want = decodeURIComponent(bibParam);
      const paper = papers.find((p) => p.bibcode === want);
      if (!paper) {
        showError(`Paper not found: ${want}`);
        return;
      }
      renderPaper(paper);
      if (location.hash) {
        const el = document.querySelector(location.hash);
        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    })
    .catch((err) => showError(err.message || String(err)));
})();
