# Watches

Reporting and sourcing can schedule repeated measurements or searches through a
client scheduler that can call SeekOut. Where the connection offers candidate
monitors, SeekOut can also keep checking a saved search of the global sources
itself, once a week, and keep the people newly in its top results; it sends no
message, so the recruiter asks to see what is new. A monitor cannot watch ATS or
internal talent searches, and its search cannot be edited. Everything else below
runs only through a client scheduler.

## What can be watched

| Watch | Repeat | Notify when |
| --- | --- | --- |
| Market | As-written count and decisive what-ifs | A count moves by at least 10% or 10 profiles, whichever is larger |
| Company talent | Departures, hires, top alumni destinations | Counts move as above or a new employer enters the top three |
| Req/pipeline | As-written count and permitted ATS stage counts ([systems](connectors/README.md)) | A stage moves or a recruiter-specified age threshold passes |
| New matches | Accepted search's first page | A fitting person is new to the role |

Use few searches; limits are shared with the recruiter's work.

### New-match alerts

Read known people from the [role workspace](project.md), permitted ATS or prior
passed-on candidates. Keep identities there, never in memory or scheduled
instructions. Each run reopens the kept search from the workspace/recent searches,
not a new search. Read its first page when ready; exclude known people and
candidates its evidence rules out. If it needs refinement or an answer, report
that the recruiter is needed.

## Setting one up

- Without a capable scheduler, do one run and offer no watch. Otherwise offer
  once per role at hand-off, or create one when requested.
- Read standing time zone, cadence and quiet-week choices; ask only missing
  ones and [remember](memory.md) them where supported.
- Make the instruction self-contained: role/company, full measurement scopes,
  baseline location, schedule, brief format, quiet conditions, and “measure and
  brief only; do not change records.” Include no candidate names or profile keys.
- Copy baseline query, filters, index and pool exactly; explain that changing
  inputs changes the population. New-match alerts instead identify the kept search.
- Rehearse the first search unchanged and confirm it reproduces the baseline.
  Correct and rehearse mismatches before scheduling.
- Keep the schedule and dated baseline where supported; explain how to stop it.

## Each run

1. Read the watch/baseline and repeat its pinned inputs.
2. Compare applied scope with the baseline's applied scope. On mismatch, retain
   the baseline and report which search needs re-pinning; do not quote its count.
3. Compare figures to decide whether to notify. Display both dated measurements,
   not a computed difference/percentage.
4. Replace successfully measured baselines with today's dated figures.
5. Notify or stay quiet as chosen. A failed/rate-limited run reports what failed
   and when it will retry; do not replace missing measurements with zero.

## The brief

Lead with what moved and both dated figures; add at most three lines covering
other changes, the implication for the req and whether to measure again.
New-match briefs show at most five people, strongest first, with search evidence
and returned profile links. Quiet runs stay silent unless a status was requested.

## The weekly brief

With two or more watches/alerts, offer one weekly run preserving every pinned
input and rule. Order it: changed measurements, new people (at most five per
search), items needing the recruiter, quiet watches. With no changes, use the
chosen silence/status preference. A limited run reports completed measurements
and the limit; never implies all watches ran.

## Rules

Keep scope/date and measured evidence on every figure. “Stop watching” deletes
the schedule and watch, then confirms.
