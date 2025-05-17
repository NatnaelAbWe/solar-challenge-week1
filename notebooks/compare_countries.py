import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway  # for ANOVA

# Load the cleaned CSVs
benin = pd.read_csv("../data/benin-malanville.csv")
togo = pd.read_csv("../data/togo-dapaong_qc.csv")
sierra = pd.read_csv("../data/sierraleone-bumbuna.csv")

# Add country labels
benin['Country'] = 'Benin'
togo['Country'] = 'Togo'
sierra['Country'] = 'Sierra Leone'

# Combine datasets
df_all = pd.concat([benin, togo, sierra], ignore_index=True)

# Boxplots for solar metrics
for metric in ['GHI', 'DNI', 'DHI']:
    sns.boxplot(x='Country', y=metric, data=df_all)
    plt.title(f"{metric} Comparison Across Countries")
    plt.show()

# Summary table
summary = df_all.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std'])
print(summary)

# One-way ANOVA (optional)
f_val, p_val = f_oneway(benin['GHI'], togo['GHI'], sierra['GHI'])
print(f"ANOVA F-value: {f_val:.2f}, p-value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Significant differences in GHI across countries")
else:
    print("⚠️ No statistically significant difference in GHI")
