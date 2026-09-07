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

The registry is machine-readable in [catalog.json](catalog.json). Rebuild this page with `python3 scripts/build_catalog.py`.

### Engine

| Program | Role | Version |
| --- | --- | --- |
| [ax](https://github.com/3-lines-studio/ax) | Headless agent engine | v0.4.9 |

### Host loader

| Program | Role | Version |
| --- | --- | --- |
| [boti](https://github.com/3-lines-studio/boti) | Botdir host loader | v0.1.1 |

### Transport

| Program | Role | Version |
| --- | --- | --- |
| [slaxi](https://github.com/3-lines-studio/slaxi) | Slack transport | v0.3.2 |

### Tool providers

| Program | Role | Version |
| --- | --- | --- |
| [wax](https://github.com/3-lines-studio/wax) | Web-fetch tool | v0.3.2 |
| [bqx](https://github.com/3-lines-studio/bqx) | BigQuery tool | v0.3.1 |
| [pgx](https://github.com/3-lines-studio/pgx) | PostgreSQL tool | v0.2.1 |
| [slackx](https://github.com/3-lines-studio/slackx) | Slack file-upload tool | v0.2.1 |
| [browserx](https://github.com/3-lines-studio/browserx) | Chromium tool | v0.2.2 |
| [bashx](https://github.com/3-lines-studio/bashx) | Bash tool | v0.2.4 |
| [fsx](https://github.com/3-lines-studio/fsx) | Filesystem tools | v0.1.2 |
| [skillx](https://github.com/3-lines-studio/skillx) | Agent Skills provider | v0.1.2 |
| [attachx](https://github.com/3-lines-studio/attachx) | Conversation attachment tool | v0.1.1 |

### Protocol bridges

| Program | Role | Version |
| --- | --- | --- |
| [acpi](https://github.com/3-lines-studio/acpi) | ACP ↔ ax bridge | v0.1.0 |
| [mcpx](https://github.com/3-lines-studio/mcpx) | MCP ↔ ax bridge | v0.1.0 |

### Specification

| Program | Role | Version |
| --- | --- | --- |
| [botdir](https://github.com/3-lines-studio/botdir) | Botdir specification | — |

## Botdir

Every program conforms to [Botdir](https://github.com/3-lines-studio/botdir), the portable directory interface for bots: a bot is a directory, and consumers, hosts, and tools derive `workspace/`, `skills/`, `state/`, `run/`, and `secrets/` from the bot root by convention.

