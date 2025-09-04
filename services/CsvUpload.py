import pandas as pd
from sqlalchemy.orm import Session
from models.db_models import Customer  # Your SQLAlchemy model


def save_customers_from_csv(file, db: Session):
    """
    Reads a CSV file, parses the data, and inserts it into the database.
    """
    # Read CSV into DataFrame
    df = pd.read_csv(file)

    # Ensure all required columns exist
    required_columns = [
        "customer_id", "name", "gender", "age", "income", "occupation",
        "city", "account_type", "account_tenure", "balance",
        "has_loan", "has_credit_card", "has_investment", "last_marketing_response"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    customers = []
    for _, row in df.iterrows():
        customer = Customer(
            customer_id=str(row["customer_id"]),
            name=row["name"],
            gender=row.get("gender"),
            age=int(row["age"]) if not pd.isna(row["age"]) else None,
            income=int(row["income"]) if not pd.isna(row["income"]) else None,
            occupation=row.get("occupation"),
            city=row.get("city"),
            account_type=row.get("account_type"),
            account_tenure=int(row["account_tenure"]) if not pd.isna(row["account_tenure"]) else None,
            balance=float(row["balance"]) if not pd.isna(row["balance"]) else 0.0,
            has_loan=_parse_bool(row["has_loan"]),
            has_credit_card=_parse_bool(row["has_credit_card"]),
            has_investment=_parse_bool(row["has_investment"]),
            last_marketing_response=row.get("last_marketing_response"),
        )
        customers.append(customer)

    # Bulk insert into Supabase PostgreSQL for efficiency
    db.bulk_save_objects(customers)
    db.commit()

    return {"inserted": len(customers)}


def _parse_bool(value) -> bool:
    """Helper to convert CSV values into bools."""
    if pd.isna(value):
        return False
    val = str(value).strip().lower()
    if val in ["true", "yes", "1"]:
        return True
    if val in ["false", "no", "0"]:
        return False
    try:
        return bool(int(val))
    except ValueError:
        return False
