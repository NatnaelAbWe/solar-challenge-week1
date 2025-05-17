# app/utils.py

import pandas as pd

def load_data(country):
    file_map = {
        "Benin": "../data/benin-malanville.csv",
        "Togo": "../data/togo-dapaong_qc.csv",
        "Sierra Leone": "../data/sierraleone-bumbuna.csv"
    }
    try:
        df = pd.read_csv(file_map[country], parse_dates=["Timestamp"])
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file for {country} not found.")
