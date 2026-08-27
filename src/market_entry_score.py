"""
ScholarMind Trade Intelligence
Market Entry Score calculation.
"""


def calculate_market_entry_score(demand, profit_margin, risk):
    """
    Calculate a Market Entry Score from 0 to 100.

    Weights:
    - Market demand: 40%
    - Profit margin: 30%
    - Risk: 30% (lower risk is better)
    """

    if not 0 <= demand <= 100:
        raise ValueError("Demand must be between 0 and 100.")

    if profit_margin < 0:
        raise ValueError("Profit margin cannot be negative.")

    if not 0 <= risk <= 100:
        raise ValueError("Risk must be between 0 and 100.")

    # Normalize profit margin.
    # 50% margin or higher receives the maximum score.
    profit_score = min(profit_margin / 50 * 100, 100)

    # Lower risk produces a higher score.
    risk_score = 100 - risk

    score = (
        (demand * 0.40)
        + (profit_score * 0.30)
        + (risk_score * 0.30)
    )

    return round(score, 2)


def classify_market_entry_score(score):
    """
    Classify the Market Entry Score.
    """

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Promising"
    elif score >= 50:
        return "Moderate"
    else:
        return "High Risk"