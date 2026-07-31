(() => {
    const cfg = window.METRIC_DETAIL;
    if (!cfg) {
      throw new Error("METRIC_DETAIL config missing — load *-taxonomy.js and set METRIC_DETAIL before metric-detail.js");
    }
    const TAXONOMY = cfg.taxonomy;
    const CATEGORY_ORDER = cfg.categoryOrder;
    const CONTEXT_FIELDS = cfg.contextFields;
    const BINARY_KEY = cfg.binaryKey;
    const DETAILS_KEY = cfg.detailsKey;

    // Fill static copy slots from config
    document.title = cfg.documentTitle;
    const setText = (id, text) => {
      const el = document.getElementById(id);
      if (el && text != null) el.textContent = text;
    };
    const setHtml = (id, html) => {
      const el = document.getElementById(id);
      if (el && html != null) el.innerHTML = html;
    };
    setText("pageHeading", cfg.pageHeading);
    setHtml("pageLede", cfg.ledeHtml);
    setText("pageMultiNote", cfg.multiNote);
    setText("categoryFiltersLabel", cfg.categoryFilterLabel);
    setText("categoryFiltersHidden", cfg.categoryFilterLabel);
    setText("chartHint", cfg.chartHint);
    setText("contextHeading", cfg.contextTitle);
    setHtml("contextNote", cfg.contextNoteHtml);
    const canvas = document.getElementById("detailChart");
    if (canvas && cfg.chartAriaLabel) canvas.setAttribute("aria-label", cfg.chartAriaLabel);
    const legend = document.getElementById("categoryLegend");
    if (legend) legend.setAttribute("aria-label", `${cfg.shortLabel} category legend`);

    const cohorts = {
      classic: { label: "Classic", color: "#0b6e6a" },
      emerging: { label: "Emerging-ML", color: "#c45c26" },
      r2d2: { label: "R2D2-citing", color: "#1f4e79" },
    };

    const toggles = {
      classic: document.getElementById("toggle-classic"),
      emerging: document.getElementById("toggle-emerging"),
      r2d2: document.getElementById("toggle-r2d2"),
    };
    const categorySelect = document.getElementById("categorySelect");
    const categoryLegendEl = document.getElementById("categoryLegend");
    const emptyState = document.getElementById("emptyState");
    const detail = document.getElementById("detail");
    const detailTitle = document.getElementById("detailTitle");
    const detailCount = document.getElementById("detailCount");
    const paperList = document.getElementById("paperList");
    const paperSearch = document.getElementById("paperSearch");
    const paperSearchWrap = document.getElementById("paperSearchWrap");
    const metricSummary = document.getElementById("metricSummary");
    const metricVariants = document.getElementById("metricVariants");
    const contextGrid = document.getElementById("contextGrid");

    let papers = [];
    let listedPapers = [];
    let selectedSubmetric = null; // {category, submetric} or null
    let currentOrder = [];
    let variantsOpen = false;
    let variantsView = "overview";

    function buildCategoryControls() {
      const allOpt = document.createElement("option");
      allOpt.value = "all";
      allOpt.textContent = cfg.allCategoriesLabel;
      categorySelect.append(allOpt);

      CATEGORY_ORDER.forEach((cid) => {
        const cat = TAXONOMY[cid];
        const opt = document.createElement("option");
        opt.value = cid;
        opt.textContent = cat.label;
        categorySelect.append(opt);

        const leg = document.createElement("span");
        leg.className = "leg-item";
        const sw = document.createElement("span");
        sw.className = "cat-swatch";
        sw.style.background = cat.color;
        sw.style.borderColor = cat.color;
        sw.style.borderStyle = cat.borderStyle || "solid";
        if (cat.distinct) {
          sw.style.backgroundImage =
            "repeating-linear-gradient(-45deg, transparent, transparent 2px, rgba(255,255,255,0.35) 2px, rgba(255,255,255,0.35) 4px)";
        }
        sw.setAttribute("aria-hidden", "true");
        leg.append(sw, document.createTextNode(` ${cat.label}`));
        categoryLegendEl.append(leg);
      });
      categorySelect.value = "all";
    }

    buildCategoryControls();

    function activeCohortKeys() {
      return Object.keys(toggles).filter((k) => toggles[k].checked);
    }

    function activeCategories() {
      const v = categorySelect.value;
      if (v === "all") return CATEGORY_ORDER.slice();
      return CATEGORY_ORDER.includes(v) ? [v] : [];
    }

    function sameSubmetric(a, b) {
      return a && b && a.category === b.category && a.submetric === b.submetric;
    }

    function orderIncludes(sel) {
      return currentOrder.some((row) => sameSubmetric(row, sel));
    }

    function drPapers() {
      const active = new Set(activeCohortKeys());
      return papers
        .filter((p) => p.metrics && p.metrics[BINARY_KEY] === 1 && active.has(p.cohort))
        .sort((a, b) => (a.bibcode < b.bibcode ? 1 : a.bibcode > b.bibcode ? -1 : 0));
    }

    function submetricLabel(category, submetric) {
      const cat = TAXONOMY[category];
      const sub = cat?.submetrics?.[submetric];
      return sub?.label || submetric;
    }

    function submetricShort(category, submetric) {
      const cat = TAXONOMY[category];
      const sub = cat?.submetrics?.[submetric];
      return sub?.short || sub?.label || submetric;
    }

    function submetricDescription(category, submetric) {
      const cat = TAXONOMY[category];
      const sub = cat?.submetrics?.[submetric];
      return sub?.description || cat?.note || "No definition available for this sub-metric.";
    }

    function submetricCountsByCohort() {
      const cats = new Set(activeCategories());
      const map = new Map();
      drPapers().forEach((p) => {
        const seen = new Set();
        (p[DETAILS_KEY] || []).forEach((d) => {
          if (!cats.has(d.category)) return;
          const key = `${d.category}::${d.submetric}`;
          if (seen.has(key)) return;
          seen.add(key);
          if (!map.has(key)) {
            map.set(key, {
              category: d.category,
              submetric: d.submetric,
              byCohort: { classic: 0, emerging: 0, r2d2: 0 },
            });
          }
          map.get(key).byCohort[p.cohort] += 1;
        });
      });
      return map;
    }

    function orderedSubmetrics() {
      const counts = submetricCountsByCohort();
      const keys = activeCohortKeys();
      return [...counts.values()]
        .map((row) => ({
          category: row.category,
          submetric: row.submetric,
          total: keys.reduce((s, k) => s + (row.byCohort[k] || 0), 0),
        }))
        .filter((x) => x.total > 0)
        .sort(
          (a, b) =>
            b.total - a.total ||
            CATEGORY_ORDER.indexOf(a.category) - CATEGORY_ORDER.indexOf(b.category) ||
            a.submetric.localeCompare(b.submetric)
        )
        .map(({ category, submetric }) => ({ category, submetric }));
    }

    function chartData() {
      currentOrder = orderedSubmetrics();
      const counts = submetricCountsByCohort();
      const keys = activeCohortKeys();
      return {
        labels: currentOrder.map((row) => submetricLabel(row.category, row.submetric)),
        datasets: keys.map((k) => ({
          label: cohorts[k].label,
          data: currentOrder.map((row) => {
            const entry = counts.get(`${row.category}::${row.submetric}`);
            return entry ? entry.byCohort[k] : 0;
          }),
          backgroundColor: cohorts[k].color,
          borderWidth: 0,
          barPercentage: 0.72,
          categoryPercentage: 0.85,
        })),
      };
    }

    function matchingEntries(p, sel) {
      const focus = sel === undefined ? selectedSubmetric : sel;
      return (p[DETAILS_KEY] || []).filter((d) => {
        if (focus) {
          return d.category === focus.category && d.submetric === focus.submetric;
        }
        return true;
      });
    }

    function papersForSubmetric(sel) {
      return drPapers().filter((p) => matchingEntries(p, sel).length > 0);
    }

    function searchQuery() {
      return (paperSearch.value || "").trim().toLowerCase();
    }

    function paperMatchesSearch(p, q) {
      if (!q) return true;
      const bits = [
        p.bibcode,
        p.title,
        cohorts[p.cohort]?.label,
        p.cohort,
        ...matchingEntries(p).flatMap((d) => [
          d.category,
          d.submetric,
          d.scope,
          d.evidence,
          TAXONOMY[d.category]?.label,
          TAXONOMY[d.category]?.submetrics?.[d.submetric]?.label,
        ]),
      ];
      return bits.filter(Boolean).join(" ").toLowerCase().includes(q);
    }

    function formatValue(d) {
      if (d.value === null || d.value === undefined) return "—";
      const v = typeof d.value === "number" ? String(d.value) : d.value;
      return d.unit ? `${v} ${d.unit}` : v;
    }

    function contextSummary(ec) {
      if (!ec) return "—";
      const parts = CONTEXT_FIELDS.map((f) => ec[f.id])
        .filter(Boolean)
        .map((s) => (s.length > 90 ? `${s.slice(0, 87)}…` : s));
      return parts.length ? parts.join(" · ") : "—";
    }

    function entryCard(d) {
      const cat = TAXONOMY[d.category];
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
        kv("Context", contextSummary(d.execution_context)),
        ev
      );
      return card;
    }

    function createPaperItem(p) {
      const li = document.createElement("li");
      const row = document.createElement("div");
      row.className = "paper-row";

      const tag = document.createElement("div");
      tag.className = "cohort-tag";
      tag.innerHTML = `<span class="swatch ${p.cohort}" aria-hidden="true"></span>${cohorts[p.cohort].label}`;

      const main = document.createElement("button");
      main.type = "button";
      main.className = "paper-main";
      main.setAttribute("aria-expanded", "false");
      const meta = document.createElement("div");
      meta.className = "paper-meta";
      meta.innerHTML = `<div class="bib"></div><div class="title"></div>`;
      meta.querySelector(".bib").textContent = p.bibcode;
      meta.querySelector(".title").textContent = p.title;
      main.append(meta);

      const open = document.createElement("a");
      open.className = "open-link";
      open.href = p.url;
      open.target = "_blank";
      open.rel = "noopener noreferrer";
      open.textContent = "Open";
      open.title = "Open paper webpage";

      const paperDetails = document.createElement("a");
      paperDetails.className = "open-link";
      paperDetails.href = `../paper.html?bib=${encodeURIComponent(p.bibcode)}`;
      paperDetails.textContent = "Paper";
      paperDetails.title = "All structured metric details for this paper";

      const actions = document.createElement("div");
      actions.style.display = "flex";
      actions.style.flexDirection = "column";
      actions.style.gap = "0.35rem";
      actions.style.alignSelf = "center";
      actions.append(paperDetails, open);

      const entriesWrap = document.createElement("div");
      entriesWrap.className = "paper-entries";
      const cards = document.createElement("div");
      cards.className = "entry-cards";
      const entries = matchingEntries(p);
      if (entries.length) {
        entries.forEach((d) => cards.append(entryCard(d)));
      } else {
        const empty = document.createElement("p");
        empty.className = "entry-empty";
        empty.textContent = `${cfg.shortLabel}-positive, but no structured subtype entries.`;
        cards.append(empty);
      }
      entriesWrap.append(cards);

      main.addEventListener("click", () => {
        const isOpen = li.classList.toggle("open");
        main.setAttribute("aria-expanded", String(isOpen));
      });

      row.append(tag, main, actions);
      li.append(row, entriesWrap);
      return li;
    }

    function renderPaperList() {
      const q = searchQuery();
      const matches = listedPapers.filter((p) => paperMatchesSearch(p, q));
      const total = listedPapers.length;
      if (selectedSubmetric === null) {
        detailCount.textContent = q
          ? `${matches.length} of ${total} paper${total === 1 ? "" : "s"} in visible cohorts`
          : `${total} paper${total === 1 ? "" : "s"} in visible cohorts`;
      } else {
        detailCount.textContent = q
          ? `${matches.length} of ${total} matching paper${total === 1 ? "" : "s"}`
          : `${total} paper${total === 1 ? "" : "s"} in visible cohorts`;
      }
      if (!matches.length) {
        const empty = document.createElement("li");
        empty.style.padding = "0.55rem 0.15rem";
        empty.style.color = "var(--muted)";
        empty.textContent = q
          ? "No papers match this search."
          : selectedSubmetric
            ? "No papers for this sub-metric in the visible cohorts."
            : `No ${cfg.shortLabel}-positive papers in the visible cohorts.`;
        paperList.replaceChildren(empty);
        return;
      }
      paperList.replaceChildren(...matches.map(createPaperItem));
    }

    function setDetailTitle(sel) {
      detailTitle.replaceChildren();
      if (!sel) {
        detailTitle.textContent = "All papers";
        return;
      }
      const cat = TAXONOMY[sel.category];
      const main = document.createElement("span");
      main.className = "title-main";
      main.textContent = submetricShort(sel.category, sel.submetric);
      const full = document.createElement("span");
      full.className = "title-full";
      full.textContent = `(${submetricLabel(sel.category, sel.submetric)})`;
      const tag = document.createElement("span");
      tag.className = "title-cat-tag";
      tag.style.color = cat?.color || "#475569";
      tag.style.borderColor = cat?.color || "#475569";
      tag.style.borderStyle = cat?.borderStyle || "solid";
      tag.textContent = cat?.label || sel.category;
      detailTitle.append(main, full, tag);
    }

    function setMetricSummary(sel) {
      metricSummary.textContent = submetricDescription(sel.category, sel.submetric);
      metricSummary.classList.add("open");
    }

    function evidenceLine(d) {
      const parts = [];
      if (d.evidence) parts.push(d.evidence);
      const val = formatValue(d);
      if (val !== "—") parts.push(`Value: ${val}`);
      if (d.baseline) parts.push(`Baseline: ${d.baseline}`);
      if (d.scope) parts.push(`Scope: ${d.scope}`);
      return parts.join(" · ") || "Classified under this sub-metric, but no evidence text was stored.";
    }

    function buildPapersPane(sel) {
      const variants = papersForSubmetric(sel).map((p) => ({
        paper: p,
        ways: matchingEntries(p, sel).map(evidenceLine),
      }));
      const list = document.createElement("ul");
      list.className = "def-variants";

      if (!variants.length) {
        const empty = document.createElement("li");
        empty.textContent = "No papers in the visible cohorts use this sub-metric.";
        list.append(empty);
        return list;
      }

      variants.forEach(({ paper, ways }) => {
        const li = document.createElement("li");
        const bib = document.createElement("div");
        bib.className = "def-bib";
        bib.textContent = `${paper.bibcode} · ${cohorts[paper.cohort].label}`;
        const title = document.createElement("div");
        title.className = "def-paper-title";
        title.textContent = paper.title;
        li.append(bib, title);

        const waysList = document.createElement("ul");
        waysList.className = "def-ways";
        ways.forEach((text) => {
          const item = document.createElement("li");
          const preview = text.length > 220 ? `${text.slice(0, 217)}…` : text;
          item.textContent = preview;
          waysList.append(item);
        });
        li.append(waysList);
        list.append(li);
      });
      return list;
    }

    function buildOverviewBody(sel) {
      const cat = TAXONOMY[sel.category];
      const subLabel = submetricLabel(sel.category, sel.submetric);
      const desc = submetricDescription(sel.category, sel.submetric);
      const wrap = document.createElement("div");
      wrap.className = "overview-body";

      const p1 = document.createElement("p");
      const s1 = document.createElement("strong");
      s1.textContent = subLabel;
      p1.append(s1, document.createTextNode(` — ${desc}`));

      const p2 = document.createElement("p");
      p2.append(
        document.createTextNode("Category: "),
        (() => {
          const s = document.createElement("strong");
          s.textContent = cat?.label || sel.category;
          return s;
        })(),
        document.createTextNode(`. ${cat?.note || ""}`)
      );

      const p3 = document.createElement("p");
      const base =
        `A paper counts toward this bar if it has at least one ${DETAILS_KEY} entry with this category and sub-metric. Papers may appear under more than one sub-metric. Per-paper evidence is listed under By paper and in expandable paper cards.`;
      p3.textContent = cfg.overviewCaveat ? `${base} ${cfg.overviewCaveat}` : base;

      wrap.append(p1, p2, p3);
      return wrap;
    }

    function setVariantsView(view) {
      variantsView = view;
      const papersBtn = metricVariants.querySelector('[data-view="papers"]');
      const overviewBtn = metricVariants.querySelector('[data-view="overview"]');
      const papersPane = metricVariants.querySelector('[data-pane="papers"]');
      const overviewPane = metricVariants.querySelector('[data-pane="overview"]');
      if (!papersBtn) return;
      papersBtn.classList.toggle("active", view === "papers");
      overviewBtn.classList.toggle("active", view === "overview");
      papersPane.classList.toggle("active", view === "papers");
      overviewPane.classList.toggle("active", view === "overview");
    }

    function buildVariantsList(sel) {
      const name = submetricLabel(sel.category, sel.submetric);
      metricVariants.replaceChildren();

      const heading = document.createElement("h3");
      heading.className = "def-variants-title";
      heading.textContent = `How papers report ${name}`;
      metricVariants.append(heading);

      const toggle = document.createElement("div");
      toggle.className = "variants-toggle";
      toggle.setAttribute("role", "tablist");
      toggle.setAttribute("aria-label", "Reporting view");

      const papersBtn = document.createElement("button");
      papersBtn.type = "button";
      papersBtn.dataset.view = "papers";
      papersBtn.textContent = "By paper";
      papersBtn.setAttribute("role", "tab");

      const overviewBtn = document.createElement("button");
      overviewBtn.type = "button";
      overviewBtn.dataset.view = "overview";
      overviewBtn.textContent = "Overview";
      overviewBtn.setAttribute("role", "tab");

      papersBtn.addEventListener("click", () => setVariantsView("papers"));
      overviewBtn.addEventListener("click", () => setVariantsView("overview"));
      toggle.append(overviewBtn, papersBtn);
      metricVariants.append(toggle);

      const papersPane = document.createElement("div");
      papersPane.className = "variants-pane";
      papersPane.dataset.pane = "papers";
      papersPane.append(buildPapersPane(sel));

      const overviewPane = document.createElement("div");
      overviewPane.className = "variants-pane";
      overviewPane.dataset.pane = "overview";
      overviewPane.append(buildOverviewBody(sel));

      metricVariants.append(papersPane, overviewPane);
      setVariantsView(variantsView);
    }

    function setVariantsOpen(open) {
      variantsOpen = Boolean(open);
      metricVariants.classList.toggle("open", variantsOpen);
      detailTitle.setAttribute("aria-expanded", String(variantsOpen));
      if (variantsOpen && selectedSubmetric) {
        buildVariantsList(selectedSubmetric);
      }
    }

    function showAllPapers() {
      selectedSubmetric = null;
      variantsOpen = false;
      listedPapers = drPapers();
      detail.classList.add("open", "browse-mode");
      setDetailTitle(null);
      detailTitle.setAttribute("aria-expanded", "false");
      metricSummary.classList.remove("open");
      metricSummary.replaceChildren();
      metricVariants.classList.remove("open");
      metricVariants.replaceChildren();
      paperSearchWrap.classList.add("open");
      renderPaperList();
    }

    function showPapers(sel) {
      const changed = !sameSubmetric(selectedSubmetric, sel);
      selectedSubmetric = { category: sel.category, submetric: sel.submetric };
      listedPapers = papersForSubmetric(selectedSubmetric);
      detail.classList.add("open");
      detail.classList.remove("browse-mode");
      setDetailTitle(selectedSubmetric);
      setMetricSummary(selectedSubmetric);
      paperSearchWrap.classList.add("open");
      if (changed) {
        variantsView = "overview";
        setVariantsOpen(false);
      } else if (variantsOpen) {
        buildVariantsList(selectedSubmetric);
      }
      renderPaperList();
      detail.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    function hidePapers() {
      showAllPapers();
    }

    function renderContext() {
      const visible = drPapers();
      const have = Object.fromEntries(CONTEXT_FIELDS.map((f) => [f.id, 0]));
      visible.forEach((p) => {
        const flags = Object.fromEntries(CONTEXT_FIELDS.map((f) => [f.id, false]));
        (p[DETAILS_KEY] || []).forEach((d) => {
          const ec = d.execution_context || {};
          CONTEXT_FIELDS.forEach((f) => {
            if (ec[f.id]) flags[f.id] = true;
          });
        });
        CONTEXT_FIELDS.forEach((f) => {
          if (flags[f.id]) have[f.id] += 1;
        });
      });
      contextGrid.replaceChildren(
        ...CONTEXT_FIELDS.map((f) => {
          const div = document.createElement("div");
          div.className = "context-stat";
          const count = have[f.id];
          const pct = visible.length ? Math.round((100 * count) / visible.length) : 0;
          div.innerHTML = `<div class="n">${count}</div><div class="lbl">${f.label}</div><div class="pct">${pct}% of ${visible.length} RMS papers</div>`;
          return div;
        })
      );
    }

    const categoryBarPlugin = {
      id: "drCategoryOutline",
      afterDatasetsDraw(chartInstance) {
        const { ctx, chartArea } = chartInstance;
        if (!currentOrder.length) return;
        const meta0 = chartInstance.getDatasetMeta(0);
        if (!meta0 || !meta0.data.length) return;

        currentOrder.forEach((row, barIndex) => {
          const cat = TAXONOMY[row.category];
          if (!cat) return;
          let top = Infinity;
          let bottom = -Infinity;
          let left = Infinity;
          let right = -Infinity;
          chartInstance.data.datasets.forEach((_, di) => {
            const meta = chartInstance.getDatasetMeta(di);
            if (meta.hidden) return;
            const el = meta.data[barIndex];
            if (!el || el.skip) return;
            const b = typeof el.getProps === "function"
              ? el.getProps(["x", "y", "base", "width"], true)
              : el;
            const half = (b.width || el.width || 0) / 2;
            const x = b.x ?? el.x;
            const y = b.y ?? el.y;
            const base = b.base ?? el.base;
            left = Math.min(left, x - half);
            right = Math.max(right, x + half);
            top = Math.min(top, y, base);
            bottom = Math.max(bottom, y, base);
          });
          if (!Number.isFinite(left) || right <= left) return;
          ctx.save();
          ctx.strokeStyle = cat.color;
          ctx.lineWidth = 2;
          if (cat.borderStyle === "dashed") ctx.setLineDash([5, 3]);
          else if (cat.borderStyle === "dotted") ctx.setLineDash([1.5, 2.5]);
          else ctx.setLineDash([]);
          const pad = 1.5;
          ctx.strokeRect(
            left - pad,
            Math.max(chartArea.top, top) - pad,
            right - left + pad * 2,
            Math.min(chartArea.bottom, bottom) - Math.max(chartArea.top, top) + pad * 2
          );
          ctx.restore();
        });
      },
    };

    const chart = new Chart(document.getElementById("detailChart"), {
      type: "bar",
      data: { labels: [], datasets: [] },
      plugins: [categoryBarPlugin],
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: { duration: 280 },
        layout: { padding: { bottom: 8 } },
        onClick(_evt, elements) {
          if (!elements.length) {
            showAllPapers();
            return;
          }
          const row = currentOrder[elements[0].index];
          if (!row) return;
          showPapers(row);
        },
        onHover(evt, elements) {
          evt.native.target.style.cursor = elements.length ? "pointer" : "default";
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title(items) {
                if (!items.length) return "";
                const row = currentOrder[items[0].dataIndex];
                if (!row) return "";
                const cat = TAXONOMY[row.category];
                return `${submetricLabel(row.category, row.submetric)} · ${cat?.label || row.category}`;
              },
              footer(items) {
                if (!items.length) return "";
                const total = items.reduce((s, it) => s + it.parsed.y, 0);
                const parts = items
                  .filter((it) => it.parsed.y > 0)
                  .map((it) => `${it.dataset.label} ${it.parsed.y}`);
                const breakdown = parts.length ? ` · ${parts.join(", ")}` : "";
                return `Papers: ${total}${breakdown} · click for paper list`;
              },
            },
          },
        },
        scales: {
          x: {
            stacked: true,
            grid: { display: false },
            ticks: {
              maxRotation: 45,
              minRotation: 45,
              font: { family: "IBM Plex Sans", size: 11 },
              color(ctx) {
                const row = currentOrder[ctx.index];
                if (!row) return "#5a6670";
                return TAXONOMY[row.category]?.color || "#5a6670";
              },
              callback(value, index) {
                const label = this.getLabelForValue(value);
                const row = currentOrder[index];
                const cat = row ? TAXONOMY[row.category] : null;
                return cat ? `${label} [${cat.short}]` : label;
              },
            },
          },
          y: {
            stacked: true,
            beginAtZero: true,
            title: {
              display: true,
              text: "Papers reporting sub-metric",
              color: "#5a6670",
              font: { family: "IBM Plex Sans", size: 12 },
            },
            grid: { color: "rgba(28, 36, 41, 0.08)" },
            ticks: { color: "#5a6670", precision: 0, font: { family: "IBM Plex Sans", size: 11 } },
          },
        },
      },
    });

    function refresh() {
      const keys = activeCohortKeys();
      const cats = activeCategories();
      chart.data = chartData();
      const nothing = keys.length === 0 || cats.length === 0 || currentOrder.length === 0;
      if (keys.length === 0) {
        emptyState.textContent = "Turn on at least one cohort to see the chart.";
      } else if (cats.length === 0) {
        emptyState.textContent = "Turn on at least one category to see the chart.";
      } else {
        emptyState.textContent = "No sub-metrics to show for the current filters.";
      }
      emptyState.classList.toggle("show", nothing);
      chart.canvas.style.opacity = nothing ? "0" : "1";
      chart.update();
      renderContext();

      if (selectedSubmetric !== null) {
        if (nothing || !orderIncludes(selectedSubmetric)) showAllPapers();
        else showPapers(selectedSubmetric);
      } else {
        showAllPapers();
      }
    }

    Object.values(toggles).forEach((el) => el.addEventListener("change", refresh));
    categorySelect.addEventListener("change", refresh);
    document.getElementById("detailClose").addEventListener("click", hidePapers);
    detailTitle.addEventListener("click", () => {
      if (selectedSubmetric === null) return;
      setVariantsOpen(!variantsOpen);
    });
    paperSearch.addEventListener("input", renderPaperList);

    fetch("../../data/papers-data.json")
      .then((r) => {
        if (!r.ok) throw new Error(`Failed to load papers-data.json (${r.status})`);
        return r.json();
      })
      .then((data) => {
        papers = data.papers || [];
        refresh();
      })
      .catch((err) => {
        emptyState.textContent = String(err.message || err);
        emptyState.classList.add("show");
        detail.classList.add("open");
        detail.classList.remove("browse-mode");
        detailTitle.textContent = "Could not load paper list";
        detailCount.textContent = String(err.message || err);
      });
})();
