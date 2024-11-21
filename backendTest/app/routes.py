print("~~~~ Changes made, Flask correctly Reloaded ~~~~") # on website edit this message should appear in the terminal

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam Kenning'}
    posts = [
        {
            'author': {'username': 'Evan'},
            'body': 'Lets test this shiii'
        },
        {
            'author': {'username': 'Zaki'},
            'body': 'Hell YEAAAHHHHHHHH'
        },
        {
            'author': {'username': 'Charles'},
            'body': 'Bless up amen'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)