# Read the selected Ashby job or application

During setup, follow the metadata-only [ATS connection route](ats.md) and end
at the starters; do not read Ashby jobs or ask for a JD fallback. A later selected
recruiting task may use an authorized reader with the required account scope.
Keep provider/account and connection identity distinct from a job ID. Verify the
plugin's schema and account access; installation does not connect the same
account automatically. If a selected task's read fails, use its scoped
JD/role-context fallback in the ATS note.
Retrieve only the bounded open-role set that task needs, then the
selected job's details. Do not infer open jobs from pipeline stages, candidate
records or filter vocabulary. If no usable reader/context is available, retain
that gap and reuse a shared JD/brief/link, or accept JD/role context within the
task's remaining question budget. Read actual content; never substitute a sample.

Resolve the job by title/location and its returned identity. A job can have
openings, postings and an interview plan; an application joins one candidate to
one job. Read that application's stages and feedback, not the candidate's latest
unrelated application. Reuse the selected job and its actual stage vocabulary.

Choose the [ATS connection](ats.md) for the task: SeekOut integration and the
host's Ashby plugin have separate access and IDs. For live application records,
use the available authorized reader; label synced results separately.
Current pipeline stages are snapshots. Only returned history/metrics with scope
and definitions support funnel rates or time in stage. Do not reconstruct them
by dividing current counts.

Check whose submitted feedback the action returns. A recruiter's own scorecards
are not every interviewer's feedback; missing ones stay missing. Transcripts and
notes cannot fill them. Use interviewing for the debrief and pipeline management
for requested writes. A stage change does not imply a recorded rejection reason,
a sent email or a merge. Verify each requested result independently.

Available schemas and errors determine account access and supported actions;
do not infer writes from directory descriptions. Use a dated export or an unsaved
proposal when the needed action is unavailable.

Keep the returned job/application or project/sequence identities with the
[workspace handoff](workspace-context.md); provider records are not workspace links
until an available SeekOut operation confirms the mapping.
