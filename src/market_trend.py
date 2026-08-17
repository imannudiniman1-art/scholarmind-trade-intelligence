"""
Market Trend Analysis

Analyzes product sales data and determines
the direction of market trends.
"""


def calculate_growth(previous_sales, current_sales):
    """Calculate sales growth percentage."""

    if previous_sales == 0:
        return 0.0

    growth = ((current_sales - previous_sales) / previous_sales) * 100
    return round(growth, 2)


def analyze_trend(previous_sales, current_sales):
    """Analyze market trend based on sales growth."""

    growth = calculate_growth(previous_sales, current_sales)

    if growth > 5:
        trend = "Increasing"
    elif growth < -5:
        trend = "Decreasing"
    else:
        trend = "Stable"

    return {
        "growth": growth,
        "trend": trend
    }