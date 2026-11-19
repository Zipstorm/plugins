# SeekOut for Antigravity

Find candidates, plan a role, evaluate talent, draft outreach, manage a pipeline and build reports with your SeekOut account. The plugin includes seven MCP V2 skills and connects to `https://mcp.seekout.io/v2/antigravity`. Your organization needs MCP access and an eligible SeekOut license.

## Install SeekOut

Install the latest published release from the public repository and confirm SeekOut is enabled.

```sh
agy plugin install https://github.com/Zipstorm/plugins
agy plugin list --json
```

To test a specific revision, including an unpublished candidate, check out the supplied review commit. From the directory containing this README and `plugin.json`, run:

```sh
agy plugin validate . --strict
agy plugin install .
agy plugin list --json
```

For this review commit, look for **SeekOut 0.3.7** on the plugin details page. A previously installed SeekOut pilot can hide the review build. Use a clean test profile or temporarily move the pilot outside the plugin directory and restart Antigravity. In Antigravity, open **Customizations → Installed → SeekOut → Accounts** and connect the supplied reviewer account. Choose that account in the browser if another account is already signed in. Return to the plugin's **MCP** tab to check its SeekOut connection. Its tools include `search_candidates`. The seven skills are `setup`, `intake`, `sourcing`, `interviewing`, `outreach`, `pipeline-management` and `reporting`.

## Try the three starters

Select each starter on the plugin details page and send the prepared message in a fresh conversation.

1. **Find people for my open role and show me why they match.** Reply **CFO** when asked for the role. Check that the plugin calls its V2 `search_candidates` tool across all regions and shows people with current CFO titles and employers in chat. In a separate fresh conversation, type **CFO** on its own. Expect a question about your intent and zero candidate searches.
2. **Compare the talent pool for my role in two locations.** Supply “Software engineers in Austin, Texas and Denver, Colorado.” Look for a measured count for each place with the same role, and compare the figures in chat with the tool output.
3. **Turn my job description into search criteria I can review.** Paste this sample: “Recruiting Operations Analyst. SQL and hands-on ATS reporting are required. Looker is preferred. The hiring manager also wants someone comfortable with startup pace.” Look for both requirements, the preference, and “startup pace” solely under questions for the hiring manager. The draft should appear in chat without a candidate search or a workspace change.

Searches can use credits. If SeekOut reports an unknown outcome, keep the request ID and stop before running a second search. When reporting an issue, share the package revision, client version and tool name privately with support.

[SeekOut documentation](https://docs.seekout.com) · [Support](https://support.seekout.com) · [Privacy](https://www.seekout.com/privacy) · [Terms](https://www.seekout.com/terms)

[Plugin license](LICENSE.md) · [Third-party notices](THIRD_PARTY_NOTICES.md)
