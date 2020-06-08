from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
from utl import api, db_functions #create_db
import sqlite3  # enable control of an sqlite database
import os
import json
import urllib
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    # load the template with the user's session info
    if 'user' in session:
        return redirect(url_for('favorites'))
    else:
        pokemon = api.getPokemon()
        return render_template('homepage.html', pokemon=pokemon)

@app.route('/login')
def login():
    if 'user' in session:
        return redirect(url_for('favorites'))
    elif request.args:
        if db_functions.checkfor_credentials(request.args.get('username'), request.args.get('password')):
            session['user'] = request.args.get('username')
            return redirect(url_for('favorites'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    if 'user' in session:
        return redirect(url_for('favorites'))
    elif request.args:
        if db_functions.checkfor_username(request.args.get('username')):
            flash('Account with that username already exists')
            return redirect(url_for('register'))
        else:
            db_functions.create_user(request.args.get('username'), request.args.get('password'))
            flash('Account Created')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged Out Succesfully")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    db_functions.create()
    app.run()
