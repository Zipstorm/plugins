# Build the search

Translate each requirement into a supported filter, boolean term or explicit
profile-assessment condition. Use the source's actual schema; preserve the
recruiter's boolean unchanged when supplied. Read the full JD before assigning
importance. Responsibilities and company context do not make every word a
candidate requirement.

## Default boolean pattern

For a current role in public profiles, put same-function, same-level title alternatives inside
`cur_title:(...)`. AND independent required skill/domain families; OR synonyms
or acceptable alternatives within each. Skills a job description requires
together are separate keywords joined with AND, even when one line lists them;
only stated alternatives ("Go or Rust") share a group. Rank preferred keywords with
`AND (preferred_terms OR true:y)`. Exclude unwanted title bands with
`AND NOT cur_title:(...)`. Omit groups the request does not need.

Use the exact title plus close variants; keep generic titles tied to the
specialty using headline or summary evidence. A JD uses at most three required
keyword families. Other stated requirements remain required for assessment,
with useful keywords optionally ranked; say which are assessed. Do not move
an explicit credential or exclusion out of enforcement just to increase count.
For ambiguous technologies, include clear spellings such as Go/Golang and
check actual work evidence. [Boolean syntax](../../../references/packs/boolean-syntax.md)
contains the operators and a worked example; [title families](../../../references/packs/title-families.md)
helps with unusual titles and levels.

## Structured scope

Put locations, employers, experience and supported credentials in structured
filters. Preserve current, past, ever and excluded populations using the
[phrasing map](../../../references/packs/filter-semantics.md). Never add a
current-title restriction to a current-or-past or historical title request. For a role held at a
named employer, resolve the company and the full requested title family first, then use one
`position` with those `company_ids` and `title_ids`. If exit years are stated, its `start` and
`end` bound the year that same job ended, inclusively. For “left”, also exclude the employer
as current. An `alumni_filter` plus a current/past title or profile keyword does not bind
the role to that job. Use alumni alone only when no role-at-employer constraint was asked.
Do not invent entity references or substitute independent filters when resolution fails.

Qualitative
words such as “deep” create no numeric floor. Preferred locations, employers
and experience stay assessed rather than becoming mandatory filters.

Use cities/metros, states and countries at their actual scope; licence state
is not residence. Several geographic regions use one public search across
those regions, not duplicate searches. No place or market named means `index: "all"`,
with no residence filter. Do not infer North America from an omitted index or from unrelated
workspace context. For a stated place, consult
[locations and indexes](../../../references/packs/location-and-indexes.md) for
ambiguous places, radius, nicknames and defaults.

## Kinds of company

For a required employer class, first use an offered company power filter.
Otherwise build a sourced employer list, resolve its entities and disclose its
coverage. A person's industry is not their employer's industry. Never drop an
unresolved recruiter-named company or replace it with boolean text. Customer
markets are not employers. See [industries](../../../references/packs/industries.md)
for class construction and [power filters](../../../references/packs/power-filters.md)
for account-specific availability.

Use the specialist recipe for domain evidence instead of inventing filters.
For dated employment, tenure, graduation or other unusual conditions, follow
the tool's field meanings and the [filter semantics](../../../references/packs/filter-semantics.md).
If a source cannot enforce a condition, name it and assess the missing evidence;
never quietly claim the search enforced it.
