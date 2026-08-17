import pandas as pd
import os
import tempfile
import streamlit as st

from src.data_loader import load_data
from src.market_trend import analyze_market_trend
from src.profit import calculate_profit
from src.risk import assess_risk
from src.recommendation import generate_recommendation
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
st.divider()

st.subheader("📊 Market Analytics")

if isinstance(data, list) and data:

    # Prepare analysis data
    analysis_data = []

    for item in data:
        market = item.get("market", "Unknown")
        demand = item.get("demand", 0)
        risk = item.get("risk", 0)
        price = item.get("price", 0)
        cost = item.get("cost", 0)
        quantity = item.get("quantity", 0)

        margin = price - cost
        profit = quantity * margin

        recommendation = generate_recommendation(
            demand,
            risk
        )

        analysis_data.append({
            "market": market,
            "demand": demand,
            "risk": risk,
            "price": price,
            "cost": cost,
            "margin": margin,
            "quantity": quantity,
            "profit": profit,
            "recommendation": recommendation
        })

    # ------------------------------------------------
    # 1. Demand per Market
    # ------------------------------------------------
    st.subheader("📊 Demand per Market")

    demand_chart = {
        item["market"]: item["demand"]
        for item in analysis_data
    }

    st.bar_chart(demand_chart)

    # ------------------------------------------------
    # 2. Price vs Cost
    # ------------------------------------------------
    st.subheader("💰 Price vs Cost")

    price_cost_chart = {
        item["market"]: {
            "Price": item["price"],
            "Cost": item["cost"]
        }
        for item in analysis_data
    }

    import pandas as pd

    price_cost_df = pd.DataFrame(price_cost_chart).T

    st.bar_chart(price_cost_df)

    # ------------------------------------------------
    # 3. Risk vs Demand
    # ------------------------------------------------
    st.subheader("⚠️ Risk vs Demand")

    risk_demand_df = pd.DataFrame([
        {
            "market": item["market"],
            "Demand": item["demand"],
            "Risk": item["risk"]
        }
        for item in analysis_data
    ])

    st.scatter_chart(
        risk_demand_df,
        x="Demand",
        y="Risk"
    )

    # ------------------------------------------------
    # 4. Profit Analysis
    # ------------------------------------------------
    st.subheader("📈 Profit Analysis")

    profit_chart = {
        item["market"]: item["profit"]
        for item in analysis_data
    }

    st.bar_chart(profit_chart)

    # ------------------------------------------------
    # 5. Recommendation Chart
    # ------------------------------------------------
    st.subheader("🧠 Recommendation Chart")

    recommendation_score = {
        "BUY": 4,
        "CAUTION": 3,
        "WATCH": 2,
        "AVOID": 1
    }

    recommendation_df = pd.DataFrame([
        {
            "market": item["market"],
            "Recommendation": recommendation_score[
                item["recommendation"]
            ]
        }
        for item in analysis_data
    ])

    st.bar_chart(
        recommendation_df.set_index("market")
    )

    # ------------------------------------------------
    # Summary table
    # ------------------------------------------------
    st.subheader("📋 Market Analysis Summary")

    summary_df = pd.DataFrame(analysis_data)

    st.dataframe(
        summary_df[
            [
                "market",
                "demand",
                "risk",
                "price",
                "cost",
                "margin",
                "quantity",
                "profit",
                "recommendation"
            ]
        ],
        use_container_width=True
    )

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

st.subheader("🧠 Trade Recommendations")

if isinstance(data, list):
    for item in data:
        market = item.get("market", "Unknown")
        demand = item.get("demand", 0)
        risk = item.get("risk", 0)

        recommendation = generate_recommendation(demand, risk)

        st.write(
            f"**{market}** — Demand: {demand}, Risk: {risk} → "
            f"**{recommendation}**"
        )
st.divider()

st.subheader("📊 Market Demand vs Risk")

if isinstance(data, list) and data:
    df = pd.DataFrame(data)

    if "market" in df.columns and "demand" in df.columns and "risk" in df.columns:
        chart_data = df.set_index("market")[["demand", "risk"]]
        st.bar_chart(chart_data)
    else:
        st.warning("Data must contain market, demand, and risk columns.")

st.divider()

st.caption(
    "ScholarMind Trade Intelligence — AI-assisted decision support for SMEs."
)