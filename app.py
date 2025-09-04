from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, world!<p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['user_name']
        return f'<h1>{username}님, 환영합니다!</h1>'
    else:
        return render_template('login.html')
