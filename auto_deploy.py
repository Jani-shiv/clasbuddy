#!/usr/bin/env python3
"""
Automated Render Deployment Script for ClassBuddy
This script helps automate the deployment process
"""

import webbrowser
import time


def open_deployment_links():
    """Open all necessary deployment links"""
    links = [
        "https://render.com/deploy?repo="
        "https://github.com/Jani-shiv/clasbuddy",
        "https://github.com/Jani-shiv/clasbuddy"
    ]
    
    print("🚀 Opening ClassBuddy Deployment Links...")
    print("=" * 50)
    
    for i, link in enumerate(links, 1):
        print(f"🔗 Opening Link {i}: {link}")
        webbrowser.open(link)
        time.sleep(2)  # Small delay between opens


def show_deployment_config():
    """Display deployment configuration"""
    config = {
        "service_name": "clasbuddy-app",
        "runtime": "python",
        "build_command": "pip install -r requirements.txt", 
        "start_command": "python main.py",
        "environment_variables": {
            "SECRET_KEY": "lAHyy8wVWCFYCbkRdk_39PLMBm14p2n6X-rut7CsMzw",
            "DOCS_ENABLED": "true",
            "ENVIRONMENT": "production",
            "LOG_LEVEL": "INFO"
        },
        "expected_urls": {
            "app": "https://clasbuddy-app.onrender.com",
            "docs": "https://clasbuddy-app.onrender.com/docs", 
            "health": "https://clasbuddy-app.onrender.com/health"
        }
    }
    
    print("\n📋 DEPLOYMENT CONFIGURATION")
    print("=" * 50)
    print(f"Service Name: {config['service_name']}")
    print(f"Runtime: {config['runtime']}")
    print(f"Build Command: {config['build_command']}")
    print(f"Start Command: {config['start_command']}")
    
    print("\n🔧 ENVIRONMENT VARIABLES TO SET:")
    for key, value in config['environment_variables'].items():
        print(f"{key}={value}")
    
    print("\n🌐 YOUR LIVE URLS (after deployment):")
    for name, url in config['expected_urls'].items():
        print(f"{name.title()}: {url}")
    
    return config

def show_deployment_steps():
    """Show step-by-step deployment instructions"""
    steps = [
        "1. 🔗 Click the deployment link (opened in browser)",
        "2. 🔐 Sign in to Render / Connect GitHub",
        "3. 📝 Set Service Name: clasbuddy-app",
        "4. 🗄️  Add PostgreSQL Database (Free tier)",
        "5. ⚙️  Copy environment variables from above",
        "6. 🚀 Click 'Create Web Service'",
        "7. ⏱️  Wait 3-5 minutes for deployment",
        "8. ✅ Test your live app!"
    ]
    
    print("\n📋 DEPLOYMENT STEPS")
    print("=" * 50)
    for step in steps:
        print(step)

def main():
    print("🎓 ClassBuddy - Automated Render Deployment")
    print("=" * 60)
    
    # Show configuration
    config = show_deployment_config()
    
    # Show steps
    show_deployment_steps()
    
    print("\n" + "=" * 60)
    print("🚀 STARTING DEPLOYMENT PROCESS...")
    print("=" * 60)
    
    # Open deployment links
    open_deployment_links()
    
    print("\n✅ Deployment links opened!")
    print("📋 Follow the steps above to complete deployment")
    print("🎉 Your ClassBuddy app will be live in ~5 minutes!")

if __name__ == "__main__":
    main()
