from fastapi import APIRouter, Depends
from sqlalchemy import text
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/tables", tags=["Admin"])
async def get_all_tables(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SHOW TABLES;"))  # MySQL query to list tables
        tables = [row[0] for row in result.fetchall()]
        return {"tables": tables}
    except Exception as e:
        return {"error": str(e)}
