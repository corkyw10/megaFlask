from app import app

# Python function decorators.
# in this case they register the function as a callback for a certain event, eg. hitting the URL "/" or "/index"
@app.route('/')
@app.route('/index')
def index():
    return "Hellos World!"

