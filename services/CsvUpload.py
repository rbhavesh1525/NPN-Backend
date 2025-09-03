import pandas as pd
from sqlalchemy.orm import Session
from models.db_models import Customer  # Make sure your model is named `Customer`
from models.schemas import CustomerData


def save_customers_from_csv(file, db: Session):
    """
    Reads a CSV file, parses the data, and inserts it into the database.
    """
    # Read CSV into DataFrame
    df = pd.read_csv(file)

    # Ensure all required columns exist
    required_columns = [
        "customer_id", "name", "gender", "age", "phone_number",
        "email", "occupation", "city", "account_type", "balance",
        "has_loan", "has_credit", "has_invest", "last_marketing_ressponse"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    customers = []
    for _, row in df.iterrows():
        customer = Customer(
            customer_id=str(row["customer_id"]),
            name=row["name"],
            gender=row["gender"],
            age=int(row["age"]) if not pd.isna(row["age"]) else None,
            phone_number=str(row["phone_number"]),
            email=row["email"],
            occupation=row["occupation"],
            city=row["city"],
            account_type=row["account_type"],
            balance=float(row["balance"]) if not pd.isna(row["balance"]) else 0.0,
            has_loan=bool(int(row["has_loan"])) if str(row["has_loan"]).isdigit() else str(row["has_loan"]).lower() in ["true", "yes", "1"],
            has_credit=bool(int(row["has_credit"])) if str(row["has_credit"]).isdigit() else str(row["has_credit"]).lower() in ["true", "yes", "1"],
            has_invest=bool(int(row["has_invest"])) if str(row["has_invest"]).isdigit() else str(row["has_invest"]).lower() in ["true", "yes", "1"],
            last_marketing_response=row.get("last_marketing_ressponse", None),
        )
        customers.append(customer)

    # Bulk insert into Supabase PostgreSQL for efficiency
    db.bulk_save_objects(customers)
    db.commit()

    return {"inserted": len(customers)}
