def generate_recommendation(trend, demand, risk):
    """
    Generate a trade recommendation based on
    market trend, demand, and risk.
    """

    if trend == "Increasing" and demand >= 20 and risk <= 10:
        return "BUY"

    if trend == "Increasing" and demand >= 20:
        return "CAUTION"

    if trend == "Decreasing" and risk >= 30:
        return "AVOID"

    return "WATCH"