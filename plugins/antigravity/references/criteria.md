# Role criteria

Each role has one rubric: up to 10 criteria, kept in SeekOut with the role's job
description, in its workspace. Every save is a new version, and screening
candidates judges by the newest one. The rubric is
a working record, not a one-time form: it starts from the job description and
changes as the recruiter learns what the market holds and what the hiring team
wants. Use it for candidate assessments and interview scorecards.

## A role with an overview

A role's [overview](role-overview.md) holds its requirements, and they are what
candidates are screened against: saving the overview keeps them as the role's
rubric, so a role with an overview has no separately drafted rubric. Its must-haves
are required, its nice-to-haves preferred and its things to avoid excluded;
trade-offs and pay are not criteria. To change a criterion, change the
requirement on the overview and save the overview again. The rules below still
decide what each requirement means and how it changes.

A criterion the recruiter means for every role is one of their
[default criteria](work-log.md#default-criteria): a new role's overview starts
with it, marked as their default.

## The evaluation criteria

When your SeekOut tools can save candidate evaluations, candidates are evaluated
on up to six of the rubric's criteria (and a search, when SeekOut ranks it, is ranked
on the same ones): at most three required, two preferred and one excluded, each with a
stable id. Choose them when you save the rubric or the overview, naming the ones that
best tell people apart and that a profile can show; a later save keeps the same ones
unless you name others; [evaluating candidates](evaluating.md) says which a profile can
show and how each is judged. Every evaluation judges exactly those criteria. Nobody is kept or dropped: `required` is a
must-have, `preferred` a nice-to-have and `excluded` a trait the role avoids, and in
the table below read a keep as someone who passes ([evaluating
candidates](evaluating.md#who-passes)) and an unknown as a question for the screen call.

## Who writes them

The first draft comes from the job description and the recruiter's words:
right after the first search, without asking (Find candidates), or while
planning a role, with confirmed answers. For a role with an overview, the
overview's requirements are that draft. Refine the same list with search
evidence, screening outcomes, measured trade-offs, interview debriefs and
outreach replies. Never start a second list for the same role. A direct request
proceeds to sourcing without a planning or acceptance detour. A later search uses
the current rubric: required and excluded criteria keep their meaning. Preferred
criteria never restrict who is searched, and ranking by them never proves fit.

Read a pasted JD as a whole before assigning importance. Explicit must-haves
and exclusions stay required and excluded; preferred qualifications stay
preferred. Responsibilities, examples of technology and the hiring company's
description do not make every mentioned term a candidate requirement. Keep
alternatives together: "Go or Rust" is one requirement, not two. The
recruiter's stated requirements direct the work; keep inferred or ambiguous ones
separate, as open questions in the brief, instead of silently promoting them to
required. A draft written without asking holds only what was stated: an unclear
priority is preferred at most, never required, and nothing about the role is
invented.

## One criterion

| Field | Content |
| --- | --- |
| name | At most 40 characters, in the recruiter's or JD's wording; keep their numbers |
| importance | `required` (no keep clearly misses it), `preferred` (ranks the keeps) or `excluded` (a deal-breaker, named as the trait that rules a person out); see [status words](status-words.md#importance) |
| question | Optional, at most 200 characters: one question asked of a profile that would establish the evidence, where the detail the name cannot hold goes |

Spend criteria on what a search cannot settle: depth, scope, ownership,
outcomes, kind of company or product. A requirement the search already
enforces (title, place, years, a named employer) needs a criterion only when the
profile must still show it. Interest, notice, sponsorship need and compensation
expectations are for the screen call, not criteria. Employment gaps and
protected traits are never criteria; tenure or short-stint criteria need the
recruiter's request.

## Showing them

A draft written in the background is not shown unless the recruiter asks. When
it is shown or a change is proposed, give a short list with its version and
source, numbered by position (C1, C2…) for that version only. Append new
criteria so existing positions stay stable.

## Tighten or loosen: reading the results

The search decides who is looked at; the rubric decides who is kept. Fix the
wrong people in the search and the wrong bar in the rubric, and change one
thing at a time so its effect shows.

| What the results show | Do |
| --- | --- |
| Screening keeps nearly everyone, or the recruiter rejects keeps for one reason | The rubric does not separate people: propose that reason as a criterion, preferred unless they call it a must-have |
| Most people are unknown on one criterion | Offer to judge it when screening and judge a visible sign instead, as evaluating candidates says |
| Passes are mostly not met because the search does not look for it | Tighten the search to require its evidence; the rubric stays |
| One required criterion no one meets, batch after batch | The bar may sit where the market isn't: offer to measure what it costs in candidates, or to make it preferred |
| A faithful search finds far fewer than the role needs | Name the criterion that limits it most and propose loosening that one |
| The recruiter likes someone who misses a required criterion | Ask whether it is still required; never relabel it silently |
| Leading titles, employers or places are off-target | Refine the search; add an excluded criterion only for a pattern the recruiter rules out |

Loosen first what was inferred or is a proxy: added years, school, a specific
tool where equivalents count, title wording. Tighten first where the role is
decided: depth, ownership, outcomes, kind of company. Never loosen a stated
must-have, a required credential or license, or a stated exclusion without the
recruiter's word.

## Keeping it current

Revisit the rubric after the first screened batch, after recruiter or hiring
manager feedback, after an accepted what-if, and after interview debriefs or
outreach replies that show a pattern. A requirement the recruiter states in
chat is their word: add it. Every other change is proposed first. Name the
version in assessments and comparisons; reassess old evidence against a new
version, and do not relabel an old assessment as current.

## Proposing a change

Show each changed criterion before and after, with its reason and evidence;
name unchanged criteria by their old version's numbers.

- A new must-have is a separate criterion. Values within one criterion are
  alternatives: Kubernetes must not become another alternative to Go or Rust.
- Change importance only for the criterion the recruiter names, and thresholds
  only to the value they specify. Split broad changes by criterion; "no change"
  with a reason is valid. Never change the bar to favour or remove a person.
- Clear decisions from an intake meeting, evidenced in recruiter notes or a
  transcript, need no repeated proposal: save one version naming the meeting
  and date, and keep unresolved decisions in the brief's open questions.
