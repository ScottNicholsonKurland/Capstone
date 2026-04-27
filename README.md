# Forecasting Urban Growth in Austin with Construction Permit Data

## Executive Summary

This project analyzes City of Austin construction permit data to identify where new development is concentrated and to test whether permit-level features can help model added square footage.

The project is best understood as a **descriptive analysis plus predictive prototype**. It uses construction permits as a faster-updating signal than census data, while treating model results cautiously.

## Business Question

Where is construction activity concentrated in Austin, and can permit metadata help predict added square footage as a proxy for development intensity?

## Tools Used

- Python
- pandas
- matplotlib
- scikit-learn
- Jupyter Notebook

## Dataset

**Source:** City of Austin Open Data Portal  
**Original project scope:** more than 1.8 million construction permit records from 2010–2017  
**Working analytical subset:** about 241,000 records after filtering to rows with positive added square footage

Key fields used:

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

## Project Objective

Austin growth affects housing, utilities, transportation, and infrastructure planning. This project asks:

1. Which Austin ZIP codes show the greatest concentration of new construction?
2. Which permit-level features are most useful for modeling added square footage?

This is **not** a causal analysis. It does not prove that permits cause infrastructure demand. It identifies patterns in construction activity.

## Analytical Approach

### 1. Data Cleaning

The analysis filters permit records to rows with positive `TotalNewAddSQFT`, coerces numeric fields, normalizes valuation fields, and removes records missing key geographic fields needed for ZIP-level and map-based analysis.

### 2. Exploratory Data Analysis

EDA focuses on:

- permit counts by ZIP code
- added square footage by ZIP code
- permit counts by number of floors
- most common permit classes
- job valuation distribution
- geographic distribution of added square footage

### 3. Predictive Modeling

The modeling script treats `TotalNewAddSQFT` as the target variable and uses a random forest regressor with permit-level metadata.

The pipeline includes:

- numeric imputation
- categorical imputation
- one-hot encoding
- random forest regression
- grid search cross-validation
- train/test evaluation with MAE and R²

## Key Findings

The project currently reports the following high-construction ZIP codes by added square footage:

| ZIP Code | Reported Added Square Footage |
|---|---:|
| 78701 | 106 million |
| 78704 | 89 million |
| 78758 | 75 million |
| 78748 | 70 million |
| 78744 | 60 million |

The project also reports that location-based fields such as ZIP code, latitude, and longitude are informative, with `NumberOfFloors` also contributing useful signal.

## Model Interpretation

The README previously reported:

- random forest R² of 0.72
- monthly time-series split R² of 0.66

Those values suggest useful predictive signal, but they should be treated as provisional until the full validation strategy is documented end-to-end in reproducible scripts.

## Why Permit Data?

Construction permits update more frequently than census releases. That makes them useful for detecting neighborhood-level development patterns earlier than slower demographic datasets.

In this project, added square footage is used as a rough proxy for construction intensity and possible downstream infrastructure pressure.

## Portfolio Value

This project demonstrates:

- Python EDA
- civic/open-data analysis
- feature engineering
- regression modeling
- cautious interpretation of model performance
- communication of limitations
