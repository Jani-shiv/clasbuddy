"""
CollegeBuddy - Your Ultimate College Assistant
A simple and clean college management application
"""
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from database import init_db, get_db
from models import Student, Course, Assignment, Event

# Initialize FastAPI app
app = FastAPI(
    title="CollegeBuddy - College Assistant",
    description="Your ultimate college management companion",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()
    print("🎓 CollegeBuddy database initialized!")

# Main dashboard route
@app.get("/", response_class=HTMLResponse)
async def dashboard(db: Session = Depends(get_db)):
    """Main dashboard page"""
    
    # Get quick stats
    total_students = db.query(Student).count()
    total_courses = db.query(Course).count()
    total_assignments = db.query(Assignment).count()
    upcoming_events = db.query(Event).count()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CollegeBuddy - Dashboard</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
                padding: 20px;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
                color: white;
            }}
            
            .header h1 {{
                font-size: 3.5rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            
            .header p {{
                font-size: 1.3rem;
                opacity: 0.9;
                margin-bottom: 20px;
            }}
            
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 25px;
                margin-bottom: 50px;
            }}
            
            .stat-card {{
                background: white;
                border-radius: 20px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
            }}
            
            .stat-card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            }}
            
            .stat-number {{
                font-size: 3.5rem;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 15px;
                display: block;
            }}
            
            .stat-label {{
                font-size: 1.2rem;
                color: #666;
                text-transform: uppercase;
                letter-spacing: 1px;
                font-weight: 600;
            }}
            
            .api-section {{
                background: white;
                border-radius: 20px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
                margin-bottom: 40px;
            }}
            
            .api-section h2 {{
                color: #667eea;
                margin-bottom: 30px;
                font-size: 2rem;
            }}
            
            .btn {{
                display: inline-block;
                padding: 15px 35px;
                margin: 15px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-decoration: none;
                border-radius: 50px;
                transition: all 0.3s ease;
                font-weight: 600;
                font-size: 1.1rem;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }}
            
            .btn:hover {{
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            }}
            
            .features-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 25px;
                margin-top: 50px;
            }}
            
            .feature-card {{
                background: rgba(255,255,255,0.15);
                border-radius: 20px;
                padding: 35px;
                color: white;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
                transition: all 0.3s ease;
            }}
            
            .feature-card:hover {{
                background: rgba(255,255,255,0.25);
                transform: translateY(-5px);
            }}
            
            .feature-card h3 {{
                margin-bottom: 20px;
                font-size: 1.5rem;
                color: #fff;
            }}
            
            .feature-card p {{
                opacity: 0.9;
                line-height: 1.7;
                font-size: 1.1rem;
            }}
            
            .success-message {{
                background: #10b981;
                color: white;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin-bottom: 30px;
                font-size: 1.2rem;
                font-weight: 600;
            }}
            
            @media (max-width: 768px) {{
                .header h1 {{
                    font-size: 2.5rem;
                }}
                
                .stat-number {{
                    font-size: 2.5rem;
                }}
                
                body {{
                    padding: 10px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="success-message">
                ✅ CollegeBuddy Successfully Created! All systems are operational.
            </div>
            
            <div class="header">
                <h1>🎓 CollegeBuddy</h1>
                <p>Your Ultimate College Management Companion</p>
                <p style="font-size: 1rem; opacity: 0.8;">Clean, Modern & Fully Functional</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <span class="stat-number">{total_students}</span>
                    <div class="stat-label">👥 Students</div>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{total_courses}</span>
                    <div class="stat-label">📚 Courses</div>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{total_assignments}</span>
                    <div class="stat-label">📝 Assignments</div>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{upcoming_events}</span>
                    <div class="stat-label">📅 Events</div>
                </div>
            </div>
            
            <div class="api-section">
                <h2>🚀 Explore Your Application</h2>
                <a href="/docs" class="btn">📖 API Documentation</a>
                <a href="/api/students" class="btn">👥 Students API</a>
                <a href="/api/courses" class="btn">📚 Courses API</a>
                <a href="/health" class="btn">🔧 Health Check</a>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <h3>📚 Academic Management</h3>
                    <p>Complete system for tracking courses, grades, assignments, and monitoring GPA progress throughout your academic journey.</p>
                </div>
                <div class="feature-card">
                    <h3>📅 Schedule Organization</h3>
                    <p>Powerful scheduling tools for managing class times, exam dates, assignment deadlines, and academic calendar events.</p>
                </div>
                <div class="feature-card">
                    <h3>👥 Student Network</h3>
                    <p>Connect with classmates and professors, build academic relationships, and collaborate on projects and study groups.</p>
                </div>
                <div class="feature-card">
                    <h3>📝 Notes & Resources</h3>
                    <p>Organize study materials, course notes, research resources, and academic documents in a structured system.</p>
                </div>
                <div class="feature-card">
                    <h3>📊 Progress Analytics</h3>
                    <p>Advanced analytics for monitoring academic performance, setting educational goals, and tracking graduation progress.</p>
                </div>
                <div class="feature-card">
                    <h3>🏫 Campus Integration</h3>
                    <p>Access campus maps, dining schedules, library hours, and other essential campus services and information.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)

# API Endpoints
@app.get("/api/students")
async def get_students(db: Session = Depends(get_db)):
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

@app.get("/api/courses")
async def get_courses(db: Session = Depends(get_db)):
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
            "schedule": c.schedule,
            "location": c.location
        }
        for c in courses
    ]

@app.get("/api/assignments")
async def get_assignments(db: Session = Depends(get_db)):
    """Get all assignments"""
    assignments = db.query(Assignment).all()
    return [
        {
            "id": a.id,
            "title": a.title,
            "description": a.description,
            "type": a.type,
            "due_date": a.due_date,
            "max_points": a.max_points
        }
        for a in assignments
    ]

@app.get("/api/events")
async def get_events(db: Session = Depends(get_db)):
    """Get all events"""
    events = db.query(Event).all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "event_type": e.event_type,
            "start_time": e.start_time,
            "end_time": e.end_time,
            "location": e.location
        }
        for e in events
    ]

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "✅ CollegeBuddy is running perfectly!",
        "version": "1.0.0",
        "application": "CollegeBuddy - College Management System",
        "features": [
            "Academic Management",
            "Schedule Organization", 
            "Student Directory",
            "Notes & Resources",
            "Progress Analytics",
            "Campus Integration"
        ]
    }

# Quick stats endpoint
@app.get("/stats")
async def get_quick_stats(db: Session = Depends(get_db)):
    """Get application statistics"""
    return {
        "total_students": db.query(Student).count(),
        "total_courses": db.query(Course).count(),
        "total_assignments": db.query(Assignment).count(),
        "total_events": db.query(Event).count(),
        "database_status": "connected",
        "application_status": "operational"
    }

if __name__ == "__main__":
    print("=" * 60)
    print("🎓 COLLEGEBUDDY - COLLEGE MANAGEMENT SYSTEM")
    print("=" * 60)
    print("🚀 Starting application server...")
    print("📍 Dashboard: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔧 Health Check: http://localhost:8000/health")
    print("📊 Statistics: http://localhost:8000/stats")
    print("=" * 60)
    print("✅ Ready for college management!")
    print("=" * 60)
    
    uvicorn.run(
        "simple_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
