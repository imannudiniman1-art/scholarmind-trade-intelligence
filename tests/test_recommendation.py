from src.recommendation import generate_recommendation


def test_generate_recommendation():
    result = generate_recommendation("Increasing", 20, 10)
    assert result is not None