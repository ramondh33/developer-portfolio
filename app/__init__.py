import logging
from flask import Flask, render_template
from .extensions import db, migrate, csrf
from .routes import main_bp

# Application Factory. Creates and configures the Flask application.
def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)

    # Configure basic logging
    logging.basicConfig(level=logging.INFO)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500

    return app