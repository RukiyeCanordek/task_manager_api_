Task Manager API (FastAPI)

A simple RESTful Task Manager API built with FastAPI for internship portfolio purposes.
This project demonstrates backend fundamentals such as:
REST API design
CRUD operations
Request validation with Pydantic
Modular project structure
SQLite database integration
SQLAlchemy ORM usage
Virtual environment usage
Git & GitHub workflow


🚀 Features
Create a new task
List all tasks
Filter tasks (done / pending)
Search tasks by keyword
Update task
Delete task
Swagger documentation support


🛠 Tech Stack
Python 3
FastAPI
Uvicorn
Pydantic
SQLAlchemy
SQLite


⚙️ Installation
Clone the repository:
git clone https://github.com/YOUR_USERNAME/task_manager_api.git
cd task_manager_api

Create virtual environment:
python -m venv .venv

Activate virtual environment (Windows):
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn app.main:app --reload


📖 API Documentation

After running the server, open:
http://127.0.0.1:8000/docs
Swagger UI will be available for testing all endpoints.


📂 Project Structure
task_manager_api/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── orm_models.py
│   ├── routers/
│   │   └── tasks.py
│
├── data/
├── requirements.txt
├── README.md


🎯 Purpose
This project was built as part of my backend learning journey and internship portfolio preparation.
It demonstrates clean API structure, database integration, and professional Git workflow.

.

👩‍💻 Author
Rukiye Canordek
