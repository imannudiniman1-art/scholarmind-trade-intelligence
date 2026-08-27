from src.trade_intelligence import TradeIntelligence


def test_trade_intelligence():
    intelligence = TradeIntelligence()
    assert intelligence is not None


def test_trade_intelligence_analysis():
    intelligence = TradeIntelligence()

    data = {
        "product": "Coffee",
        "price": 100,
        "quantity": 50,
        "unit_cost": 60,
        "additional_cost": 500,
        "demand": 85,
        "risk": 20,
    }

    result = intelligence.analyze(data)

    assert result["status"] == "success"
    assert result["product"] == "Coffee"
    assert result["revenue"] == 5000
    assert result["total_cost"] == 3500
    assert result["profit"] == 1500
    assert result["profit_margin"] == 30
    assert result["demand"] == 85
    assert result["risk_score"] == 20
    assert result["risk_level"] == "Low Risk"
    assert result["recommendation"] == "BUY"


def test_recommendation():
    intelligence = TradeIntelligence()

    data = {
        "product": "Coffee",
        "price": 100,
        "quantity": 10,
        "unit_cost": 60,
        "demand": 85,
        "risk": 20,
    }

    assert intelligence.recommend(data) == "BUY"


def test_risk_assessment():
    intelligence = TradeIntelligence()

    data = {
        "product": "Coffee",
        "price": 100,
        "quantity": 10,
        "risk": 70,
    }

    assert intelligence.assess_risk(data) == "High Risk"