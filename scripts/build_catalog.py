#!/usr/bin/env python3
"""Build the AX ecosystem catalog page from catalog.json.

The README renders each tool's version as a live shields.io badge, so the
versions shown are always current on every render and never need manual
refresh. A scheduled workflow re-runs this so that:

* the machine-readable `versions.json` cache of latest tags stays fresh, and
* the README stays in sync whenever `catalog.json` is edited (add/remove/rename
  a tool or tweak its metadata).

The README itself is deterministic: it only changes when `catalog.json`
changes, because the version column is a badge, not baked text.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
README = ROOT / "README.md"
VERSIONS = ROOT / "versions.json"

KIND_ORDER = ["engine", "host", "transport", "provider", "bridge", "spec"]
KIND_TITLE = {
    "engine": "Engine",
    "host": "Host loader",
    "transport": "Transport",
    "provider": "Tool providers",
    "bridge": "Protocol bridges",
    "spec": "Specification",
}


def latest_tag(name):
    """Best-effort: the latest release tag, else the newest tag, else None."""
    for args in (
        ["gh", "api", f"repos/3-lines-studio/{name}/releases/latest", "--jq", ".tag_name"],
        ["gh", "api", f"repos/3-lines-studio/{name}/tags?per_page=1", "--jq", ".[0].name"],
    ):
        try:
            out = subprocess.run(args, capture_output=True, text=True, timeout=20)
            if out.returncode == 0:
                tag = out.stdout.strip()
                if tag:
                    return tag
        except Exception:
            pass
    return None


def render_badge(name):
    return f"https://img.shields.io/github/v/release/3-lines-studio/{name}?style=flat-square&label="


def main():
    data = json.loads(CATALOG.read_text())
    tools = data["tools"]

    # Machine-readable cache of live latest tags (best-effort).
    cached = {}
    for t in tools:
        if t.get("kind") == "spec":
            continue
        cached[t["name"]] = latest_tag(t["name"]) or ""
    VERSIONS.write_text(
        json.dumps({"registry": data["registry"], "tools": cached}, indent=2) + "\n"
    )

    groups = {k: [] for k in KIND_ORDER}
    for t in tools:
        groups.setdefault(t.get("kind", ""), []).append(t)

    lines = [
        "# AX ecosystem",
        "",
        data["description"],
        "",
        "## Install",
        "",
        "One installer serves every program in the ecosystem:",
        "",
        "```sh",
        data["installer"],
        "```",
        "",
        "Install any program by name, without changing the installer:",
        "",
        "```sh",
        "curl -fsSL https://ax.3lines.studio/install.sh | sh -s -- wax bqx pgx",
        "```",
        "",
        "Every program is a single static binary released to its own repository. `ax` owns agent "
        "execution and has no built-in tools; every capability is an explicit external provider.",
        "",
        "## Catalog",
        "",
        "Versions below are live badges from each repo's latest release — they update automatically. "
        "The registry is machine-readable in [catalog.json](catalog.json); cached latest tags are in "
        "[versions.json](versions.json). Regenerate with `python3 scripts/build_catalog.py` (or rely "
        "on the scheduled refresh).",
        "",
    ]

    for kind in KIND_ORDER:
        entries = groups.get(kind) or []
        if not entries:
            continue
        lines.append(f"### {KIND_TITLE[kind]}")
        lines.append("")
        lines.append("| Program | Role | Version |")
        lines.append("| --- | --- | --- |")
        for t in entries:
            name = t["name"]
            repo = t["repo"]
            if t.get("kind") == "spec":
                ver = "specification"
            else:
                ver = f"![v]({render_badge(name)})"
            lines.append(f"| [{name}]({repo}) | {t['role']} | {ver} |")
        lines.append("")

    lines += [
        "## Botdir",
        "",
        "Every program conforms to [Botdir](https://github.com/3-lines-studio/botdir), the portable "
        "directory interface for bots: a bot is a directory, and consumers, hosts, and tools derive "
        "`workspace/`, `skills/`, `state/`, `run/`, and `secrets/` from the bot root by convention.",
        "",
    ]

    README.write_text("\n".join(lines) + "\n")
    print(f"wrote {README.name} and {VERSIONS.name} for {len(tools)} tools")


if __name__ == "__main__":
    sys.exit(main())
