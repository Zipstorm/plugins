# Install a specific version

Check out the commit or tag supplied with your review invitation. The [Antigravity package](../plugins/antigravity/README.md) has its own manifest, connection settings, skills and installation instructions. Point the Antigravity installer at `plugins/antigravity/`.

## Agent Plugins 1.0

From the repository root, export a separate portable directory:

```sh
python3 scripts/export-antigravity-portable.py plugins/antigravity /tmp/seekout-portable
```

Choose a new output directory. The export carries the same skill and reference files and the same remote SeekOut connection as the native package. It writes the portable `plugin.json` and `mcp.json` for a client that supports the [Agent Plugins format](https://agent-plugins.org/). Antigravity's native installation also provides the **Find candidates** starter and SeekOut logo.
