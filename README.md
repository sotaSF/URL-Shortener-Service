# URL Shortener

A simple URL shortening service built with Django.

## Features

- Submit a long URL and get back a short, unique code
- Visiting the short code redirects to the original URL
- Tracks how many times each short link has been accessed
- Uses Django's messages framework (Post/Redirect/Get pattern) to avoid duplicate submissions on page reload

## Tech stack

- Django
- SQLite
- Bootstrap 4 (CDN)

## Setup

1. Clone the repo and move into the project folder:
   ```
   git clone <repo-url>
   cd URL-Shortener-Service
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in `urlShortener/` (next to `manage.py`) based on `.env.example`, and set your own `SECRET_KEY`:
   ```
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the dev server:
   ```
   python manage.py runserver
   ```

The app will be available at `http://127.0.0.1:8000/`.

