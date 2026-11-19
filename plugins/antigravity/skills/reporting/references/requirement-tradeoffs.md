# Requirement trade-offs

The report's baseline search is the role as stated (a job description that
names its requirements is enough). Trade-offs name only the changes from it,
one to twelve, each changing one negotiable requirement and preserving every
other anchor:

- another place: `{place: "Austin, TX"}`;
- a requirement added: `{add: {companies: ["Snowflake"]}}`;
- a requirement dropped, whole or one value: `{drop: "degrees"}`,
  `{drop: {companies: "Databricks"}}`;
- a requirement loosened: `{widen: {years_of_experience: {min: 3}}}`.

Filter names are the search's own filters; a skill written in the search's
boolean is not a filter, so a change cannot add or drop it. SeekOut derives each
variant from the baseline, saves it in the workspace, labels it from its change
("Plus Snowflake", "Without degrees") and counts it: never search each variant yourself, and
never invent a change the recruiter or job description does not support.
Preferred skills remain preferences in the baseline. A variant changes one
thing; a cumulative stack of changes is not an independent relaxation.

A talent map beside it maps the same baseline. Once the variants are measured,
write the body around them: what each requirement costs, recommended options
and the decisions for the hiring manager. The option you recommend is the one
the next steps cite first, by its variant's report ref. Show measured counts,
not invented drops, estimates or ranking weights. Keep comparisons hypothetical
until accepted. A bigger pool alone does not establish candidate fit or a
reason to relax a legitimate requirement.
