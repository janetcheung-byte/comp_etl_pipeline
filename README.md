# Compensation ETL Pipeline

This project demonstrates how to extract, transform, and load public compensation-related data using the U.S. Bureau of Labor Statistics API.

## Features

- Uses BLS API to fetch time series compensation data
- Cleans and transforms raw JSON into a tabular format
- Saves results to CSV for further analysis

## Setup

```bash
pip install requests pandas
python main.py
```

## Output

CSV file at `data/processed/bls_compensation.csv` with series data for CPI and Services.