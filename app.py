import json
import os
import tempfile

import pandas as pd
import streamlit as st

from src.market_entry_score import (
    calculate_market_entry_score,
    classify_market_entry_score
)

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ScholarMind Trade Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            linear-gradient(
                180deg,
                #f8faff 0%,
                #ffffff 45%,
                #f8faff 100%
            );
    }

    /* Main container */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Main title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #202938;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        font-size: 1.15rem;
        color: #667085;
        margin-bottom: 2rem;
    }

    /* Hero box */
    .hero-box {
        padding: 1.5rem;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #eef4ff,
            #ffffff
        );
        border: 1px solid #dce6f7;
        margin-bottom: 1.5rem;
    }

    /* Section cards */
    .section-card {
        padding: 1.2rem;
        border-radius: 16px;
        background: #ffffff;
        border: 1px solid #e4e7ec;
        margin-bottom: 1rem;
    }

    /* Recommendation */
    .recommendation-box {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        background: #f8fafc;
        border: 1px solid #e4e7ec;
        margin-bottom: 0.7rem;
    }

    /* Small text */
    .small-text {
        color: #667085;
        font-size: 0.95rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #98a2b3;
        font-size: 0.9rem;
        padding-top: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FUNCTIONS
# ============================================================

def load_data(file_path):
    """Load CSV or JSON trade data."""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".csv":
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")

    if extension == ".json":

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):

            if isinstance(data.get("data"), list):
                return data["data"]

            return [data]

    return []


def to_number(value):
    """Convert values safely to float."""

    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def generate_recommendation(demand, risk):
    """Generate simple market recommendation."""

    if demand >= 70 and risk <= 30:
        return "BUY / EXPAND"

    if demand >= 60 and risk <= 50:
        return "CONSIDER"

    if demand >= 40 and risk <= 60:
        return "MONITOR"

    if risk >= 70:
        return "AVOID / HIGH RISK"

    return "LOW PRIORITY"


