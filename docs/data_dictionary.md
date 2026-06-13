\# Data Dictionary

\## NCHS Natality Detail File, 1969–1971



\*\*Source:\*\* National Center for Health Statistics (NCHS)  

\*\*File format:\*\* Fixed-width ASCII, 215 characters per record  

\*\*Record count:\*\* 1,800,103 births  



\---



\## Outcome Variable



| Variable | Tape Position | Length | Description | Valid Range | Missing Code |

|---|---|---|---|---|---|

| `birthweight\_grams` | 73–76 | 4 | Birthweight in grams | 227–8165 | 9999 |



\---



\## Features Used in Model



| Variable | Tape Position | Length | Description | Codes |

|---|---|---|---|---|

| `mat\_age\_recode8` | 49 | 1 | Mother's age (8 groups) | 1=<15, 2=15–19, 3=20–24, 4=25–29, 5=30–34, 6=35–39, 7=40–44, 8=45–49 |

| `mat\_edu\_recode6` | 102 | 1 | Mother's education (6 groups) | 1=0–8yrs, 2=9–11yrs, 3=12yrs, 4=13–15yrs, 5=16+yrs, 6=Not stated |

| `race\_child\_recode3` | 40 | 1 | Race of child (3 groups) | 1=White, 2=Other, 3=Black |

| `plurality\_recode2` | 83 | 1 | Plurality (2 groups) | 1=Singleton, 2=Multiple |

| `sex\_child` | 35 | 1 | Sex of child | 1=Male, 2=Female |

| `gestation\_recode10` | 95–96 | 2 | Gestational age (10 groups) | 0=Not applicable, 1=<20wks, 2=20–27wks, ..., 10=Not stated |



\---



\## Engineered Features



| Variable | Construction | Rationale |

|---|---|---|

| `mat\_age\_squared` | Midpoint of age group, squared | Captures U-shaped age-birthweight relationship |

| `age\_x\_plurality` | Age midpoint × plurality code | Plurality penalty varies by maternal age |

| `age\_x\_race\_black` | Age midpoint × Black indicator | Age effect differs by race |



\---



\## Exclusion Criteria



Records excluded from analysis:



| Variable | Excluded codes | Reason |

|---|---|---|

| `birthweight\_grams` | 9999 | Not stated |

| `mat\_age\_recode8` | 9 | Not stated |

| `mat\_edu\_recode6` | 0 | State not reporting |

| `gestation\_recode10` | 0, 10 | Not applicable / Not stated |



\*\*Total excluded:\*\* 47,392 records  

\*\*Final analytical sample:\*\* 1,752,711 births



\---



\## Year-Specific Coding Differences



| Variable | 1969 | 1970–1971 |

|---|---|---|

| Resident status | Foreign residents not identified | Code 4 added for foreign residents |

| Geographic codes | 1960 Census definitions | 1970 Census definitions |

| Plurality | Field is blank | Coded 1–5 |

| Mother's place of birth | Not coded | Present in records |

