# Boolean syntax

Public-profile syntax; sourcing's query reference decides which constraints belong here.

## Fields

| Field | Matches |
| --- | --- |
| `cur_title:` | Current title; current-or-past titles require a structured requirement ([semantics](filter-semantics.md)) |
| `past_titles:` | Any past title |
| `headline:` | Headline, as a secondary constraint |
| `summary:`, `positions/description:` | Summary and job-description text |
| `full_name:`, `first_name:`, `last_name:`, `url:` | Person lookup |
| Unfielded text | Skills, summary, work history; use for tools/domains |
| `true:y` | Every profile; only inside an optional preferred-keyword group, never a required group or exclusion |

Other fields: `city:`, `state:`, `country:`, `schools:`, `majors:`, `degrees:`,
`grad_year:`, `languages:`, `projects:`, `publications:`, `patents:`,
`prev_locations:`, `industry:`, `li_industry:`, `volunteering:`, `groups:`,
`courses:`, `interests:`, `honors_awards:`. Anything with a structured requirement
goes there, not in the boolean.

Invalid: `prev_company:`, singular `past_company:`, `cur_co:`, `skills:()`,
`certifications:()`, `cur_seniority:`, structured-requirement names as fields,
and caret boosts (`^10`). Domains are quoted free text, not title-specialisation fields.

Locations, employers and years of experience belong in structured filters,
at the requested scope, tense and bounds. Company name patterns or independent
employer groups that those filters cannot express remain disclosed assessment
criteria; do not replace the filters with company-name boolean clauses.

## Operators and matching

| Syntax | Behaviour |
| --- | --- |
| `AND`, `OR`, `NOT` | AND is default; free-text NOT also excludes incidental mentions |
| `(A OR B) AND C` | Explicit grouping |
| `AND ("Kafka" OR "Apache Kafka" OR true:y)` | Preferred matches contribute to ranking; nonmatches remain eligible. No fixed rank or weight is promised. |
| `"data pipeline"` | Exact phrase; no operators inside quotes |
| `eng*`, `organi?ation` | `*` many characters, `?` one; no leading `*` |
| `"senior engineer"~1` | Phrase proximity; do not chain groups |
| `SDE2~` | Single-word fuzzy match, not phrases |
| `manager` | Stemming includes manage/managing/management; no plural lists |

Multi-word titles are automatically quoted; free-text phrases are not. Title
matching is whole-word: `NOT cur_title:("Staff")` excludes all titles containing
Staff. Compress level exclusions to bare level words.

## Patterns

Default public-profile shape: title alternatives, separate required families,
an optional preferred group, and unwanted title bands. OR expands one family;
AND preserves independent requirements. Omit groups the request does not need.

```text
cur_title:("Senior Data Engineer" OR "Sr Data Engineer")
AND ("Apache Spark" OR "Spark")
AND ("Apache Airflow" OR "Airflow")
AND ("Apache Kafka" OR "Kafka" OR true:y)
AND NOT cur_title:("Staff" OR "Principal" OR "Manager" OR "Director")
```

Here Spark and Airflow are required, Kafka is preferred, and the named title
bands are excluded. The optional group must stay parenthesized: a top-level
`OR true:y` would bypass the required groups. This syntax is specific to
SeekOut; do not copy `true:y` into another source's query language.

A requested branding phrase can constrain a headline while the role stays in
the title: `cur_title:("Product Manager") AND headline:("AI safety")`.
Level exclusion: `cur_title:("Engineer") AND "python" AND NOT cur_title:("Intern" OR "Junior")`.
