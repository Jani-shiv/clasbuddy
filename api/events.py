from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.event import Event
from typing import List
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[dict])
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.post("/", response_model=dict)
def create_event(event: dict, db: Session = Depends(get_db)):
    db_event = Event(**event)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event.__dict__

@router.get("/{event_id}", response_model=dict)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event.__dict__

@router.put("/{event_id}", response_model=dict)
def update_event(event_id: int, event: dict, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event.__dict__

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return {"ok": True}
