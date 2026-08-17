from src.risk import assess_risk


def test_assess_risk():
    result = assess_risk(10)
    assert result is not None