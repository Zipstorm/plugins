# Recruiting Agent Plugins

Source repository for a recruiting-focused plugin suite that will eventually ship a portable Agent Plugins package plus harness-specific packages for Codex, Claude Code, Cursor, and Antigravity.

This commit is intentionally **basic scaffolding only**. It contains no skills, workflow implementations, hooks, commands, agents, rules, permissions, or MCP connections. The generated packages are valid manifest-only foundations and provide no recruiting behavior yet.

## Repository map

- `plugin.json` — valid Agent Plugins v1 manifest for the portable scaffold.
- `adapters/` — non-portable client extension points and packaging declarations.
- `plugins/recruiting-codex/` — validated Codex-native, manifest-only plugin source.
- `.agents/plugins/marketplace.json` — repo/team marketplace entry generated with the Codex plugin creator.
- `release/` — suite version, artifact identities, and channel policy.
- `schemas/` — portable upstream schema plus repository configuration schemas.
- `scripts/` — dependency-free deterministic build and validation tooling.
- `tests/` — build determinism and structure tests.
- `docs/` — architecture, compatibility, distribution, and release guidance.

Generated packages go to `dist/`, which is ignored by Git and recreated for CI or releases.

## Verify the scaffold

Requires Python 3.9 or newer and `make`:

```sh
make check
```

The command validates source metadata, builds all five artifacts twice in the tests, checks byte-for-byte determinism, and confirms that no runtime components have been added.

To build once:

```sh
make build
```

See [Architecture](docs/architecture.md), [Compatibility](docs/compatibility.md), [Distribution](docs/distribution.md), and [Releasing](docs/releasing.md).
