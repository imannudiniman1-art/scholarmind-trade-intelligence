"""
ScholarMind Trade Intelligence
Data loading utilities.
"""

import csv
import json
from pathlib import Path


def load_data(file_path):
    """
    Load data from JSON or CSV file.

    Returns:
        dict or list: Loaded data.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    suffix = path.suffix.lower()

    # Load JSON
    if suffix == ".json":
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    # Load CSV
    if suffix == ".csv":
        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    raise ValueError(f"Unsupported file format: {suffix}")
