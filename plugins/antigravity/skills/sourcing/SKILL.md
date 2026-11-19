---
name: sourcing
description: Find, refine or reopen candidate searches, or find similar people, for a role. A follow-up about the current report belongs to reporting.
---

# Find the right people

Follow the starter the recruiter sent, even if Antigravity attaches a different skill. Use the information already in this conversation. A reply to a starter supplies the missing input for that same task.

- **Find people for my open role and show me why they match.** Use sourcing. If the role is missing, ask “What role are you hiring for?” in chat. A title in reply is enough to run the installed SeekOut connection’s `search_candidates` on that turn. For a public search without a location, explicitly set `request.index` to `"all"` and leave location filters empty. Show up to three returned people in chat with their current title, employer, a detail that supports the requested match, and a profile link when available. For a title-only request, the current title is the evidence.
- **Compare the talent pool for my role in two locations.** Use reporting. Ask only for the missing role or locations. Measure the same role and criteria in each place. Show each place’s returned count in chat, with its geographic scope. If a place is unmeasured, say which one.
- **Turn my job description into search criteria I can review.** Use intake. Read the pasted or attached description, or ask for it. Draft the required and preferred criteria in chat and flag any ambiguity for the recruiter. The supplied description is input to this draft. The MCP instructions for recording a job description in a workspace apply to a requested role plan or save. A search also needs its own request.

When a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do.

Turn the recruiter's requirements into a SeekOut search, inspect the people it
returns, and explain the result. Use SeekOut to run and change searches, read
more results or a candidate's full profile, find a named person from their name
or profile link, and reopen a saved search. Run direct search requests now;
do not insert intake or an acceptance step. A role named without saying whether
to find people now or plan it first is not yet a direct request: ask that once,
as **intake** does. Reuse the role's existing criteria
and workspace.

Use the recruiter's explicit target first, otherwise this conversation's
current work item, then visible context consistent with that work. Ask only
if the target remains materially ambiguous; keep unrelated chats and roles
separate. Run every candidate search in SeekOut. Use the role's workspace for work on that role. A follow-up about the current search refines it; a what-if creates
a labelled search beside it. A follow-up about the role's current
[overview](../../references/role-overview.md) changes the overview and saves it
again (**intake**).
A follow-up about the current report (a plan's
trade-offs or talent map) revises that report instead (**reporting**).

Preserve required, preferred and excluded criteria, including alternatives and
employer tense. With no requested place or market, explicitly search all regions (`index: "all"`);
never add North America or inherit an unrelated workspace’s geography. A role held at a named
employer belongs in one `position` filter with resolved company and title references, including
exit-year bounds when stated; it is not a current-title requirement. Add no unstated
qualifications or numeric thresholds. Check
returned filters and candidate evidence before calling a search successful;
counts and search rank do not prove fit. Report a valid empty result honestly.

Use [query construction](references/query.md) and [running a search](references/run.md).
For a thin or mismatched pool, use [bounded refinement](references/refine.md);
fix your interpretation before proposing any change to the recruiter's bar.
Present results in SeekOut with a short explanation of scope and limitations.

After presenting the results, give your best-effort read on whether the
search is ready to pick candidates from and ask the recruiter whether to start
picking or refine ([ready to pick candidates?](references/refine.md#ready-to-pick-candidates)).
Carry out an already-requested step to pick candidates without asking. Once the
recruiter chooses to pick candidates, follow **pipeline-management** and its
[screening](../../references/screening.md); when screening keeps no one, say
what blocked it and recommend one next step.

Read only the recipe the work needs:

- [Defence, clearance and federal roles](../../references/packs/cleared.md)
- [Nursing](../../references/packs/nursing.md), [other clinicians](../../references/packs/healthcare.md)
- [GitHub and open source](../../references/packs/github.md), [research](../../references/packs/academic.md)
- [Employees or past applicants](references/internal.md)
- [Named people or lookalikes](references/find-similar.md)
- [Other sources and combined slates](references/other-sources.md)
- [Confidential searches, referrals and proactive pools](references/other-asks.md)
- [Japan](../../references/packs/market-japan.md)

To plan a role from its job description, build its
[role overview](../../references/role-overview.md).
For a measured plan beyond it, use [plan a role](../../references/report-building.md).
**Intake** defines the role; **interviewing** assesses named people;
**reporting** measures markets; **pipeline-management** saves candidates.

For host forms, presentation and connected systems, read [client guidance](client-adapter.md).
