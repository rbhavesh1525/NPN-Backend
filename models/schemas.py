from pydantic import BaseModel, Field
from typing import Optional

class CustomerData(BaseModel):
    customer_id: str
    name: str
    gender: Optional[str] = None
    age: Optional[int] = None
    income: Optional[int] = None
    occupation: Optional[str] = None
    city: Optional[str] = None
    account_type: Optional[str] = None
    account_tenure: Optional[int] = None
    balance: Optional[float] = 0.0
    has_loan: Optional[bool] = False
    has_credit_card: Optional[bool] = False
    has_investment: Optional[bool] = False
    last_marketing_response: Optional[str] = None

    class Config:
        orm_mode = True  # allows SQLAlchemy -> Pydantic conversion
