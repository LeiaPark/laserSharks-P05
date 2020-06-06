from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
from utl import api #db_functions, create_db
import sqlite3  # enable control of an sqlite database
import os
import json
import urllib
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)

if __name__ == "__main__":
    app.debug = True
    app.run()
