from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    def index():
    if 'username' in session:
        return 'Hey there, %s' % escape(session['username']', how is your day going?')
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/secret')
def secret_message():
    return 'The cucumber cries at midnight!'
