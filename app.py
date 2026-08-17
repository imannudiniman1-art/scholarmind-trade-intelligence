"""
ScholarMind Trade Intelligence

AI-assisted market and trade analysis for SMEs.
Built with Streamlit.
"""

import json
import os
import tempfile

import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ScholarMind Trade Intelligence",
    page_icon="🧠",
    layout="wide",
)


# ============================================================
# APPLICATION TITLE
# ============================================================

st.title("🧠 ScholarMind Trade Intelligence")

st.write(
    "AI-assisted market analysis and decision support "
    "for SMEs and trade intelligence."
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_data(file_path):
    """
    Load trade data from JSON or CSV.
    Returns a list of dictionaries.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".json":
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # JSON may contain either a list or a dictionary
        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            # If JSON contains a data key
            if isinstance(data.get("data"), list):
                return data["data"]

            # Otherwise treat dictionary as one record
            return [data]

        return []

    if extension == ".csv":
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")

    raise ValueError("Unsupported file format. Please use CSV or JSON.")


def generate_recommendation(demand, risk):
    """
    Generate a simple trade recommendation
    based on demand and risk.
    """

    try:
        demand = float(demand)
    except (ValueError, TypeError):
        demand = 0

    try:
        risk = float(risk)
    except (ValueError, TypeError):
        risk = 0

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
    """
    Convert recommendation into a numeric score
    for visualization.
    """

    scores = {
        "BUY / EXPAND": 100,
        "CONSIDER": 75,
        "MONITOR": 50,
        "LOW PRIORITY": 25,
        "AVOID / HIGH RISK": 10,
    }

    return scores.get(recommendation, 0)


# ============================================================
# INITIALIZE DATA
# ============================================================

# IMPORTANT:
# This prevents NameError when no file has been uploaded.
data = []


# ============================================================
# LOAD TRADE DATA
# ============================================================

st.divider()

st.header("📂 Load Trade Data")

uploaded_file = st.file_uploader(
    "Upload a JSON or CSV file",
    type=["json", "csv"],
)


if uploaded_file is not None:

    try:

        suffix = os.path.splitext(uploaded_file.name)[