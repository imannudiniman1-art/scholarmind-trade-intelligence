import pytest

from src.data_loader import load_trade_data, validate_trade_data


def test_valid_trade_data():
    data = {
        "product": "Coffee",
        "price": 5.0,
        "quantity": 100,
    }

    assert validate_trade_data(data) is True
    assert load_trade_data(data) == data


def test_missing_required_field():
    data = {
        "product": "Coffee",
        "price": 5.0,
    }

    with pytest.raises(ValueError):
        validate_trade_data(data)


def test_invalid_price():
    data = {
        "product": "Coffee",
        "price": 0,
        "quantity": 100,
    }

    with pytest.raises(ValueError):
        validate_trade_data(data)


def test_invalid_quantity():
    data = {
        "product": "Coffee",
        "price": 5.0,
        "quantity": 0,
    }

    with pytest.raises(ValueError):
        validate_trade_data(data)


def test_invalid_data_type():
    with pytest.raises(TypeError):
        validate_trade_data("invalid")