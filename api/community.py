from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.community import Club, ChatMessage
from typing import List
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/clubs", response_model=List[dict])
def list_clubs(db: Session = Depends(get_db)):
    return db.query(Club).all()

@router.get("/chat", response_model=List[dict])
def get_chat(db: Session = Depends(get_db)):
    return db.query(ChatMessage).all()

@router.post("/chat", response_model=dict)
def post_chat(message: dict, db: Session = Depends(get_db)):
    msg = ChatMessage(**message)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg.__dict__
