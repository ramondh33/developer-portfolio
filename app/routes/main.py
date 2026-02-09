# Import necessary modules and classes from Flask and other parts of the application.
import logging
from flask import Blueprint, render_template, flash, redirect, url_for
from ..extensions import db
from ..models import Project, ContactMessage
from ..forms import ContactForm

# Define a Blueprint for the main routes of the application.
main_bp = Blueprint('main', __name__)

# Define the home route that handles both GET and POST requests.
@main_bp.get('/')
@main_bp.post('/')
def home():
    # Create an instance of the contact form and retrieve all projects from the database.
    form = ContactForm()
    projects = Project.query.order_by(Project.id.desc()).all()

    # Handle form submission.
    if form.validate_on_submit():

        # Create a new contact message instance with form data.
        contact_message = ContactMessage(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )
        db.session.add(contact_message)
        db.session.commit()

        # Provide user feedback and redirect to the home page.
        logging.getLogger(__name__).info("New contact message from %s", contact_message.email)
        flash("Thank you for your message! I'll get back to you soon.", 'success')
        return redirect(url_for('main.home'))

    return render_template('home.html', form=form, projects=projects)

# Define a route for the about page.
@main_bp.get('/about')
def about():
    return render_template('about.html')

# Define a route for the projects page.
@main_bp.get('/projects')
def projects():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('projects.html', projects=projects)

