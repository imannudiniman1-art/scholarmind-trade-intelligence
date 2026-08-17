from src.profit import calculate_profit


def test_calculate_profit():
    assert calculate_profit(100, 120, 10) == 10