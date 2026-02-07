# Import flask and render_template from the flask module to create a web application and render HTML templates.
from flask import Flask, render_template, request

# Create an instance of the Flask class, which will be our WSGI application.
app = Flask(__name__)

# Define a list of projects, where each project is represented as a dictionary containing its title, description, and technologies used. This data can be passed to the HTML template to dynamically display the projects on the webpage.
projects = [
    {
        "title": "AI Dashboard",
        "description": "A data-driven dashboard built with Python and Flask.",
        "tech": "Python, Flask, HTML, CSS"
    },
    {
        "title": "Portfolio Website",
        "description": "My personal portfolio showcasing my projects and skills.",
        "tech": "Flask, Jinja, CSS"
    },
    {
        "title": "API Service",
        "description": "A REST API that serves JSON data to frontend apps.",
        "tech": "Python, Flask, REST"
    }
]

# Home route GET + POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    success_message = None

    # This block runs only when the form is submitted.
    if request.method == 'POST':
        # Get form values by name attributes
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Simple validation 
        if name and email and message:
            # Print to terminal (test for now, later send email or save to database)
            print(f"New contact message: {name}, {email}, {message}")
            success_message = "Thank you for your message! I'll get back to you soon."
        else:
            success_message = "Please fill in all fields before submitting."
    
    # Render page and send data to HTML.
    return render_template('home.html', projects=projects, success_message=success_message)

# Route for the about page.
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the projects page.
@app.route('/projects')
def projects_page():
    return render_template('projects.html')

# Make sure the app runs only when we execute app.py directly.
if __name__ == '__main__':

    # Run the Flask application in debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
    app.run()