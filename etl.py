from extract import read_csv
from transform import clean_data
from load import load_to_postgres
import os

if __name__ == "__main__":
    raw_path = os.path.join("data", "raw", "index_1.csv")
    processed_path = os.path.join("data", "processed", "cleaned_sales.parquet")

    df = read_csv(raw_path)
    df_clean = clean_data(df)

    # ✅ Fix: create the directory if it doesn't exist
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    # Save cleaned file as parquet
    df_clean.to_parquet(processed_path, index=False)

    # Load to PostgreSQL
    load_to_postgres(
        df_clean,
        table_name='coffee_sales',
        user='postgres',
        password='112311',
        db='postgres'
    )
