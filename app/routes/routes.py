"""
Handles the routing of the application.
"""
from flask import request
from flask import Blueprint

from app.controllers import Controller

routes = Blueprint("routes", __name__)

# Controllers
controller = Controller()

@routes.before_request
def restrict_host():
    allowed_hosts = ["fornepal.com", "app.fornepali.com"]
    host_header = request.headers.get("Host", "")
    # Remove port if present (e.g., app.fornepali.com:8080)
    host = host_header.split(":")[0]
    if host not in allowed_hosts:
        return "Forbidden: Invalid Host", 403

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
