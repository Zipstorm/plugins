# Choose the ATS connection for the task

SeekOut's integrated ATS and an ATS plugin connected to the conversation are
separate paths. Access to one does not establish access to the other.

For SeekOut ATS search or export, check the account's ATS capability with
connection details included. Use its returned connection ID, provider and name;
read the availability reason before choosing a destination. A failed or refused
capability read is not proof that no integration exists. Each operation checks
access again; a listed connection does not promise every ATS action.
An empty feature list leaves a capability unknown, not unsupported.

Installing a plugin does not automatically connect the existing SeekOut
account. Setup reads connection metadata only, as the
[connections index](README.md#finding-a-missing-connector) says.

For a selected recruiting task, inspect actual job-list/read actions before use.
Verify the provider/account scope separately. Reuse an explicit or unique
account match; otherwise resolve it within the current question budget.
Never choose among ambiguous accounts just because one reader is available.

Read a bounded set of open jobs from the selected account using supported
filters, then the chosen job's full context as needed. Connection metadata,
pipeline counts and candidate-search/filter vocabulary are not open-role or
job-description records. Exclude non-job actions and sentinel entries such as
exporting prospects from role choices. Preserve returned job IDs, locations, source dates
and read limitations. When a task uses a JD fallback, read actual source content and
preserve its provenance; a pasted brief or public job page is not an ATS import.
A bare ATS job ID needs a working authorized reader. If the last answer cannot
be read and no usable context remains, explain the gap and stop: no question
beyond that workflow's budget, no retry loop, no example role and no invented brief.

For live applications, interview feedback or stage changes through a connected
ATS plugin, use that plugin's available actions and returned job/application IDs.
SeekOut capability checks do not discover host plugins or grant them access.
Do not pass a SeekOut connection ID as a provider record ID, or switch paths to
retry an uncertain write. An ATS stage is not a workspace status: a change in
one is never written to the other unless the recruiter asks for both.

Keep the source, account, job and observation date explicit. Synced SeekOut
results and live ATS records can differ; never merge their counts. Read the
chosen provider adapter, such as [Ashby](ashby.md) or [Gem](gem.md), for its
record model. Keep the selected identities in the [workspace handoff](workspace-context.md).
Setup performs no job-to-workspace linking. A selected task may reuse a confirmed
mapping; claim a persisted association only after a supported write confirms it.
