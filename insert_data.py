from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product

engine = create_engine("sqlite:///database.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

product1 = Product(title="Product A", price=40, count=25, description="Description for Product A")
product2 = Product(title="Product B", price=45, count=30, description="Description for Product B")

db.add(product1)
db.add(product2)
db.commit()

print("Added two records to the products table:")
print(f"1. {product1.title}, price: {product1.price}, count: {product1.count}")
print(f"2. {product2.title}, price: {product2.price}, count: {product2.count}")

db.close()