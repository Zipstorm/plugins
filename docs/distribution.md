# Install a specific version

Clone this repository, check out the commit or tag supplied with your review invitation, and run these commands from the repository root.

```sh
agy plugin validate . --strict
agy plugin install .
agy plugin list --json
```

The [Antigravity package](../plugins/antigravity/README.md) also supports installation directly from `plugins/antigravity/`. Its manifest, MCP configuration and rule are the source for the files that Antigravity discovers at the repository root. After updating them, run `python3 scripts/sync-antigravity-root.py`. Use `--check` to verify those files match. Both install paths use the same seven skill files.

Edit SeekOut’s license at the repository root. The same sync command copies it into the native package. The portable exporter carries the native license and third-party notices into the standalone download.

To check what a reviewer gets from GitHub, run **Verify Antigravity installation** on `main` in the repository’s Actions tab. It installs from the public URL on a fresh runner and compares the installed package with that revision.

## Agent Plugins 1.0

From the repository root, export a separate portable directory:

```sh
python3 scripts/export-antigravity-portable.py plugins/antigravity /tmp/seekout-portable
```

Choose a new output directory. The export carries the same skill and reference files and the same remote SeekOut connection as the native package. It writes the portable `plugin.json` and `mcp.json` for a client that supports the [Agent Plugins format](https://agent-plugins.org/). Antigravity's native installation also provides three suggested prompts and the SeekOut logo.
