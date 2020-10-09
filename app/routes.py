from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User

# Python function decorators.
# in this case they register the function as a callback for a certain event, eg. hitting the URL "/" or "/index"
@app.route('/')
@app.route('/index')
@login_required
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
    # If the current user is already authenticate redirect to index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Initialise the Login form
    form = LoginForm()
    if form.validate_on_submit():
        # search and return result for username in user table
        user = User.query.filter_by(username=form.username.data).first()
        # Warning will flash if username doesn't exist or password is incorrect
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Log user in and remember based on user preference, redirect
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return(render_template('login.html', title='Sign In', form=form))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

