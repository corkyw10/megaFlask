from flask import render_template
from app import app
from app.forms import LoginForm

# Python function decorators.
# in this case they register the function as a callback for a certain event, eg. hitting the URL "/" or "/index"
@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Coco"}
    posts = [
        {
            'author': {'username': 'Coco'},
            'body': 'Go get me a cupajoe'
        },
        {
            'author': {'username': 'Angel'},
            'body': 'I wanna take you to the ocean'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return(render_template('login.html', title='Sign In', form=form))

