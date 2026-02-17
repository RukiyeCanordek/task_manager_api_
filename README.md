# Task Manager API (FastAPI)

A simple RESTful Task Manager API built with FastAPI and SQLite 

This project demonstrates backend fundamentals such as:

- REST API design
- CRUD operations
- Request validation with Pydantic
- Modular project structure
- SQLite database integration
- SQLAlchemy ORM usage
- Virtual environment usage
- Git & GitHub workflow

---

## 📌 Features

- Create a new task
- List all tasks
- Filter tasks (done / pending)
- Search tasks by keyword
- Update task
- Delete task
- Swagger documentation support

---

## 🛠 Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- SQLite

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RukiyeCanordek/task_manager_api.git
cd task_manager_api

Create a virtual environment:
python -m venv .venv


Activate the virtual environment (Windows):
.venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the server:
uvicorn app.main:app --reload


📖 API Documentation

After running the server, open:
http://127.0.0.1:8000/docs


👩‍💻 Author
Rukiye Canordek

