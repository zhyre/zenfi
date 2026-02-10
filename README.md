## About

Zenfi is a **personal productivity tracking system** designed to help individuals **focus better, track tasks, and log work sessions**. It provides insights into your energy, focus, and productivity trends, helping users **work smarter and stay balanced**.

## Goal

The goal of Zenfi is to **empower users to manage their time and productivity more effectively** by:

* Logging work sessions and tasks easily
* Tracking productivity patterns over time
* Providing visual insights for better decision-making
* Laying the foundation for future **data-driven recommendations**

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** React.js
* **Database:** PostgreSQL (Railway)
* **Libraries / Tools:** Axios, React Router, Chart.js, Django CORS Headers

## Project Structure

```
zenfi/
├── backend/             # Django backend
│   ├── manage.py
│   ├── ZenfiCore/       # Django project settings
│   └── apps/            # Apps: users, tasks, work_sessions, feedback
├── frontend/            # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/  # Buttons, charts, navbar
│   │   ├── pages/       # Login, Dashboard, SessionForm
│   │   └── services/    # API calls
│   └── package.json
├── docs/                # Documentation & diagrams
├── notebooks/           # Jupyter notebooks for data science
└── README.md
```
