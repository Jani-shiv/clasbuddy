from sqlalchemy import Column, Integer, String, DateTime, Text
from db.database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
