<div align="center">
  <h1>🎓 CollegeBuddy</h1>
  <h3>Your Ultimate College Management Assistant</h3>
  <p>
    <img src="https://img.shields.io/badge/FastAPI-0.104.1-green?logo=fastapi" />
    <img src="https://img.shields.io/badge/SQLAlchemy-1.4.53-blue?logo=sqlalchemy" />
    <img src="https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite" />
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  </p>
  <img src="https://user-images.githubusercontent.com/placeholder/collegebuddy-ui.png" alt="CollegeBuddy UI" width="800"/>
  <br/>
  <i>Modern, beautiful, and fully functional college management system built with FastAPI.</i>
</div>

---

## 🚀 Features

- **Academic Management**: Track courses, grades, assignments, and GPA progress.
- **Schedule Management**: Organize class schedules, exam dates, and deadlines.
- **Student Directory**: Connect with classmates and professors.
- **Notes & Resources**: Store and organize study materials and course notes.
- **Progress Tracking**: Monitor academic performance and graduation goals.
- **Campus Information**: Access campus maps, dining, library hours, and more.
- **Modern UI**: Clean, responsive dashboard with quick stats and feature highlights.
- **RESTful API**: Well-documented endpoints for all major resources.

---

## 🖥️ Dashboard Preview

> ![Dashboard Preview](https://user-images.githubusercontent.com/placeholder/collegebuddy-dashboard.png)

---

## 📦 Tech Stack

- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTML5, CSS3 (Jinja2 for templates)
- **Other**: Uvicorn, Python-Multipart, Jinja2

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jani-shiv/clasbuddy.git
   cd clasbuddy
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   # For full UI and API
   python app.py
   # Or for a simple version
   python simple_app.py
   ```
4. **Access the dashboard:**
   - [http://localhost:8000](http://localhost:8000)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health: [http://localhost:8000/health](http://localhost:8000/health)

---

## 🛠️ Project Structure

```
├── app.py            # Main FastAPI app with UI
├── simple_app.py     # Minimal FastAPI app
├── api.py            # API endpoints
├── models.py         # SQLAlchemy models
├── database.py       # DB config & sample data
├── requirements.txt  # Python dependencies
├── collegebuddy.db   # SQLite database
└── README.md         # Project documentation
```

---

## 📚 API Endpoints

- `/api/students` — List all students
- `/api/courses` — List all courses
- `/api/assignments` — List all assignments
- `/api/events` — List all events
- `/health` — Health check
- `/stats` — Quick stats
- `/docs` — Interactive API docs

---

## ✨ Screenshots

> ![Students List](https://user-images.githubusercontent.com/placeholder/collegebuddy-students.png)
> ![Courses List](https://user-images.githubusercontent.com/placeholder/collegebuddy-courses.png)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
  <b>Made with ❤️ for students and educators</b>
</div>
