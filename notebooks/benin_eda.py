# notebooks/benin_eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load data
df = pd.read_csv("../data/benin_raw.csv", parse_dates=["Timestamp"])
print(df.info())
print(df.describe())

# Missing values
missing = df.isna().sum()
print("Missing values:\n", missing[missing > 0])

# Outlier detection
columns_to_check = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust"]
df_clean = df.copy()
z_scores = df_clean[columns_to_check].apply(zscore)
df_clean = df_clean[(np.abs(z_scores) < 3).all(axis=1)]

# Fill missing values with median
df_clean = df_clean.fillna(df_clean.median(numeric_only=True))

# Time series plot
df_clean.set_index("Timestamp")[["GHI", "DNI", "DHI"]].resample("D").mean().plot()
plt.title("Daily Solar Radiation - Benin")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_clean[columns_to_check].corr(), annot=True, cmap="viridis")
plt.title("Correlation Heatmap")
plt.show()

# Save cleaned data
df_clean.to_csv("../data/benin_clean.csv", index=False)
