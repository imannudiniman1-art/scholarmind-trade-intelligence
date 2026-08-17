from src.market_trend import calculate_growth, analyze_trend


def test_calculate_growth():
    assert calculate_growth(1000, 1250) == 25.0


def test_increasing_trend():
    result = analyze_trend(1000, 1250)

    assert result["growth"] == 25.0
    assert result["trend"] == "Increasing"


def test_decreasing_trend():
    result = analyze_trend(1000, 800)

    assert result["growth"] == -20.0
    assert result["trend"] == "Decreasing"


def test_stable_trend():
    result = analyze_trend(1000, 1020)

    assert result["growth"] == 2.0
    assert result["trend"] == "Stable"