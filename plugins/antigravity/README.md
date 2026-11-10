# SeekOut for Antigravity

Use the **Find candidates** starter to search for people by role with your SeekOut account. The package includes the `sourcing` skill and connects to `https://mcp.seekout.io/v2/gemini`. Your SeekOut organization must have MCP access and an eligible license.

## Install a review candidate

Check out the commit supplied with the review invitation. From the package directory containing this README, run:

```sh
agy plugin validate --strict .
agy plugin install .
agy plugin list --json
```

Check that the enabled SeekOut entry shows version **0.2.0**, the expected installation path, and the `sourcing` skill. Open **Customizations → Installed → SeekOut → Accounts**, sign in to the plugin's SeekOut connection, and complete the browser flow. If the browser remembers another SeekOut account, use a separate browser profile for review. In the plugin's **MCP** tab, confirm that `search_candidates` is available.

## Try the two entry points

1. In a fresh conversation, type **CFO**. Expect a question about your intent. The first turn should show zero candidate searches.
2. Open the installed SeekOut plugin, click **Find candidates**, and send the prefilled message. When asked for the role, reply **CFO**. Expect current CFO results on that turn. Expand the execution details and confirm that the installed plugin's `search_candidates` handled the call. A call to `search_people` identifies the older connection.

Searches may consume credits. If a search returns an unknown outcome, record its request ID and tool name before deciding whether to retry. Include the package commit, client version and result when reporting a problem. Use the support channel for private troubleshooting details.

[SeekOut documentation](https://docs.seekout.com) · [Support](https://support.seekout.com) · [Privacy](https://www.seekout.com/privacy) · [Terms](https://www.seekout.com/terms)
