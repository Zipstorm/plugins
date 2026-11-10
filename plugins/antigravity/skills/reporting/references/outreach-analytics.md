# Outreach analytics

Keep each source and its coverage distinct. A saved SeekOut workspace Outreach
aggregate is an observation of the provider's named candidate counts at its
recorded observation time. Its coverage window and denominators are unspecified.
It counts candidates in SeekOut Outreach campaigns in that workspace, not email
sent outside SeekOut.
For a SeekOut-saved Outreach report, add an outreach metrics module: SeekOut
reads the counts of the report's home workspace into it, and they carry one
report ref and their observation time. Only counts saved this way have their
source, so only they can be cited exactly. Do not copy workspace aggregate
counts from a standalone Outreach read into the report's body: a
hand-copied count has no saved source and cannot be cited. If the module
cannot be measured, say so and do not invent or substitute the counts.
Quote only the saved values, preserve unknown versus zero, and name the source
and its coverage. Do not infer a role, campaign, date range, delivery status,
message count, response rate, denominator, auto-reply treatment, or reply content
from those aggregates. A sourced figure does not verify surrounding prose.

Adding the module answers its counts and their report ref: write the body
from them, with no read in between. For each non-null count you use, write it
as its canonical decimal string linked to the module's report ref. A captured zero is a real
zero; an absent count is unknown, never 0.

A separately authorized mailbox or campaign source may support a dated set,
message or reply analysis only when its own coverage and field definitions
support it. Keep mailbox threads separate from SeekOut people counts; calendar
and ATS records cannot establish replies. Complete pagination or label coverage
partial. Calculate a rate only when the source explicitly establishes both its
numerator and denominator; a zero denominator means undefined, not 0%.

Useful markdown explains response patterns and messaging hypotheses when those
claims are supported. Interest and decline reasons require an authorized source
of actual reply text; the workspace aggregate does not contain it. Questions are
not declines; overlapping themes cannot be summed. Preserve opt-outs. Aggregate
sensitive circumstances without quotes; name people only when requested.
