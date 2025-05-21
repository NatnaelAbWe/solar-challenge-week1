# notebooks/compare_countries.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

DATA_PATHS = {
    "Benin": "../data/benin-malanville.csv",
    "Togo": "../data/togo-dapaong_qc.csv",
    "Sierra Leone": "../data/sierraleone-bumbuna.csv"
}

METRICS = ["GHI", "DNI", "DHI"]

def load_country_data(name, path):
    df = pd.read_csv(path)
    df["Country"] = name
    return df

def load_all_data():
    return pd.concat([load_country_data(name, path) for name, path in DATA_PATHS.items()], ignore_index=True)

def plot_boxplots(df):
    for metric in METRICS:
        plt.figure()
        sns.boxplot(x="Country", y=metric, data=df)
        plt.title(f"{metric} Comparison Across Countries")
        plt.tight_layout()
        plt.show()

def display_summary(df):
    summary = df.groupby("Country")[METRICS].agg(["mean", "median", "std"])
    print("\nSummary Statistics:")
    print(summary)

def perform_anova(df, metric="GHI"):
    samples = [df[df["Country"] == country][metric] for country in df["Country"].unique()]
    f_val, p_val = f_oneway(*samples)
    print(f"\nANOVA for {metric} — F-value: {f_val:.2f}, p-value: {p_val:.4f}")
    if p_val < 0.05:
        print("✅ Statistically significant differences detected.")
    else:
        print("⚠️ No statistically significant differences detected.")

def main():
    df_all = load_all_data()
    plot_boxplots(df_all)
    display_summary(df_all)
    perform_anova(df_all, metric="GHI")

if __name__ == "__main__":
    main()
