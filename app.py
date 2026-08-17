import pandas as pd
import os
import tempfile
import streamlit as st

from src.data_loader import load_data
from src.market_trend import analyze_market_trend
from src.profit import calculate_profit
from src.risk import assess_risk
from src.recommendation import generate_recommendation


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
        import tempfile
        import os

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as tmp:
            tmp.write(uploaded_file.getbuffer())
            temp_path = tmp.name

        data = load_data(temp_path)

        os.unlink(temp_path)

        st.success("Trade data loaded successfully.")

        if isinstance(data, list):
            st.dataframe(data, use_container_width=True)
        else:
            st.write(data)

    except Exception as e:
        st.error(f"Unable to load data: {e}")

st.divider()

st.header("🧠 Trade Intelligence")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Market Trend", "Strong Market Demand")

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