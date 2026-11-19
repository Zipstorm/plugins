---
name: pipeline-management
description: Save or list a role's candidates, export profiles, read ATS pipeline status, update recruiting records and track candidate-update commitments. Reporting owns performance reports and analytics.
---

# Keep recruiting records useful and current

Follow the starter the recruiter sent, even if Antigravity attaches a different skill. Use the information already in this conversation. A reply to a starter supplies the missing input for that same task.

- **Find people for my open role and show me why they match.** Use sourcing. If the role is missing, ask “What role are you hiring for?” in chat. A title in reply is enough to run the installed SeekOut connection’s `search_candidates` on that turn. For a public search without a location, explicitly set `request.index` to `"all"` and leave location filters empty. Show up to three returned people in chat with their current title, employer, a detail that supports the requested match, and a profile link when available. For a title-only request, the current title is the evidence.
- **Compare the talent pool for my role in two locations.** Use reporting. Ask only for the missing role or locations. Measure the same role and criteria in each place. Show each place’s returned count in chat, with its geographic scope. If a place is unmeasured, say which one.
- **Turn my job description into search criteria I can review.** Use intake. Read the pasted or attached description, or ask for it. Draft the explicit requirements and preferences in chat. Put vague language or unclear priority only under “Questions for the hiring manager”. Ask what observable work the phrase describes before assigning a priority or using a proxy. The supplied description is input to this draft. The MCP instructions for recording a job description in a workspace apply to a requested role plan or save. A search also needs its own request.

When a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do.

Start with the requested people, role and destination. Use the recruiter's
explicit target first, otherwise this conversation's current work item, then
visible context consistent with that work. Ask only if the target remains
materially ambiguous; keep unrelated chats and roles separate. Keep the
workspace, search, ATS connection and application explicit before a write.

Use SeekOut to save the candidates the recruiter selects to the role's
workspace, list who is saved there, read and set where each of them stands,
and export people to a spreadsheet or the connected ATS. When the current work is a
workspace's candidates, a follow-up such as "more like these" or "drop the last two" uses
that workspace's candidates. **Sourcing** finds additional people; it does not
silently add them to the workspace.

A SeekOut workspace holds the candidates picked for a role and each one's
status there. An ATS holds applications and stages. Saving to one, or setting a
status in one, does not update the other, and an assessment is not a human
disposition.

Choose the work requested:

- [Saved people](references/project-records.md): save or list candidates.
- [Candidate status](references/candidate-status.md): who was contacted,
  replied or is interested, in one workspace or across roles; set or correct it.
- [Screening](../../references/screening.md): judge a batch for the workspace, and what to recommend when it keeps no one;
  when your SeekOut tools can save candidate evaluations, evaluate a search's top people and save every evaluation.
- [ATS pipeline](references/ats-read.md): current applications, stages, counts and stalled work.
- [Record changes](references/change-plans.md): notes, dispositions, requisitions and postings.
- [Exports](references/export.md): files or ATS pushes with confirmed destinations.
- [Candidate updates](references/candidate-updates.md): commitments, owners and next actions.

When the workspace holds the candidates the recruiter wants, recommend how to reach
them and why (**outreach**), weighing the workspace's suggested next step.
Carry out an already-requested next step; otherwise leave it as a recommendation.

Use the relevant [connector guidance](../../references/connectors/README.md).
Report actual results and unresolved items. A proposal is useful when a write
is unavailable, but does not complete a request to save or change something.

Keep source, date, scope and missing evidence visible. Follow the
[ATS evidence and safeguards](../../references/packs/ats.md).
Sourcing finds people; interviewing assesses them; outreach writes/sends messages;
reporting turns evidence into stakeholder updates and analytics.

For host forms, presentation and connected systems, read [client guidance](client-adapter.md).
