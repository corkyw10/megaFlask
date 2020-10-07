from flask import render_template
from app import app

# Python function decorators.
# in this case they register the function as a callback for a certain event, eg. hitting the URL "/" or "/index"
@app.route('/')
@app.route('/index')
def index():
    user = {"name": "Coco"}
    return render_template('index.html', user=user)

