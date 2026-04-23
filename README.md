# Forecasting Urban Growth in Austin with Construction Permit Data

This project analyzes City of Austin construction permit data to identify where new development is concentrated and to model added square footage as a proxy for future growth pressure. The core idea is that construction permits update more frequently than census data and may provide an earlier signal of where infrastructure demand is increasing. The analysis combines exploratory data analysis with a random forest regressor trained on permit-level features such as ZIP code, permit class, council district, floors, housing units, and job valuation. :contentReference[oaicite:1]{index=1}

## Project Objective

Austin has grown rapidly for years, and the location and intensity of new construction affects utilities, transportation, housing, and public infrastructure planning. This project asks two related questions:

1. Which Austin ZIP codes show the greatest concentration of new construction?
2. Can permit-level features help predict added square footage (`TotalNewAddSQFT`) as a rough proxy for future growth intensity?

This is a descriptive and predictive project, not a causal one. The goal is to identify patterns in permit activity, not to prove that permits directly cause infrastructure demand. :contentReference[oaicite:2]{index=2}

## Dataset

**Source:** City of Austin Open Data Portal  
**Original scope described in project materials:** more than 1.8 million construction permit records from 2010–2017  
**Working analytical subset described in the project:** about 241,000 records after filtering to rows with positive added square footage :contentReference[oaicite:3]{index=3}

Key fields used in the analysis include:

- `TotalNewAddSQFT`
- `OriginalZip`
- `Latitude`
- `Longitude`
- `PermitClass`
- `StatusCurrent`
- `CouncilDistrict`
- `NumberOfFloors`
- `HousingUnits`
- `TotalJobValuation`

## Analytical Approach

### 1. Data cleaning
The exploratory analysis script filters the permit data to rows with positive `TotalNewAddSQFT`, coerces numeric fields into usable form, normalizes valuation fields, and removes rows missing key geographic fields needed for mapping and ZIP-level summaries.

### 2. Exploratory data analysis
EDA focuses on:

- permit counts by ZIP code
- permit counts by number of floors
- most common permit classes
- job valuation distribution
- geographic distribution of added square footage

### 3. Predictive modeling
The modeling script treats `TotalNewAddSQFT` as the target variable and uses a random forest regressor to model it from permit metadata. The pipeline includes:

- numeric imputation
- categorical imputation
- one-hot encoding for categorical features
- random forest regression
- grid search cross-validation
- train/test evaluation using MAE and R²

## Key Findings

Based on the project’s current documented results:

- The highest-construction ZIP codes were reported as:
  - **78701**: 106 million square feet
  - **78704**: 89 million
  - **78758**: 75 million
  - **78748**: 70 million
  - **78744**: 60 million :contentReference[oaicite:4]{index=4}

- The project reports that location-based variables such as ZIP code, latitude, and longitude were among the most informative features, with `NumberOfFloors` also providing useful signal. :contentReference[oaicite:5]{index=5}

- A random forest regressor reportedly achieved an **R² of 0.72**, and a monthly time-series split reportedly returned **R² = 0.66**. Those values suggest useful predictive signal, though they should be interpreted cautiously until the pipeline and validation split are fully documented in a reproducible script. :contentReference[oaicite:6]{index=6}

## Why Permit Data?

Construction permit data updates much more frequently than census releases. That makes it potentially useful for detecting neighborhood-level development patterns earlier than slower demographic datasets. In this project, added square footage is treated as a rough proxy for construction intensity and possible downstream infrastructure pressure. :contentReference[oaicite:7]{index=7}

## Limitations

This project has several important limitations:

- **Proxy target:** Added square footage is not the same as population growth, infrastructure load, or economic value. It is only a rough signal.
- **Selection effects:** Filtering to positive `TotalNewAddSQFT` excludes some permit categories and may bias the analytical sample.
- **Observational data:** The project identifies patterns and predictive relationships, not causal effects.
- **Validation detail:** Reported model performance is promising, but the repository should document the validation method more explicitly to support reproducibility.
- **Repository modernization:** Some older files in the repository predate the cleaned portfolio version and should be removed or archived before final publication. :contentReference[oaicite:8]{index=8}

## Repository Structure

Suggested cleaned structure:

```text
Capstone/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── sample_permits.csv
│   └── README.md
├── notebooks/
│   └── austin_growth_analysis.ipynb
├── src/
│   ├── eda.py
│   └── model.py
├── images/
│   ├── zip_code_counts.png
│   ├── square_footage_map.png
│   ├── permit_class_counts.png
│   └── model_results.png
└── presentation/
    └── capstone_presentation.pdf
