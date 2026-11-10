# Distributing SeekOut recruiting skills

## Source and layout

Authors edit the skill catalog and client packages in the private MCP repository beside the V2 skill composer. The catalog owns each skill's name, recruiting purpose, supported clients and behavior examples. Each client owns its discovery description and instructions. It can rewrite the full skill or offer a skill exclusive to that client. Changing a common example schedules evaluation for every client offering the skill. A client whose wording already passes needs no rewrite.

Export each reviewed client package into its own install root. For example, an Antigravity package with a sourcing skill would look like this:

```text
plugins/antigravity/
  plugin.json                     portable identity and version
  mcp.json                        portable MCP connection
  .antigravity-plugin/plugin.json  native metadata and starter prompts
  mcp_config.json                 native MCP connection
  skills/sourcing/SKILL.md        recruiting guidance for this client
  assets/
  README.md                       installation and reviewer walkthrough
```

Use the same portable layout under `plugins/claude-code/` and `plugins/cursor/`. Add a native manifest or marketplace entry where the host requires one. Generate or check overlapping names, versions and endpoints against the same source. Keep exports self-contained so a reviewer can install a client directory from a checkout of one commit. Only distributable package files belong in the export. Keep account credentials, live results and release records in their private systems. [Agent Plugins format](https://agent-plugins.org/) · [Client compatibility](https://agent-plugins.org/compatible-clients)

## What a passing sourcing update looks like

| Recruiter action | Expected first turn |
| --- | --- |
| Type only “CFO” in a fresh chat | Ask what they want to do. The trace shows zero candidate searches. |
| Start **Find candidates**, send it if the client prefills the composer, then reply “CFO” | Search for current CFOs using the package's configured connection and show the results. |

Test the actual entry point on each client. Record a missing starter if the client lacks it. When an installed skill and an MCP-served copy coexist, use the installed copy when its presence in the session is established. A client name alone cannot establish installation. Preserve direct MCP access when the session's skill source is unknown.

## Publishing one client

1. Export the candidate from a known source revision and check the file list, portable schemas, native manifest and endpoint. Record the candidate commit and package path.
2. Install that revision in the intended client. Verify which copy loaded. Test wording changes live with a signed-in reviewer account. Changes to setup or OAuth also require a fresh sign-in. Record the client version, entry action, tool name and server, and whether results appeared. A second active connection can produce a convincing result using the wrong server.
3. After the live cases pass, publish the tested package and create its client tag. Give the reviewer the repository link, tag, commit, package path and client guide. Share test credentials privately. Where a marketplace fetches the repo itself, confirm the revision and directory it actually loaded.
4. Have the release workflow update one private table keyed by client. Keep the latest candidate and test result separate from the shipped tag and commit, and record any hold reason. A failed candidate leaves the previous release available. Other clients can advance independently.
5. Read back the published tag and check a fresh installation. If a publish or status update fails, reconcile the table against the published files before retrying. A delayed retry must preserve a newer shipped revision. For a rollback, publish the last passing contents under a new version and tag, then verify both a fresh install and the update path for an existing install.
