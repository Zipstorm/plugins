---
name: setup
description: Open SeekOut Home, connect a recruiting account to SeekOut, choose context sources, learn what the plugin can do, or change a SeekOut workflow preference. Don't use for employee onboarding plans, general IT support, or configuring unrelated apps.
---

# Set up SeekOut

Use these instructions for SeekOut recruiting tasks. For unrelated requests, use the client's usual workflow and leave SeekOut tools idle. If a fresh conversation contains only a role such as “CFO”, ask what the user wants to do.

Follow the starter the recruiter sent, even if Antigravity attaches a different skill. Use the information already in this conversation. A reply to a starter supplies the missing input for that same task.

- **Use SeekOut to find people for my open role and show me why they match.** Use sourcing. If the role is missing, ask “What role are you hiring for?” in chat. A title in reply is enough to run the installed SeekOut connection’s `search_candidates` on that turn. For a public search without a location, explicitly set `request.index` to `"all"` and leave location filters empty. Show up to three returned people in chat with their current title, employer, a detail that supports the requested match, and a profile link when available. For a title-only request, the current title is the evidence.
- **Use SeekOut to compare the talent pool for my role in two locations.** Use reporting. Ask only for the missing role or locations. Measure the same role and criteria in each place. Show each place’s returned count in chat, with its geographic scope. If a place is unmeasured, say which one.
- **Use SeekOut to turn my job description into search criteria I can review.** Use intake. Read the pasted or attached description, or ask for it. Draft the explicit requirements and preferences in chat. Put vague language or unclear priority only under “Questions for the hiring manager”. Ask what observable work the phrase describes before assigning a priority or using a proxy. The supplied description is input to this draft. The MCP instructions for recording a job description in a workspace apply to a requested role plan or save. A search also needs its own request.

Setup prepares the recruiter to choose their first task. It ends at the three
starters and waits; role intake, searches and measurements belong to the selected
workflow afterward. Opening SeekOut alone opens Home, not onboarding. An
explicit recruiting task goes to its owning skill without a setup detour.

| Request | Read |
| --- | --- |
| First-time setup or starting over | [Walkthrough](references/walkthrough.md) |
| Connections or a changed provider | [Their environment](references/get-started.md) |
| Which plugins or connectors would help | [Connections by use case](references/plugin-recommendations.md) |
| Standing preferences or other workflows | [Make it mine](references/make-it-mine.md) |

## One question path, two decisions

Ask the source and starter choices with your own question tool, as client guidance
says, and reuse the same one after connection decisions. Follow the current
schema of what you use; a host question skill is discovered and read before the
first question. Do not substitute a SeekOut form, another tool or invented form
syntax. If none is available, explain that limitation and stop. Ask in plain chat only where client guidance permits it, or
where no client guidance names a mechanism and no question tool is offered.

Setup asks at most two questions total, each in its own turn: the context source
and the starters. Skip known answers; a built-in free-text alternative names
another source for that same decision. A connection card is a separate optional decision, never
shown alongside a pending starter question. Do not add a role, JD, account,
workspace, preferences or readiness questionnaire. A dismissed question pauses
setup. Selecting Skip connections or declining a connection advances to the
starters; neither selects a task.

## Prepare, then stop

Follow the walkthrough's source question → concrete example → optional
connection decision → starters sequence. Keep the example in the final visible
response after tools, not only preliminary commentary. Keep paragraphs to at
most two sentences; no account audits, recommendation-history labels or feature
catalogues.

During onboarding, inspect only the chosen provider's connection metadata and
relevant directory entries. A source choice permits a relevant recommendation,
not reading private documents, messages or ATS jobs. Installation, sign-in and
usable read access are distinct; never claim a successful read from metadata.
Do not create workspaces, JDs, rubrics, searches, reports or standing preferences.
Optional connections never block the final starter choice.

The [starter handoff](references/starter-prompts.md) maps the final choices to
[Home actions](references/home-actions.md). Wait for the recruiter's selection;
then that workflow owns its intake, question budget, supported writes and result
delivery. Preserve supplied context without inventing missing facts. Explicit
preference changes and paid actions retain their own supported workflows.

For host forms, presentation and connected systems, read [client guidance](client-adapter.md).
