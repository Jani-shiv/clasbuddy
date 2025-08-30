# ClassBuddy 2.0 - Production Mobile Launch

## 🚀 Project Overview

ClassBuddy 2.0 is a comprehensive college assistant platform featuring:
- Modern FastAPI backend with PostgreSQL/MySQL support
- React Native mobile app for iOS and Android
- AI-powered features with OpenAI and Anthropic integration
- Secure authentication and user management
- Real-time features and offline support
- Comprehensive observability and monitoring

## 📋 Architecture Overview

### Backend Architecture
```
FastAPI (Python 3.11+)
├── Authentication (JWT + OAuth2)
├── Database (PostgreSQL/MySQL + SQLAlchemy)
├── AI Services (OpenAI, Anthropic, Refact.ai)
├── Caching (Redis)
├── Monitoring (Prometheus, Sentry)
└── API Documentation (OpenAPI/Swagger)
```

### Mobile Architecture
```
React Native 0.72+
├── State Management (Redux Toolkit)
├── Navigation (React Navigation v6)
├── UI Components (React Native Paper)
├── Authentication (Keychain/Keystore)
├── Offline Support (SQLite + Redux Persist)
├── Push Notifications (Firebase)
└── Analytics (Firebase Analytics)
```

## 🛠 Setup Instructions

### Backend Setup

1. **Clone and Setup Environment**
   ```bash
   git clone https://github.com/jani-shiv/clasbuddy.git
   cd clasbuddy
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Database Setup**
   ```bash
   # For PostgreSQL
   createdb classbuddy
   
   # Run migrations
   alembic upgrade head
   
   # Or create tables directly
   python -c "from db.database import create_tables; create_tables()"
   ```

4. **Run Development Server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Mobile Setup

1. **Prerequisites**
   - Node.js 18+
   - React Native CLI
   - Android Studio (for Android)
   - Xcode (for iOS, macOS only)

2. **Install Dependencies**
   ```bash
   cd mobile
   npm install
   ```

3. **iOS Setup (macOS only)**
   ```bash
   cd ios
   pod install
   cd ..
   npx react-native run-ios
   ```

4. **Android Setup**
   ```bash
   npx react-native run-android
   ```

### Docker Setup

1. **Development with Docker Compose**
   ```bash
   docker-compose up -d
   ```

2. **Production Docker Build**
   ```bash
   docker build -t classbuddy:latest .
   docker run -p 8000:8000 classbuddy:latest
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DATABASE_URL` | Database connection string | Yes | `sqlite:///./classbuddy.db` |
| `SECRET_KEY` | JWT secret key | Yes | - |
| `OPENAI_API_KEY` | OpenAI API key | No | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | No | - |
| `REDIS_URL` | Redis connection string | No | `redis://localhost:6379/0` |
| `SENTRY_DSN` | Sentry DSN for error tracking | No | - |

## 🔒 Security Features

### Authentication & Authorization
- JWT-based authentication
- Secure password hashing (bcrypt)
- Role-based access control
- Session management
- Token refresh mechanism

### API Security
- CORS configuration
- Rate limiting
- Input validation
- SQL injection protection
- XSS protection headers

### Mobile Security
- Secure token storage (Keychain/Keystore)
- Biometric authentication support
- Certificate pinning
- API request signing

## 📊 Monitoring & Observability

### Metrics & Monitoring
- Prometheus metrics collection
- Custom business metrics
- Performance monitoring
- Resource usage tracking

### Logging
- Structured logging (JSON format)
- Log levels configuration
- Request/response logging
- Error tracking with context

### Error Tracking
- Sentry integration
- Automatic error capture
- Performance monitoring
- Release tracking

## 🚀 Deployment

### Cloud Deployment Options

#### AWS Deployment
1. **ECS with Fargate**
   ```bash
   # Build and push to ECR
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
   docker build -t classbuddy .
   docker tag classbuddy:latest YOUR_ECR_URI/classbuddy:latest
   docker push YOUR_ECR_URI/classbuddy:latest
   ```

#### Google Cloud Deployment
1. **Cloud Run**
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/classbuddy
   gcloud run deploy --image gcr.io/PROJECT_ID/classbuddy --platform managed
   ```

#### Azure Deployment
1. **Container Instances**
   ```bash
   az acr build --registry YOUR_REGISTRY --image classbuddy .
   az container create --resource-group YOUR_RG --name classbuddy --image YOUR_REGISTRY.azurecr.io/classbuddy
   ```

## 📱 Mobile App Store Submission

### Android (Google Play Store)
1. **Prepare Release Build**
   ```bash
   cd mobile/android
   ./gradlew assembleRelease
   ```

2. **Generate Signed APK**
   - Create keystore file
   - Configure signing in `android/app/build.gradle`
   - Build signed APK

3. **Play Store Submission**
   - Create Play Console account
   - Upload APK/AAB
   - Complete store listing
   - Submit for review

### iOS (App Store)
1. **Prepare Release Build**
   ```bash
   cd mobile
   npx react-native run-ios --configuration Release
   ```

2. **Archive and Upload**
   - Use Xcode to archive
   - Upload to App Store Connect
   - Complete app metadata

## � Development Tools

### Code Quality
- **Black**: Python code formatting
- **isort**: Import sorting
- **ESLint**: JavaScript/TypeScript linting
- **Prettier**: Code formatting
- **Pre-commit hooks**: Automated quality checks

### Testing
- **Backend**: pytest, pytest-asyncio
- **Frontend**: Jest, React Native Testing Library
- **Integration**: API testing with httpx
- **E2E**: Detox (planned)

## 📈 Performance Optimization

### Backend Performance
- Database query optimization
- Connection pooling
- Response caching
- Async request handling
- Background task processing

### Mobile Performance
- Image optimization
- Code splitting
- Lazy loading
- Offline data sync
- Memory management

## � Support & Maintenance

### Post-Launch Monitoring
- Monitor application metrics
- Track user feedback
- Analyze crash reports
- Monitor API performance
- Review security logs

### Update Strategy
- Regular dependency updates
- Security patch deployment
- Feature releases (monthly)
- Emergency hotfixes
- Database migrations

---

**Built with ❤️ by the ClassBuddy Team**
