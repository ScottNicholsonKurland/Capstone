from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


DATA_PATH = Path("data/Issued_Construction_Permits.csv")
MODEL_OUTPUT_COLUMNS = [
    "PermitClass",
    "StatusCurrent",
    "OriginalZip",
    "CouncilDistrict",
    "NumberOfFloors",
    "HousingUnits",
    "TotalJobValuation",
]
TARGET_COLUMN = "TotalNewAddSQFT"


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load the permit dataset from CSV."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Data file not found: {csv_path.resolve()}")
    return pd.read_csv(csv_path)


def clean_currency_series(series: pd.Series) -> pd.Series:
    """Convert currency-like strings such as '$123,456' to numeric."""
    return pd.to_numeric(
        series.astype(str).str.replace(r"[\$,]", "", regex=True),
        errors="coerce",
    )


def prepare_modeling_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare the permit data for modeling.

    Modeling goal:
        Predict added square footage (TotalNewAddSQFT) from permit metadata.

    Cleaning steps:
    - coerce numeric columns
    - drop rows without a valid positive target
    - keep only columns relevant to modeling
    """
    prepared = df.copy()

    numeric_candidates = ["NumberOfFloors", "HousingUnits", TARGET_COLUMN]
    for col in numeric_candidates:
        if col in prepared.columns:
            prepared[col] = pd.to_numeric(prepared[col], errors="coerce")

    if "TotalJobValuation" in prepared.columns:
        prepared["TotalJobValuation"] = clean_currency_series(
            prepared["TotalJobValuation"]
        )

    missing_required = [col for col in MODEL_OUTPUT_COLUMNS + [TARGET_COLUMN] if col not in prepared.columns]
    if missing_required:
        raise KeyError(
            "Dataset is missing required columns: " + ", ".join(sorted(missing_required))
        )

    prepared = prepared[MODEL_OUTPUT_COLUMNS + [TARGET_COLUMN]].copy()
    prepared = prepared.dropna(subset=[TARGET_COLUMN])
    prepared = prepared.loc[prepared[TARGET_COLUMN] > 0].copy()

    return prepared


def split_features_target(
    df: pd.DataFrame, target_column: str = TARGET_COLUMN
) -> tuple[pd.DataFrame, pd.Series]:
    """Split the dataframe into features X and target y."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def build_model(feature_frame: pd.DataFrame) -> GridSearchCV:
    """
    Build a pipeline and grid search for a random forest regressor.

    Numeric columns:
        median imputation
    Categorical columns:
        most-frequent imputation + one-hot encoding
    """
    numeric_features = feature_frame.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = [
        col for col in feature_frame.columns if col not in numeric_features
    ]

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                RandomForestRegressor(
                    random_state=42,
                    n_jobs=-1,
                ),
            ),
        ]
    )

    param_grid = {
        "model__n_estimators": [100, 200],
        "model__max_depth": [10, 20, None],
        "model__min_samples_split": [2, 5],
        "model__min_samples_leaf": [1, 2],
    }

    search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=5,
        scoring="neg_mean_absolute_error",
        n_jobs=-1,
        refit=True,
    )

    return search


def evaluate_model(
    model: GridSearchCV,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> dict[str, float]:
    """Fit the model and return train/test evaluation metrics."""
    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    metrics = {
        "train_mae": mean_absolute_error(y_train, train_predictions),
        "test_mae": mean_absolute_error(y_test, test_predictions),
        "train_r2": r2_score(y_train, train_predictions),
        "test_r2": r2_score(y_test, test_predictions),
    }
    return metrics


def print_summary(
    df: pd.DataFrame,
    metrics: dict[str, float],
    best_params: dict[str, object],
) -> None:
    """Print a concise project summary."""
    print("\nAustin permit growth modeling summary")
    print("-" * 40)
    print(f"Rows used for modeling: {len(df):,}")
    print(f"Target: {TARGET_COLUMN}")
    print(f"Median target value: {df[TARGET_COLUMN].median():,.0f}")
    print(f"Mean target value: {df[TARGET_COLUMN].mean():,.0f}")

    print("\nBest hyperparameters")
    for key, value in best_params.items():
        print(f"{key}: {value}")

    print("\nEvaluation metrics")
    for key, value in metrics.items():
        print(f"{key}: {value:,.4f}")


def main() -> None:
    raw_df = load_data(DATA_PATH)
    modeling_df = prepare_modeling_data(raw_df)
    X, y = split_features_target(modeling_df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    search = build_model(X)
    metrics = evaluate_model(search, X_train, X_test, y_train, y_test)

    print_summary(
        df=modeling_df,
        metrics=metrics,
        best_params=search.best_params_,
    )


if __name__ == "__main__":
    main()
