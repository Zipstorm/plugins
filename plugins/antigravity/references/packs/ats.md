# ATS pack

For ATS search/provider vocabulary. Sourcing owns rediscovery; pipeline management
owns pipeline questions, compliance and exports. Status/stage/job/reason/source/
recruiter values are connection-specific and case-sensitive; wrong values can
silently produce empty/partial results. Look them up first.

## What the ATS holds

Combine profile criteria (titles, employers, locations, schools, skills,
seniority, industry, credentials and experience) with application criteria:
`status`, `current_stage`, `source`, `job_id`, `requisition_id`, `rejection_reason`,
`recruiter`, `application_type` and `last_updated`.

- `last_updated`: `moreThan:<months>` or `lessThan:<months>`, in whole months.
  It measures activity, not time in stage; translating weeks/days broadens scope.
  Idle candidates need the provider's in-process status plus last activity.
- Jobs/requisitions use `id / name`. Application type distinguishes applicants
  from sourced prospects where supported.
- Read applied/ignored filters: unsupported filters may be refused or ignored.
  Never include an ignored constraint in the reported count's scope.
- Source is searchable but absent from results. Stage/recruiter/rejection facets
  are top values and all-time; only the applied-date timeline is per-period.
  For exact req totals, count the req-scoped search. Preserve completeness warnings.

## Provider vocabularies

These are orientation, not substitutes for live connection values:

| Provider | Status/stage | Other distinctions |
| --- | --- | --- |
| Ashby | HIRED, PENDING, DECLINED; org-named stages separate | Free-text rejection reasons; prospects by application type |
| Greenhouse | active, rejected, hired, converted; milestones/interview stages separate | Prospects convert on application; rejection buckets: They are not interested, We are not interested, Hired, Other; screening-answer count only, never answers |
| iCIMS | Stage doubles as status; opaque status values | Prospects use folders; sample stages from pipeline (no suggestions); disposition reasons often empty |
| Workday | REVIEW, REJECTED, INTERVIEW, DECLINED, HIRED, ASSESSMENT, SCREEN, REFERENCE, OFFER, BACKGROUND; same stage vocabulary | Sparse req-specific reasons; configured application types; current step is a result-only sub-stage |

Silver medallists use rejected (Greenhouse) or DECLINED (Ashby), paired with
actual reasons. Workday REJECTED versus DECLINED is undefined here; verify.
Current-step questions may be answered from Workday results but cannot filter it.

## Compliance patterns

Use these safeguards for pipeline questions. Refuse protected-group
pipeline comparisons, salary-history screening, individual hiring/acceptance/
ghosting predictions, culture-fit/likeability scores and verbatim personnel feedback.
For pay-transparency or EU candidate-data questions, identify the jurisdiction and
organisation policy/lawful basis and direct applicability to the responsible owner;
do not turn a fixed template into legal advice.

Answer legitimate parts of a mixed request. Route protected-characteristic
reporting to the organization's segregated EEO process; use the approved role
band instead of salary history, and sourced criterion summaries or rejection
reason aggregates instead of verbatim personnel feedback. Do not approximate
a refused figure from other counts or hide a discriminatory rationale in a
neutral disposition code. Current status remains a snapshot, not a prediction.
