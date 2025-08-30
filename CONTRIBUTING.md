# Contributing to ClassBuddy

We love your input! We want to make contributing to ClassBuddy as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## 🚀 Development Process

We use GitHub to host code, track issues and feature requests, as well as accept pull requests.

### Pull Requests Process

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

### Branch Naming Convention

- `feature/feature-name` - for new features
- `bugfix/bug-description` - for bug fixes  
- `hotfix/critical-fix` - for critical production fixes
- `docs/documentation-update` - for documentation updates

## 🐛 Bug Reports

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/Jani-shiv/clasbuddy/issues/new?template=bug_report.md).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## 💡 Feature Requests

We use GitHub issues to track feature requests. Submit a feature request by [opening a new issue](https://github.com/Jani-shiv/clasbuddy/issues/new?template=feature_request.md).

**Great Feature Requests** include:

- A clear and concise description of what the problem is
- A clear and concise description of what you want to happen
- Any additional context or screenshots about the feature request

## 🔧 Development Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL (optional, SQLite used by default)

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/Jani-shiv/clasbuddy.git
cd clasbuddy

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run database migrations
alembic upgrade head

# Start development server
python main.py
```

### Mobile Setup

```bash
# Navigate to mobile directory
cd mobile

# Install dependencies
npm install

# For iOS (macOS only)
cd ios && pod install && cd ..

# Start Metro bundler
npm start

# Run on Android
npm run android

# Run on iOS
npm run ios
```

### Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in production mode
docker-compose -f docker-compose.prod.yml up --build
```

## 🧪 Testing

### Backend Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_auth.py
```

### Mobile Tests

```bash
cd mobile

# Run Jest tests
npm test

# Run with coverage
npm test -- --coverage

# Run E2E tests (if available)
npm run test:e2e
```

## 📝 Code Style

### Python

We use:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

```bash
# Format code
black .
isort .

# Lint code
flake8 .
mypy .
```

### TypeScript/JavaScript

We use:

- **Prettier** for code formatting
- **ESLint** for linting

```bash
cd mobile

# Format code
npm run format

# Lint code
npm run lint
```

## 📚 Documentation

- Update README.md if you change functionality
- Add docstrings to new functions and classes
- Update API documentation in `/docs`
- Add inline comments for complex logic

## 🏷️ Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```text
type(scope): description

feat(auth): add OAuth2 Google integration
fix(api): resolve CORS issues in production
docs(readme): update installation instructions
style(mobile): fix linting issues
refactor(db): optimize query performance
test(auth): add integration tests for login
chore(deps): update dependencies
```

## 🔍 Code Review Process

1. All submissions require review before merging
2. We may ask for changes before a PR can be merged
3. We'll assign reviewers based on the area of code
4. Address feedback promptly and professionally

## 📋 Issue Templates

When creating issues, please use our templates:

- **Bug Report**: For reporting bugs
- **Feature Request**: For suggesting enhancements
- **Question**: For asking questions about usage
- **Documentation**: For documentation improvements

## 🚀 Release Process

1. Update version numbers in relevant files
2. Update CHANGELOG.md
3. Create a release branch
4. Tag the release
5. Deploy to staging for testing
6. Deploy to production
7. Create GitHub release with release notes

## 💬 Community

- Join our [Discord server](https://discord.gg/clasbuddy) for discussions
- Follow us on [Twitter](https://twitter.com/clasbuddy) for updates
- Check out our [blog](https://clasbuddy.dev/blog) for development updates

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation
- Annual contributor highlights

## 📞 Contact

- Project Lead: [@Jani-shiv](https://github.com/Jani-shiv)
- Email: [shivjani2005@gmail.com](mailto:shivjani2005@gmail.com)
- Project Issues: [GitHub Issues](https://github.com/Jani-shiv/clasbuddy/issues)

Thank you for contributing to ClassBuddy! 🎓✨
