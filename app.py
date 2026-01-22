"""
This module initializes and runs a Flask web application.
Classes:
    Main: Main application class that handles application flow and initialization.
Functions:
    Ensures a single instance of the Main class (Singleton pattern).
    Main.init(self): Initializes the application, sets up the database, and runs the Flask app.
Usage:
    Run this module directly to start the Flask web application.
"""

from flask import Flask
from app.routes import routes

class Main:
    """
    Main application class.
    Handles application flow, user authentication, and database initialization.
    """

    _instance = None  # Class-level variable to store the single instance

    def __new__(cls, *args, **kwargs):
        """
        Create and return a singleton instance of the class.
        This method overrides the default behavior of the `__new__` method to
        ensure that only one instance of the class is created. If an instance
        already exists, it returns the existing instance; otherwise, it creates
        a new one.
        Args:
            *args: Variable length argument list passed to the class constructor.
            **kwargs: Arbitrary keyword arguments passed to the class constructor.
        Returns:
            Main: The singleton instance of the class.
        """
        if not cls._instance:
            cls._instance = super(Main, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def init(self):
        """
        Main execution method to
        initialize the application.
        """

        import os
        app = Flask(__name__)
        # The secret key is used by Flask to encrypt session cookies and other security-related tasks.
        app.secret_key = '4589CC-2KJDHSALNLDAS-398567-2KJDSALDAS'
        app.register_blueprint(routes)

        # Use PORT env variable if set (for Railway), else default to 5000
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=False, host='0.0.0.0', port=port)

if __name__ == "__main__":

    # Entry point of the application
    main = Main()  # Instantiate Main class
    main.init()  # Run the application
