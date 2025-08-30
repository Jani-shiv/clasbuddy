from sqlalchemy import Column, Integer, String
from db.database import Base

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    description = Column(String)
    location = Column(String)
