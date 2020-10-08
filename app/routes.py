from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return(render_template('login.html', title='Sign In', form=form))

