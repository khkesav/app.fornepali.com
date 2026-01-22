# wsgi.py for production deployment
from app import Main

if __name__ == "__main__":
    main = Main()
    main.init()
else:
    # For WSGI servers like Gunicorn
    main = Main()
    app = main._instance
