"""
Database Models for CollegeBuddy Application
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    major = Column(String)
    year = Column(String)  # Freshman, Sophomore, Junior, Senior
    gpa = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    enrollments = relationship("Enrollment", back_populates="student")
    grades = relationship("Grade", back_populates="student")


class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    credits = Column(Integer)
    professor = Column(String)
    semester = Column(String)
    year = Column(Integer)
    schedule = Column(String)  # e.g., "MWF 10:00-11:00"
    location = Column(String)
    
    # Relationships
    enrollments = relationship("Enrollment", back_populates="course")
    assignments = relationship("Assignment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrolled_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Active")  # Active, Dropped, Completed
    
    # Relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Assignment(Base):
    __tablename__ = "assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String, index=True)
    description = Column(Text)
    type = Column(String)  # Homework, Quiz, Exam, Project
    due_date = Column(DateTime)
    max_points = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    course = relationship("Course", back_populates="assignments")
    grades = relationship("Grade", back_populates="assignment")


class Grade(Base):
    __tablename__ = "grades"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    points_earned = Column(Float)
    points_possible = Column(Float)
    percentage = Column(Float)
    letter_grade = Column(String)
    submitted_at = Column(DateTime)
    graded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    student = relationship("Student", back_populates="grades")
    assignment = relationship("Assignment", back_populates="grades")


class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    title = Column(String, index=True)
    content = Column(Text)
    course_code = Column(String)
    tags = Column(String)  # Comma-separated tags
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    event_type = Column(String)  # Class, Exam, Assignment, Social, Other
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    location = Column(String)
    course_code = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
