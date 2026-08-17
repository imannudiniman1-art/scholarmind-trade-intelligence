def calculate_growth(old_value, new_value):
    if old_value == 0:
        return 0.0

    return ((new_value - old_value) / old_value) * 100


def analyze_trend(old_value, new_value):
    growth = calculate_growth(old_value, new_value)

    if growth > 2:
        trend = "Increasing"
    elif growth < -2:
        trend = "Decreasing"
    else:
        trend = "Stable"

    return {
        "trend": trend,
        "growth": growth
    }