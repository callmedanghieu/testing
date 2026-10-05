"""Convert plain YAML scalars that contain ': ' into block scalars (they would not parse)."""
import re
from pathlib import Path

import yaml

PAT = re.compile(r'^(\s*)(diagnosis|prompt|explanation|title|question|answer|back|front|why): (?![|>"\'\[{])(.*: .*)$')
for f in Path(__file__).resolve().parents[1].joinpath("content").rglob("*.yaml"):
    lines = f.read_text().split("\n")
    n = 0
    for i, line in enumerate(lines):
        m = PAT.match(line)
        if m:
            ind, key, val = m.groups()
            lines[i] = f"{ind}{key}: |\n{ind}  {val}"
            n += 1
    if n:
        f.write_text("\n".join(lines))
        print(f"{f.name}: fixed {n}")
    yaml.safe_load(f.read_text())
print("all content YAML parses")
