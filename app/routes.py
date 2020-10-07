from app import app

# Python function decorators.
# in this case they register the function as a callback for a certain event, eg. hitting the URL "/" or "/index"
@app.route('/')
@app.route('/index')
def index():
    user = {"name": "Coco"}
    return '''
    <html>
        <head>
            <title>Homepage - Mega Flask</title>
        </head>
        <body>
            <h1>Hello there ''' + user["name"] + '''! </h1>
        </body>
    </html>
    '''

