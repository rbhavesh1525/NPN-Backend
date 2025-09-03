from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base  # we will create this Base in database.py

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String)
    age = Column(Integer)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    occupation = Column(String)
    city = Column(String)
    account_type = Column(String)
    balance = Column(Float, default=0.0)
    has_loan = Column(Boolean, default=False)
    has_credit = Column(Boolean, default=False)
    has_invest = Column(Boolean, default=False)
    last_marketing_response = Column(String)

