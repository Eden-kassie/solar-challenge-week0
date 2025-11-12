# app/utils.py
import pandas as pd
import plotly.express as px

def load_data(path: str):
    """Load a CSV file and return a pandas DataFrame."""
    return pd.read_csv(path)

def get_summary_stats(df):
    """Return mean, median, and std for GHI, DNI, and DHI."""
    return df[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)

def plot_box(df, metric):
    """Create a boxplot for a given metric colored by Country."""
    fig = px.box(df, x="Country", y=metric, color="Country",
                 title=f"{metric} Comparison Across Countries")
    return fig

def plot_bar(df):
    """Bar chart of average GHI by country."""
    avg_ghi = df.groupby("Country")["GHI"].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(avg_ghi, x="Country", y="GHI",
                 title="Average GHI by Country", color="Country")
    return fig
