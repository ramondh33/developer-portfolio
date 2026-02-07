# Import flask and render_template from the flask module to create a web application and render HTML templates.
from flask import Flask, render_template

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

# Define a route for the root URL ("/") and associate it with the home function. When a user visits the root URL, the home function will be called, which will render and return the 'home.html' template to the user's browser.
@app.route('/')
def home():
    # Render the 'home.html' template and return it as the response to the user's request.
    return render_template('home.html', projects=projects)

# Make sure the app runs only when we execute app.py directly.
if __name__ == '__main__':

    # Run the Flask application in debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
    app.run(debug=True)