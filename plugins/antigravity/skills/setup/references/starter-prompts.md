# End setup at the starters

The walkthrough's final question is setup's endpoint. Showing choices
or receiving a source answer does not select a recruiting task. Wait; do not
run intake or require a useful recruiting result as setup completion.

After the recruiter accepts a starter, map its title (without the benefit suffix)
to the corresponding [Home action](home-actions.md):

| Choice | Workflow |
| --- | --- |
| Find candidates | `find_candidates` |
| Figuring out who to target | `plan_role` |
| Understand what's possible in the market | `explore_market` |

A free-text answer to the starter question is also an accepted selection.
Route it once, without a third setup question: when it plainly means one of
these three, continue that action as above; when it names other work (outreach,
pipeline tracking), setup is complete and that request goes
to its owning skill. Never force it into one of the three starters. If it
selects no task, setup stays paused at the starters.

Only then continue that action's attached recipe once, through its owning skill.
The selected workflow owns role intake, its question budget, workspaces, results
and display. Setup's source/starter choices do not consume that intake budget.
Reuse any role facts already supplied rather than asking for them again. Do not
execute the other recipes or ask the recruiter to reconfirm the accepted starter.
A dismissed final question selects nothing and pauses setup.

Carry the chosen provider and verified connection state, deferred/declined
connections and any recruiter-supplied context into that workflow. Source choice
alone did not authorize content reads; the selected task determines the needed
scope and permissions. Separate illustrative examples from role facts. Preserve
required/preferred/excluded criteria, work arrangements, responsibilities,
provenance and unresolved gaps if the recruiter already supplied them.

An explicit task request outside onboarding goes directly to its owning skill,
including outreach or pipeline work. Do not restart setup to make it fit the
three starters. The selected task's supported operations and paid consent rules
still apply; a setup answer never substitutes for consent or saves a preference.
