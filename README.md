\# Birthweight Analysis

\## NCHS Vital Statistics Natality Data, 1969–1971



\*\*Principal Investigator:\*\* Verrah  

\*\*Institution:\*\* University of Michigan MIDAS Fellows Program  

\*\*Last Updated:\*\* June 2026



\---



\## Research Aim



To characterize how maternal educational attainment is associated 

with racial disparities in low birthweight among births occurring 

in the United States in 1969–1971, and whether the magnitude of 

this association differs across U.S. counties and states.



\---



\## Project Structure

birthweight-analysis/



├── data/



│   ├── raw/          Original NCHS .dat files (not shared)



│   ├── processed/    Cleaned analytical datasets



│   └── external/     SEER population denominators



├── analysis/



│   ├── notebooks/    Jupyter notebooks



│   └── scripts/      Python analysis scripts



├── results/



│   ├── figures/      Charts, maps, visualizations



│   └── tables/       Summary statistics, model outputs



├── docs/             Data dictionaries, codebooks



├── reports/          Final written reports



├── Dockerfile        Container definition



├── requirements.txt  Python dependencies



└── README.md         This file



\---



\## Data Sources



| Source | Description | Years | Access |

|---|---|---|---|

| NCHS Natality Detail File | Individual birth records | 1969–1971 | Public-use via CDC |

| NVSS Bridged-Race Population | County population denominators | 1969–2015 | Public-use via SEER |

| Hauer County Projections | County population projections | 2020–2100 | Open Science Framework |



\---



\## Reproducibility



All analysis is containerized using Docker. To reproduce:



```bash

\# Build the container

docker build -t birthweight-analysis .



\# Run validation

docker run birthweight-analysis



\# Launch Jupyter

docker-compose up jupyter

```



\---



\## Key Findings (Preliminary)



\- Baseline linear regression model achieves Test RMSE of 485.9 grams

\- Model R² of 0.30 explains approximately 30% of birthweight variance

\- Maternal education and race are significant independent predictors

\- Age × race interaction reveals heterogeneous effects across groups



\---



\## Citation



If you use this code or analysis, please cite:



> Verrah (2026). Birthweight Analysis: NCHS Vital Statistics 

> 1969-1971. GitHub. 

> https://github.com/Verrah/birthweight-analysis

