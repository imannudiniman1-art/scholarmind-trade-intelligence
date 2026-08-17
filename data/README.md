# Data

This directory contains data resources used by the ScholarMind Trade Intelligence project.

## Purpose

The data layer supports analysis and decision-making related to trade intelligence, including:

- Product and market information
- Trade-related datasets
- Historical values used for trend analysis
- Data used for profit and risk assessment
- Input data for recommendation generation

## Data Formats

The project supports common structured data formats, including:

- JSON
- CSV

## Data Loading

Data can be loaded using the project's data loading utilities.

Example:

```python
from src.load_data import load_data

data = load_data("data/example.json")


For CSV data:

from src.load_data import load_data

data = load_data("data/example.csv").   


## Data Policy

No private, confidential, or personally identifiable information should be committed to this repository.
When using external datasets, appropriate source attribution and licensing information should be maintained.

## Example Data

Small example datasets may be included for testing and demonstration purposes.
Large datasets should not be committed directly to the repository. Instead, provide instructions or references for obtaining them.

## Status

The data loading functionality is covered by automated tests.