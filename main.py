from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text 

from sqlalchemy.orm import Session
from database import get_db


# Import all routers
from routers import csv_route

# Create FastAPI app
app = FastAPI(title="Marketing Automation API", version="1.0.0")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers (modular)
app.include_router(csv_route.router, prefix="/api/csv", tags=["CSV"])
#app.include_router(customer_router.router, prefix="/api/customers", tags=["Customers"])
#app.include_router(campaign_router.router, prefix="/api/campaigns", tags=["Campaigns"])
#app.include_router(history_router.router, prefix="/api/history", tags=["History"])

@app.on_event("startup")
def startup_db_check():
    try:
        db: Session = next(get_db())
        db.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print("❌ Database connection failed:", e)

# Root health-check
@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Welcome to the Marketing Automation API! Visit /docs for API documentation."}

