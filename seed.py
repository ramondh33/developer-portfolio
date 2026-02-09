from app import create_app
from app.extensions import db
from app.models import Project

# This script seeds the database with initial project data if no projects exist.
app = create_app()

# Run the seeding process within the application context
with app.app_context():
    # Check if there are any projects in the database
    if Project.query.count() == 0:
        db.session.add_all([
            Project(title="AI Dashboard", description="A dashboard to monitor AI performance and metrics."),
            Project(title="Portfolio Website", description="A personal portfolio website showcasing projects and skills."),
            Project(title="Weather App", description="An app to display current weather conditions and forecasts."),
        ])
        db.session.commit()
        print("Seeded projects.")
    else:
        print("Projects already exist. No seeding needed.")