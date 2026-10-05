"""Load and validate everything in content/ (single source of truth)."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SOURCES = ROOT / "sources"

ORIGINS = {
    "source-demo": "SOURCE · demonstrated in the lecture",
    "source-question": "SOURCE · question posed in the lecture",
    "source-assigned": "SOURCE · explicitly left to the learner in the lecture",
    "generated": "GENERATED · written for this system (reinforces a concept from the source)",
}
KINDS = {"query", "modify", "error", "injection", "selfcheck"}
MODULES = ["M0", "M1", "M2", "M3", "M4", "M5", "M6"]
MODULE_TITLES = {
    "M0": "Querying", "M1": "Relating", "M2": "Designing", "M3": "Writing",
    "M4": "Viewing", "M5": "Optimizing", "M6": "Scaling",
}
SOURCE_FILES = {
    "lecture0": "cs50_sql_lecture0-720p-en.txt",
    "lecture1": "cs50_sql_lecture1-720p_resize-en.txt",
    "lecture2": "cs50_sql_lecture2-720p-en.txt",
    "lecture3": "cs50_sql_lecture3-720p-en.txt",
    "lecture4": "cs50_sql_lecture4-720p-en.txt",
    "lecture5": "cs50_sql_lecture5-720p_MBR-en.txt",
    "lecture6": "cs50_sql_lecture6-720p_MBR-en.txt",
}
LECTURE_TITLES = {"lecture0": "Querying", "lecture1": "Relating", "lecture2": "Designing", "lecture3": "Writing", "lecture4": "Viewing",
                  "lecture5": "Optimizing", "lecture6": "Scaling"}


def _load(path):
    return yaml.safe_load(path.read_text()) or []


def exercises():
    out = []
    for m in MODULES:
        p = CONTENT / "exercises" / f"{m}.yaml"
        if p.exists():
            for ex in _load(p):
                ex.setdefault("module", m)
                out.append(ex)
    return out


def debugging():
    p = CONTENT / "debugging.yaml"
    return _load(p) if p.exists() else []


def review():
    out = []
    for m in MODULES:
        p = CONTENT / "review" / f"{m}.yaml"
        if p.exists():
            for it in _load(p):
                it.setdefault("module", m)
                out.append(it)
    return out


_lines_cache: dict[str, list[str]] = {}


def source_lines(file: str) -> list[str]:
    if file not in _lines_cache:
        _lines_cache[file] = (SOURCES / f"{file}.txt").read_text().splitlines()
    return _lines_cache[file]


def _norm(s: str) -> str:
    s = re.sub(r"\[\?|\?\]|\[INAUDIBLE\]", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def check_ref(ref: dict) -> str | None:
    """Return an error message if a source reference is broken, else None."""
    f = ref.get("file")
    if f not in SOURCE_FILES:
        return f"unknown source file {f!r}"
    a, _, b = str(ref["lines"]).partition("-")
    a, b = int(a), int(b or a)
    lines = source_lines(f)
    if not (1 <= a <= b <= len(lines)):
        return f"{f} lines {a}-{b} out of range (1-{len(lines)})"
    if ref.get("quote"):
        window = _norm(" ".join(lines[a - 1:b]))
        if _norm(ref["quote"]) not in window:
            return f"quote not found in {f} L{a}-{b}: {ref['quote']!r}"
    return None


def ref_label(ref: dict) -> str:
    return f"{ref['file']} L{ref['lines']}"


def validate_exercise(ex: dict) -> list[str]:
    errs = []
    for k in ("id", "title", "origin", "concepts", "difficulty", "kind", "prompt", "hints", "solution", "source"):
        if k not in ex:
            errs.append(f"{ex.get('id')}: missing {k}")
    if ex.get("origin") not in ORIGINS:
        errs.append(f"{ex.get('id')}: bad origin {ex.get('origin')}")
    if ex.get("kind") not in KINDS:
        errs.append(f"{ex.get('id')}: bad kind {ex.get('kind')}")
    if len(ex.get("hints", [])) != 3:
        errs.append(f"{ex.get('id')}: needs exactly 3 hints")
    for r in ex.get("source", []):
        e = check_ref(r)
        if e:
            errs.append(f"{ex.get('id')}: {e}")
    if not ex.get("source"):
        errs.append(f"{ex.get('id')}: no source reference")
    return errs
