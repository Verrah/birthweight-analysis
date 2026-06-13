\# Exploratory Data Analysis

\## NCHS Natality Detail File, 1969–1971



\---



\## Overview



This notebook documents initial exploratory analysis of the 

1969–1971 NCHS natality data prior to model development.



\---



\## Key Descriptive Statistics



\### Birthweight Distribution



| Statistic | Value |

|---|---|

| Mean | 3,289g |

| Median | 3,317g |

| SD | 573g |

| Low birthweight (<2500g) | 7.8% |

| Very low birthweight (<1500g) | 1.2% |



\---



\### Births by State (Top 5)



| State | Births |

|---|---|

| California | 176,763 |

| New York | 155,268 |

| Texas | 113,310 |

| Illinois | 97,951 |

| Ohio | 95,076 |



\---



\### Education × Birth Order Pattern



Higher education concentrates births at lower birth orders.

Mothers with 16+ years of education show steep decline

after second child. Mothers with 0–8 years show flatter

distribution across all birth orders.



\---



\## Data Quality Notes



\- 47,392 records excluded for missing key variables (2.6%)

\- Plurality field blank for all 1969 records (1970–71 only)

\- Education not reported by all states in 1969–1971

\- Race coding uses 1969–1971 NCHS scheme (not OMB 1997)



\---



\## Next Steps



1\. Fit baseline linear regression (see `analysis/scripts/`)

2\. Add engineered features (age-squared, interactions)

3\. Compare Model A vs Model B on test set

4\. Generate county-level maps of predicted birthweight

