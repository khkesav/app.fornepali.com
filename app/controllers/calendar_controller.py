"""
Controller for calendar-related operations.
    list: A list of supported calendar systems, e.g., ["gregorian", "nepali"].
"""
from flask import jsonify

class CalendarController:

    def calendar(self):
        """
        Retrieves the list of supported calendar systems.

        This method returns a list of calendar systems that the application supports.

        Returns:
            list: A list of supported calendar systems.
        """
        return ["gregorian", "nepali"]
