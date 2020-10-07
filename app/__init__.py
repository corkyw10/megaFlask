from flask import Flask

# Create an instance of Flask
# __name__ is a predefined Python variable that refers to the name of the module in which it is used
# Flask uses the name of the module as the starting point to load any associated resources
app = Flask(__name__)

from app import routes

