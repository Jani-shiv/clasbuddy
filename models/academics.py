from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from db.database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    instructor = Column(String)
    assignments = relationship("Assignment", back_populates="course")
    attendances = relationship("Attendance", back_populates="course")

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    due_date = Column(Date)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="assignments")

class Attendance(Base):
    __tablename__ = "attendances"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    present = Column(Boolean, default=False)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="attendances")
