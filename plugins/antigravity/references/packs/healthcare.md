# Healthcare signals

Read when an ask is for physicians or other clinicians: physician, doctor, MD,
NPI, board certified, a named clinical field (cardiologist, dermatologist,
oncologist, radiologist, anesthesiologist, psychiatrist, surgeon, pediatrician)
or a named hospital system. These are signals to carry on a public-profile
search; nurses, including nurse anesthetists, are in [nursing](nursing.md).

## Carrying the signals

| Recruiter says | On the search |
| --- | --- |
| cardiologists | Title clause with the clinical title and its forms: `cur_title:("Cardiologist" OR "Cardiology Physician")` |
| interventional cardiologists | The sub-field's title, with the sub-field as a quoted term: `"Interventional Cardiology"` |
| primary care | Family Medicine and Internal Medicine titles together; say so in the answer |
| MD, DO | The degrees filter |
| board certified | The certifications filter when the recruiter requires it; otherwise a check criterion |
| at <hospital system> | Current employer, each campus or entity name the lookup returns |
| Spanish-speaking | The languages filter |
| in <city> | The location filter: where they practise or live |
| licensed in <state>, active NPI | Check criteria judged on each person's evidence; a licence state never stands in for where they live |

Clinical work that is only background to a title, employer or seniority ask
("former physician now a pharma executive") is an ordinary public search with
the clinical history as evidence.

## Examples

| Ask | Search |
| --- | --- |
| Dermatologists in California | `cur_title:("Dermatologist")`, California |
| Emergency medicine doctors in NYC | `cur_title:("Emergency Medicine Physician" OR "Emergency Physician")`, New York City |
| Cardiologists now in pharma or biotech | Past title cardiologist, current employer industry judged on evidence |

## Evidence

Cite what each profile shows: title, employer, specialty, certifications,
degrees, schools, languages and location. When the ask names something a field
should show (board certification, a language) and it is empty for a candidate,
say it is missing. Licence and NPI status on a profile is a snapshot; never
present it as live.
