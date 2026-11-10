# Internal talent pack

For employee-data vocabulary; sourcing's internal reference owns the workflow.
Check field coverage against the employee population before relying on it.

## What the employee data holds

| Field | Meaning |
| --- | --- |
| Department, office, country, state | Employee organisation/location |
| Seniority, title | Internal level/title |
| Internal skills | HRIS skill tags |
| Profile skills | Public-profile skills, often sparse |
| Manager | Direct reports |
| Hierarchy | All descendants, any depth |
| Profile history | Employers, titles, schools, majors, degrees, certifications |
| Years of experience | Whole years |
| Hire date, role start | Recruiter-supplied dates |

Use department/office/level/title/manager values exactly as supplied or returned;
use internal skill matching for skill names. Population varies especially for
skills, department, manager and hierarchy.

## Organisation-configured career data

Optional fields include current/wanted skills (Career Compass), job family/group,
and the employee's name/email, not their manager's. These are text searches,
not exact matches. Verify the field exists and its coverage against workforce
size; results on absent/unpopulated fields are unverified.

## Government-organisation fields

Some organisations configure clearance, polygraph, program and contract fields.
Confirm names/values in returned career data. Clearance belongs in its own field,
never current skills.

## Evidence in results

Use returned career data, department/office, manager/hierarchy, hire/role dates,
projects, technologies, repositories and skills. Career data may include wanted
skills, family/group/code, completion/about, transition/remote preferences,
prospective functions and redeployment status; availability is organisation-specific.
