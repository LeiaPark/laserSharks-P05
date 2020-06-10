import sqlite3  # enable control of an sqlite database
DB_FILE = "pokedex.db"

def create():
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops


    # < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

    #==========================================================

    # test SQL stmt in sqlite3 shell, save as string
    create_table_users = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT);"
    insert_user = "INSERT OR IGNORE INTO users(user_id, username, password) VALUES( 1, \"admin\", \"stuy\");"
    create_table_favorites = "CREATE TABLE IF NOT EXISTS favorites(user_id INTEGER PRIMARY KEY AUTOINCREMENT, list TEXT);"
    insert_favorites = "INSERT OR IGNORE INTO favorites(user_id, list) VALUES( 1, \"1\");"
    
    create_table_gen1 = "CREATE TABLE IF NOT EXISTS gen1(name TEXT, pokemon_id INTEGER, image TEXT);"
    create_table_gen2 = "CREATE TABLE IF NOT EXISTS gen2(name TEXT, pokemon_id INTEGER, image TEXT);"
    
    c.execute(create_table_users)
    c.execute(insert_user)
    c.execute(create_table_favorites)
    c.execute(insert_favorites)

    c.execute(create_table_gen1)
    c.execute(create_table_gen2)

    db.commit()  # save changes
    db.close()  # close database

def checkfor_credentials(username, password):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT username, password FROM users WHERE users.username = \"%s\" AND users.password = \"%s\";" % (username, password)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response # returns null if credentials are wrong, and the correct info if correct

def checkfor_username(username):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT username FROM users WHERE username == \"%s\";" % (username)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

    return response

def create_user(username, password):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "INSERT INTO users(username, password) VALUES(\"%s\", \"%s\");" % (username, password)
    response = list(c.execute(query))
    query = "INSERT INTO favorites(list) VALUES(\"\");"
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database

def get_user_id(username):
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops

    query = "SELECT user_id FROM users WHERE username == \"%s\";" % (username)
    response = list(c.execute(query))
    db.commit()  # save changes
    db.close()  # close database
    return response

def get_favs(user_id):
    faves = []
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT list FROM favorites WHERE favorites.user_id == ?;", (user_id[0]))
    l = ''.join((c.fetchall()[0])).split()
    for f in l:
        faves.append(int(f))
    db.commit()
    db.close()
    return faves

def add_fave(user_id,pokemon_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    new = ''
    prev = c.execute("SELECT list FROM favorites WHERE user_id == ?;", (user_id[0]))
    l = ''.join((c.fetchall()[0])).split()
    for f in l:
        new = new + f + ' '
    new = new + str(pokemon_id)
    c.execute("UPDATE favorites SET list=? WHERE user_id == ?;", ((new,user_id[0][0])))
    db.commit()
    db.close()
              
def remove_fave(user_id,pokemon_id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    new = ''
    prev = c.execute("SELECT list FROM favorites WHERE user_id == ?;", (user_id[0]))
    l = ''.join((c.fetchall()[0])).split()
    for f in l:
        if (f == str(pokemon_id)):
            pass
        else:
            new = new + f + ' '
    c.execute("UPDATE favorites SET list=? WHERE user_id == ?;", ((new,user_id[0][0])))
    db.commit()
    db.close()

def check1():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM gen1;")
    x = c.fetchall();
    if x:
        return False
    return True

def add_gen1(gen1):
    ''' gen1: array of arrays [ ['bulbasaur',1,'imagesrc'], ... ] '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for pokemon in gen1:
        c.execute("INSERT INTO gen1(name, pokemon_id, image) VALUES(?,?,?);", (pokemon[0],pokemon[1],pokemon[2]))
    db.commit()
    db.close()

def retrieve_gen1():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    gen1 = []
    c.execute("SELECT * FROM gen1;")
    temp = []
    for pokemon in c.fetchall():
        temp.append(pokemon[0])
        temp.append(pokemon[1])
        temp.append(pokemon[2])
        gen1.append(temp)
        temp = []
    db.commit()
    db.close()
    return gen1

def check2():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM gen2;")
    x = c.fetchall();
    if x:
        return False
    return True

def add_gen2(gen2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for pokemon in gen2:
        c.execute("INSERT INTO gen2(name, pokemon_id, image) VALUES(?,?,?);", (pokemon[0],pokemon[1],pokemon[2]))
    db.commit()
    db.close()

def retrieve_gen2():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    gen2 = []
    c.execute("SELECT * FROM gen2;")
    temp = []
    for pokemon in c.fetchall():
        temp.append(pokemon[0])
        temp.append(pokemon[1])
        temp.append(pokemon[2])
        gen2.append(temp)
        temp = []
    db.commit()
    db.close()
    return gen2
