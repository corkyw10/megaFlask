from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Create an instance of Flask
# __name__ is a predefined Python variable that refers to the name of the module in which it is used
# Flask uses the name of the module as the starting point to load any associated resources
app = Flask(__name__)
app.config.from_object(Config)
# most flask extensions are initialised as so:
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# model module defines the structure of the database
from app import routes, models

