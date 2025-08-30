"""
ClassBuddy API - Ultra Minimal Version for Vercel
Compatible with all FastAPI versions
"""
from fastapi import FastAPI

# Create minimal FastAPI app without middleware
app = FastAPI(
    title="ClassBuddy API",
    version="2.0.0"
)

@app.get("/")
def root():
    return {
        "message": "🎓 ClassBuddy - College Assistant Platform",
        "version": "2.0.0",
        "status": "online",
        "platform": "Vercel",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ClassBuddy API",
        "platform": "Vercel"
    }

@app.get("/api/test")
def test():
    return {
        "message": "API working!",
        "test": True,
        "platform": "Vercel"
    }
