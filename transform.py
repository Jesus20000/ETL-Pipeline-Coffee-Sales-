import pandas as pd

def clean_data(df):
    df = df.dropna(subset=["card"]).copy()  # <- add .copy()

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["hour"] = df["datetime"].dt.hour
    df["is_cash"] = df["cash_type"].apply(lambda x: 1 if x.strip().lower() == "cash" else 0)

    return df
