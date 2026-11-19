---
name: setup
description: Set up SeekOut with useful context sources and optional connections, ending at the three starters; explain capabilities or change a standing workflow preference. Opening SeekOut alone does not start onboarding.
---

# Set up SeekOut

When the recruiter selects SeekOut’s **Find candidates** starter, follow sourcing even if the client attaches another skill. Use the role and constraints in this conversation. If the role is missing, ask only “What role should I search for?” in chat and wait. A title in reply is enough to run the installed SeekOut connection’s `search_candidates` on that turn and show matching profiles. In the chat reply, give up to three returned names with their current roles and companies, plus a returned profile link when available. Include this list even after a results-view tool runs. Looking up saved roles, drafting outreach or saving a screening rubric requires its own request.

When a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do.

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
