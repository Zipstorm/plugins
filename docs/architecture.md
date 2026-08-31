# Architecture

## Boundaries

This repository is the source of truth for distributable recruiting agent plugins. It does not own remote services, tenant state, customer configuration, credentials, authentication, or UI; those remain in the separately deployed agent platform.

The repository has three layers:

1. The portable core uses Agent Plugins v1. Its only current component is root `plugin.json`. A missing `skills/` directory and missing `mcp.json` are valid and intentional.
2. `adapters/<client>/` owns non-portable extension declarations for Codex, Claude Code, Cursor, and Antigravity. Client hooks, agents/subagents, commands, instructions/rules, MCP overrides, permissions, and packaging metadata must never be added to the portable core.
3. `scripts/build.py` composes distinct artifacts from the suite declaration and only copies adapter components whose descriptors say `implemented` and provide both an existing source path and a contained package path.

## Current no-skills state

There is no `src/workflows/` tree yet because no recruiting workflow has been approved for implementation. There are no `SKILL.md` files, prompt profiles, behavior contracts, or executable extension files. This avoids turning placeholders into accidental runtime behavior.

When workflow work begins, introduce shared behavioral contracts under `src/workflows/<workflow>/` and standalone harness profiles as a separate reviewed change. The build should compose them at build time; it should not create one skill full of runtime client conditionals.

## Artifact model

`release/suite.json` declares five unique package identities synchronized to one suite SemVer:

- `recruiting`
- `recruiting-codex`
- `recruiting-claude-code`
- `recruiting-cursor`
- `recruiting-antigravity`

Distinct names prevent differently tuned content from sharing an identity. `dist/release-manifest.json` binds each artifact to its harness profile, source commit, suite version, compatibility schema, content digest, and archive digest. Workflow contracts are currently the empty object.

`dist/` is ephemeral and Git-ignored. Release automation should build it from a clean tagged commit and publish the archives and checksums immutably.

## Native packaging

Codex has a validated native manifest at `plugins/recruiting-codex/.codex-plugin/plugin.json` and a repository marketplace entry. It deliberately declares no skills, apps, MCP servers, capabilities, or starter prompts.

No native manifests are created for the other clients until their selected formats and installation flows are confirmed. Their current artifacts are uniquely named portable manifest-only envelopes, not claims of native installability.
