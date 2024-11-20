from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam Kenning'}
    posts = [
        {
            'author': {'username': 'Evan'},
            'body': 'Lets test this shiiiittt'
        },
        {
            'author': {'username': 'Zaki'},
            'body': 'FUCK YEAAAHHHHHHHH'
        }
    ]
    
    return render_template('index.html', title='Home', user=user, posts=posts)

print("~~~~ Changes made, Flask correctly Reloaded ~~~~")
