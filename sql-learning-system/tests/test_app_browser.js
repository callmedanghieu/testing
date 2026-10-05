// End-to-end check of the web trainer in headless Chromium (Playwright).
// Run: NODE_PATH=$(npm root -g) node tests/test_app_browser.js [screenshot-dir]
const { chromium } = require("playwright");
const path = require("path");
const url = "file://" + path.resolve(__dirname, "../app/index.html");
const shots = process.argv[2];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const errors = [];
  page.on("pageerror", e => errors.push("pageerror: " + e.message));
  const external = [];
  page.on("requestfailed", r => { if (!r.url().startsWith("file:")) external.push(r.url()); });
  page.on("console", m => {
    if (m.type() !== "error") return;
    if (/^Failed to load resource/.test(m.text())) return; // external fonts may be blocked offline; reported below
    errors.push("console: " + m.text());
  });
  const ok = (cond, msg) => { if (!cond) { errors.push("ASSERT: " + msg); } };

  await page.goto(url + "#home");
  await page.waitForSelector(".hero h1", { timeout: 20000 });
  ok((await page.textContent(".hero h1")).includes("Ride the line"), "home renders");
  if (shots) await page.screenshot({ path: shots + "/home.png", fullPage: true });

  // Lesson tab renders markdown tables / code
  await page.goto(url + "#M3");
  await page.waitForSelector("#tabbody article h2");
  ok(await page.$("#tabbody article table"), "lesson table rendered");

  // Solve an exercise through the UI: wrong first, then right
  await page.goto(url + "#M4-E02");
  await page.waitForSelector("#ed");
  ok(await page.isDisabled("#solution"), "solution locked before any attempt");
  await page.fill("#ed", `SELECT "title" FROM "longlist";`);
  await page.click("#check");
  ok((await page.textContent("#fb")).includes("✘"), "wrong answer rejected");
  await page.click("#hint");
  ok((await page.textContent("#hints")).includes("Hint 1"), "hint 1 shown");
  await page.fill("#ed", `SELECT "title" FROM "longlist" WHERE "name" = 'Fernanda Melchor';`);
  await page.click("#check");
  ok((await page.textContent("#fb")).includes("✔"), "right answer accepted");
  ok((await page.textContent("#out")).includes("Paradais"), "result table shows Paradais");
  if (shots) await page.screenshot({ path: shots + "/exercise.png", fullPage: true });

  // modify-type exercise with probes, plus solution reveal (two clicks)
  await page.goto(url + "#M3-E14");
  await page.waitForSelector("#ed");
  const sol = await page.evaluate(() => DATA.exercises.find(e => e.id === "M3-E14").solution);
  await page.fill("#ed", sol);
  await page.click("#check");
  ok((await page.textContent("#fb")).includes("✔"), "trigger exercise accepted");
  await page.click("#solution"); await page.click("#solution");
  ok((await page.textContent("#out")).includes("CREATE TRIGGER"), "solution revealed after two clicks");

  // injection exercise
  await page.goto(url + "#M6-E08");
  await page.waitForSelector("#ed");
  await page.fill("#ed", "1 OR 1 = 1");
  await page.click("#check");
  ok((await page.textContent("#fb")).includes("✔"), "injection accepted");

  // debugging item starts with the broken query pre-loaded
  await page.goto(url + "#D1-04");
  await page.waitForSelector("#ed");
  ok((await page.inputValue("#ed")).includes('"id" = ('), "broken query pre-loaded");

  // review: answer a predict card
  await page.goto(url + "#review");
  await page.click('[data-deck="M0"]');
  await page.waitForSelector("#deck");
  await page.click('[data-rate="good"]').catch(() => {}); // card 1 is a quick card: rating hidden until reveal
  await page.click("#reveal").catch(() => {});
  await page.click('[data-rate="good"]');
  await page.waitForSelector("#deck .choices button");
  await page.click("#deck .choices button >> nth=1");
  ok((await page.textContent("#ans")).includes("Right"), "predict card answered correctly (B)");
  await page.click("#runit");
  ok((await page.textContent("#runout")).includes("0"), "predict card runs SQL");

  // sandbox
  await page.goto(url + "#sandbox");
  await page.waitForSelector("#sbx");
  await page.fill("#sbx", `SELECT COUNT(*) AS "n" FROM "books";`);
  await page.click("#srun");
  ok((await page.textContent("#sout")).includes("78"), "sandbox runs");

  // progress persisted
  const prog = await page.evaluate(() => JSON.parse(localStorage.getItem("sqlline:progress")));
  ok(prog.items["M4-E02"].passed && prog.items["M4-E02"].attempts === 2 && prog.items["M4-E02"].hints === 1, "progress saved");

  // every item page renders without throwing
  const ids = await page.evaluate(() => Object.keys(ITEMS).concat(MODS.map(m => m.id), ["debug", "sources", "errata", "roadmap", "backup"]));
  for (const id of ids) { await page.goto(url + "#" + id); await page.waitForSelector("#view h1, #view h2, #view article"); }

  // phone width + dark mode screenshots, and no horizontal page scroll
  await page.setViewportSize({ width: 390, height: 844 });
  for (const id of ["home", "M2-E08", "M3"]) {
    await page.goto(url + "#" + id); await page.waitForTimeout(150);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    ok(overflow <= 1, `no horizontal scroll on phone (${id}): ${overflow}px`);
  }
  if (shots) await page.screenshot({ path: shots + "/phone.png", fullPage: false });
  await page.emulateMedia({ colorScheme: "dark" });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(url + "#M5-E03"); await page.waitForSelector("#ed");
  if (shots) await page.screenshot({ path: shots + "/dark.png", fullPage: true });

  await browser.close();
  if (external.length) console.log("note: external resources unavailable here (fonts fall back): " + [...new Set(external.map(u => new URL(u).host))].join(", "));
  console.log(errors.length ? errors.join("\n") : "app browser test: all checks passed (" + ids.length + " pages rendered)");
  process.exit(errors.length ? 1 : 0);
})();
