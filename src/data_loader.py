import csv
import json
from pathlib import Path


def load_csv(file_path):
    """Load data from a CSV file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def load_json(file_path):
    """Load data from a JSON file."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_data(file_path):
    """Load CSV or JSON data based on the file extension."""
    path = Path(file_path)

    if path.suffix.lower() == ".csv":
        return load_csv(path)

    if path.suffix.lower() == ".json":
        return load_json(path)

    raise ValueError("Unsupported file format. Use CSV or JSON.")
