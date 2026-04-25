# Forecasting Urban Growth in Austin with Construction Permit Data

This project analyzes City of Austin construction permit data to identify where new development is concentrated and to model added square footage as a proxy for future growth pressure. The core idea is that construction permits update more frequently than census data and may provide an earlier signal of where infrastructure demand is increasing. The analysis combines exploratory data analysis with a random forest regressor trained on permit-level features such as ZIP code, permit class, council district, floors, housing units, and job valuation.

## Project Objective

Austin has grown rapidly for years, and the location and intensity of new construction affects utilities, transportation, housing, and public infrastructure planning. This project asks two related questions:

1. Which Austin ZIP codes show the greatest concentration of new construction?
2. Can permit-level features help predict added square footage (`TotalNewAddSQFT`) as a rough proxy for future growth intensity?

This is a descriptive and predictive project, not a causal one. The goal is to identify patterns in permit activity, not to prove that permits directly cause infrastructure demand.

## Dataset

**Source:** City of Austin Open Data Portal  
**Original scope described in project materials:** more than 1.8 million construction permit records from 2010–2017  
**Working analytical subset described in the project:** about 241,000 records after filtering to rows with positive added square footage.

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
  - **78744**: 60 million

- The project reports that location-based variables such as ZIP code, latitude, and longitude were among the most informative features, with `NumberOfFloors` also providing a useful signal.

- A random forest regressor reportedly achieved an **R² of 0.72**, and a monthly time-series split reportedly returned **R² = 0.66**. Those values suggest a useful predictive signal, though they should be interpreted cautiously until the pipeline and validation split are fully documented in a reproducible script.

## Why Permit Data?

Construction permit data updates much more frequently than census releases. That makes it potentially useful for detecting neighborhood-level development patterns earlier than slower demographic datasets. In this project, added square footage is treated as a rough proxy for construction intensity and possible downstream infrastructure pressure.

