# Power filters

Use when an attribute lacks an ordinary requirement. Sourcing's query reference
owns application/checking. Browse the live catalogue: availability depends on
pool, region, organisation entitlements and custom filters.

## Taxonomy

| Category | Look for |
| --- | --- |
| General | Clearance/work authorisation, education tiers, non-clinical healthcare |
| Software | Technical specialisms across development, data/ML, infrastructure and hardware |
| Engineering | Non-software engineering specialisms |
| Companies | Employer/sector lists, startup stages, acquisitions, layoffs, IPOs |
| Non-tech roles | HR, finance, sales/marketing and other role flags |
| Security clearances | Levels for Enhanced Clearance accounts; [cleared](cleared.md) |

## Notes on the catalogue

- Filters AND together; each narrows the pool.
- A catalogue id goes in `power_filters` exactly as returned, never nested
  inside another filter. A company list (Fortune 500, YC, a startup stage) is
  the first carrier for a kind of company the recruiter requires. An id the
  organization does not include is refused; carry the kind with a built list
  instead and say so.
- The design filter includes UI/UX, visual/graphic design, not a Product Designer broadening.
- Generic clearance authorisation duplicates “has a clearance”; do not add both.
- US work-authorisation filtering describes likely citizenship/green-card status,
  not verified individual eligibility.
- Top-30 universities follows US News; check pool behaviour when relying on it.
  Catalogue examples never substitute for returned filter values.
