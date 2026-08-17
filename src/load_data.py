"""
ScholarMind Trade Intelligence
Data loading utilities.
"""

import json
from pathlib import Path


def load_data(file_path):
    """
    Load JSON data from a file.

    Parameters
    ----------
    file_path : str or Path
        Path to the JSON data file.

    Returns
    -------
    dict or list
        Loaded JSON data.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)