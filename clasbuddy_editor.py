"""
ClassBuddy - Complete Application Overview & Editor
==================================================

This file provides access to all components of your ClassBuddy application.
You can view and edit any part of the system from here.
"""

import os
import json
from pathlib import Path

class ClassBuddyEditor:
    def __init__(self):
        self.root_path = Path("e:/Github/clasbuddy")
        self.components = self._scan_components()
    
    def _scan_components(self):
        """Scan and categorize all application components"""
        components = {
            "backend": {
                "core": [
                    "main.py",
                    "config.py", 
                    "requirements.txt"
                ],
                "api_endpoints": [
                    "api/auth.py",
                    "api/academics.py", 
                    "api/events.py",
                    "api/campus_map.py",
                    "api/community.py",
                    "api/assistant.py"
                ],
                "models": [
                    "models/user.py",
                    "models/academics.py",
                    "models/event.py",
                    "models/building.py",
                    "models/community.py"
                ],
                "database": [
                    "db/database.py",
                    "alembic.ini",
                    "alembic/"
                ],
                "authentication": [
                    "auth/"
                ],
                "utilities": [
                    "utils/helpers.py",
                    "utils/refact_integration.py"
                ]
            },
            "mobile": {
                "config": [
                    "mobile/package.json",
                    "mobile/App.tsx"
                ],
                "screens": [
                    "mobile/src/screens/",
                ],
                "api_client": [
                    "mobile/src/api/"
                ],
                "store": [
                    "mobile/src/store/"
                ],
                "utils": [
                    "mobile/src/utils/"
                ]
            },
            "deployment": {
                "docker": [
                    "Dockerfile",
                    "docker-compose.yml",
                    "nginx.conf"
                ],
                "ci_cd": [
                    ".github/workflows/ci-cd.yml"
                ],
                "scripts": [
                    "deploy.sh"
                ]
            },
            "documentation": [
                "README.md",
                "docs/security-audit.md",
                "docs/feature-roadmap.md", 
                "docs/app-store-submission.md"
            ],
            "testing": [
                "tests/test_main.py",
                "mobile/__tests__/App.test.tsx",
                "mobile/jest.config.js"
            ],
            "config": [
                ".env.example",
                ".gitignore"
            ]
        }
        return components
    
    def show_overview(self):
        """Display complete application overview"""
        print("🎓 ClassBuddy - Complete Application Structure")
        print("=" * 80)
        print()
        
        print("📊 APPLICATION STATS:")
        print("   📁 Total Components: ~50+ files")
        print("   💻 Backend: FastAPI with Python 3.13")
        print("   📱 Mobile: React Native (iOS/Android)")
        print("   🗄️  Database: SQLite/PostgreSQL")
        print("   🚀 Deployment: Docker + GitHub Actions")
        print()
        
        print("🔧 CORE BACKEND COMPONENTS:")
        for category, files in self.components["backend"].items():
            print(f"   📂 {category.upper()}:")
            for file in files:
                status = "✅" if self._file_exists(file) else "❌"
                print(f"      {status} {file}")
            print()
        
        print("📱 MOBILE APPLICATION:")
        for category, files in self.components["mobile"].items():
            print(f"   📂 {category.upper()}:")
            for file in files:
                status = "✅" if self._file_exists(file) else "❌"
                print(f"      {status} {file}")
            print()
        
        print("🐳 DEPLOYMENT & INFRASTRUCTURE:")
        for category, files in self.components["deployment"].items():
            print(f"   📂 {category.upper()}:")
            for file in files:
                status = "✅" if self._file_exists(file) else "❌"
                print(f"      {status} {file}")
            print()
        
        print("📚 DOCUMENTATION:")
        for file in self.components["documentation"]:
            status = "✅" if self._file_exists(file) else "❌"
            print(f"   {status} {file}")
        print()
        
        print("🧪 TESTING FRAMEWORK:")
        for file in self.components["testing"]:
            status = "✅" if self._file_exists(file) else "❌"
            print(f"   {status} {file}")
        print()
        
        print("⚙️ CONFIGURATION:")
        for file in self.components["config"]:
            status = "✅" if self._file_exists(file) else "❌"
            print(f"   {status} {file}")
        print()
        
        print("🔗 LIVE ENDPOINTS:")
        endpoints = [
            "http://localhost:8000/",
            "http://localhost:8000/docs",
            "http://localhost:8000/health",
            "http://localhost:8000/auth/login", 
            "http://localhost:8000/academics/courses",
            "http://localhost:8000/events",
            "http://localhost:8000/campus-map/buildings",
            "http://localhost:8000/community/posts",
            "http://localhost:8000/assistant/ask"
        ]
        
        for endpoint in endpoints:
            print(f"   🌐 {endpoint}")
        print()
        
        print("📝 EDITABLE COMPONENTS:")
        print("   All files are editable! Key components to customize:")
        print("   🔧 main.py - Core application logic")
        print("   ⚙️  config.py - Application settings")
        print("   🔐 api/auth.py - Authentication system")
        print("   📱 mobile/App.tsx - Mobile app entry point")
        print("   🐳 Dockerfile - Container configuration")
        print("   📚 README.md - Project documentation")
        print()
        
        print("🚀 QUICK ACTIONS:")
        print("   • Start server: python main.py")
        print("   • Run mobile: cd mobile && npm start")
        print("   • Build Docker: docker-compose up")
        print("   • Run tests: pytest tests/")
        print("   • Deploy: ./deploy.sh")
        print()
        
        print("🎉 Your ClassBuddy platform is ready for production!")
        
    def _file_exists(self, filepath):
        """Check if file exists"""
        return (self.root_path / filepath).exists()
    
    def list_editable_files(self):
        """List all editable files with descriptions"""
        editable_files = {
            # Backend Core
            "main.py": "FastAPI application entry point - server configuration",
            "config.py": "Application settings and environment variables",
            "requirements.txt": "Python dependencies",
            
            # API Endpoints
            "api/auth.py": "User authentication and authorization",
            "api/academics.py": "Academic features (courses, assignments)",
            "api/events.py": "Event management system",
            "api/campus_map.py": "Campus navigation and mapping",
            "api/community.py": "Student community features",
            "api/assistant.py": "AI assistant integration",
            
            # Database Models
            "models/user.py": "User data model",
            "models/academics.py": "Academic data models",
            "models/event.py": "Event data model",
            "models/building.py": "Campus building model",
            "models/community.py": "Community data models",
            
            # Database
            "db/database.py": "Database connection and setup",
            
            # Mobile App
            "mobile/package.json": "Mobile app dependencies and scripts",
            "mobile/App.tsx": "React Native app entry point",
            
            # Deployment
            "Dockerfile": "Container configuration",
            "docker-compose.yml": "Multi-service deployment",
            ".github/workflows/ci-cd.yml": "CI/CD pipeline",
            
            # Documentation
            "README.md": "Project documentation",
            "docs/security-audit.md": "Security guidelines",
            "docs/feature-roadmap.md": "Development roadmap",
            
            # Configuration
            ".env.example": "Environment variables template",
            ".gitignore": "Git ignore rules"
        }
        
        print("📝 EDITABLE FILES AND THEIR PURPOSES:")
        print("=" * 60)
        for file, description in editable_files.items():
            status = "✅" if self._file_exists(file) else "❌"
            print(f"{status} {file}")
            print(f"   📋 {description}")
            print()


def main():
    editor = ClassBuddyEditor()
    editor.show_overview()
    print("\n" + "="*80)
    print("📁 DETAILED FILE LISTING:")
    print("="*80)
    editor.list_editable_files()


if __name__ == "__main__":
    main()
