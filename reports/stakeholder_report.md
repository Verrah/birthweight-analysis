\# Predicting Birthweight in the United States

\## Stakeholder Report | NCHS Vital Statistics 1969–1971



\---



\## What We Built and Why



We developed a statistical model to predict the birthweight 

of newborns using information recorded on U.S. birth 

certificates between 1969 and 1971.



\---



\## What the Model Predicts



Birthweight in grams (continuous outcome).



\---



\## Features Used



\- Mother's age (8 categories)

\- Mother's education (6 categories)

\- Race of child (3 categories)

\- Plurality (singleton vs multiple)

\- Sex of child

\- Gestational age (10 categories)

\- Age-squared term (non-linear age effect)

\- Age × plurality interaction

\- Age × race interaction



\---



\## Performance



| Metric | Value | Interpretation |

|---|---|---|

| Test RMSE | 485.9 grams | Average prediction error \~half a pound |

| Test R² | 0.30 | Model explains 30% of birthweight variance |



\---



\## Key Limitation



Race is included as a variable and confirms Black infants 

are born lighter on average than White infants even after 

accounting for maternal age, education, plurality, and 

gestational age. However, the birth certificate data do 

not capture structural racism, neighborhood disinvestment, 

differential prenatal care access, or discrimination in 

clinical settings. The race coefficient reflects accumulated 

social conditions, not biology.



\---



\## Connection to Data Challenge



This model contributes a county-level projection of 

predicted mean birthweight by maternal race and education 

level for the 1969–1971 baseline period, serving as the 

starting point for tracking how birthweight disparities 

evolved across U.S. counties between 1969 and 2015.

