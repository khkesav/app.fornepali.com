"""
Handles the routing of the application.
"""
from flask import request
from flask import Blueprint

from app.controllers import Controller

routes = Blueprint("routes", __name__)

# Controllers
controller = Controller()

@routes.route("/")
def index():
    """
    Renders the dashboard page of application.

    This function is responsible for rendering the main index page of the application.
    It calls the `index` method of the IndexController.

    Returns:
        Response: String
    """
    return "Application is running."
