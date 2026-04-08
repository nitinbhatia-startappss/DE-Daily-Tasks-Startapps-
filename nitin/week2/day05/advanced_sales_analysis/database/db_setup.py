from sqlalchemy import create_engine
from database.models import Base

engine = create_engine("sqlite:///sales.db")

Base.metadata.create_all(engine)

print("Database created successfully")