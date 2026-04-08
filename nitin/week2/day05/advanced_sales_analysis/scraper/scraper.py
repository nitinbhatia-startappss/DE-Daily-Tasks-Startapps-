from faker import Faker
import random
import json
import os

fake = Faker()

def fetch_data():
    data = []

    for order_id in range(1, 101):
        user_id = random.randint(1, 20)

        order = {
            "id": order_id,
            "userId": user_id,
            "date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "products": []
        }

        for _ in range(random.randint(1, 3)):
            order["products"].append({
                "productId": random.randint(1, 10),
                "quantity": random.randint(1, 5),
                "price": round(random.uniform(100, 1000), 2)
            })

        data.append(order)

    print("Data generated")
    return data


def save_data(data):
    print("Saving data...")

    os.makedirs("data", exist_ok=True)

    with open("data/raw_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved")


if __name__ == "__main__":
    print("RUNNING SCRAPER")
    data = fetch_data()
    print("SAMPLE:", data[0])
    save_data(data)