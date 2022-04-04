from django.shortcuts import render
from flask import Flask, session, redirect, url_for, escape, request, render_template

from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav()


topbar = Navbar('topbar',
                View('Home', 'home'),
                View('Login', 'login'),
                View('Logout', 'logout'),
                Link('Render Docs', 'https://render.com/docs')
                )

nav.register_element('top', topbar)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@ app.route('/')
def home():
    return render_template('home.html')


@ app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     session['username'] = request.form['username']
    #     return redirect(url_for('/'))
    return render_template('login.html')


@ app.route('/logout')
def logout():
    # remove the username from the session if it's there
    # session.pop('username', None)
    return render_template('logout.html')


@ app.route('/secret')
def secret_message():
    return 'The cucumber cries at midnight!'


nav.init_app(app)
