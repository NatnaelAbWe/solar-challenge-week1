# notebooks/benin_eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

RAW_DATA_PATH = "../data/benin_raw.csv"
CLEAN_DATA_PATH = "../data/benin_clean.csv"
SOLAR_COLS = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]

def load_data(path):
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    print(df.info())
    print(df.describe())
    return df

def clean_data(df, columns):
    z_scores = df[columns].apply(zscore)
    df = df[(np.abs(z_scores) < 3).all(axis=1)]
    df = df.fillna(df.median(numeric_only=True))
    return df

def plot_daily_solar(df):
    df.set_index("Timestamp")[["GHI", "DNI", "DHI"]].resample("D").mean().plot()
    plt.title("Daily Solar Radiation - Benin")
    plt.xlabel("Date")
    plt.ylabel("Radiation (W/m²)")
    plt.tight_layout()
    plt.show()

def plot_heatmap(df, columns):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[columns].corr(), annot=True, cmap="viridis")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data(RAW_DATA_PATH)

    print("\nMissing values:")
    missing = df.isna().sum()
    print(missing[missing > 0])

    df_clean = clean_data(df, SOLAR_COLS)

    plot_daily_solar(df_clean)
    plot_heatmap(df_clean, SOLAR_COLS)

    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"\nCleaned data saved to {CLEAN_DATA_PATH}")

if __name__ == "__main__":
    main()
