#!/usr/bin/env python3
"""Minimal, dependency-free check for the published Agent Skill layout."""

from pathlib import Path
import re
import sys

repo = Path(__file__).resolve().parents[1]
skill = repo / "compass-research"
manifest = skill / "SKILL.md"
errors = []

if not manifest.is_file():
    errors.append("Missing compass-research/SKILL.md")
else:
    body = manifest.read_text(encoding="utf-8")
    parts = body.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        front = parts[1]
        fields = {}
        for line in front.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        name = fields.get("name", "")
        desc = fields.get("description", "")
        if not name or name != skill.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append("Invalid skill name or folder mismatch")
        if not desc or len(desc) > 1024:
            errors.append("Description is missing or >1024 characters")
        if not parts[2].strip():
            errors.append("SKILL.md has no instructions")

        # Only validate relative markdown links in the main skill; URLs are external.
        for target in re.findall(r"\]\(([^)]+\.md)\)", parts[2]):
            if not (skill / target).is_file():
                errors.append(f"Broken skill reference: {target}")

for filename in ["README.md", "README.zh-CN.md", "LICENSE", "tests/scenarios.md"]:
    if not (repo / filename).is_file():
        errors.append(f"Missing distribution file: {filename}")

if errors:
    print("INVALID\n" + "\n".join(f"- {err}" for err in errors))
    sys.exit(1)
print("PASS: Compass skill metadata, files, and reference paths are structurally valid.")