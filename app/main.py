# app/main.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data  # 👈 import the helper function

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("☀️ Solar Data Dashboard")

country = st.selectbox("Select a Country", ["Benin", "Togo", "Sierra Leone"])
df = load_data(country)

st.subheader(f"{country} Summary")
st.write(df.describe())

metric = st.selectbox("Select Metric to Plot", ["GHI", "DNI", "DHI"])
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Timestamp", y=metric, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
