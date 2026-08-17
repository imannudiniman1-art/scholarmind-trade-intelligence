from src.market_trend import calculate_growth, analyze_trend


def test_calculate_growth():
    assert calculate_growth(100, 120) == 20.0


def test_increasing_trend():
    result = analyze_trend(100, 120)

    assert result["trend"] == "Increasing"
    assert result["growth"] == 20.0


def test_decreasing_trend():
    result = analyze_trend(100, 80)

    assert result["trend"] == "Decreasing"
    assert result["growth"] == -20.0


def test_stable_trend():
    result = analyze_trend(100, 102)

    assert result["trend"] == "Stable"
    assert result["growth"] == 2.0
