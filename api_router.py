
"""
API Endpoints for CollegeBuddy Application
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from models import Student, Course, Assignment, Grade, Note, Event, Enrollment
from datetime import datetime

router = APIRouter(prefix="/api", tags=["API"])

# Student endpoints
@router.get("/students", response_model=List[dict])
def get_students(db: Session = Depends(get_db)):
    """Get all students"""
    students = db.query(Student).all()
    return [
        {
            "id": s.id,
            "student_id": s.student_id,
            "name": s.name,
            "email": s.email,
            "major": s.major,
            "year": s.year,
            "gpa": s.gpa
        }
        for s in students
    ]

@router.get("/students/{student_id}")
def get_student(student_id: str, db: Session = Depends(get_db)):
    """Get student by ID"""
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {
        "id": student.id,
        "student_id": student.student_id,
        "name": student.name,
        "email": student.email,
        "major": student.major,
        "year": student.year,
        "gpa": student.gpa,
        "created_at": student.created_at
    }

# Course endpoints
@router.get("/courses", response_model=List[dict])
def get_courses(db: Session = Depends(get_db)):
    """Get all courses"""
    courses = db.query(Course).all()
    return [
        {
            "id": c.id,
            "course_code": c.course_code,
            "name": c.name,
            "description": c.description,
            "credits": c.credits,
            "professor": c.professor,
            "semester": c.semester,
            "year": c.year,
            "schedule": c.schedule,
            "location": c.location
        }
        for c in courses
    ]

@router.get("/courses/{course_code}")
def get_course(course_code: str, db: Session = Depends(get_db)):
    """Get course by code"""
    course = db.query(Course).filter(Course.course_code == course_code).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return {
        "id": course.id,
        "course_code": course.course_code,
        "name": course.name,
        "description": course.description,
        "credits": course.credits,
        "professor": course.professor,
        "semester": course.semester,
        "year": course.year,
        "schedule": course.schedule,
        "location": course.location
    }

@router.post("/courses")
def create_course(course_data: dict, db: Session = Depends(get_db)):
    """Create a new course"""
    course = Course(**course_data)
    db.add(course)
    db.commit()
    db.refresh(course)
    return {"message": "Course created successfully", "course_id": course.id}

# Assignment endpoints
@router.get("/assignments")
def get_assignments(course_code: Optional[str] = None, db: Session = Depends(get_db)):
    """Get assignments, optionally filtered by course"""
    query = db.query(Assignment).join(Course)
    
    if course_code:
        query = query.filter(Course.course_code == course_code)
    
    assignments = query.all()
    return [
        {
            "id": a.id,
            "title": a.title,
            "description": a.description,
            "type": a.type,
            "due_date": a.due_date,
            "max_points": a.max_points,
            "course_code": a.course.course_code,
            "course_name": a.course.name
        }
        for a in assignments
    ]

# Grade endpoints
@router.get("/grades/{student_id}")
def get_student_grades(student_id: str, db: Session = Depends(get_db)):
    """Get grades for a specific student"""
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    grades = db.query(Grade).filter(Grade.student_id == student.id).all()
    return [
        {
            "id": g.id,
            "assignment_title": g.assignment.title,
            "course_code": g.assignment.course.course_code,
            "points_earned": g.points_earned,
            "points_possible": g.points_possible,
            "percentage": g.percentage,
            "letter_grade": g.letter_grade,
            "graded_at": g.graded_at
        }
        for g in grades
    ]

# Schedule endpoints
@router.get("/schedule/{student_id}")
def get_student_schedule(student_id: str, db: Session = Depends(get_db)):
    """Get class schedule for a student"""
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    enrollments = db.query(Enrollment).filter(
        Enrollment.student_id == student.id,
        Enrollment.status == "Active"
    ).all()
    
    schedule = []
    for enrollment in enrollments:
        course = enrollment.course
        schedule.append({
            "course_code": course.course_code,
            "course_name": course.name,
            "professor": course.professor,
            "schedule": course.schedule,
            "location": course.location,
            "credits": course.credits
        })
    
    return schedule

# Events endpoints
@router.get("/events")
def get_events(
    student_id: Optional[str] = None,
    event_type: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get events, optionally filtered"""
    query = db.query(Event)
    
    if event_type:
        query = query.filter(Event.event_type == event_type)
    
    events = query.order_by(Event.start_time).all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "event_type": e.event_type,
            "start_time": e.start_time,
            "end_time": e.end_time,
            "location": e.location,
            "course_code": e.course_code
        }
        for e in events
    ]

# Notes endpoints
@router.get("/notes/{student_id}")
def get_student_notes(student_id: str, db: Session = Depends(get_db)):
    """Get notes for a student"""
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    notes = db.query(Note).filter(Note.student_id == student.id).all()
    return [
        {
            "id": n.id,
            "title": n.title,
            "content": n.content,
            "course_code": n.course_code,
            "tags": n.tags.split(",") if n.tags else [],
            "created_at": n.created_at,
            "updated_at": n.updated_at
        }
        for n in notes
    ]

@router.post("/notes")
def create_note(note_data: dict, db: Session = Depends(get_db)):
    """Create a new note"""
    note = Note(**note_data)
    db.add(note)
    db.commit()
    db.refresh(note)
    return {"message": "Note created successfully", "note_id": note.id}

# Statistics endpoints
@router.get("/stats/{student_id}")
def get_student_stats(student_id: str, db: Session = Depends(get_db)):
    """Get academic statistics for a student"""
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Get enrolled courses count
    enrolled_courses = db.query(Enrollment).filter(
        Enrollment.student_id == student.id,
        Enrollment.status == "Active"
    ).count()
    
    # Get upcoming assignments
    upcoming_assignments = db.query(Assignment).join(Course).join(Enrollment).filter(
        Enrollment.student_id == student.id,
        Assignment.due_date > datetime.now()
    ).count()
    
    # Get total notes
    total_notes = db.query(Note).filter(Note.student_id == student.id).count()
    
    return {
        "student_name": student.name,
        "gpa": student.gpa,
        "enrolled_courses": enrolled_courses,
        "upcoming_assignments": upcoming_assignments,
        "total_notes": total_notes,
        "academic_year": student.year
    }

# Make router importable for app.py
__all__ = ["router"]
