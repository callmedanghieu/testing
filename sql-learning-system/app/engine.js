/* Grading engine for the browser trainer: a JavaScript port of tools/sqlcheck.py.
   Works in the browser (window.SQLEngine) and in Node (module.exports) on top of sql.js.
   tests/test_engine.js checks that it agrees with the Python engine on every item. */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.SQLEngine = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  function make(SQL, datasets) {
    function freshDb(name) {
      const db = new SQL.Database();
      db.run("PRAGMA foreign_keys = ON");
      if (name) db.exec(datasets[name]);
      return db;
    }
    function prepare(ex) {
      const db = freshDb(ex.db);
      if (ex.setup) db.exec(ex.setup);
      return db;
    }
    function inTransaction(db) {
      try { db.exec("BEGIN"); db.exec("ROLLBACK"); return false; } catch (e) { return true; }
    }
    function runScript(db, sql, continueOnError) {
      let last = { columns: null, rows: null, error: null, notes: [] };
      let it;
      try { it = db.iterateStatements(sql); } catch (e) { return Object.assign({}, last, { error: e.message }); }
      for (;;) {
        let r;
        try { r = it.next(); } catch (e) {
          if (!continueOnError) return Object.assign({}, last, { error: e.message });
          last.notes.push(e.message); break;
        }
        if (r.done) break;
        const st = r.value;
        try {
          const cols = st.getColumnNames();
          const rows = [];
          while (st.step()) rows.push(st.get());
          if (cols.length) last = { columns: cols, rows: rows, error: null, notes: last.notes };
        } catch (e) {
          if (!continueOnError) { try { st.free(); } catch (_) {} return Object.assign({}, last, { error: e.message }); }
          last.notes.push(e.message);
        }
        try { st.free(); } catch (_) {}
      }
      return last;
    }
    function normValue(v) {
      if (typeof v === "number") { const r = Math.round(v * 1e6) / 1e6; return r === 0 ? 0 : r; }
      if (v instanceof Uint8Array) return Array.from(v).map(b => b.toString(16).padStart(2, "0")).join("");
      return v;
    }
    const normRows = rows => (rows || []).map(r => r.map(normValue));
    const key = row => JSON.stringify(row);
    const sortRows = rows => rows.map(key).sort();
    const show = row => "(" + row.map(v => v === null ? "None" : typeof v === "string" ? "'" + v + "'" : String(v)).join(", ") + ")";

    function compare(user, ref, ordered) {
      if (user.error) return [false, "Your SQL raised an error: " + user.error];
      if (user.columns === null) return [false, "Your SQL did not return any rows/columns. End with a SELECT."];
      if (ref.columns !== null && user.columns.length !== ref.columns.length)
        return [false, `Column count differs: you returned ${user.columns.length} (${user.columns.join(", ")}), expected ${ref.columns.length} (${ref.columns.join(", ")}).`];
      const u = normRows(user.rows), r = normRows(ref.rows);
      if (ordered && JSON.stringify(u) === JSON.stringify(r)) return [true, "Correct."];
      const us = sortRows(u), rs = sortRows(r);
      if (JSON.stringify(us) === JSON.stringify(rs))
        return ordered ? [false, "Right rows, wrong order. Check your ORDER BY."] : [true, "Correct."];
      const msg = [`Expected ${r.length} row(s); you returned ${u.length}.`];
      const missing = r.filter(x => !us.includes(key(x))).slice(0, 3);
      const extra = u.filter(x => !rs.includes(key(x))).slice(0, 3);
      if (missing.length) msg.push("Missing e.g. " + missing.map(show).join("; "));
      if (extra.length) msg.push("Unexpected e.g. " + extra.map(show).join("; "));
      if (new Set(us).size !== us.length && new Set(rs).size === rs.length)
        msg.push("You have duplicate rows - check your JOIN or consider DISTINCT / GROUP BY.");
      return [false, msg.join(" ")];
    }
    function planText(db, q) {
      const res = db.exec("EXPLAIN QUERY PLAN " + q);
      if (!res.length) return "";
      return res[0].values.map(r => r[r.length - 1]).join(" | ");
    }
    function stateSnapshot(db, ex) {
      const snap = [];
      for (const p of ex.probes || []) {
        try { db.exec(p); snap.push(["probe", p, "ok"]); } catch (e) { snap.push(["probe", p, "error"]); }
      }
      for (const c of ex.check || []) {
        if (typeof c === "object") {
          const text = planText(db, c.plan).toUpperCase();
          for (const n of c.contains || []) snap.push(["plan", n, text.includes(n.toUpperCase())]);
          for (const n of c.not_contains || []) snap.push(["plan-not", n, !text.includes(n.toUpperCase())]);
        } else {
          try {
            const res = db.exec(c);
            const rows = res.length ? normRows(res[0].values) : [];
            snap.push(["check", c, sortRows(rows)]);
          } catch (e) { snap.push(["check", c, "error: " + e.message.split(":")[0]]); }
        }
      }
      return snap;
    }
    function evaluate(ex, userSql) {
      const opened = [];
      const origPrepare = prepare;
      const track = e => { const db = origPrepare(e); opened.push(db); return db; };
      try { return evaluateWith(ex, userSql, track); }
      finally { for (const db of opened) { try { db.close(); } catch (_) {} } }
    }
    function evaluateWith(ex, userSql, prepare) {
      const kind = ex.kind;
      if (kind === "selfcheck") return [false, "Self-check exercise: compare your answer with the reference solution."];
      for (const word of ex.require || [])
        if (!userSql.toUpperCase().includes(word.toUpperCase())) return [false, `This exercise asks you to use ${word}.`];
      if (kind === "injection") {
        const u = runScript(prepare(ex), ex.template.replace("{input}", userSql.trim()));
        const r = runScript(prepare(ex), ex.template.replace("{input}", ex.solution.trim()));
        return compare(u, r, !!ex.ordered);
      }
      if (kind === "error") {
        const u = runScript(prepare(ex), userSql);
        if (!u.error) return [false, "Your statement succeeded, but this exercise wants it to be rejected."];
        if (!u.error.toLowerCase().includes(ex.expect_error.toLowerCase())) return [false, "It failed, but with a different error: " + u.error];
        return [true, "Correct. SQLite refused it: " + u.error];
      }
      if (kind === "query") {
        return compare(runScript(prepare(ex), userSql), runScript(prepare(ex), ex.solution), !!ex.ordered);
      }
      if (kind === "modify") {
        const udb = prepare(ex), rdb = prepare(ex);
        const coe = !!ex.continue_on_error;
        const u = runScript(udb, userSql, coe);
        if (u.error) return [false, "Your SQL raised an error: " + u.error];
        if (inTransaction(udb)) return [false, "A transaction is still open: you never ran COMMIT (or ROLLBACK)."];
        runScript(rdb, ex.solution, coe);
        const us = stateSnapshot(udb, ex), rs = stateSnapshot(rdb, ex);
        for (let i = 0; i < Math.max(us.length, rs.length); i++) {
          const a = us[i], b = rs[i];
          if (JSON.stringify(a) === JSON.stringify(b)) continue;
          if (a[0] === "probe")
            return [false, `Test statement \`${a[1]}\` was ${a[2] === "ok" ? "accepted" : "rejected"} by your database but ${b[2] === "ok" ? "accepted" : "rejected"} by the reference.`];
          if (a[0] === "plan" || a[0] === "plan-not")
            return [false, `Query plan check failed: expected the plan ${a[0] === "plan" ? "to contain" : "NOT to contain"} '${a[1]}'.`];
          return [false, `After your SQL, \`${a[1]}\` does not return the expected rows. Compare with "Show expected".`];
        }
        return [true, "Correct. The database ends up in the expected state."];
      }
      throw new Error("unknown kind " + kind);
    }
    function formatResult(res, sql) {
      if (res.error) return "ERROR: " + res.error;
      if (!res.rows || !res.rows.length) return "(no rows)";
      let rows = res.rows;
      if ((sql || "").toUpperCase().includes("EXPLAIN QUERY PLAN")) rows = rows.map(r => [r[r.length - 1]]);
      return rows.map(r => r.map(v => v === null ? "NULL" : String(v)).join(" | ")).join("; ");
    }
    return { freshDb, prepare, runScript, evaluate, compare, planText, formatResult, inTransaction };
  }
  return { make };
});
