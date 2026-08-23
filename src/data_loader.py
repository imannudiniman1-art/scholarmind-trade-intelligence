"""
ScholarMind Trade Intelligence
Data loading and validation utilities.
"""


REQUIRED_FIELDS = [
    "product",
    "price",
    "quantity",
]


def validate_trade_data(data):
    """
    Validate a single trade data record.

    Parameters
    ----------
    data : dict
        Trade data containing product, price, and quantity.

    Returns
    -------
    bool
        True when the data is valid.

    Raises
    ------
    TypeError
        If data is not a dictionary.
    ValueError
        If required fields are missing or values are invalid.
    """

    if not isinstance(data, dict):
        raise TypeError("Trade data must be a dictionary.")

    missing_fields = [
        field for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing_fields:
        raise ValueError(
            f"Missing required fields: {missing_fields}"
        )

    if not isinstance(data["product"], str) or not data["product"].strip():
        raise ValueError("Product must be a non-empty string.")

    if data["price"] <= 0:
        raise ValueError("Price must be greater than zero.")

    if data["quantity"] <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return True


def load_trade_data(data):
    """
    Validate and return trade data.
    """

    validate_trade_data(data)

    return data