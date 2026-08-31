# Harness adapters

Each adapter descriptor reserves the same extension interface: skills, hooks, agents/subagents, commands, instructions/rules, MCP overrides, permissions, and packaging metadata. These are client concerns, not portable Agent Plugins v1 fields.

A `planned` component has no file path and is never packaged. An `implemented` component must name an existing repository source and a contained destination path. The build copies only those declared implementations; validation rejects undeclared or incomplete scaffold state.
