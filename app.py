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


from app import app

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

if __name__ == "__main__":

    # Entry point of the application
    main = Main()  # Instantiate Main class
    main.init()  # Run the application
