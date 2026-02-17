from dagster import Definitions, asset
from .fake_data_gen import generate_fake_data
import duckdb
import os

def get_db_path():
    return "/opt/dagster/app/analytics.duckdb"

@asset
def raw_users():
    df_users, _, _ = generate_fake_data()
    with duckdb.connect(database=get_db_path()) as con:
        # Hapus cara lama, pake cara 'Overwrite' yang lebih aman buat Raw Layer
        con.execute("DROP TABLE IF EXISTS raw_users")
        con.execute("CREATE TABLE raw_users AS SELECT * FROM df_users")
    return df_users

@asset
def raw_products():
    _, df_products, _ = generate_fake_data()
    with duckdb.connect(database=get_db_path()) as con:
        con.execute("DROP TABLE IF EXISTS raw_products")
        con.execute("CREATE TABLE raw_products AS SELECT * FROM df_products")
    return df_products

@asset
def raw_orders():
    _, _, df_orders = generate_fake_data()
    with duckdb.connect(database=get_db_path()) as con:
        con.execute("DROP TABLE IF EXISTS raw_orders")
        con.execute("CREATE TABLE raw_orders AS SELECT * FROM df_orders")
    return df_orders

defs = Definitions(
    assets=[raw_users, raw_products, raw_orders],
    executor=None
)