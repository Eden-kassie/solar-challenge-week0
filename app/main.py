# app/main.py
import streamlit as st
import pandas as pd
from app.utils import load_data, get_summary_stats, plot_box, plot_bar

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("☀️ Cross-Country Solar Potential Dashboard")
st.markdown("Compare GHI, DNI, and DHI across Benin, Sierra Leone, and Togo.")

# --- Sidebar ---
st.sidebar.header("Controls")
metric = st.sidebar.selectbox("Select Metric:", ["GHI", "DNI", "DHI"])

# --- Data Loading (simulate dynamic fetch) ---
data_paths = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_leone_clean.csv",
    "Togo": "data/togo_clean.csv"
}

dfs = []
for country, path in data_paths.items():
    try:
        df_temp = load_data(path)
        df_temp["Country"] = country
        dfs.append(df_temp)
    except FileNotFoundError:
        st.warning(f"⚠️ Missing data for {country}")

if dfs:
    df = pd.concat(dfs, ignore_index=True)

    # --- KPI Section ---
    st.subheader("Summary Statistics")
    st.dataframe(get_summary_stats(df))

    # --- Plots ---
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(plot_box(df, metric), use_container_width=True)

    with col2:
        st.plotly_chart(plot_bar(df), use_container_width=True)

    # --- Insights ---
    st.markdown("### 🔍 Insights")
    st.markdown("""
    - **Togo** tends to have the highest average GHI values.
    - **Benin** shows more stable solar potential across time.
    - **Sierra Leone** exhibits greater variability, suggesting more cloud cover.
    """)

else:
    st.error("No datasets found. Please add cleaned CSVs in the `data/` folder.")
