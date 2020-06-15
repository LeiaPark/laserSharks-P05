import sqlite3  # enable control of an sqlite database
import os
import json
import urllib
import random
from random import randint
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for

from utl import api, db_functions #create_db

app = Flask(__name__)
app.secret_key = os.urandom(24)
db_functions.create()
if db_functions.check('gen1'):
    print("ADDING GENERATION 1...")
    db_functions.add_gen('gen1',api.get_gen1())
if db_functions.check('gen2'):
    print("ADDING GENERATION 2...")
    db_functions.add_gen('gen2',api.get_gen2())
if db_functions.check('gen3'):
    print("ADDING GENERATION 3...")
    db_functions.add_gen('gen3',api.get_gen3())
if db_functions.check('gen4'):
    print("ADDING GENERATION 4...")
    db_functions.add_gen('gen4',api.get_gen4())
if db_functions.check('gen5'):
    print("ADDING GENERATION 5...")
    db_functions.add_gen('gen5',api.get_gen5())
if db_functions.check('gen6'):
    print("ADDING GENERATION 6...")
    db_functions.add_gen('gen6',api.get_gen6())
if db_functions.check('gen7'):
    print("ADDING GENERATION 7...")
    db_functions.add_gen('gen7',api.get_gen7())

print(None == None)

mons = db_functions.retrieve_gen('gen7') + db_functions.retrieve_gen('gen6') + db_functions.retrieve_gen('gen5') + db_functions.retrieve_gen('gen4') + db_functions.retrieve_gen('gen3') + db_functions.retrieve_gen('gen2') + db_functions.retrieve_gen('gen1')
#mons = db_functions.retrieve_gen('gen1')
#print(mons)
print(len(mons))
randompokemon=[]
def get_monname(name):
    name = name.lower().strip()
    for pokemon in mons:
        for n in pokemon:
            if n == name:
                return pokemon
    return False

def get_monid(pokemon_id):
    for pokemon in mons:
        if pokemon[1] == pokemon_id:
            return pokemon
        #for n in pokemon:
        #    if n == pokemon_id:
        #        return pokemon
    return False

def get_montypes(types):
    ans = []
    for pokemon in mons:
        t = pokemon[3].split()
        for x in t:
            if x == types:
                ans.append(pokemon)
    return ans

gens = ['gen1','gen2','gen3','gen4','gen5','gen6','gen7']
types = ['normal','fighting','flying','poison','ground','rock','bug','ghost','steel','fire','water','grass','electric','psychic','ice','dragon','fairy','dark']

@app.route('/')
def index():
    # add the if request args stuff djfadjfh
    print(request.args)
    if request.args:
        print(request.args)
        s = request.args.get('sort')
        if s in gens:
            pokemon = db_functions.retrieve_gen(request.args.get('sort'))
        elif s in types:
            pokemon = get_montypes(s)
        elif s == 'default':
            pokemon = mons
    else:
        pokemon = mons
    user="null"
    if 'user' in session:
        user=session['user']
    return render_template('homepage.html', pokemon=pokemon, user=user)

@app.route('/login')
def login():
    if 'user' in session:
        user=session['user']
        return redirect(url_for('index'))
    elif request.args:
        if db_functions.checkfor_credentials(request.args.get('username'), request.args.get('password')):
            session['user'] = request.args.get('username')
            session['id'] = db_functions.get_user_id(request.args.get('username'))
            user=session['user']
            return redirect(url_for('index'))
        else:
            flash('Invalid Credentials')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    if 'user' in session:
        user=session['user']
        return redirect(url_for('index'))
    elif request.args:
        if db_functions.checkfor_username(request.args.get('username')):
            flash('Account with that username already exists')
            return redirect(url_for('register'))
        elif request.args.get('password1') != request.args.get('password2'):
            flash('Passwords Don\'t Match')
            return redirect(url_for('register'))
        else:
            db_functions.create_user(request.args.get('username'), request.args.get('password1'))
            flash('Account Created')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/favorites')
def favorites():
    if 'user' in session:
        pokemon = mons
        return render_template('favorites.html',
                               favorites=db_functions.get_favs(session['id']),
                               pokemon=pokemon)
    else:
        return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user' in session:
        print(request.args.get('pokemon_id'))
        db_functions.add_fave(session['id'],request.args.get('pokemon_id'))
        flash('Added to Favorites')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/remove', methods=['GET', 'POST'])
def remove():
    if 'user' in session:
        db_functions.remove_fave(session['id'],request.args.get('pokemon_id'))
        flash('Removed from Favorites')
        return redirect(url_for('favorites'))
    else:
        return redirect(url_for('login'))

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

@app.route('/search')
def search():
    s = request.args.get('keyword')
    if get_monname(s):
        user="null"
        if 'user' in session:
            user=session['user']
        return render_template('search.html', search=s, result=get_monname(s), user=user)
    elif hasNumbers(s):
        if get_monid(int(s)):
            user="null"
            if 'user' in session:
                user=session['user']
            return render_template('search.html', search=s, result=get_monid(int(s)), user=user)
        else:
            flash('ID not found')
            return redirect(url_for('index'))
    else:
        flash('Pokemon not found')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged Out Succesfully")
    return redirect(url_for("index"))

@app.route('/game')
def game():
    if 'user' in session:
        session['randompokemon'] = mons[randint(0, len(mons) - 1)]
        print(session['randompokemon'])
        return render_template('game.html', mon = session['randompokemon'])
    else:
        return redirect(url_for('login'))

@app.route('/checkanswer')
def check():
    ans = request.args.get('answer')
    session['answer'] = ans
    if(ans==session['randompokemon'][0]):
        return redirect(url_for("win"))
    else:
        return redirect(url_for("lose"))

@app.route('/win')
def win():
    if('answer' in session):
        session.pop('answer', None)
        return render_template('win.html', mon = session['randompokemon'])
    return redirect(url_for("game"))

@app.route('/lose')
def lose():
    if('answer' in session):
        session.pop('answer', None)
        return render_template('lose.html', mon = session['randompokemon'])
    return redirect(url_for("game"))
if __name__ == "__main__":
    app.debug = True
    db_functions.create()
    app.run()
