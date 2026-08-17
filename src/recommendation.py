def generate_recommendation(trend, growth, profit):
    if trend == "Increasing" and growth > 0 and profit > 0:
        return "Increase investment"

    if trend == "Decreasing" or profit < 0:
        return "Reduce risk"

    return "Maintain current strategy"