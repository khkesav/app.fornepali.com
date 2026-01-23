from flask import Flask
from app.routes import routes

app = Flask(__name__)
app.secret_key = '4589CC-2KJDHSALNLDAS-398567-2KJDSALDAS'
app.register_blueprint(routes)
