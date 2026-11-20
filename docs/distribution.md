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

## Check recruiting tasks in Antigravity

Use a fresh profile for the revision under review so an older SeekOut installation cannot handle the prompts. Under **Customizations → Installed → SeekOut**, confirm the version matches the manifest. Connect the account shared privately for review under **Accounts**. Open a fresh conversation for each check.

| Start with | Continue with | Expected behavior |
| --- | --- | --- |
| The starter to find people for an open role | Answer “CFO” | SeekOut searches on that turn and shows returned people, their current roles and why they match. |
| “CFO” on its own | — | Antigravity asks what you want to do before running a candidate search. |
| The starter to compare talent pools | “Software engineers in Austin, Texas and Denver, Colorado” | SeekOut measures the same role in both places and shows each returned count. |
| The starter to turn a job description into criteria | “Recruiting Operations Analyst. SQL and ATS reporting are required. Looker is preferred. The hiring manager wants someone comfortable with startup pace.” | The draft separates the two requirements from the preference and asks what “startup pace” means. The conversation ends with a draft until you request a search or save. |

To check skill discovery, start each example in a new conversation. The middle prompt should select the named skill. The last prompt should leave all SeekOut skills and tools idle.

| Skill | Recruiting prompt | Unrelated prompt |
| --- | --- | --- |
| `intake` | Turn these hiring-manager notes into requirements for the new backend engineer role. | Turn these product kickoff notes into a project brief. |
| `interviewing` | Help me prepare for tomorrow's panel interview with a candidate for our backend engineer role. | Help me prepare for tomorrow's quarterly product roadmap meeting. |
| `outreach` | Draft a first message inviting a candidate to discuss our open backend engineer role. | Draft a first message to a prospective customer about our product. |
| `pipeline-management` | Which candidates for our backend engineer role are at the onsite stage in our ATS? | Which deals in our sales pipeline are at the negotiation stage? |
| `reporting` | Write a weekly recruiting funnel digest with pass-through rates for the backend engineer role. | Write a weekly digest of product launches and customer feedback. |
| `setup` | Help me connect my recruiting account to the SeekOut plugin. | Help me connect my accounting software to my bank. |
| `sourcing` | Find backend engineers for my open role in Austin. | Find vendors for a new payroll system. |

Also try “Find time for my dentist appointment.” Scheduling a personal appointment should leave SeekOut idle.

For issues, report the package commit, Antigravity version, and which prompt or step failed. Share account details and live candidate results privately.

## Agent Plugins 1.0

From the repository root, export a separate portable directory:

```sh
python3 scripts/export-antigravity-portable.py plugins/antigravity /tmp/seekout-portable
```

Choose a new output directory. The export carries the same skill and reference files and the same remote SeekOut connection as the native package. It writes the portable `plugin.json` and `mcp.json` for a client that supports the [Agent Plugins format](https://agent-plugins.org/). Antigravity's native installation also provides three suggested prompts and the SeekOut logo.
