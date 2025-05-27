#  Flask Habit Tracker

A simple web-based Habit Tracker application built with **Flask**, **PostgreSQL**, and **APScheduler**. Track daily habits, monitor weekly progress, and receive summary emails!

---

##  Features

- User registration and login
- Habit creation and daily check-ins
- Weekly progress summary email via SendGrid
- Responsive frontend using HTML & CSS
- Background scheduler for sending emails
- Data persistence with PostgreSQL

---

##  Tech Stack

- **Backend:** Flask, SQLAlchemy, APScheduler
- **Database:** PostgreSQL
- **Email:** SendGrid API
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Deployment-Ready:** Easily Dockerizable

---

habit-tracker-flask/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── email_utils.py
│   ├── scheduler.py
│   └── templates/
│       └── *.html
│
├── static/
│   └── screenshots/
│       ├── dashboard.png
│       └── email_report.png
│
├── seed_sample_data.py
├── requirements.txt
├── .env
└── README.md


##  Screenshots

| Habit Dashboard | Weekly Email Report |
|------------------|---------------------|
| ![dashboard](static/screenshots/dashboard.png) | ![email](static/screenshots/email_report.png) |

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/habit-tracker-flask.git
cd habit-tracker-flask
