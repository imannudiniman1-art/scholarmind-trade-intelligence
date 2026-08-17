"""
Profit analysis module for ScholarMind Trade Intelligence.
"""


def calculate_profit(price, cost, quantity):
    """Calculate total profit for a trade."""
    return (price - cost) * quantity


def calculate_profit_margin(price, cost):
    """Calculate profit margin as a percentage."""
    if price == 0:
        return 0

    return ((price - cost) / price) * 100


def analyze_profit(data):
    """
    Analyze profit for each trade record.

    Expected fields:
    - product
    - price
    - cost
    - quantity
    """

    results = []

    for item in data:
        price = float(item["price"])
        cost = float(item["cost"])
        quantity = float(item["quantity"])

        profit = calculate_profit(
            price,
            cost,
            quantity
        )

        margin = calculate_profit_margin(
            price,
            cost
        )

        results.append({
            "product": item["product"],
            "market": item.get("market", ""),
            "quantity": quantity,
            "price": price,
            "cost": cost,
            "profit": profit,
            "profit_margin": round(margin, 2)
        })

    return results


def total_profit(data):
    """Calculate total profit across all trades."""

    results = analyze_profit(data)

    return sum(
        item["profit"]
        for item in results
    )