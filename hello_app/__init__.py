from flask import Flask  # Import the Flask class
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
