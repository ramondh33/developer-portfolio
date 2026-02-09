import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import create_app
from app.extensions import db
from app.models import Project


# This file contains fixtures for testing the Flask application. It sets up a test database and provides a test client for making requests to the application during tests.
@pytest.fixture()
# The app fixture creates a Flask application instance configured for testing, initializes the database, and adds a sample project to the database. After the tests are done, it drops the database tables to clean up.
def app():
    app = create_app("config.TestConfig")
    # Set up the database and add a sample project
    with app.app_context():
        db.create_all()
        db.session.add(Project(title="Test", description="Desc", tech="Flask"))
        db.session.commit()
    # Yield the app instance to be used in tests, and ensure that the database is cleaned up after tests are completed.
    yield app
    with app.app_context():
        db.drop_all()

# The client fixture provides a test client for the Flask application, allowing tests to make HTTP requests to the application without running a live server.
@pytest.fixture()
def client(app):
    return app.test_client()
