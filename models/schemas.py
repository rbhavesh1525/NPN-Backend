from pydantic import BaseModel, Field
from typing import Optional

class CustomerData(BaseModel):
    customer_id: str
    name: str
    gender: Optional[str]
    age: Optional[int]
    phone_number: Optional[str]
    email: Optional[str]
    occupation: Optional[str]
    city: Optional[str]
    account_type: Optional[str]
    balance: Optional[float] = 0.0
    has_loan: Optional[bool] = False
    has_credit: Optional[bool] = False
    has_invest: Optional[bool] = False
    last_marketing_response: Optional[str] = Field(alias="last_marketing_ressponse")

    class Config:
        orm_mode = True   # allows SQLAlchemy -> Pydantic conversion
        allow_population_by_field_name = True  # support aliases
