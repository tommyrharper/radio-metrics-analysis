/**
 * Persist cohort visibility toggles (classic / emerging / r2d2) across pages.
 */
(function (global) {
  const STORAGE_KEY = "radio-metrics-cohort-toggles";
  const KEYS = ["classic", "emerging", "r2d2"];

  function defaults() {
    return { classic: true, emerging: true, r2d2: false };
  }

  function load() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaults();
      const parsed = JSON.parse(raw);
      const out = defaults();
      KEYS.forEach((k) => {
        if (typeof parsed[k] === "boolean") out[k] = parsed[k];
      });
      // Keep at least one cohort on so charts/lists are never empty by accident.
      if (!KEYS.some((k) => out[k])) return defaults();
      return out;
    } catch {
      return defaults();
    }
  }

  function save(state) {
    const next = defaults();
    KEYS.forEach((k) => {
      if (typeof state[k] === "boolean") next[k] = state[k];
    });
    if (!KEYS.some((k) => next[k])) {
      // Reject turning off the last cohort — revert caller via reload of prefs.
      return load();
    }
    localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
    return next;
  }

  function apply(toggles) {
    const state = load();
    KEYS.forEach((k) => {
      if (toggles[k]) toggles[k].checked = state[k];
    });
    return state;
  }

  function saveFrom(toggles) {
    const state = {};
    KEYS.forEach((k) => {
      state[k] = !!(toggles[k] && toggles[k].checked);
    });
    const saved = save(state);
    // If save rejected (all off), re-apply stored state to checkboxes.
    KEYS.forEach((k) => {
      if (toggles[k]) toggles[k].checked = saved[k];
    });
    return saved;
  }

  /**
   * Apply stored prefs and persist on change.
   * @param {Record<string, HTMLInputElement>} toggles
   * @param {() => void} [onChange]
   */
  function bind(toggles, onChange) {
    apply(toggles);
    KEYS.forEach((k) => {
      const el = toggles[k];
      if (!el) return;
      el.addEventListener("change", () => {
        saveFrom(toggles);
        if (typeof onChange === "function") onChange();
      });
    });
    // Sync charts/lists to restored prefs (apply alone only updates checkboxes).
    if (typeof onChange === "function") onChange();
  }

  global.CohortPrefs = { load, save, apply, saveFrom, bind, STORAGE_KEY };
})(typeof window !== "undefined" ? window : globalThis);
