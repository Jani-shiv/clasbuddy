"""
CollegeBuddy - Your Ultimate College Assistant
A comprehensive college management application built with FastAPI
"""
import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import init_db, get_db
from api_router import router as api_router
from models import Student, Course, Assignment, Event
import os

# Initialize FastAPI app
app = FastAPI(
    title="CollegeBuddy - College Assistant",
    description="Your ultimate college management companion",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include API router
app.include_router(api_router)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()
    print("🎓 CollegeBuddy database initialized!")

# Main dashboard route
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    """Main dashboard page"""
    
    # Get quick stats
    total_students = db.query(Student).count()
    total_courses = db.query(Course).count()
    total_assignments = db.query(Assignment).count()
    upcoming_events = db.query(Event).count()
    
    # Recent students
    recent_students = db.query(Student).limit(5).all()
    
    # Recent courses
    recent_courses = db.query(Course).limit(5).all()
    
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
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
                color: white;
            }}
            
            .header h1 {{
                font-size: 3rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            
            .header p {{
                font-size: 1.2rem;
                opacity: 0.9;
            }}
            
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 40px;
            }}
            
            .stat-card {{
                background: white;
                border-radius: 15px;
                padding: 30px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                transition: transform 0.3s ease;
            }}
            
            .stat-card:hover {{
                transform: translateY(-5px);
            }}
            
            .stat-number {{
                font-size: 3rem;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 10px;
            }}
            
            .stat-label {{
                font-size: 1.1rem;
                color: #666;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            .content-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-bottom: 40px;
            }}
            
            .content-card {{
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }}
            
            .content-card h3 {{
                color: #667eea;
                margin-bottom: 20px;
                font-size: 1.5rem;
                border-bottom: 2px solid #f0f0f0;
                padding-bottom: 10px;
            }}
            
            .list-item {{
                padding: 15px;
                margin-bottom: 10px;
                background: #f8f9fa;
                border-radius: 8px;
                border-left: 4px solid #667eea;
            }}
            
            .list-item h4 {{
                color: #333;
                margin-bottom: 5px;
            }}
            
            .list-item p {{
                color: #666;
                font-size: 0.9rem;
            }}
            
            .api-links {{
                background: white;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
            }}
            
            .api-links h3 {{
                color: #667eea;
                margin-bottom: 20px;
            }}
            
            .btn {{
                display: inline-block;
                padding: 12px 25px;
                margin: 10px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 25px;
                transition: all 0.3s ease;
                font-weight: 500;
            }}
            
            .btn:hover {{
                background: #764ba2;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }}
            
            .feature-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-top: 40px;
            }}
            
            .feature-card {{
                background: rgba(255,255,255,0.1);
                border-radius: 15px;
                padding: 25px;
                color: white;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255,255,255,0.2);
            }}
            
            .feature-card h4 {{
                margin-bottom: 15px;
                font-size: 1.3rem;
            }}
            
            .feature-card p {{
                opacity: 0.9;
                line-height: 1.6;
            }}
            
            @media (max-width: 768px) {{
                .content-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .header h1 {{
                    font-size: 2rem;
                }}
                
                .container {{
                    padding: 10px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎓 CollegeBuddy</h1>
                <p>Your Ultimate College Management Companion</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">{total_students}</div>
                    <div class="stat-label">Students</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{total_courses}</div>
                    <div class="stat-label">Courses</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{total_assignments}</div>
                    <div class="stat-label">Assignments</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{upcoming_events}</div>
                    <div class="stat-label">Events</div>
                </div>
            </div>
            
            <div class="content-grid">
                <div class="content-card">
                    <h3>📚 Recent Students</h3>
                    {"".join([f'''
                    <div class="list-item">
                        <h4>{student.name}</h4>
                        <p>{student.major} • {student.year} • GPA: {student.gpa}</p>
                    </div>
                    ''' for student in recent_students])}
                </div>
                
                <div class="content-card">
                    <h3>📖 Recent Courses</h3>
                    {"".join([f'''
                    <div class="list-item">
                        <h4>{course.course_code} - {course.name}</h4>
                        <p>{course.professor} • {course.credits} credits</p>
                    </div>
                    ''' for course in recent_courses])}
                </div>
            </div>
            
            <div class="api-links">
                <h3>🚀 Explore CollegeBuddy Features</h3>
                <a href="/docs" class="btn">📚 API Documentation</a>
                <a href="/api/students" class="btn">👥 View Students</a>
                <a href="/api/courses" class="btn">📖 View Courses</a>
                <a href="/api/events" class="btn">📅 View Events</a>
            </div>
            
            <div class="feature-grid">
                <div class="feature-card">
                    <h4>📚 Academic Management</h4>
                    <p>Track courses, grades, assignments, and monitor your GPA progress throughout your academic journey.</p>
                </div>
                <div class="feature-card">
                    <h4>📅 Schedule Management</h4>
                    <p>Organize class schedules, exam dates, and important deadlines in one convenient location.</p>
                </div>
                <div class="feature-card">
                    <h4>👥 Student Directory</h4>
                    <p>Connect with classmates and professors, build your academic network and collaborate effectively.</p>
                </div>
                <div class="feature-card">
                    <h4>📝 Notes & Resources</h4>
                    <p>Organize study materials, course notes, and academic resources for easy access and review.</p>
                </div>
                <div class="feature-card">
                    <h4>📊 Progress Tracking</h4>
                    <p>Monitor academic performance, set goals, and track your progress toward graduation.</p>
                </div>
                <div class="feature-card">
                    <h4>🏫 Campus Information</h4>
                    <p>Access campus maps, dining hall hours, library schedules, and other essential campus resources.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "CollegeBuddy is running successfully!",
        "version": "1.0.0",
        "features": [
            "Academic Management",
            "Schedule Management", 
            "Student Directory",
            "Notes & Resources",
            "Progress Tracking",
            "Campus Information"
        ]
    }

# Quick stats endpoint
@app.get("/stats")
async def get_quick_stats(db: Session = Depends(get_db)):
    """Get quick statistics"""
    return {
        "total_students": db.query(Student).count(),
        "total_courses": db.query(Course).count(),
        "total_assignments": db.query(Assignment).count(),
        "total_events": db.query(Event).count()
    }

if __name__ == "__main__":
    print("🎓 Starting CollegeBuddy Application...")
    print("📍 Dashboard: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🔧 Health Check: http://localhost:8000/health")
    print("=" * 50)
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
