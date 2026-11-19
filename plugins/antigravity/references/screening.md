# Screening candidates for a workspace

When your SeekOut tools can save candidate evaluations, follow
[evaluating candidates](#evaluating-candidates) below instead: every person read is
evaluated and saved, and nobody is kept or dropped.

Screen in batches of up to 25. Read their profiles 5 to a call, all of a batch's
reads in one turn, never more in one call and never one person alone: a read of 25
keeps only titles, employers and dates, while a read of 5 keeps each headline,
skills and role descriptions. Judge each person from that read, reading no one again,
against the role's saved rubric ([criteria](criteria.md); for a role with an
overview, its requirements), one profile at a time, using the
[evidence rules](evidence.md). Read the workspace's rubric
before the first batch; when it has none, set one up as that read says. Adding
people screens no one: add only the keeps, by name. Keep the people who pass, as
[evaluating candidates](evaluating.md#who-passes) says; their preferred criteria rank
the keeps. Each reason names the criterion it rests on.

Asked to pick up to N candidates from a search, N is how many to keep, not how many to
read: screen batch after batch until N people pass or the search runs out of good
matches, then add the keeps and say how many were read. With no number given, N
is 25.

## Missed is not unshown

A pass rests on a criterion the profile contradicts, never on one it is silent on:
a silent profile is missing evidence, not a missing skill ([evaluating
candidates](evaluating.md#when-there-is-no-evidence)). Group the passes by the
criterion they missed, and name any criterion most people left unknown.

## When a batch keeps fewer than half

Don't stop at "added none" or "added 8". Either the search is too broad (it
returns people who don't fit) or the criteria are too strict for the market
(no one fits). Say which, what blocked the batch, and recommend one next step,
chosen by the cause, changing neither the search nor the rubric until the
recruiter agrees:

- **Most people unknown on one criterion.** It held no one back, but it tells no one
  apart: offer what [evaluating candidates](evaluating.md#when-there-is-no-evidence)
  says.
- **Up to three required criteria block most passes.** Offer once
  to make them preferred for the rest of the run, naming how many each failed and how
  many more would be kept. On a yes, save the changed rubric and re-judge the people
  already read from those reads; on a no, keep the bar.
- **Mostly not met because the search doesn't look for it.** The search is
  returning the wrong people. Recommend refining it so the criterion's evidence is
  required in profile text, then screening the new results.
- **One criterion that no one meets, batch after batch.** The bar may be set where
  the market isn't. Offer to measure what that requirement costs in candidates
  (a requirement trade-off), and leave the decision to the recruiter.
- **Several batches in a row with no keeps.** The search has run past its good
  matches. Recommend refining it rather than screening more of the same results.

Lead with the outcome and the blocking criterion, then any criterion most people left
unknown, the recommendation and one question that lets the recruiter choose it.
Example: "Kept 3 of 25. Streaming pipelines blocked 20 of them: their careers are in
BI reporting, not pipelines. I'd refine the search to require streaming work (Kafka,
Flink or Spark Streaming). Shall I?"

## Never

- Lower the bar silently, move a criterion between required and preferred, or
  change a saved rubric without the recruiter's word.
- Add anyone the recruiter didn't agree to, look up contacts or message anyone
  as part of screening.
- Present an unknown as met: missing evidence travels with the person.

## Evaluating candidates

When your SeekOut tools can save candidate evaluations, picking candidates is
evaluating the people at the top of a search against the role's evaluation criteria
and saving every evaluation: the evaluated people become the role's candidates,
ordered by how many criteria they meet and then by their ranking position, if any. Nobody is
ruled out or held back, and the number chosen is how many to evaluate.

### Before the first person

Read the workspace's rubric and its evaluation criteria: up to six, at most three
required, two preferred and one excluded, each with its id ([criteria](criteria.md#the-evaluation-criteria);
for a role with an overview, its requirements are the rubric). With no rubric, or
none marked for evaluation, set one up as that read says, then read it again. Every
evaluation judges exactly those criteria, no more and no fewer.

### Which search

When the request names a search (one attached to it, or the one this conversation
just showed), evaluate that one. When it names none ("evaluate the next 25
candidates", "evaluate more against the rubric"), evaluate the workspace's search
this conversation still holds: the one its evaluated candidates came from. With
several held and nothing in the request or the workspace to tell them apart, ask once
which, naming each search.

When this conversation holds no live search for the workspace (none was run or shown
here, or its results have expired), ask the recruiter to reopen the original saved
search in its workspace and request evaluation from those results.
Never run a new search in its place or ask the recruiter for a
list of people.

### Which people, in which order

Evaluate N people, N the number the recruiter chose (10, 25, 50 or 100; with none
chosen, ask once with your own question tool, 25 first). Read them in the search's
own order: its ranked order when it is ranked, which holds for its first 100 people.
The workspace's candidates show
who has already been evaluated and their ranking positions:

- **The top N** is the first N in that order. Someone already evaluated against the
  current criteria is not evaluated again unless the recruiter asks to re-evaluate
  them.
- **The next N** ("next", "more") is the next N in that order not yet evaluated:
  carry on from the first person after the highest ranking position already
  evaluated from that search, never from the top again.

When everyone in a ranked search's first 100 has been evaluated, say so and stop. Note
each person's ranking position as the search gives it. A search whose people carry no
ranking position is not ranked: evaluate in its own order (the next N continue after
the people already evaluated) and give no one a ranking position; when it says why it
was not ranked, say so in one line with that reason.

### Each batch

Batches of up to 25, read 5 to a call as above. Judge each person from that read,
reading no one again, as [evaluating candidates](evaluating.md) says:

- For every evaluation criterion, a verdict (met, partly, unknown or not met) and one
  line of evidence from their own profile, an inference marked as one.
- A summary of one or two sentences: who they are for this role and what most
  decides it.

Save the whole batch at once, every person evaluated, each with their verdicts,
evidence, summary and ranking position: saving adds them to the role's candidates.
Then the next batch, without asking between batches, until N people are evaluated or
the search runs out.

### When the request is done

After the request's last batch is saved, and only then, show the workspace's
Candidates in the SeekOut pane, once: that is where the evaluated people are ranked.
When the request said not to open or move the SeekOut pane, answer in chat and leave
the pane as it is. Do not show it after each batch, and never hand the recruiter a
SeekOut website link to see them instead.

Lead with how many were evaluated and how many pass ([evaluating
candidates](evaluating.md#who-passes)), then the strongest few. When one criterion is
mostly unknown, say so and offer what [evaluating
candidates](evaluating.md#when-there-is-no-evidence) says. When one is mostly not met because the search doesn't look for it, recommend refining
the search so its evidence is required. When one criterion no one meets, offer to
measure what it costs in candidates, and leave the decision to the recruiter.
Recommend one next step, changing neither the search nor the criteria until the
recruiter agrees.

A person evaluated against older criteria is evaluated again only when asked; the new
evaluation replaces the old one.

### Never, when evaluating

- Change the criteria, their importance or the evaluation criteria without the
  recruiter's word.
- Leave an evaluated person unsaved, or save anyone without their evaluation.
- Look up contacts or message anyone as part of an evaluation.
- Start again from the top of a search when asked for the next people.
- Present an unknown as met: missing evidence travels with the person.
