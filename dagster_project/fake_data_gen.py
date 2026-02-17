import pandas as pd
from faker import Faker
import random
import duckdb
import os
import sqlalchemy

fake = Faker()

def generate_and_save_data():
    """
    Generates synthetic data and ingests it into a DuckDB database.
    Designed for reliability within CI/CD environments (e.g., GitHub Actions).
    """
    # Retrieve database path from environment variable or use default
    db_path = os.getenv("DUCKDB_PATH", "analytics.duckdb")
    
    # 1. Data Generation (Synthetic Data Layer)
    users = [
        {
            "user_id": i + 1, 
            "name": fake.name(), 
            "address": fake.address().replace("\n", ", "), 
            "created_at": "2026-02-01"
        } for i in range(10)
    ]
    
    products = [
        {"product_id": 1, "name": "Laptop Asus TUF", "category": "Electronics", "price": 15000000},
        {"product_id": 2, "name": "Samsung Tab S10", "category": "Electronics", "price": 7000000},
        {"product_id": 3, "name": "iPhone 15", "category": "Electronics", "price": 20000000},
    ]
    
    orders = [
        {
            "order_id": i + 1, 
            "user_id": random.randint(1, 10), 
            "product_id": random.randint(1, 3), 
            "amount": random.randint(1, 2), 
            "order_date": "2026-02-15"
        } for i in range(20)
    ]

    df_users = pd.DataFrame(users)
    df_products = pd.DataFrame(products)
    df_orders = pd.DataFrame(orders)

    # 2. Database Ingestion (Reliable Ingestion via SQLAlchemy)
    # Using SQLAlchemy engine to ensure compatibility and stability
    engine = sqlalchemy.create_engine(f"duckdb:///{db_path}")
    
    # Persisting DataFrames to DuckDB using 'replace' strategy for the Raw Layer
    df_users.to_sql("raw_users", engine, if_exists="replace", index=False)
    df_products.to_sql("raw_products", engine, if_exists="replace", index=False)
    df_orders.to_sql("raw_orders", engine, if_exists="replace", index=False)
    
    print(f"✅ Success: Data successfully ingested into {db_path} via SQLAlchemy engine.")

if __name__ == "__main__":
    generate_and_save_data()