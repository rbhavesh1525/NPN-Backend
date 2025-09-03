# routers/csv_route.py
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import CsvUpload  # Make sure CsvUpload has a method to save CSV

router = APIRouter()

@router.post("/upload-csv")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Use the method from CsvUpload to save CSV data
    result = CsvUpload.save_customers_from_csv(file.file, db)
    return {"status": "success", "result": result}
