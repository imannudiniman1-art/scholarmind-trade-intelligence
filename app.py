import json
import os
import tempfile

import pandas as pd
import streamlit as st


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="ScholarMind Trade Intelligence",
    page_icon="🧠",
    layout="wide"
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

st.title("🧠 ScholarMind Trade Intelligence")

st.write(
    "AI-assisted market analysis and decision support "
    "for SMEs."
)


# ============================================================
# INITIAL DATA
# ============================================================

data = []


# ============================================================
# UPLOAD DATA
# ============================================================

st.divider()

st.header("📂 Load Trade Data")

uploaded_file = st.file_uploader(
    "Upload a JSON or CSV file",
    type=["json", "csv"]
)


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

        os.unlink(temp_path)

        st.success("✅ Trade data loaded successfully.")

        if isinstance(data, list) and data:

            st.dataframe(
                pd.DataFrame(data),
                use_container_width=True
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


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    for item in data:

        if not isinstance(item, dict):
            continue

        market = item.get("market", "Unknown")

        demand = item.get("demand", 0)
        risk = item.get("risk", 0)
        price = item.get("price", 0)
        cost = item.get("cost", 0)
        quantity = item.get("quantity", 0)

        try:
            demand = float(demand)
        except:
            demand = 0

        try:
            risk = float(risk)
        except:
            risk = 0

        try:
            price = float(price)
        except:
            price = 0

        try:
            cost = float(cost)
        except:
            cost = 0

        try:
            quantity = float(quantity)
        except:
            quantity = 0

        margin = price - cost

        profit = quantity * margin

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
                "profit": profit,
                "recommendation": recommendation
            }
        )


    # --------------------------------------------------------
    # TRADE INTELLIGENCE
    # --------------------------------------------------------

    st.subheader("🧠 Trade Intelligence")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Market Trend",
            "Strong Demand"
        )

    with col2:
        st.metric(
            "Profit Analysis",
            "Ready"
        )

    with col3:
        st.metric(
            "Risk Analysis",
            "Ready"
        )

    with col4:
        st.metric(
            "Recommendation",
            "Ready"
        )


    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    st.divider()

    st.subheader("💡 Trade Recommendations")

    for item in analysis_data:

        st.write(
            f"**{item['market']}** — "
            f"Demand: {item['demand']:.0f}, "
            f"Risk: {item['risk']:.0f} → "
            f"**{item['recommendation']}**"
        )


    # --------------------------------------------------------
    # DEMAND
    # --------------------------------------------------------

    st.divider()

    st.subheader("📊 Demand per Market")

    demand_data = {
        item["market"]: item["demand"]
        for item in analysis_data
    }
        if demand_data:
          st.bar_chart(demand_data)


    # --------------------------------------------------------
    # PRICE VS COST
    # --------------------------------------------------------

    st.subheader("💰 Price vs Cost")

    price_cost_data = {
        item["market"]: {
            "Price": item["price"],
            "Cost": item["cost"]
        }
        for item in analysis_data
    }

    if price_cost_data:

        price_cost_df = pd.DataFrame(
            price_cost_data
        ).T

        st.bar_chart(price_cost_df)


    # --------------------------------------------------------
    # RISK VS DEMAND
    # --------------------------------------------------------

    st.subheader("⚠️ Risk vs Demand")

    risk_demand_df = pd.DataFrame(
        [
            {
                "Market": item["market"],
                "Demand": item["demand"],
                "Risk": item["risk"]
            }
            for item in analysis_data
        ]
    )

    if not risk_demand_df.empty:

        st.scatter_chart(
            risk_demand_df,
            x="Demand",
            y="Risk"
        )


    # --------------------------------------------------------
    # PROFIT
    # --------------------------------------------------------

    st.subheader("📈 Profit Analysis")

    profit_data = {
        item["market"]: item["profit"]
        for item in analysis_data
    }

    if profit_data:
        st.bar_chart(profit_data)


    # --------------------------------------------------------
    # RECOMMENDATION SCORE
    # --------------------------------------------------------

    st.subheader("🎯 Recommendation Score")

    recommendation_data = {
        item["market"]: recommendation_score(
            item["recommendation"]
        )
        for item in analysis_data
    }

    if recommendation_data:

        recommendation_df = pd.DataFrame(
            {
                "Recommendation Score":
                    recommendation_data
            }
        )

        st.bar_chart(recommendation_df)


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    st.divider()

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
                "quantity",
                "margin",
                "profit",
                "recommendation"
            ]
        ],
        use_container_width=True
    )


    # --------------------------------------------------------
    # BEST MARKET
    # --------------------------------------------------------

    st.subheader("🚀 Priority Market")

    best_market = max(
        analysis_data,
        key=lambda x: x["demand"] - x["risk"]
    )

    st.success(
        f"Priority Market: **{best_market['market']}**"
    )

    st.write(
        f"Demand: **{best_market['demand']:.0f}**"
    )

    st.write(
        f"Risk: **{best_market['risk']:.0f}**"
    )

    st.write(
        f"Recommendation: **{best_market['recommendation']}**"
    )


# ============================================================
# NO DATA MESSAGE
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

    st.write(
        """
        - market
        - demand
        - risk
        - price
        - cost
        - quantity
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "ScholarMind Trade Intelligence — "
    "AI-assisted decision support for SMEs."
)