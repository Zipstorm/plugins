# Screening for the Shortlist

Screen in batches of up to 25, one profile read per batch, and judge each person
against the role's saved rubric ([criteria](criteria.md)), one profile at a
time, using the [evidence rules](evidence.md). Read the workspace's rubric
before the first batch; when it has none, set one up as that read says. Adding
people screens no one: add only the keeps, by name. Keep someone only
when every required criterion is met and no excluded one is hit; their preferred
criteria rank the keeps. Each reason names the criterion it rests on.

## Not met is not the same as not shown

For every pass, record which kind it is:

- **Not met:** the profile contradicts the criterion (they want fully remote work
  for an onsite role, their career is in another field).
- **Not shown:** the profile is silent on it. Profiles summarise careers and rarely
  describe design depth, ownership or how a system was built, so a silent profile
  is missing evidence, not a missing skill.

Group the passes by the criterion that failed, and say for each group whether it
is mostly not met or not shown.

## When a batch keeps fewer than half

Don't stop at "added none" or "added 8". Either the search is too broad (it
returns people who don't fit) or the criteria are too strict for the market
(no one fits). Say which, what blocked the batch, and recommend one next step,
chosen by the cause, changing neither the search nor the rubric until the
recruiter agrees:

- **Mostly not shown on one criterion.** The people may well qualify; the profiles
  just don't say. Recommend shortlisting the closest few as provisional (those who
  meet every other required criterion and contradict none), with that criterion as
  their screen question, for example "Have you designed storage schemas and RBAC
  models for a production platform?". The criterion stays required; the screen call
  establishes it. Add them only when the recruiter agrees.
- **Mostly not met because the search doesn't look for it.** The search is
  returning the wrong people. Recommend refining it so the criterion's evidence is
  required in profile text, then screening the new results.
- **One criterion that no one meets, batch after batch.** The bar may be set where
  the market isn't. Offer to measure what that requirement costs in candidates
  (a requirement trade-off), and leave the decision to the recruiter.
- **Several batches in a row with no keeps.** The search has run past its good
  matches. Recommend refining it rather than screening more of the same results.

Lead with the outcome and the blocking criterion, then the not-met/not-shown
split, the recommendation and one question that lets the recruiter choose it.
Example: "Kept none of 25. Storage-schema and RBAC design blocked 24 of them, and
none of those profiles contradicts it: they show infrastructure as code but don't
say whether they designed storage or access models. I'd shortlist the 5 closest as
provisional, with that as their screen question. Shall I add them, or refine the
search to require storage and RBAC design?"

## Never

- Lower the bar silently, move a criterion between required and preferred, or
  change a saved rubric without the recruiter's word.
- Add anyone the recruiter didn't agree to, look up contacts or message anyone
  as part of screening.
- Present a provisional keep as a qualified candidate: their gap travels with them.
