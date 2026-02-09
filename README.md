# Developer Portfolio

This is my personal developer portfolio built with Flask. I originally started it as a simple project to practice web development, and then I refactored it into a more production-style application to learn better backend structure and testing.

The goal of this project was to move beyond "just making it work" and start thinking more like a real software engineer.

## What This Project Does

This is a portfolio website that includes:

- Home page with featured projects.
- About page.
- Projects page (data from database).
- Contact form (validated + stored in database).
- Basic error handling (404/500 pages).
- Automated tests.
- CI with GitHub Actions.

## Tech Stack

- Python
- Flask (App Factory pattern)
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF (form validation + CSRF)
- Gunicorn (for production server)
- Pytest (testing)
- SQLite (local database)

## Project Structure

```csharp
developer-portfolio/
│
├── app/
│   ├── __init__.py        # App factory
│   ├── models.py          # Database models
│   ├── forms.py           # Flask-WTF forms
│   ├── extensions.py      # DB, Migrate, CSRF
│   ├── routes/            # Blueprints
│   ├── templates/         # Jinja templates
│   └── static/            # CSS + images
│
├── tests/                 # Pytest tests
├── config.py              # Config classes
├── wsgi.py                # Gunicorn entrypoint
└── requirements.txt
```

## How To Run Locally

1. Clone the repository

```bash
git clone https://github.com/yourusername/developer-portfolio.git
cd developer-portfolio
```

2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt

```

4. Set environment variables

```bash
export FLASK_APP=wsgi:app
export SECRET_KEY=dev-secret
```

(Windows users can use SET insteas of EXPORT)

5. Initialize the database

```bash
flask db upgrade
```

6. Run the app

```bash
flask run
```

Open:

```cpp
http://127.0.0.1:5000
```

## Running Tests

To run the test suite:

```bash
pytest -q
```

Tests include:

- Route status checks
- Contact form validation
- Basic database interaction

## Running with Gunicorn (Production Style)

To simulate production:

```bash
gunicorn wsgi:app
```

Then open:

```cpp
http://127.0.0.1:8000
```

## What I Learned From This Project

- How to structure a Flask app using the app factory pattern
- How to use Blueprints
- How to handle forms securely with Flask-WTF
- How to use SQLAlchemy models instead of hardcoded data.
- How to set up GitHub Actions for CI
- How to write basic tests with pytest
- Why environment variables are important

This project helped me understand the difference between a tutorial project and something closer to production-ready.

## Future Improvements

Some things I would like to add in the future:

- Admin dashboard for managing projects
- Authentication
- Better UI improvements
- Deploy to a cloud provider
- More test coverage
- Update/Upgrade front/back-end tech stack (add some javascript or switch to django)

## About Me

I am currently focused on improving my backend development skills and working toward becoming a remote developer. This project is part of that journey.