def generate_recommendation(demand, risk):
    """
    Generate a simple trade recommendation
    based on market demand and risk.

    High demand + low risk -> BUY
    High demand + high risk -> CAUTION
    Low demand + low risk -> WATCH
    Low demand + high risk -> AVOID
    """

    if demand >= 80 and risk < 30:
        return "BUY"

    if demand >= 80 and risk >= 30:
        return "CAUTION"

    if demand < 80 and risk < 30:
        return "WATCH"

    return "AVOID"