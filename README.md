# 🚀 Django Assignment

## ✅ Features

- Django REST API with public and protected endpoints
- User authentication using DRF TokenAuth
- Background task execution using Celery + Redis
- Telegram bot integration (`/start` saves username)
- Secure `.env` configuration with `python-decouple`

---

## ⚙️ Setup Instructions

# Command:
git clone https://github.com/OmmprakashMohanty01/Django-project.git

# Command:
cd django_assignment

# Command:
python3 -m venv env

# Command:
source env/bin/activate

# Command:
pip install -r requirements.txt

# Command:
cp .env.example .env

# Command:
python manage.py migrate

# Command:
python manage.py runserver

---

## 🕹️ Run Background Worker (Celery)

# Command:
celery -A backend worker --loglevel=info

---

## 🤖 Run Telegram Bot

# Command:
python telegram_bot.py

---

## 🗂️ Environment Variables (`.env.example`)

# .env content:
SECRET_KEY=your_django_secret_key_here  
DEBUG=True  
BOT_TOKEN=your_telegram_bot_token_here  

---

## 💬 API Endpoints

# Public Endpoint (no auth):
GET /api/public/

# Protected Endpoint (token required):
GET /api/protected/

# Login to get token:
POST /api/login/

# Trigger Celery task:
GET /api/run-task/

---

## 🙌 Author

Ommprakash Mohanty — [Telegram Bot](https://t.me/Ommprakash001_bot)
