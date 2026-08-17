from src.trade_intelligence import TradeIntelligence


def test_trade_intelligence():
    intelligence = TradeIntelligence()
    assert intelligence is not None