# External actions

For messages, calendar events, system writes, saves, exports and ATS pushes.
Offer recurring work only when an available scheduler can call its required tools.

Credit spend (contacts, exports, SeekOut-generated drafts) is confirmed in
chat: For more than 25 people, tell the recruiter how many people and the most
credits it can spend, and call only after they agree. Quote only returned
spend/balance.

## Doing it once

Use the available connector, not a browser, SMTP, mailto or alternate API.
Recheck calendar availability immediately before creating an event; a lost slot
requires a new choice.

Classify the result:

- **Confirmed:** explicit success; name/link the resulting item and verify it
  with a read when available.
- **Failed:** explicit evidence nothing happened; report the error.
- **Unknown:** timeout, disconnection, cancellation or ambiguous delivery.
  Read back if possible. Never retry an unknown outcome or resend it, or switch
  providers.

For an unknown SeekOut write/spend, resend the identical request with its
original key to recover its outcome. A new key creates a second action.

## When a capability is missing

Distinguish absent tools, sign-in, denied scope, stale data, transient failures,
quota and empty results. Stop only affected work; use offered capabilities and
suggest a missing connection once, respecting declines.

## Reporting

Report confirmed outcomes; queued/partial is not complete, and chat content is
not saved until its write succeeds. Keep returned identifiers in conversation
for follow-up calls; show the recruiter the item's title, time or returned link.
