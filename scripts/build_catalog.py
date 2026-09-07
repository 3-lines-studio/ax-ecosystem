#!/usr/bin/env python3
"""Build the AX ecosystem catalog README from catalog.json.

Fetches each tool's latest released version from GitHub and renders the
registry page grouped by kind. Requires the GitHub CLI (`gh`) for release
lookups; a tool with no release renders without a version.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
README = ROOT / "README.md"

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
    """Return the latest release tag, else the latest tag, else None."""
    for query in (
        f"repos/3-lines-studio/{name}/releases/latest|--jq|.tag_name",
        f"repos/3-lines-studio/{name}/tags?per_page=1|--jq|.[0].name",
    ):
        args = query.split("|")
        try:
            out = subprocess.run(
                ["gh", "api", args[0], args[1], args[2]],
                capture_output=True, text=True, timeout=20,
            )
            if out.returncode == 0:
                tag = out.stdout.strip()
                if tag:
                    return tag
        except Exception:
            pass
    return None


def main():
    data = json.loads(CATALOG.read_text())
    tools = data["tools"]

    for t in tools:
        t["latest_tag"] = latest_tag(t["name"]) if t.get("kind") != "spec" else None

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
        "The registry is machine-readable in [catalog.json](catalog.json). Rebuild this page with "
        "`python3 scripts/build_catalog.py`.",
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
            ver = t.get("latest_tag") or "—"
            lines.append(f"| [{name}]({t['repo']}) | {t['role']} | {ver} |")
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
    n = len(tools)
    released = sum(1 for t in tools if t.get("latest_tag"))
    print(f"wrote {README.name} with {n} tools ({released} with a release)")


if __name__ == "__main__":
    sys.exit(main())
