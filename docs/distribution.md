# Distribution and updates

## Initial path

The first supported catalog shape is the repo/team Codex marketplace at `.agents/plugins/marketplace.json`, pointing to `plugins/recruiting-codex`. The file was created by the installed Codex plugin creator and is validated in CI. This task does not install that marketplace or modify a personal marketplace outside the repository.

For a non-default repo marketplace, a maintainer may explicitly add the repository marketplace root to Codex and then install `recruiting-codex@personal`. Treat this as a scaffold smoke test only: the plugin currently provides no behavior. Start a new Codex task after reinstalling an updated local plugin so component discovery uses the new package state.

## Future paths

GitHub Releases should publish the immutable ZIP archives, `release-manifest.json`, and `CHECKSUMS.sha256` created by `make build`. Package registries may be added later as transport layers, but must preserve artifact names, suite versions, and digests rather than rebuilding or renaming content.

Claude Code, Cursor, and Antigravity installation instructions are intentionally absent until native package formats are selected and verified. Do not copy guessed config files into client discovery locations.
