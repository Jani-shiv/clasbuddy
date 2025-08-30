pip install -r requirements.txt

# ClassBuddy: All-in-One College Assistant

ClassBuddy is a modular, extensible college assistant platform built with FastAPI, SQLAlchemy, and SQLite. It provides a suite of tools for students to manage events, academics, campus navigation, community engagement, and AI-powered Q&A, all in one place.

---

## 🚀 Features

- **Events**: Full CRUD for campus events (create, view, update, delete)
- **Campus Maps**: Search for buildings by name or code
- **Academics**: Track courses, assignments, and attendance
- **Community**: Discover clubs and simulate chat
- **AI Assistant**: Rule-based/NLP Q&A (with Refact.ai integration ready for advanced features)

---

## 🗂️ Project Structure

```
classbuddy/
│   main.py                # FastAPI entry point
│   requirements.txt       # Python dependencies
│   README.md              # Project documentation
│
├── api/                   # API routers for each feature
├── db/                    # Database setup
├── models/                # SQLAlchemy models
├── services/              # (Expandable) Business logic
├── utils/                 # Helpers (NLP, Refact.ai, etc.)
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jani-shiv/ClassBuddy.git
   cd ClassBuddy/classbuddy
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python -c "from db.database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

5. **Run the development server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Open your browser**
   - API root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧩 API Overview

### Events
- `GET /events/` — List all events
- `POST /events/` — Create a new event
- `GET /events/{event_id}` — Get event details
- `PUT /events/{event_id}` — Update event
- `DELETE /events/{event_id}` — Delete event

### Campus Map
- `GET /campus-map/search?q=...` — Search buildings by name or code

### Academics
- `GET /academics/courses` — List courses
- `GET /academics/assignments` — List assignments
- `GET /academics/attendance` — List attendance records

### Community
- `GET /community/clubs` — List clubs
- `GET /community/chat` — Get chat messages
- `POST /community/chat` — Post a chat message

### AI Assistant
- `POST /assistant/ask` — Ask a question (rule-based/NLP, ready for Refact.ai)

---

## 🤖 Refact.ai Integration

ClassBuddy is ready for advanced AI features using [Refact.ai](https://refact.ai/). See `utils/refact_integration.py` for a starting point. You can expand the AI assistant to use Refact.ai for more powerful Q&A, summarization, or other LLM-powered features.

---

## 🛠️ Contributing

1. Fork the repo and create your feature branch (`git checkout -b feature/YourFeature`)
2. Commit your changes (`git commit -am 'Add new feature'`)
3. Push to the branch (`git push origin feature/YourFeature`)
4. Open a Pull Request

---

## 👤 Author

- GitHub: [jani_shiv](https://github.com/jani-shiv)
- Project maintained by jani_shiv

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
