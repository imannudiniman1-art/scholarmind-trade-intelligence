import pytest

from src.profit import (
    calculate_revenue,
    calculate_total_cost,
    calculate_profit,
    calculate_profit_margin,
)


def test_calculate_revenue():
    assert calculate_revenue(10, 100) == 1000


def test_calculate_total_cost():
    assert calculate_total_cost(6, 100, 50) == 650


def test_calculate_profit():
    assert calculate_profit(1000, 650) == 350


def test_calculate_profit_margin():
    assert calculate_profit_margin(350, 1000) == 35


def test_invalid_selling_price():
    with pytest.raises(ValueError):
        calculate_revenue(0, 100)


def test_invalid_quantity():
    with pytest.raises(ValueError):
        calculate_revenue(10, 0)


def test_negative_additional_cost():
    with pytest.raises(ValueError):
        calculate_total_cost(6, 100, -10)


def test_zero_revenue_margin():
    with pytest.raises(ValueError):
        calculate_profit_margin(100, 0)