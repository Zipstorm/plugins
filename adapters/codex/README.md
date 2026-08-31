# Codex adapter

This directory reserves Codex-specific packaging and future extension points. Only `packagingMetadata` is implemented: it points to the validated `.codex-plugin/plugin.json`. Skills, hooks, agents/subagents, commands, instructions/rules, MCP overrides, and permissions remain declared as `planned` and have no loadable files.

The repo-local marketplace points to `plugins/recruiting-codex`. Add a component only after its format is confirmed, its source exists, and `adapter.json` marks it `implemented`.
