# app/utils.py

import pandas as pd
from typing import Optional

DATA_PATHS = {
    "Benin": "../data/benin-malanville.csv",
    "Togo": "../data/togo-dapaong_qc.csv",
    "Sierra Leone": "../data/sierraleone-bumbuna.csv"
}

def load_data(country: str, timestamp_col: str = "Timestamp") -> pd.DataFrame:
    """
    Load dataset for a given country.

    Parameters:
    - country (str): Name of the country.
    - timestamp_col (str): Name of the datetime column to parse.

    Returns:
    - pd.DataFrame: Loaded dataset.

    Raises:
    - ValueError: If the country is not in the dataset map.
    - FileNotFoundError: If the file is missing.
    """
    if country not in DATA_PATHS:
        raise ValueError(f"{country} is not a recognized country. Choose from: {list(DATA_PATHS.keys())}")

    try:
        df = pd.read_csv(DATA_PATHS[country], parse_dates=[timestamp_col])
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file for {country} not found: {e}")
