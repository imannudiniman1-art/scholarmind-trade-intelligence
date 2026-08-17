def analyze_market_trend(data):
    """
    Analyze market demand and classify the market trend.
    """

    if data is None or len(data) == 0:
        return "No data available"

    average_demand = data["demand"].mean()

    if average_demand >= 80:
        return "Strong Market Demand"
    elif average_demand >= 60:
        return "Moderate Market Demand"
    else:
        return "Weak Market Demand"