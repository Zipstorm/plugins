# SeekOut for Antigravity

Find candidates, plan a role, evaluate talent, draft outreach, manage a pipeline and build reports with your SeekOut account. The plugin includes seven MCP V2 skills and connects to `https://mcp.seekout.io/v2/antigravity`. Your organization needs MCP access and an eligible SeekOut license.

## Install the review build

Check out the supplied commit and run these commands from `plugins/antigravity/`:

```sh
agy plugin validate . --strict
agy plugin install .
agy plugin list --json
```

Look for **SeekOut 0.3.2** on the plugin details page. A previously installed SeekOut pilot can hide the review build. Use a clean test profile or temporarily move the pilot outside the plugin directory and restart Antigravity. In Antigravity, open **Customizations → Installed → SeekOut → Accounts** and connect the supplied reviewer account. Choose that account in the browser if another account is already signed in. Return to the plugin's **MCP** tab to check its SeekOut connection. Its tools include `search_candidates`. The seven skills are `setup`, `intake`, `sourcing`, `interviewing`, `outreach`, `pipeline-management` and `reporting`.

## Test candidate search

1. In a fresh SeekOut conversation, enter **CFO**. Expect a question about what you want to do. The tool trace should show zero candidate searches.
2. In another fresh conversation, select the plugin's **Find candidates** starter and send it. Reply **CFO** when it asks for the role. Expect the plugin's V2 connection to run a search on that turn and return current CFO profiles. Check the tool trace for `search_candidates` on the plugin's SeekOut server. A `search_people` call belongs to a V1 connection.
3. Review the returned roles and scope in chat. A title search with no requested location should keep all regions in scope. A returned count alone does not verify that the intended people appeared.

Searches can use credits. If SeekOut reports an unknown outcome, keep the request ID and stop before running a second search. When reporting an issue, share the package revision, client version and tool name privately with support.

[SeekOut documentation](https://docs.seekout.com) · [Support](https://support.seekout.com) · [Privacy](https://www.seekout.com/privacy) · [Terms](https://www.seekout.com/terms)
