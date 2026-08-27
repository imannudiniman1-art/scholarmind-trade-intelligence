"""
ScholarMind Trade Intelligence
Main integration layer for trade analysis.
"""

from src.data_loader import load_trade_data
from src.profit import (
    calculate_revenue,
    calculate_total_cost,
    calculate_profit,
    calculate_profit_margin,
)
from src.risk import assess_risk
from src.recommendation import generate_recommendation


class TradeIntelligence:
    """
    Main interface for ScholarMind Trade Intelligence.
    """

    def __init__(self):
        self.name = "ScholarMind Trade Intelligence"

    def analyze(self, data):
        """
        Analyze a single trade opportunity.
        """

        # 1. Validate trade data
        trade = load_trade_data(data)

        # 2. Calculate revenue
        revenue = calculate_revenue(
            trade["price"],
            trade["quantity"]
        )

        # 3. Calculate total cost
        unit_cost = trade.get("unit_cost", trade["price"])
        additional_cost = trade.get("additional_cost", 0)

        total_cost = calculate_total_cost(
            unit_cost,
            trade["quantity"],
            additional_cost
        )

        # 4. Calculate profit
        profit = calculate_profit(
            revenue,
            total_cost
        )

        # 5. Calculate profit margin
        margin = calculate_profit_margin(
            profit,
            revenue
        )

        # 6. Risk score
        risk_score = trade.get("risk", 50)

        # 7. Risk classification
        risk_level = assess_risk(risk_score)

        # 8. Market demand
        demand = trade.get("demand", 0)

        # 9. Recommendation
        recommendation = generate_recommendation(
            demand,
            risk_score
        )

        return {
            "status": "success",
            "product": trade["product"],
            "revenue": revenue,
            "total_cost": total_cost,
            "profit": profit,
            "profit_margin": margin,
            "demand": demand,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "recommendation": recommendation,
        }

    def recommend(self, data):
        """
        Generate recommendation from trade data.
        """

        result = self.analyze(data)
        return result["recommendation"]

    def assess_risk(self, data):
        """
        Assess risk from trade data.
        """

        risk_score = data.get("risk", 50)
        return assess_risk(risk_score)