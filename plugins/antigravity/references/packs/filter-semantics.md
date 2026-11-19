# Filter semantics

Canonical employer/title tense and location-exclusion map. Use it when translating
a request into populations.

## Populations

Employers and titles each come in the same eight scopes.

| Scope | Includes | Excludes |
| --- | --- | --- |
| Current | Currently at X, or currently holds X | Not currently X; a past X is fine |
| Current or past | Currently or ever X | Never X, current or past |
| Most recent past | The most recent past job or role is X (one job) | The most recent past job or role is not X |
| Any past | Any past job or role is X, including the most recent | No past stint as X; people currently X stay |

Most recent past is a strict subset of any past. The current-or-past employer
scope holds one OR-set. If a request needs two independent employer groups
that the available structured filters cannot express, disclose that limitation
and assess the missing condition from employment evidence. Never flatten the
groups into one OR-set or substitute company-name boolean clauses. "Worked
at", "former", "ex-" and "just left" never mean current alone.

A current title is the boolean's `cur_title:()` clause. An "is or was" title
requirement already carries the title, so never add `cur_title:()` for the same
title as well.

## Phrasing map

| Recruiter says | Population |
| --- | --- |
| "currently at X", "now at X", "at X", "most recently at X", "X engineers" | Currently at X |
| "worked at X", "who've worked at X", "X experience", "X background", "X pedigree" | Currently or ever at X |
| "ex-X", "former X", "formerly at X", "previously at X", "used to work at X", "X alumni" | Ever at X, and not currently at X |
| "recently left X", "just left X", "last worked at X" | Most recent past employer is X |
| "had a past job at X" (whether or not they are there now) | A past employer is X |
| "worked at X earlier, but not in their last job" | A past employer is X, and the most recent past employer is not X |
| "not currently at X" | Not currently at X |
| "never worked at X", "no X background" | Never at X, current or past |
| "exclude anyone who used to work at X", "exclude ex-X" | No past stint at X |
| "exclude anyone who just left X", "whose last job was at X" | Most recent past employer is not X |
| "is or was a T", "currently or previously a T", "at any point" | Currently or ever a T |
| "used to be a T", "former T", "was previously a T" | A past role is T |
| "whose most recent role was T", "last role was T" | Most recent past role is T |
| "not currently a T" | Not currently a T |
| "never been a T" | Never a T, current or past |
| "exclude former Ts", "skip anyone who was previously a T" | No past role as T |
| "exclude anyone whose last role was T" | Most recent past role is not T |

Places take the same include and exclude:

| Recruiter says | Population |
| --- | --- |
| "in X but not Y", "X, excluding Y", "X except Y" | In X, and not in Y |
| "anywhere except Y", "not in Y" | Not in Y |

"From X" depends on the ask: in a direct role slate it means current; when the
ask is about background or pedigree it means current or past. An exclusion with
no tense ("no one from X") leaves out people there now: search with it, and say
that people who used to work there can be left out too.

## Worked examples

“Exclude anyone who used to work at Amazon” means no past stint there, not
“never at Amazon” (also excludes current-only staff), and not “most recent past
is not Amazon” (misses earlier stints). “Is or was Product Manager” uses the
current-or-past title requirement without an additional `cur_title:()`.

## Employer and role on the same job

When the ask names a role held at a particular employer, resolve the company and
the complete requested title family, then put their returned references together
in `position.company_ids` and `position.title_ids`. Optional `start` and `end` are
inclusive bounds on that job’s ending year, not its starting year. For “left”,
also exclude that employer as current. Do not add `cur_title` for this historical
role: someone who later changed roles still qualifies. `alumni_filter` plus an
independent title or profile keyword can match different jobs; use alumni alone
only when no role-at-employer constraint is stated. A resolution failure is a
blocked criterion to report, never permission to invent a reference or loosen it.
