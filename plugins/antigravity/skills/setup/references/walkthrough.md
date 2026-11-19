# Source-first setup

Setup ends at the starters. Do not ask for a role or JD, pick an example role,
read private source content, or run a recruiting task during this walkthrough.
An illustrative example teaches a benefit; it is not a vacancy or a search.

## Use one question flow

Read client guidance first, then ask with your own question tool: a host question skill is
discovered and read before asking, and every control follows its current
schema. Use the same one for both questions, each in its own turn, including
after Install or Not now. Never switch to a SeekOut form or another tool to
continue. Use plain chat only where client guidance permits it, or where no
question tool is offered; when none is available, state the limitation and
stop. A dismissed question pauses setup
without reopening it through another mechanism.

Keep only conversation context: the question mechanism, accepted source,
connection state/decision and pending starter choice. Reuse known answers and
resume the pending step. Do not save these as standing preferences. Setup has
at most two questions total; the later selected starter has its own intake budget.

## 1. Source first

Ask **“Where does your hiring context live?”** before directory discovery.
Use these complete option labels, with the benefit inside the label rather
than relying on a separate description field:

- **Google Drive — JDs and leveling guides**
- **SharePoint — hiring documents**
- **Slack — hiring-team conversations**
- **Skip connections**

These are source choices, not claims that the providers are connected or eligible
for installation. Reuse a provider already named instead of asking again; where
the conversation establishes different providers, substitute those names with a
short relevant benefit. Let the question's free-text alternative name
another provider. Do not display installed/recently suggested/declined metadata
in these labels. No source or starter is selected by a preselected option alone.

Skip connections goes directly to step 4. An ambiguous source such as “our ATS”
with no known provider is deferred without an extra provider/account question.

## 2. Make the benefit concrete

After a source choice, use one explicitly illustrative example:

- Documents: “Example: a JD says ‘senior’; the leveling guide defines the scope.
  Together, they can turn a vague title into a clear target.”
- Team conversations: “Example: ‘startup experience’ really means launching a
  product from scratch. Hiring-team context can clarify the evidence to look for.”
- ATS: “Example: a requisition title says ‘engineer’; its responsibilities reveal
  ownership of production reliability. That context can sharpen who to target.”

Add at most one sentence tying the selected source to the benefit. Do not imply
anything has been read or that the example describes this recruiter's business.
Respect a request to omit examples. Keep this example in the **final visible
response after tool calls**, not only commentary or an earlier response version.

## 3. A separate, optional connection decision

Follow [connections by use case](plugin-recommendations.md). Use the selected provider’s available metadata and the host’s own eligibility and permission flow. If the host offers a suitable connection, explain its benefit with the source example and let the recruiter decide. Keep a pending decision separate from the starter question.

Continue to the starters when the connection is resolved, the recruiter skips it or the host offers no action. Keep the source example visible. Describe verified connection state accurately. Content reads belong to a subsequent recruiting task.

## 4. End at the starters

Say **“You’re ready to choose where to start.”** This means ready to choose a
task, not that every integration is connected. Ask **“Where would you like to
start?”** through the same question mechanism with these complete labels:

- **Find candidates — see relevant people**
- **Figuring out who to target — sharpen the hiring criteria**
- **Understand what's possible in the market — explore talent and trade-offs**

The benefit is part of each option label; do not omit it, and outside plain
chat do not repeat the list in prose. **Stop and wait here.** Do not ask about a
role, choose a starter, launch its recipe, or require a result to call this setup
handoff complete. Only an accepted selection starts the
[owning workflow](starter-prompts.md), including a free-text answer, which that
handoff routes.
