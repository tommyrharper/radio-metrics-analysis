/**
 * Sticky comparison tray: selection count, clear, enter comparison mode.
 * Requires ComparisonStore. Call ComparisonBar.mount({ compareHref }).
 */
(function (global) {
  function mount(opts) {
    const store = global.ComparisonStore;
    if (!store) throw new Error("ComparisonStore missing");
    const compareHref = (opts && opts.compareHref) || "site/compare.html";

    let bar = document.getElementById("compareBar");
    if (!bar) {
      bar = document.createElement("div");
      bar.id = "compareBar";
      bar.className = "compare-bar";
      bar.hidden = true;
      bar.innerHTML = `
        <div class="compare-bar-inner">
          <span class="compare-bar-count" id="compareBarCount"></span>
          <div class="compare-bar-actions">
            <button type="button" class="compare-bar-clear" id="compareBarClear">Clear</button>
            <a class="compare-bar-go" id="compareBarGo" href="${compareHref}">Compare papers</a>
          </div>
        </div>`;
      document.body.append(bar);
      document.getElementById("compareBarClear").addEventListener("click", () => store.clear());
    }

    const countEl = document.getElementById("compareBarCount");
    const go = document.getElementById("compareBarGo");
    go.href = compareHref;

    function refresh(bibs) {
      const n = bibs.length;
      bar.hidden = n === 0;
      document.body.classList.toggle("has-compare-bar", n > 0);
      countEl.textContent =
        n === 0
          ? ""
          : `${n} paper${n === 1 ? "" : "s"} in comparison` +
            (n < 2 ? " · add at least one more" : "");
      const ready = n >= 2;
      go.classList.toggle("disabled", !ready);
      go.setAttribute("aria-disabled", String(!ready));
      go.tabIndex = ready ? 0 : -1;
    }

    go.addEventListener("click", (evt) => {
      if (store.count() < 2) evt.preventDefault();
    });

    refresh(store.list());
    store.subscribe(refresh);
    return { refresh };
  }

  function syncToggleButton(btn, bibcode) {
    const store = global.ComparisonStore;
    if (!store || !btn) return;
    function paint() {
      const on = store.has(bibcode);
      btn.classList.toggle("in-compare", on);
      btn.setAttribute("aria-pressed", String(on));
      btn.textContent = on ? "In comparison" : "Compare";
      btn.title = on
        ? "Remove from comparison"
        : `Add to comparison (max ${store.MAX_PAPERS})`;
    }
    paint();
    store.subscribe(paint);
    btn.addEventListener("click", (evt) => {
      evt.preventDefault();
      evt.stopPropagation();
      const res = store.toggle(bibcode);
      if (!res.ok && res.reason === "max") {
        btn.title = `Comparison is full (max ${store.MAX_PAPERS}). Remove a paper first.`;
      }
      paint();
    });
  }

  global.ComparisonBar = { mount, syncToggleButton };
})(typeof window !== "undefined" ? window : globalThis);
