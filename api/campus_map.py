from fastapi import APIRouter, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.building import Building
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search", response_model=List[dict])
def search_buildings(q: str = Query(..., description="Building name or code"), db: Session = Depends(get_db)):
    results = db.query(Building).filter(
        (Building.name.ilike(f"%{q}%")) | (Building.code.ilike(f"%{q}%"))
    ).all()
    if not results:
        raise HTTPException(status_code=404, detail="No buildings found")
    return [b.__dict__ for b in results]
