from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base  # declarative_base() from database.py

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    income = Column(Integer, nullable=True)
    occupation = Column(String, nullable=True)
    city = Column(String, nullable=True)
    account_type = Column(String, nullable=True)
    account_tenure = Column(Integer, nullable=True)
    balance = Column(Float, default=0.0)
    has_loan = Column(Boolean, default=False)
    has_credit_card = Column(Boolean, default=False)
    has_investment = Column(Boolean, default=False)
    last_marketing_response = Column(String, nullable=True)
