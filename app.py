import streamlit as st
import pandas as pd

from src.data_loader import load_data


st.set_page_config(
    page_title="ScholarMind Trade Intelligence",
    page_icon="📊",
    layout="wide",
)


st.title("📊 ScholarMind Trade Intelligence")

st.markdown(
    """
    **AI-powered trade intelligence and decision support platform for SMEs.**

    Analyze trade data to understand market trends, profitability,
    risk, and business recommendations.
    """
)

st.divider()

st.header("📂 Load Trade Data")

uploaded_file = st.file_uploader(
    "Upload a JSON or CSV file",
    type=["json", "csv"],
)

if uploaded_file is not None:

    try:
        if uploaded_file.name.endswith(".json"):
            data = load_data(uploaded_file)

        elif uploaded_file.name.endswith(".csv"):
            data = load_data(uploaded_file)

        st.success("Data loaded successfully!")

        st.subheader("📋 Data Preview")

        if isinstance(data, pd.DataFrame):
            st.dataframe(data, use_container_width=True)

        else:
            st.write(data)

    except Exception as e:
        st.error(f"Unable to load data: {e}")

else:
    st.info(
        "Upload a trade dataset to begin the analysis."
    )


st.divider()

st.header("🧠 Trade Intelligence")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Market Trend", "Ready")

with col2:
    st.metric("Profit Analysis", "Ready")

with col3:
    st.metric("Risk Analysis", "Ready")

with col4:
    st.metric("Recommendation", "Ready")


st.divider()

st.caption(
    "ScholarMind Trade Intelligence — AI-assisted decision support for SMEs."
)