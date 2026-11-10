# Worked title searches

Read when writing a title clause and an example would settle the shape. Each
row applies the [title families](title-families.md) facts and the sourcing
skill's query decisions to one request.

| Request | Query | Notes |
| --- | --- | --- |
| Head of AI/ML in SF biotech | `cur_title:("Head of AI" OR "Head of Machine Learning")` | San Francisco; biotech judged on each person's employer evidence ([industries](industries.md)), never in the boolean |
| ML engineers in Seattle with voice in production | `cur_title:("Machine Learning Engineer" OR "ML Engineer") AND ("voice" OR "speech" OR "ASR" OR "TTS" OR "conversational AI") AND ("production" OR "deployed models")` | No Applied Scientist |
| ML engineers in Bengaluru with strong Python and PyTorch | `cur_title:("Machine Learning Engineer" OR "ML Engineer" OR "Deep Learning Engineer") AND "Python" AND "PyTorch"` | Asia, India, Bengaluru. Never `(Python OR PyTorch)`. "Strong" is not a years floor |
| Principal data engineers in Chicago who built ETL or data platforms | `cur_title:("Principal Data Engineer" OR "Principal Data Platform Engineer") AND (ETL OR "data pipeline" OR "data platform" OR "data warehouse" OR "data lakehouse")` | No Staff, Senior Staff, Lead or Principal Software Engineer |
| Staff data engineers in Berlin or Amsterdam on data platforms | `cur_title:("Staff Data Engineer" OR "Staff Data Platform Engineer")` plus data-platform phrases | Europe, both cities |
| DevOps engineers in Sydney with Kubernetes and platform engineering | `cur_title:("DevOps Engineer") AND (Kubernetes OR k8s) AND "platform engineering"` | Oceania, Australia, Sydney |
| Staff backend engineers at named companies | `cur_title:("Staff Backend Engineer" OR "Staff Back End Engineer" OR "Staff Backend Software Engineer")` | Each company as a current employer. Never Staff Software Engineer, Staff Engineer or Staff Platform Engineer; backend focus also goes in the criteria |
