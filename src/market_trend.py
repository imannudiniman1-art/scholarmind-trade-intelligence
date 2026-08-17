def analyze_market_trend(data):
    """
    Analyze basic market trend from price data.
    """

    if not data:
        return {
            "trend": "stable",
            "change": 0
        }

    first = data[0]
    last = data[-1]

    change = last - first

    if change > 0:
        trend = "up"
    elif change < 0:
        trend = "down"
    else:
        trend = "stable"

    return {
        "trend": trend,
        "change": change
    }


