def generate_recommendation(data):
    """
    Generate a simple business recommendation
    based on demand, risk, and profit.
    """

    recommendations = []

    for item in data:
        product = item.get("product", "Unknown")
        demand = item.get("demand", 0)
        risk = item.get("risk", 0)
        price = item.get("price", 0)
        cost = item.get("cost", 0)

        profit = price - cost

        if demand >= 80 and risk <= 25 and profit > 0:
            recommendation = "High potential"
        elif risk >= 30:
            recommendation = "High risk"
        elif profit > 0:
            recommendation = "Moderate potential"
        else:
            recommendation = "Low potential"

        recommendations.append({
            "product": product,
            "recommendation": recommendation
        })

    return recommendations