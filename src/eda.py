from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path("data/Issued_Construction_Permits.csv")
OUTPUT_DIR = Path("images")


def load_permit_data(csv_path: Path) -> pd.DataFrame:
    """
    Load permit data from CSV.

    Parameters
    ----------
    csv_path : Path
        Path to the permit CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded permit dataframe.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.
    """
    if not csv_path.exists():
        raise FileNotFoundError(f"Data file not found: {csv_path.resolve()}")

    return pd.read_csv(csv_path)


def clean_permit_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean permit data for exploratory analysis.

    Key steps:
    - keep rows with positive added square footage
    - normalize TotalJobValuation to numeric
    - drop rows missing core geographic fields
    """
    cleaned = df.copy()

    cleaned["TotalNewAddSQFT"] = pd.to_numeric(
        cleaned["TotalNewAddSQFT"], errors="coerce"
    )

    if "TotalJobValuation" in cleaned.columns:
        cleaned["TotalJobValuation"] = (
            cleaned["TotalJobValuation"]
            .astype(str)
            .str.replace(r"[\$,]", "", regex=True)
            .replace({"nan": None})
        )
        cleaned["TotalJobValuation"] = pd.to_numeric(
            cleaned["TotalJobValuation"], errors="coerce"
        )

    cleaned["NumberOfFloors"] = pd.to_numeric(
        cleaned.get("NumberOfFloors"), errors="coerce"
    )
    cleaned["HousingUnits"] = pd.to_numeric(
        cleaned.get("HousingUnits"), errors="coerce"
    )

    cleaned = cleaned.loc[cleaned["TotalNewAddSQFT"] > 0].copy()

    required_columns = ["OriginalZip", "Longitude", "Latitude", "TotalNewAddSQFT"]
    existing_required = [col for col in required_columns if col in cleaned.columns]
    cleaned = cleaned.dropna(subset=existing_required)

    return cleaned


def summarize_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a compact data-quality summary for each column.
    """
    summary = pd.DataFrame(
        {
            "dtype": df.dtypes.astype(str),
            "non_null_count": df.notna().sum(),
            "null_count": df.isna().sum(),
            "null_pct": (df.isna().mean() * 100).round(2),
            "n_unique": df.nunique(dropna=True),
        }
    ).sort_values(by="null_pct", ascending=False)

    return summary


def plot_zip_code_counts(df: pd.DataFrame, top_n: int = 20) -> plt.Figure:
    """
    Plot permit counts by zip code.
    """
    zip_counts = df["OriginalZip"].astype(str).value_counts().head(top_n)

    fig, ax = plt.subplots(figsize=(14, 6))
    zip_counts.plot(kind="bar", ax=ax)

    ax.set_title(f"Top {top_n} ZIP Codes by Permit Count")
    ax.set_xlabel("ZIP Code")
    ax.set_ylabel("Permit Count")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig


def plot_floor_counts(df: pd.DataFrame, top_n: int = 15) -> plt.Figure:
    """
    Plot counts of NumberOfFloors values.
    """
    floor_counts = df["NumberOfFloors"].fillna(0).value_counts().sort_index().head(top_n)

    fig, ax = plt.subplots(figsize=(14, 6))
    floor_counts.plot(kind="bar", ax=ax)

    ax.set_title("Permit Count by Number of Floors")
    ax.set_xlabel("Number of Floors")
    ax.set_ylabel("Permit Count")
    ax.tick_params(axis="x", rotation=0)

    fig.tight_layout()
    return fig


def plot_permit_class_counts(df: pd.DataFrame, top_n: int = 15) -> plt.Figure:
    """
    Plot the most common permit classes.
    """
    if "PermitClass" not in df.columns:
        raise KeyError("Column 'PermitClass' not found in dataframe.")

    class_counts = df["PermitClass"].fillna("Unknown").value_counts().head(top_n)

    fig, ax = plt.subplots(figsize=(14, 6))
    class_counts.plot(kind="bar", ax=ax)

    ax.set_title(f"Top {top_n} Permit Classes")
    ax.set_xlabel("Permit Class")
    ax.set_ylabel("Permit Count")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig


def plot_job_valuation_histogram(df: pd.DataFrame) -> plt.Figure:
    """
    Plot the distribution of total job valuation.
    """
    if "TotalJobValuation" not in df.columns:
        raise KeyError("Column 'TotalJobValuation' not found in dataframe.")

    valuation = df["TotalJobValuation"].dropna()

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.hist(valuation, bins=50)

    ax.set_title("Distribution of Total Job Valuation")
    ax.set_xlabel("Total Job Valuation (USD)")
    ax.set_ylabel("Frequency")

    fig.tight_layout()
    return fig


def plot_square_footage_map(df: pd.DataFrame, max_points: Optional[int] = 20000) -> plt.Figure:
    """
    Create a longitude/latitude scatter plot sized by added square footage.

    This replaces the prior Google Maps/Bokeh implementation so the repo
    does not require an API key and remains easy to run locally.
    """
    plot_df = df.copy()

    if max_points is not None and len(plot_df) > max_points:
        plot_df = plot_df.sample(max_points, random_state=42)

    marker_sizes = (plot_df["TotalNewAddSQFT"].clip(lower=1) ** (1 / 3)) / 4

    fig, ax = plt.subplots(figsize=(12, 10))
    ax.scatter(
        plot_df["Longitude"],
        plot_df["Latitude"],
        s=marker_sizes,
        alpha=0.4,
    )

    ax.set_title("Austin Construction Permits by Location and Added Square Footage")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    fig.tight_layout()
    return fig


def print_key_stats(df: pd.DataFrame) -> None:
    """
    Print a few high-value descriptive statistics for quick inspection.
    """
    total_sqft = df["TotalNewAddSQFT"].sum()
    total_projects = len(df)

    print("\nCleaned dataset summary")
    print("-" * 30)
    print(f"Projects with positive added square footage: {total_projects:,}")
    print(f"Total added square footage: {total_sqft:,.0f}")

    if "HousingUnits" in df.columns:
        print(f"Total housing units: {df['HousingUnits'].fillna(0).sum():,.0f}")

    if "NumberOfFloors" in df.columns:
        print("\nNumberOfFloors summary:")
        print(df["NumberOfFloors"].describe())

    print("\nTop ZIP codes by permit count:")
    print(df["OriginalZip"].astype(str).value_counts().head(10))


def save_figure(fig: plt.Figure, filename: str, output_dir: Path = OUTPUT_DIR) -> None:
    """
    Save a matplotlib figure to disk.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_dir / filename, dpi=300, bbox_inches="tight")


def main() -> None:
    df = load_permit_data(DATA_PATH)
    cleaned = clean_permit_data(df)

    quality_summary = summarize_data_quality(cleaned)
    print(quality_summary.head(20))

    print_key_stats(cleaned)

    figs = {
        "zip_code_counts.png": plot_zip_code_counts(cleaned),
        "floor_counts.png": plot_floor_counts(cleaned),
        "permit_class_counts.png": plot_permit_class_counts(cleaned),
        "job_valuation_histogram.png": plot_job_valuation_histogram(cleaned),
        "square_footage_map.png": plot_square_footage_map(cleaned),
    }

    for filename, fig in figs.items():
        save_figure(fig, filename)
        plt.close(fig)


if __name__ == "__main__":
    main()
