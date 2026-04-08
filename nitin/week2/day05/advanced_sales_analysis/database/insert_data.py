import json
from sqlalchemy.orm import sessionmaker
from db_setup import engine
from database.models import Customer, Order, OrderItem

Session = sessionmaker(bind=engine)
session = Session()

with open("data/raw_data.json") as f:
    data = json.load(f)

for order in data:

    customer = Customer(
        id=order["userId"],
        name=f"Customer {order['userId']}"
    )
    session.merge(customer)

    new_order = Order(
        id=order["id"],
        customer_id=order["userId"],
        order_date=order["date"]
    )
    session.merge(new_order)

    for item in order["products"]:
        order_item = OrderItem(
            order_id=order["id"],
            product=str(item["productId"]),
            quantity=item["quantity"],
            price=item["price"]  
        )
        session.add(order_item)

session.commit()

print("Data inserted successfully")