from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Club(Base):
    __tablename__ = "clubs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    message = Column(Text)
    timestamp = Column(String)
