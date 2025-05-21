# app/main.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

def display_summary(df, country):
    """Display summary statistics for a country."""
    st.subheader(f"{country} Summary Statistics")
    st.dataframe(df.describe())

def plot_metric(df, metric):
    """Plot a time series line chart for a selected metric."""
    st.subheader(f"{metric} Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="Timestamp", y=metric, ax=ax)
    ax.set_title(f"{metric} Time Series")
    ax.set_xlabel("Date")
    ax.set_ylabel(metric)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="Solar Dashboard", layout="wide")
    st.title("☀️ Solar Data Dashboard")

    country = st.selectbox("Select a Country", ["Benin", "Togo", "Sierra Leone"])
    df = load_data(country)

    display_summary(df, country)

    metric = st.selectbox("Select Metric to Plot", ["GHI", "DNI", "DHI"])
    plot_metric(df, metric)

if __name__ == "__main__":
    main()
