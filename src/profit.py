"""
ScholarMind Trade Intelligence
Profit and margin calculation utilities.
"""


def calculate_revenue(selling_price, quantity):
    """Calculate total revenue."""
    if selling_price <= 0:
        raise ValueError("Selling price must be greater than zero.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return selling_price * quantity


def calculate_total_cost(unit_cost, quantity, additional_cost=0):
    """Calculate total trade cost."""
    if unit_cost <= 0:
        raise ValueError("Unit cost must be greater than zero.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if additional_cost < 0:
        raise ValueError("Additional cost cannot be negative.")

    return (unit_cost * quantity) + additional_cost


def calculate_profit(revenue, total_cost):
    """Calculate net profit."""
    if revenue < 0:
        raise ValueError("Revenue cannot be negative.")

    if total_cost < 0:
        raise ValueError("Total cost cannot be negative.")

    return revenue - total_cost


def calculate_profit_margin(profit, revenue):
    """Calculate profit margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")

    return (profit / revenue) * 100