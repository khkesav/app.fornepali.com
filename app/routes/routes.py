"""
Handles the routing of the application.
"""
from flask import request
from flask import Blueprint

from app.controllers import Controller
from app.controllers.date_controller import DateController

routes = Blueprint("routes", __name__)

# Controllers
controller = Controller()
date_controller = DateController()

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

@routes.route("/api/calendar", methods=["GET"])
def get_calendar():
    """
    Retrieves the list of supported calendar systems.

    This function handles GET requests to fetch the available calendar systems.
    It calls the `get_calendar` method of the Controller.

    Returns:
        Response: JSON
    """
    return controller.get_calendar()

@routes.route("/api/convert-date", methods=["POST"])
def convert_date():
    """
    Converts a date from one calendar system to another.

    This function handles POST requests to convert dates. It extracts the date and
    target calendar system from the request JSON payload and calls the `convert_date`
    method of the DateController.

    Returns:
        Response: JSON
    """
    data = request.get_json(silent=True)
    if data:
        year = data.get("year")
        month = data.get("month")
        day = data.get("day")
        date = f"{year}-{month}-{day}"
        target = data.get("from")
    else:
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        date = f"{year}-{month}-{day}"
        target = request.form.get("from")
    return date_controller.convert_date(date, target)

@routes.route("/health")
def health_check():
    """
    Health check endpoint to verify that the application is running.

    This function returns a simple JSON response indicating the health status of the application.

    Returns:
        Response: JSON
    """
    return {"status": "healthy"}, 200