def recommendation_score(recommendation):
    """Convert recommendation to score."""

    scores = {
        "BUY / EXPAND": 100,
        "CONSIDER": 75,
        "MONITOR": 50,
        "LOW PRIORITY": 25,
        "AVOID / HIGH RISK": 10
    }

    return scores.get(recommendation, 0)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero-box">

    <div class="main-title">
    🧠 ScholarMind Trade Intelligence
    </div>

    <div class="subtitle">
    AI-assisted market analysis and decision support for SMEs.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    ### 🚀 Trade Intelligence Dashboard

    Upload your trade dataset to analyze:

    **📊 Market Demand · 💰 Profit · ⚠️ Risk · 🎯 Recommendation**
    """
)


# ============================================================
# QUICK INFORMATION
# ============================================================

st.markdown("### ⚡ Quick Guide")

q1, q2, q3 = st.columns(3)

with q1:
    st.info(
        "📂 **Upload Data**\n\n"
        "CSV or JSON trade dataset."
    )

with q2:
    st.info(
        "📊 **Analyze Market**\n\n"
        "Demand, price, cost and risk."
    )

with q3:
    st.info(
        "🎯 **Get Recommendation**\n\n"
        "Identify priority markets."
    )


# ============================================================
# DATA UPLOAD
# ============================================================

st.divider()

st.header("📂 Load Trade Data")

uploaded_file = st.file_uploader(
    "📂 Pilih file CSV atau JSON",
    type=["csv", "json"],
    help="Pilih dataset perdagangan dari perangkat Anda."
)


if "trade_data" not in st.session_state:
    st.session_state.trade_data = []

data = st.session_state.trade_data


if uploaded_file is not None:

    try:

        file_name = uploaded_file.name
        suffix = os.path.splitext(file_name)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as tmp:

            tmp.write(uploaded_file.getbuffer())
            temp_path = tmp.name

        data = load_data(temp_path)

        st.session_state.trade_data = data

        os.unlink(temp_path)

        if isinstance(data, list) and data:

            st.success(
                "✅ Trade data loaded successfully."
            )

            st.markdown("### 📄 Uploaded Dataset")

            st.dataframe(
                pd.DataFrame(data),
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "The file does not contain usable trade data."
            )

    except Exception as e:

        st.error(
            f"Unable to load data: {e}"
        )


# ============================================================
# MARKET ANALYTICS
# ============================================================

if isinstance(data, list) and data:

    st.divider()

    st.header("📊 Market Analytics")

    analysis_data = []

    # ========================================================
    # PREPARE DATA
    # ========================================================

    for item in data:

        if not isinstance(item, dict):
            continue

        market = item.get("market", "Unknown")

        demand = to_number(
            item.get("demand", 0)
        )

        risk = to_number(
            item.get("risk", 0)
        )

        price = to_number(
            item.get("price", 0)
        )

        cost = to_number(
            item.get("cost", 0)
        )

        quantity = to_number(
            item.get("quantity", 0)
        )

        margin = price - cost

        profit_margin = (
            (margin / price) * 100
            if price > 0
            else 0
        )

        profit = quantity * margin
# Keep profit margin within the valid scoring range
       score_profit_margin = max(
            0,
            min(100, profit_margin)
        )

        entry_score =calculate_market_entry_score(
            demand=demand,

        profit_margin=score_profit_margin,
            risk=risk
        )

        entry_class = classify_market_entry_score(
            entry_score
        )

        recommendation = generate_recommendation(
            demand,
            risk
        )

        analysis_data.append(
            {
                "market": market,
                "demand": demand,
                "risk": risk,
                "price": price,
                "cost": cost,
                "quantity": quantity,
                "margin": margin,
                "profit_margin": profit_margin,
                "profit": profit,
                "entry_score": entry_score,
                "entry_class": entry_class,
                "recommendation": recommendation
            }
        )

    # ========================================================
    # TRADE INTELLIGENCE
    # ========================================================

    if analysis_data:

        st.subheader("🧠 Trade Intelligence")

        col1, col2, col3, col4 = st.columns(4)

        avg_demand = (
            sum(x["demand"] for x in analysis_data)
            / len(analysis_data)
        )

        avg_risk = (
            sum(x["risk"] for x in analysis_data)
            / len(analysis_data)
        )

        total_profit = sum(
            x["profit"] for x in analysis_data
        )

        best_market = max(
            analysis_data,
            key=lambda x: x["demand"] - x["risk"]
        )

        with col1:
            st.metric(
                "Average Demand",
                f"{avg_demand:.1f}"
            )

        with col2:
            st.metric(
                "Average Risk",
                f"{avg_risk:.1f}"
            )

        with col3:
            st.metric(
                "Total Profit",
                f"{total_profit:,.0f}"
            )

        with col4:
            st.metric(
                "Priority Market",
                str(best_market["market"])
            )

        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.divider()

        st.subheader("💡 Trade Recommendations")

        for item in analysis_data:

            st.markdown(
                f"""
                <div class="recommendation-box">

                <strong>🏪 {item['market']}</strong><br>

                <span class="small-text">
                Demand: {item['demand']:.0f}
                &nbsp; | &nbsp;
                Risk: {item['risk']:.0f}
                &nbsp; | &nbsp;
                Profit: {item['profit']:,.0f}
                </span>

                <br><br>

                🎯 Recommendation:
                <strong>{item['recommendation']}</strong>

                </div>
                """,
                unsafe_allow_html=True
            )

        # ====================================================
        # COMPACT MARKET ANALYTICS CHARTS
        # ====================================================

        st.divider()

        st.subheader("📈 Market Analytics Charts")

        demand_df = pd.DataFrame(
            [
                {
                    "Market": x["market"],
                    "Demand": x["demand"]
                }
                for x in analysis_data
            ]
        )

        price_cost_df = pd.DataFrame(
            [
                {
                    "Market": x["market"],
                    "Price": x["price"],
                    "Cost": x["cost"]
                }
                for x in analysis_data
            ]
        )

        risk_demand_df = pd.DataFrame(
            [
                {
                    "Market": x["market"],
                    "Demand": x["demand"],
                    "Risk": x["risk"]
                }
                for x in analysis_data
            ]
        )

        profit_df = pd.DataFrame(
            [
                {
                    "Market": x["market"],
                    "Profit": x["profit"]
                }
                for x in analysis_data
            ]
        )

        recommendation_df = pd.DataFrame(
            [
                {
                    "Market": x["market"],
                    "Recommendation Score":
                        recommendation_score(
                            x["recommendation"]
                        )
                }
                for x in analysis_data
            ]
        )

        # ====================================================
        # ROW 1
        # ====================================================

        chart1, chart2 = st.columns(2)

        with chart1:

            st.markdown("**📊 Demand per Market**")

            st.bar_chart(
                demand_df.set_index("Market"),
                height=240
            )

        with chart2:

            st.markdown("**💰 Price vs Cost**")

            st.bar_chart(
                price_cost_df.set_index("Market"),
                height=240
            )

        # ====================================================
        # ROW 2
        # ====================================================

        chart3, chart4 = st.columns(2)

        with chart3:

            st.markdown("**⚠️ Risk vs Demand**")

            st.scatter_chart(
                risk_demand_df,
                x="Demand",
                y="Risk",
                height=240
            )

        with chart4:

            st.markdown("**📈 Profit Analysis**")

            st.bar_chart(
                profit_df.set_index("Market"),
                height=240
            )

        # ====================================================
        # RECOMMENDATION SCORE
        # ====================================================

        st.markdown("**🎯 Recommendation Score**")

        st.bar_chart(
            recommendation_df.set_index("Market"),
            height=220
        )

        # ====================================================
        # SUMMARY
        # ====================================================

        st.divider()

        st.subheader("📋 Market Analysis Summary")

        summary_df = pd.DataFrame(
            analysis_data
        )

        st.dataframe(
            summary_df[
                [
                    "market",
                    "demand",
                    "risk",
                    "price",
                    "cost",
                    "quantity",
                    "margin",
                    "profit",
                    "recommendation"
                ]
            ],
            use_container_width=True,
            hide_index=True,
            height=260
        )

        # ====================================================
        # PRIORITY MARKET
        # ====================================================

        st.divider()

        st.subheader("🚀 Priority Market")

        priority = max(
            analysis_data,
            key=lambda x:
            x["demand"] - x["risk"]
        )

        st.success(
            f"🏆 Priority Market: **{priority['market']}**"
        )

        p1, p2, p3 = st.columns(3)

        with p1:

            st.metric(
                "Demand",
                f"{priority['demand']:.0f}"
            )

        with p2:

            st.metric(
                "Risk",
                f"{priority['risk']:.0f}"
            )

        with p3:

            st.metric(
                "Recommendation",
                priority["recommendation"]
            )


        # ====================================================
        # PRIORITY MARKET
        # ====================================================

        st.divider()

        st.subheader("🚀 Priority Market")

        

        


# ============================================================
# NO DATA
# ============================================================

else:

    st.divider()

    st.info(
        "👆 Upload a CSV or JSON trade dataset "
        "to start Market Analytics."
    )

    st.subheader("📄 Required Data Fields")

    st.write(
        "Your dataset should contain:"
    )

    st.markdown(
        """
        - `market`
        - `demand`
        - `risk`
        - `price`
        - `cost`
        - `quantity`
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🧠 <strong>ScholarMind Trade Intelligence</strong><br>

    AI-assisted decision support for SMEs.<br>

    Market Analytics · Profit Analysis · Risk Analysis ·
    Trade Recommendations

    </div>
    """,
    unsafe_allow_html=True
)
