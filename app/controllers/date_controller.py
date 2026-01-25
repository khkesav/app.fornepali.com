from flask import jsonify
from nepali_date_utils import converter;

class DateController:

    def convert_date(self, date, target):
        """
            Converts a date from one calendar system to another.

            This method takes a date string and the target calendar system as input,
            performs the conversion, and returns the converted date.

            Args:
                date (str): The date string to be converted.
                target (str): The target calendar system (e.g., 'en-np', 'np-en').
        """
        if target == "en-np":
            converted_date = converter.ad_to_bs(date)
            return jsonify({
                "original_date": date,
                "converted_date": converted_date,
                "target": target
            })
        elif target == "np-en":
            converted_date = converter.bs_to_ad(date)
            return jsonify({
                "original_date": date,
                "converted_date": converted_date,
                "target": target
            })
        else:
            raise ValueError("Unsupported target calendar system.")