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

    # 2. SIMPAN KE DUCKDB (Lebih aman buat GitHub Actions)
    con = duckdb.connect(db_path)
    
    # Daftarkan dataframe sebagai view sementara agar DuckDB bisa baca
    con.register("df_users_temp", df_users)
    con.register("df_products_temp", df_products)
    con.register("df_orders_temp", df_orders)

    # Buat tabel asli dari view tersebut
    con.execute("CREATE TABLE IF NOT EXISTS raw_users AS SELECT * FROM df_users_temp")
    con.execute("CREATE TABLE IF NOT EXISTS raw_products AS SELECT * FROM df_products_temp")
    con.execute("CREATE TABLE IF NOT EXISTS raw_orders AS SELECT * FROM df_orders_temp")
    
    # Refresh data jika sudah ada
    con.execute("OR REPLACE TABLE raw_users AS SELECT * FROM df_users_temp")
    con.execute("OR REPLACE TABLE raw_products AS SELECT * FROM df_products_temp")
    con.execute("OR REPLACE TABLE raw_orders AS SELECT * FROM df_orders_temp")
    
    con.close()
    print(f"✅ Success: Data ingested into {db_path}")

if __name__ == "__main__":
    generate_and_save_data()