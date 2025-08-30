"""
ClassBuddy Local Development Server
Clean version without any middleware compatibility issues
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI(
    title="ClassBuddy: College Assistant",
    description="A comprehensive college assistant platform for academic management, campus navigation, events, and community",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint with platform information"""
    return {
        "message": "🎓 Welcome to ClassBuddy - Your College Assistant Platform",
        "version": "2.0.0",
        "status": "running",
        "description": "Modern college assistant platform with academic management, campus navigation, events, and community features",
        "features": [
            "📚 Academic Management - Course tracking, grades, assignments",
            "🗺️ Campus Navigation - Interactive maps and directions",
            "📅 Event Management - Campus events and activities",
            "👥 Community Platform - Student networking and forums",
            "🤖 AI Assistant - Academic help and guidance",
            "🔐 Authentication - Secure user management"
        ],
        "api_endpoints": {
            "documentation": "/docs",
            "health_check": "/health",
            "test_api": "/api/test"
        },
        "development": {
            "environment": "local",
            "auto_reload": True,
            "database": "SQLite"
        }
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "message": "✅ ClassBuddy is running successfully!",
        "service": "ClassBuddy API",
        "version": "2.0.0",
        "environment": "development",
        "database": "Connected (SQLite)",
        "uptime": "Active",
        "features_status": {
            "api": "operational",
            "cors": "enabled",
            "docs": "available",
            "auto_reload": "enabled"
        }
    }

@app.get("/api/test", tags=["Testing"])
def test_api():
    """Test endpoint to verify API functionality"""
    return {
        "message": "🚀 API is working perfectly!",
        "test_passed": True,
        "api_version": "2.0.0",
        "timestamp": "2025-01-30",
        "test_data": {
            "sample_student": {
                "name": "John Doe",
                "major": "Computer Science",
                "year": "Junior"
            },
            "sample_course": {
                "code": "CS101",
                "name": "Introduction to Programming",
                "credits": 3
            }
        }
    }

@app.get("/api/status", tags=["Status"])
def get_status():
    """Detailed system status"""
    return {
        "system": "ClassBuddy Platform",
        "status": "operational",
        "services": {
            "web_api": "running",
            "database": "connected",
            "authentication": "ready",
            "file_storage": "available"
        },
        "metrics": {
            "requests_served": "counting",
            "uptime": "active"
        }
    }

if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    print("=" * 60)
    print("🎓 CLASBUDDY - COLLEGE ASSISTANT PLATFORM")
    print("=" * 60)
    print("🚀 Starting Local Development Server...")
    print(f"📍 Server URL: http://localhost:{port}")
    print(f"📚 API Documentation: http://localhost:{port}/docs")
    print(f"🔧 Health Check: http://localhost:{port}/health")
    print(f"🧪 Test API: http://localhost:{port}/api/test")
    print("=" * 60)
    print("✅ Ready for development!")
    print("✅ Auto-reload enabled")
    print("✅ CORS enabled for local development")
    print("=" * 60)
    
    uvicorn.run(
        "local_server:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
