def generate_recommendation(demand, risk):
    """
    Generate a trade recommendation
    based on demand and risk.
    """

    if demand >= 80 and risk < 30:
        return "BUY"

    if demand >= 80 and risk >= 30:
        return "CAUTION"

    if demand < 80 and risk < 30:
        return "WATCH"

    return "AVOID"