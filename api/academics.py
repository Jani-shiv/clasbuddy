from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.academics import Course, Assignment, Attendance
from typing import List
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Courses
@router.get("/courses", response_model=List[dict])
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# Assignments
@router.get("/assignments", response_model=List[dict])
def list_assignments(db: Session = Depends(get_db)):
    return db.query(Assignment).all()

# Attendance
@router.get("/attendance", response_model=List[dict])
def list_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()
