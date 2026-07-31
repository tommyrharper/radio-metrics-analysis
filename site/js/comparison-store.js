/**
 * Shared paper-comparison selection (localStorage).
 * Used by index, paper detail, metric detail, and compare pages.
 */
(function (global) {
  const STORAGE_KEY = "radio-metrics-compare-bibs";
  const MAX_PAPERS = 5;
  const CHANGE_EVENT = "compare-selection-changed";

  function read() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed.filter((x) => typeof x === "string") : [];
    } catch {
      return [];
    }
  }

  function write(bibs) {
    const next = [...new Set(bibs)].slice(0, MAX_PAPERS);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
    global.dispatchEvent(new CustomEvent(CHANGE_EVENT, { detail: { bibs: next } }));
    return next;
  }

  const ComparisonStore = {
    MAX_PAPERS,
    CHANGE_EVENT,
    list() {
      return read();
    },
    count() {
      return read().length;
    },
    has(bibcode) {
      return read().includes(bibcode);
    },
    clear() {
      return write([]);
    },
    add(bibcode) {
      const cur = read();
      if (cur.includes(bibcode)) return { bibs: cur, ok: true, reason: null };
      if (cur.length >= MAX_PAPERS) {
        return { bibs: cur, ok: false, reason: `max` };
      }
      return { bibs: write([...cur, bibcode]), ok: true, reason: null };
    },
    remove(bibcode) {
      return write(read().filter((b) => b !== bibcode));
    },
    toggle(bibcode) {
      if (read().includes(bibcode)) {
        return { bibs: write(read().filter((b) => b !== bibcode)), added: false, ok: true };
      }
      const res = this.add(bibcode);
      return { bibs: res.bibs, added: res.ok, ok: res.ok, reason: res.reason };
    },
    subscribe(fn) {
      const handler = (e) => fn(e.detail.bibs);
      global.addEventListener(CHANGE_EVENT, handler);
      return () => global.removeEventListener(CHANGE_EVENT, handler);
    },
  };

  global.ComparisonStore = ComparisonStore;
})(typeof window !== "undefined" ? window : globalThis);
