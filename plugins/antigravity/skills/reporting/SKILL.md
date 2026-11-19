---
name: reporting
description: Answer role, market and pipeline questions with insight reports, maps, requirement trade-offs, updates and digests. Revise the current report for follow-up questions and what-ifs.
---

# Build an insight

Follow the starter the recruiter sent, even if Antigravity attaches a different skill. Use the information already in this conversation. A reply to a starter supplies the missing input for that same task.

- **Find people for my open role and show me why they match.** Use sourcing. If the role is missing, ask “What role are you hiring for?” in chat. A title in reply is enough to run the installed SeekOut connection’s `search_candidates` on that turn. For a public search without a location, explicitly set `request.index` to `"all"` and leave location filters empty. Show up to three returned people in chat with their current title, employer, a detail that supports the requested match, and a profile link when available. For a title-only request, the current title is the evidence.
- **Compare the talent pool for my role in two locations.** Use reporting. Ask only for the missing role or locations. Measure the same role and criteria in each place. Show each place’s returned count in chat, with its geographic scope. If a place is unmeasured, say which one.
- **Turn my job description into search criteria I can review.** Use intake. Read the pasted or attached description, or ask for it. Draft the required and preferred criteria in chat and flag any ambiguity for the recruiter. A search, a saved brief or a saved rubric needs its own request.

When a fresh conversation contains only a role such as “CFO”, ask what the recruiter wants to do.

A job description for a role starts its
[role overview](../../references/role-overview.md); a report answers what the
overview does not.

Answer simple count/status questions directly. Build requested reports in
SeekOut, which measures modules and keeps them in the role's workspace. Reuse
criteria and answers. Read the [build guide](../../references/report-building.md)
and relevant recipes ([market report](references/market-report.md) for broad
asks). Related modules are optional: investigate useful leads, then retain only
the visuals that explain the decision. Stop when the requested question is answered.
A file the recruiter asks for (a PDF, a one-pager) follows
[deliverables](../../references/deliverables.md).

Use the explicit target, otherwise this conversation's current work, then
consistent visible context. Ask only about remaining material ambiguity; keep
unrelated chats and roles separate. Report follow-ups and what-ifs create its
next version. Search, candidate and outreach follow-ups belong to those workflows.

| The recruiter wants to know | Module |
|---|---|
| Where the talent is | [Talent map](references/talent-map.md) (`talent_map`) |
| One market's employers, titles, skills, seniority | [Market overview](references/market-overview.md) (`market_profile`, one place) |
| Markets' totals compared | [Market comparison](references/market-comparison.md) (`market_profile`, several places) |
| Each requirement's effect on the pool | [Requirement trade-offs](references/requirement-tradeoffs.md) (`requirement_tradeoffs`) |
| Where a company's people come from/go | [Company talent flow](references/company-flow.md) (`company_flow`) |
| An industry's employers in a place | [Company landscape](references/company-landscape.md) (`company_landscape`) |
| Who internally could fill the role | [Internal talent](references/internal-talent.md) (`internal_talent`) |
| Workspace outreach performance | [Outreach analytics](references/outreach-analytics.md) (`outreach_metrics`) |

Role-based modules share one baseline: the existing search, else one search of the role.
Maps, overviews and trade-offs name places or changes from it; SeekOut measures
variants at creation, without separate per-market/requirement calls. Place
modules in the surrounding body. Other insights use SeekOut reads alone:
[pipeline update](references/pipeline-update.md),
[hiring manager update](references/hiring-manager-update.md),
[weekly digest](references/digest.md),
[funnel / source analysis](references/funnel-diagnosis.md),
[push-back brief](references/pushback-brief.md) (around requirement trade-offs)
and [job description](references/job-description.md) (body alone).

## Ask as you learn

Planning clarifies what matters; exploration asks the market question only
when unsaid. Reuse context, accepting partial briefs. Use the client's question
tool for at most three questions total, including this starter's opening; never
ask for module choices. Non-role questions skip role intake, JD and rubric.
A declined or dismissed question pauses the starter until the recruiter supplies
context or asks to continue; never substitute an unrelated role.

Measure, read facts, then write. Preserve the baseline; what-ifs stay hypothetical.
An explicit change needs no reconfirmation and re-measures dependent modules.
Ask only when the next action needs an unaccepted change; leave it pending if
the question budget is spent.

## Next steps and the recommended option

For role plans, recommend baseline evidence review and at most one conditional
alternative: inspect a hypothetical variant or draft a hiring-manager push-back.
For market exploration, give one next action that follows the finding, usually
opening the recommended search. Non-role questions get a relevant investigation,
not an automatic sourcing offer. Other report types may have up to five useful
next steps, recommendation first with its evidence.
Opening, branching or screening a search cites its report ref: baseline or
variant as applicable. Outreach, advancing, contacts and email drafts cite none.
Never screen a hypothetical changed-requirement pool
against an incompatible unchanged rubric. Continue already-requested steps; otherwise recommend
them. Drafting an email does not authorize sending it.

## The rubric

One rubric per workspace, up to 10 named criteria with profile questions:
required, preferred (rank keeps) and excluded (deal-breakers). Role planning saves
the recruiter's stated requirements and confirmed interpretations; market findings
never silently downgrade them. Otherwise save/edit only when asked. Candidate
screening uses the newest rubric unchanged. A role with an overview has its
requirements as its rubric ([criteria](../../references/criteria.md)): change
them on the overview, never in a separate rubric.

Only for separate research requests: [company brief](references/company-brief.md)
or [pay](references/pay.md). **Sourcing** owns candidate discovery;
**pipeline-management** owns record changes.

For host forms, presentation and connected systems, read [client guidance](client-adapter.md).
