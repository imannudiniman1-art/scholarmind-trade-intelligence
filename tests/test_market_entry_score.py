from src.market_entry_score import (
    calculate_market_entry_score,
    classify_market_entry_score,
)


def test_market_entry_score():
    score = calculate_market_entry_score(
        demand=85,
        profit_margin=30,
        risk=20,
    )

    assert score == 76.0


def test_market_entry_score_classification():
    assert classify_market_entry_score(90) == "Excellent"
    assert classify_market_entry_score(75) == "Promising"
    assert classify_market_entry_score(60) == "Moderate"
    assert classify_market_entry_score(40) == "High Risk"


def test_invalid_demand():
    try:
        calculate_market_entry_score(
            demand=120,
            profit_margin=30,
            risk=20,
        )
        assert False
    except ValueError:
        assert True


def test_invalid_risk():
    try:
        calculate_market_entry_score(
            demand=80,
            profit_margin=30,
            risk=120,
        )
        assert False
    except ValueError:
        assert True