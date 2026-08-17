from src.recommendation import generate_recommendation


def test_generate_recommendation():
    assert generate_recommendation(85, 20) == "BUY"
    assert generate_recommendation(85, 30) == "CAUTION"
    assert generate_recommendation(75, 20) == "WATCH"
    assert generate_recommendation(75, 30) == "AVOID"