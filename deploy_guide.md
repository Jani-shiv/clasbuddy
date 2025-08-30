# 🚀 ClassBuddy Render Deployment Guide

## Quick Deploy Links
- **🔗 Deploy Now:** https://render.com/deploy?repo=https://github.com/Jani-shiv/clasbuddy
- **📝 Repository:** https://github.com/Jani-shiv/clasbuddy

## Environment Variables for Render

Copy and paste these into Render's environment variables section:

```
SECRET_KEY=lAHyy8wVWCFYCbkRdk_39PLMBm14p2n6X-rut7CsMzw
DOCS_ENABLED=true
ENVIRONMENT=production
LOG_LEVEL=INFO
```

## Step-by-Step Deployment

### 1. Click Deploy Button
Go to: https://render.com/deploy?repo=https://github.com/Jani-shiv/clasbuddy

### 2. Connect GitHub Account
- Sign in to Render
- Authorize GitHub access

### 3. Configure Service
- **Service Name:** clasbuddy-app
- **Environment:** Python 3
- **Build Command:** pip install -r requirements.txt
- **Start Command:** python main.py

### 4. Add Database
- Click "Add Database"
- Choose PostgreSQL (Free tier)
- Database will auto-populate DATABASE_URL

### 5. Set Environment Variables
Paste the variables above in the Environment section

### 6. Deploy
Click "Create Web Service" - deployment takes ~3-5 minutes

## Your Live URLs (after deployment)
- **App:** https://clasbuddy-app.onrender.com
- **API Docs:** https://clasbuddy-app.onrender.com/docs
- **Health:** https://clasbuddy-app.onrender.com/health

## Expected Features Live
✅ FastAPI backend with all endpoints
✅ Interactive API documentation
✅ Database with all tables
✅ Authentication system
✅ All academic, events, community features
✅ AI assistant (when API keys added)
✅ Campus map functionality

## Optional: Add AI Features Later
Add these environment variables for AI features:
```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

## Troubleshooting
- Build fails? Check logs in Render dashboard
- 500 errors? Verify environment variables
- Database issues? Ensure PostgreSQL is connected

Your ClassBuddy platform will be production-ready! 🎓
