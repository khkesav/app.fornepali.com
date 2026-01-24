"""
This module contains the base controller class for the application.
It provides common functionality to be used by other controllers.
"""

from flask import render_template, redirect, url_for

class Controller:
    """
    Base controller class to be extended by other controllers.
    Provides common functionality for all controllers.
    """

    def __init__(self):
        pass

    def index(self):
        """
        Renders the index page template.
        Returns:
            Response: The rendered 'index.html' template.
        """

        return self.render_template("index.html")

    def render_template(self, template_name, **context):
        """
        Render a template with the given context.

        Args:
            template_name (str): The name of the template to render.
            context (dict): The context to pass to the template.

        Returns:
            Response: The rendered template.
        """
        return render_template(template_name, **context)

    def redirect(self, location):
        """
        Redirect to a different location.

        Args:
            location (str): The location to redirect to.

        Returns:
            Response: The redirect response.
        """
        return redirect(location)

    def url_for(self, endpoint, **values):
        """
        Generate a URL for the given endpoint.

        Args:
            endpoint (str): The endpoint to generate the URL for.
            values (dict): The values to pass to the URL.

        Returns:
            str: The generated URL.
        """
        return url_for(endpoint, **values)
