from etl.extract import fetch_bls_data
from etl.transform import transform_bls_json
from etl.load import save_to_csv

def main():
    series_ids = ['CUUR0000SA0', 'SUUR0000SA0']
    start_year = 2020
    end_year = 2024

    print("Fetching data...")
    raw_json = fetch_bls_data(series_ids, start_year, end_year)

    print("Transforming data...")
    df = transform_bls_json(raw_json)

    print("Saving data...")
    save_to_csv(df, "data/processed/bls_compensation.csv")

    print("Done.")

if __name__ == "__main__":
    main()