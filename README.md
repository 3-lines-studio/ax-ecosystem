# AX ecosystem

Small Unix programs that compose through process boundaries: a headless agent engine, tool providers, transports, a host loader, and protocol bridges, wired together by the Botdir portable directory interface.

## Install

One installer serves every program in the ecosystem:

```sh
curl -fsSL https://ax.3lines.studio/install.sh | sh
```

Install any program by name, without changing the installer:

```sh
curl -fsSL https://ax.3lines.studio/install.sh | sh -s -- wax bqx pgx
```

Every program is a single static binary released to its own repository. `ax` owns agent execution and has no built-in tools; every capability is an explicit external provider.

## Catalog

Versions below are live badges from each repo's latest release — they update automatically. The registry is machine-readable in [catalog.json](catalog.json); cached latest tags are in [versions.json](versions.json). Regenerate with `python3 scripts/build_catalog.py` (or rely on the scheduled refresh).

### Engine

| Program | Role | Version |
| --- | --- | --- |
| [ax](https://github.com/3-lines-studio/ax) | Headless agent engine | ![v](https://img.shields.io/github/v/release/3-lines-studio/ax?style=flat-square&label=) |

### Host loader

| Program | Role | Version |
| --- | --- | --- |
| [boti](https://github.com/3-lines-studio/boti) | Botdir host loader | ![v](https://img.shields.io/github/v/release/3-lines-studio/boti?style=flat-square&label=) |

### Transport

| Program | Role | Version |
| --- | --- | --- |
| [slaxi](https://github.com/3-lines-studio/slaxi) | Slack transport | ![v](https://img.shields.io/github/v/release/3-lines-studio/slaxi?style=flat-square&label=) |

### Tool providers

| Program | Role | Version |
| --- | --- | --- |
| [wax](https://github.com/3-lines-studio/wax) | Web-fetch tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/wax?style=flat-square&label=) |
| [bqx](https://github.com/3-lines-studio/bqx) | BigQuery tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/bqx?style=flat-square&label=) |
| [pgx](https://github.com/3-lines-studio/pgx) | PostgreSQL tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/pgx?style=flat-square&label=) |
| [slackx](https://github.com/3-lines-studio/slackx) | Slack file-upload tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/slackx?style=flat-square&label=) |
| [browserx](https://github.com/3-lines-studio/browserx) | Chromium tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/browserx?style=flat-square&label=) |
| [bashx](https://github.com/3-lines-studio/bashx) | Bash tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/bashx?style=flat-square&label=) |
| [fsx](https://github.com/3-lines-studio/fsx) | Filesystem tools | ![v](https://img.shields.io/github/v/release/3-lines-studio/fsx?style=flat-square&label=) |
| [skillx](https://github.com/3-lines-studio/skillx) | Agent Skills provider | ![v](https://img.shields.io/github/v/release/3-lines-studio/skillx?style=flat-square&label=) |
| [attachx](https://github.com/3-lines-studio/attachx) | Conversation attachment tool | ![v](https://img.shields.io/github/v/release/3-lines-studio/attachx?style=flat-square&label=) |

### Protocol bridges

| Program | Role | Version |
| --- | --- | --- |
| [acpi](https://github.com/3-lines-studio/acpi) | ACP ↔ ax bridge | ![v](https://img.shields.io/github/v/release/3-lines-studio/acpi?style=flat-square&label=) |
| [mcpx](https://github.com/3-lines-studio/mcpx) | MCP ↔ ax bridge | ![v](https://img.shields.io/github/v/release/3-lines-studio/mcpx?style=flat-square&label=) |

### Specification

| Program | Role | Version |
| --- | --- | --- |
| [botdir](https://github.com/3-lines-studio/botdir) | Botdir specification | specification |

## Botdir

Every program conforms to [Botdir](https://github.com/3-lines-studio/botdir), the portable directory interface for bots: a bot is a directory, and consumers, hosts, and tools derive `workspace/`, `skills/`, `state/`, `run/`, and `secrets/` from the bot root by convention.

