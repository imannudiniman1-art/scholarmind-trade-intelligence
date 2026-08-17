def generate_recommendation(demand, risk, profit):
    """
    Generate a simple business recommendation
    based on demand, risk, and profit.
    """

    if demand >= 80 and risk < 30 and profit > 0:
        return "Strong Buy"

    if demand >= 70 and risk < 50 and profit > 0:
        return "Recommended"

    if profit > 0 and risk < 60:
        return "Consider"

    return "Avoid"