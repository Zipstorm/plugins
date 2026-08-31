# Compatibility matrix

The machine-readable source is `release/compatibility.json`; schema version 1 distinguishes actual implementation from planned work.

| Profile | Artifact | Portable manifest | Native manifest | Runtime components | Installation status |
| --- | --- | --- | --- | --- | --- |
| Portable | `recruiting` | Implemented | Not applicable | None; skills planned | Not verified |
| Codex | `recruiting-codex` | Implemented | Implemented and validated | None | Repo marketplace scaffold only |
| Claude Code | `recruiting-claude-code` | Implemented | Planned | None | Not verified |
| Cursor | `recruiting-cursor` | Implemented | Planned | None | Not verified |
| Antigravity | `recruiting-antigravity` | Implemented | Planned | None | Not verified |

Agent Plugins v1 makes skills and MCP servers portable component types. This repository implements neither today. Hooks, agents/subagents, commands, instructions/rules, client MCP overrides, permissions, and native packaging metadata are adapter concerns and are not portable components.

“Implemented” in this table means a file exists and is validated; it does not imply recruiting functionality. All packages remain `scaffold-no-skills`.
