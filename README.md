# Cars Dealership Full-Stack Capstone

A runnable starter implementation for the IBM Full-stack Development Capstone submission.

## Stack
- Django + Django REST Framework
- SQLite
- React component source
- HTML/CSS frontend
- Simple dealer/review/car-make APIs
- Session-style login/logout endpoints
- Sentiment endpoint

## Run
```bash
cd server
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

API base: `http://127.0.0.1:8000/api/`

Demo user: `root`
Demo password: `rootpass123`

This repository is intentionally structured so the learner can run the application and capture genuine evidence for the graded assignment.
