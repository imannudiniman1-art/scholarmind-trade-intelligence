def calculate_profit(cost, price, expense=0):
    """
    Calculate profit from a trade.

    Profit = selling price - cost - expense
    """
    return price - cost - expense


def calculate_profit_margin(cost, price, expense=0):
    """
    Calculate profit margin as percentage.
    """
    profit = calculate_profit(cost, price, expense)

    if price == 0:
        return 0

    return (profit / price) * 100