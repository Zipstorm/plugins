# Location and indexes

Read when a search names a place outside a plain US city, needs a region other
than North America, or names talent-flow markets. Sourcing decides which
requirement to use and when to widen in its query reference ("Location and
region") and refine reference; another skill decides by its own rules. These
facts apply either way.

## Regions of the public pool

Public profiles are split into six regional indexes: North America, Europe,
Asia, Oceania, South America and Africa. `index: "all"` searches the six at once.
When no place or market was requested, explicitly choose all; an omitted index
can default to North America and silently exclude the other five. Profiles outside the active
region are absent, not ranked lower. Outside North America, set the region,
then the country, then the city (Europe, Germany, Berlin); in a one-region
search never skip the country. There is no Asia Pacific or Japan index; Japan is a country in Asia.

| Index | Covers | Watch for |
| --- | --- | --- |
| North America | US states and territories, Canada, Mexico, Central America | Puerto Rico is filed as a country, not a state |
| Europe | UK, Ireland, continental Europe, the Nordics, Switzerland | Turkey is not here |
| Asia | All of Asia and the Middle East, including Turkey, Israel, United Arab Emirates and Saudi Arabia | |
| Oceania | Australia, New Zealand, Pacific Islands | |
| South America | Brazil, Argentina, Chile, Colombia, Peru and the rest of South America | |
| Africa | All African countries | |

- Russia: search Europe and Asia.
- "AMER" or "Americas" is North America plus South America: search each and
  report each region's count.
- A talent-flow market is an index, optionally narrowed to a country, never a
  city. "The US and London" is North America with the United States, and Europe
  with the United Kingdom.

## Which filter

Cities and metros go in `locations`; US states and Canadian provinces in
`state`; countries in `country`. A state or country in `locations` either
fails or binds one city. Places in several regions (San Francisco and London)
run as one search with index all and every city in `locations`, with no
country filter, which would remove the other regions' cities. Its result names
the regions that held the places; the others hold none of them, so do not
search them again.

## What a state covers

| Index | States |
| --- | --- |
| North America | US states (full names, including District of Columbia) and Canadian provinces |
| Europe | UK nations (England, Scotland, Wales, Northern Ireland) and German Länder |
| Oceania | Australian states |
| South America | Brazilian states |

- A state name given as a city either does nothing or resolves to one metro in
  that state; the state itself is statewide.
- Write full names (United Arab Emirates, not UAE); the recruiter reads them
  back.

## Metro facts

| Place | Means |
| --- | --- |
| A city | A city resolves to a place whose reach may be the city or its metro. Check the count; if it looks too small for the market, add the metro's "Area" form ("New York City Area"), or each city the recruiter accepts. The state of New York adds upstate. |
| Delhi NCR | Delhi NCR in Asia. If no single place resolves, add Delhi, Gurugram and Noida as separate cities. |
| Metro Manila (the Philippines' National Capital Region) | Asia, the Philippines, Manila. A bare "NCR" usually means Delhi, so check which the recruiter means. |
| A city that will not resolve | Try the local or "Area" form: Milan Area or Milano, München, İstanbul, Tokyo Area. |

## Regions

| Region | Index | Places |
| --- | --- | --- |
| Midwest | North America | States: Illinois, Michigan, Ohio, Indiana, Wisconsin, Minnesota, Iowa, Missouri, Kansas, Nebraska, North Dakota, South Dakota |
| Southeast (US) | North America | States: Georgia, Florida, North Carolina, Tennessee, Virginia, South Carolina |
| West Coast | North America | States: California, Oregon, Washington |
| East Coast | North America | States: New York, New Jersey, Massachusetts, Connecticut, Pennsylvania, Virginia, Maryland, District of Columbia |
| Southeast Asia | Asia | Countries: Singapore, Philippines, Thailand, Vietnam, Indonesia, Malaysia |
| DACH | Europe | Countries: Germany, Austria, Switzerland |
| Nordics | Europe | Countries: Sweden, Denmark, Norway, Finland |
| Middle East | Asia | Countries: United Arab Emirates, Saudi Arabia, Israel |

Gulf Coast states are coastal only: Austin and Dallas are not Gulf Coast.

## Nicknames and time zones

A regional nickname is its named cities, each with its state, in `locations`:

| Nickname | Cities |
| --- | --- |
| Northern Virginia | Arlington, Alexandria, Fairfax, Reston, McLean, Herndon, Ashburn (Virginia) |
| DMV | Washington (District of Columbia); Bethesda, Silver Spring, Rockville (Maryland); Arlington, Alexandria (Virginia) |
| Inland Empire | Riverside, San Bernardino, Rancho Cucamonga, Ontario, Corona, Temecula (California) |

A US time zone is the list of states in it, in `state`. A state split between
zones is listed under the zone most of its people are in; say so when the
recruiter's zone is a hard limit.

| Zone | States | Canadian provinces |
| --- | --- | --- |
| Eastern (ET) | Connecticut, Delaware, District of Columbia, Florida, Georgia, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Vermont, Virginia, West Virginia | Ontario, Quebec |
| Central (CT) | Alabama, Arkansas, Illinois, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, Tennessee, Texas, Wisconsin | Manitoba, Saskatchewan |
| Mountain (MT) | Arizona, Colorado, Idaho, Montana, New Mexico, Utah, Wyoming | Alberta |
| Pacific (PT) | California, Nevada, Oregon, Washington | British Columbia |

Alaska and Hawaii have their own zones. Add the provinces only when the
recruiter includes Canada.
