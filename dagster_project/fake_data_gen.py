import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

def generate_fake_data():
    # 1. Generate Users
    users = []
    for _ in range(10):
        users.append({
            "user_id": _ + 1,
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "created_at": "2026-02-01"
        })
    
    # 2. Generate Products
    products = [
        {"product_id": 1, "name": "Laptop Asus TUF", "category": "Electronics", "price": 15000000},
        {"product_id": 2, "name": "Samsung Tab S10", "category": "Electronics", "price": 7000000},
        {"product_id": 3, "name": "iPhone 15", "category": "Electronics", "price": 20000000},
    ]

    # 3. Generate Orders
    orders = []
    for i in range(20):
        orders.append({
            "order_id": i + 1,
            "user_id": random.randint(1, 10),
            "product_id": random.randint(1, 3),
            "amount": random.randint(1, 2),
            "order_date": "2026-02-15"
        })

    return pd.DataFrame(users), pd.DataFrame(products), pd.DataFrame(orders)