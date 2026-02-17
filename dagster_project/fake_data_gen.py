import pandas as pd
from faker import Faker
import random
import duckdb
import os

fake = Faker()

def generate_and_save_data():
    # Ambil path dari environment variable atau default ke root
    db_path = os.getenv("DUCKDB_PATH", "analytics.duckdb")
    
    # 1. Generate Data (Logika lo yang lama)
    users = [{"user_id": i + 1, "name": fake.name(), "address": fake.address().replace("\n", ", "), "created_at": "2026-02-01"} for i in range(10)]
    products = [
        {"product_id": 1, "name": "Laptop Asus TUF", "category": "Electronics", "price": 15000000},
        {"product_id": 2, "name": "Samsung Tab S10", "category": "Electronics", "price": 7000000},
        {"product_id": 3, "name": "iPhone 15", "category": "Electronics", "price": 20000000},
    ]
    orders = [{"order_id": i + 1, "user_id": random.randint(1, 10), "product_id": random.randint(1, 3), "amount": random.randint(1, 2), "order_date": "2026-02-15"} for i in range(20)]

    df_users = pd.DataFrame(users)
    df_products = pd.DataFrame(products)
    df_orders = pd.DataFrame(orders)

    # 2. SIMPAN KE DUCKDB (Versi Paling Stabil buat GitHub Actions)
    import sqlalchemy # Kita pake bantuan sqlalchemy (biasanya ikut keinstall pas install dbt-duckdb)
    
    # Bikin koneksi via SQLAlchemy engine
    engine = sqlalchemy.create_engine(f"duckdb:///{db_path}")
    
    # Tulis data pake pandas to_sql (Ini 100% aman dari error 'str not recognized')
    df_users.to_sql("raw_users", engine, if_exists="replace", index=False)
    df_products.to_sql("raw_products", engine, if_exists="replace", index=False)
    df_orders.to_sql("raw_orders", engine, if_exists="replace", index=False)
    
    print(f"✅ Success: Data ingested into {db_path} using SQLAlchemy engine")

if __name__ == "__main__":
    generate_and_save_data()