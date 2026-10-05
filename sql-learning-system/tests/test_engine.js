// Parity test: the browser engine (app/engine.js on sql.js) must agree with the Python engine.
// Run: node tests/test_engine.js   (uses app/vendor/sql-asm.js; needs app/data.json from tools/build.py)
const path = require("path");
const fs = require("fs");
const root = path.resolve(__dirname, "..");
const initSqlJs = require(path.join(root, "app/vendor/sql-asm.js"));
const { make } = require(path.join(root, "app/engine.js"));
const data = JSON.parse(fs.readFileSync(path.join(root, "app/data.json"), "utf8"));

initSqlJs().then(SQL => {
  const E = make(SQL, data.datasets);
  let fails = 0, checks = 0;
  const fail = (...m) => { fails++; console.log("FAIL", ...m); };
  for (const ex of data.exercises.concat(data.debugging)) {
    if (ex.kind === "selfcheck") continue;
    checks++;
    const [ok, msg] = E.evaluate(ex, ex.solution);
    if (!ok) fail(ex.id, "reference solution rejected:", msg);
    if (ex.broken) {
      const [bok] = E.evaluate(ex, ex.broken);
      if (bok) fail(ex.id, "broken version accepted");
    }
    if (ex.kind === "modify" || ex.kind === "query") {
      const [tok] = E.evaluate(ex, "SELECT 1;");
      if (tok) fail(ex.id, "trivial answer accepted");
    }
  }
  for (const it of data.review) {
    if (it.type !== "predict") continue;
    checks++;
    const db = E.freshDb(it.db);
    if (it.setup) db.exec(it.setup);
    const out = E.formatResult(E.runScript(db, it.sql), it.sql);
    db.close();
    const exp = it.choices[it.answer];
    const ok = exp.startsWith("ERROR") ? out.startsWith(exp) : out === exp;
    if (!ok) fail(it.id, "predict mismatch:", out, "vs", exp);
  }
  console.log(`engine parity: ${checks} items checked, ${fails} failures`);
  process.exit(fails ? 1 : 0);
});
