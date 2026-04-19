from sqlalchemy import create_engine
import pandas as pd
import os

def get_engine():
    engine = create_engine(
        "postgresql+psycopg2://postgres:1720@localhost:5432/stock_pipeline"
    )
    return engine

def save_to_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Data saved to {path}")

def save_to_postgres(df, table_name):
    engine = get_engine()

    df.to_sql(
        table_name,
        engine,
        if_exists='append',
        index=False
    )

    print(f"Loaded data into {table_name}")


def load_dim_stock():
    engine = get_engine()

    data = pd.DataFrame([
        ("AAPL", "Apple Inc.", "Technology"),
        ("TSLA", "Tesla Inc.", "Automotive"),
        ("MSFT", "Microsoft Corp.", "Technology"),
        ("GOOGL", "Alphabet Inc.", "Technology")
    ], columns=["symbol", "company_name", "sector"])

    data.to_sql("dim_stock", engine, if_exists="append", index=False)

    print("dim_stock loaded")