from src.load_data import load_data


def test_load_csv(tmp_path):
    file = tmp_path / "data.csv"

    file.write_text(
        "product,price\n"
        "Laptop,1000\n"
        "Phone,500\n",
        encoding="utf-8"
    )

    result = load_data(file)

    assert len(result) == 2
    assert result[0]["product"] == "Laptop"
    assert result[0]["price"] == "1000"


def test_load_json(tmp_path):
    file = tmp_path / "data.json"

    file.write_text(
        '[{"product": "Laptop", "price": 1000}]',
        encoding="utf-8"
    )

    result = load_data(file)

    assert len(result) == 1
    assert result[0]["product"] == "Laptop"
    assert result[0]["price"] == 1000


def test_unsupported_format(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("test", encoding="utf-8")

    try:
        load_data(file)
        assert False
    except ValueError:
        assert True