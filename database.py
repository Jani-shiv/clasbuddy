"""
Database Configuration for CollegeBuddy Application
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# SQLite database configuration
DATABASE_URL = "sqlite:///./collegebuddy.db"

# Create database engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
def create_tables():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)

# Database dependency
def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize database
def init_db():
    """Initialize database with sample data"""
    create_tables()
    
    db = SessionLocal()
    try:
        # Check if data already exists
        from models import Student, Course
        if db.query(Student).first() is None:
            # Add sample data
            add_sample_data(db)
    finally:
        db.close()

def add_sample_data(db):
    """Add sample data to the database"""
    from models import Student, Course, Assignment, Event
    from datetime import datetime, timedelta
    
    # Sample students
    students = [
        Student(
            student_id="STU001",
            name="Alice Johnson",
            email="alice@college.edu",
            major="Computer Science",
            year="Junior",
            gpa=3.75
        ),
        Student(
            student_id="STU002", 
            name="Bob Smith",
            email="bob@college.edu",
            major="Mathematics",
            year="Senior",
            gpa=3.90
        ),
        Student(
            student_id="STU003",
            name="Carol Davis",
            email="carol@college.edu", 
            major="Physics",
            year="Sophomore",
            gpa=3.60
        )
    ]
    
    # Sample courses
    courses = [
        Course(
            course_code="CS101",
            name="Introduction to Programming",
            description="Learn Python programming fundamentals",
            credits=3,
            professor="Dr. Wilson",
            semester="Fall",
            year=2025,
            schedule="MWF 10:00-11:00",
            location="CS Building Room 101"
        ),
        Course(
            course_code="MATH201",
            name="Calculus II",
            description="Advanced calculus concepts",
            credits=4,
            professor="Prof. Anderson",
            semester="Fall", 
            year=2025,
            schedule="TTh 2:00-3:30",
            location="Math Building Room 205"
        ),
        Course(
            course_code="PHYS101",
            name="General Physics I",
            description="Mechanics and thermodynamics",
            credits=4,
            professor="Dr. Thompson",
            semester="Fall",
            year=2025,
            schedule="MWF 1:00-2:00",
            location="Physics Lab 301"
        )
    ]
    
    # Sample assignments
    assignments = [
        Assignment(
            course_id=1,
            title="Python Basics Quiz",
            description="Quiz on Python syntax and fundamentals",
            type="Quiz",
            due_date=datetime.now() + timedelta(days=3),
            max_points=100
        ),
        Assignment(
            course_id=1,
            title="Programming Project 1",
            description="Build a simple calculator application",
            type="Project",
            due_date=datetime.now() + timedelta(days=14),
            max_points=200
        ),
        Assignment(
            course_id=2,
            title="Integration Problems",
            description="Solve integration practice problems",
            type="Homework",
            due_date=datetime.now() + timedelta(days=7),
            max_points=50
        )
    ]
    
    # Sample events
    events = [
        Event(
            title="CS101 Midterm Exam",
            description="Midterm examination for Introduction to Programming",
            event_type="Exam",
            start_time=datetime.now() + timedelta(days=21),
            end_time=datetime.now() + timedelta(days=21, hours=2),
            location="CS Building Room 101",
            course_code="CS101"
        ),
        Event(
            title="Math Study Group",
            description="Weekly calculus study session",
            event_type="Social",
            start_time=datetime.now() + timedelta(days=2),
            end_time=datetime.now() + timedelta(days=2, hours=2),
            location="Library Study Room 3"
        )
    ]
    
    # Add all sample data
    for student in students:
        db.add(student)
    
    for course in courses:
        db.add(course)
        
    db.commit()  # Commit to get IDs
    
    for assignment in assignments:
        db.add(assignment)
        
    for event in events:
        db.add(event)
    
    db.commit()
    print("✅ Sample data added to database")
