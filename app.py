from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/secret')
def secret_message():
    return 'This cucumber cries at midnight!'
