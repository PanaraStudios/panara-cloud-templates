#!/usr/bin/env python3
"""Combine blueprints/<id>/meta.json into the root meta.json the panel reads."""
import json
import os
import sys

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
blueprints = os.path.join(root, "blueprints")
entries, problems = [], []
for name in sorted(os.listdir(blueprints)):
    folder = os.path.join(blueprints, name)
    if not os.path.isdir(folder):
        continue
    for required in ("meta.json", "docker-compose.yml", "template.toml"):
        if not os.path.isfile(os.path.join(folder, required)):
            problems.append(f"{name}: missing {required}")
    try:
        entry = json.load(open(os.path.join(folder, "meta.json"), encoding="utf-8"))
    except Exception as error:  # noqa: BLE001
        problems.append(f"{name}: {error}")
        continue
    if entry.get("id") != name:
        problems.append(f"{name}: meta.json id is {entry.get('id')!r}")
    entries.append(entry)
if problems:
    print("\n".join(problems), file=sys.stderr)
    sys.exit(1)
with open(os.path.join(root, "meta.json"), "w", encoding="utf-8") as out:
    json.dump(entries, out, indent=2)
    out.write("\n")
print(f"{len(entries)} templates")
