"""
Simple ClassBuddy Local Development Server
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Simple FastAPI app
app = FastAPI(
    title="ClassBuddy: College Assistant",
    description="A comprehensive college assistant platform",
    version="2.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "🎓 Welcome to ClassBuddy - College Assistant Platform",
        "version": "2.0.0",
        "status": "running",
        "features": [
            "Academic Management",
            "Campus Navigation", 
            "Event Management",
            "Community Platform",
            "AI Assistant",
            "Authentication"
        ],
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "api": "/api"
        }
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "ClassBuddy is running successfully!",
        "database": "SQLite (local)",
        "environment": "development"
    }

@app.get("/api/test")
def test_endpoint():
    return {
        "message": "API is working!",
        "test": True,
        "timestamp": "2025-08-30"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print("🚀 Starting ClassBuddy Local Development Server...")
    print(f"📍 Server will be available at: http://localhost:{port}")
    print(f"📚 API Documentation: http://localhost:{port}/docs")
    print(f"🔧 Health Check: http://localhost:{port}/health")
    
    uvicorn.run(
        "simple_main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
