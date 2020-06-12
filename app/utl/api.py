import os
import json
import urllib
import random
import urllib.request
from urllib.request import Request, urlopen

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def get_gen1():
    request = Request("https://pokeapi.co/api/v2/pokemon/?limit=151", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name(str), id(int), picture(str), type(array)'''
    temp = [] #holds the information while parsing through pokemons
    m = 150
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
           # typ.append(mondata[0]['types'][x]['type']['name'])
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen2():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=151&limit=100", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    temp = [] #holds the information while parsing through pokemons
    m = 99
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen3():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=251&limit=135", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    m = 134
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen4():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=386&limit=107", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    m = 106
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen5():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=494&limit=155", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    m = 154
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen6():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=649&limit=72", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    m = 71
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d

def get_gen7():
    request = Request("https://pokeapi.co/api/v2/pokemon/?offset=721&limit=88", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    m = 87
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        l = len(mondata[0]['types'])
        typ = ''
        for x in range(l):
            typ = typ + mondata[0]['types'][x]['type']['name'] + ' '
        temp.append(typ)
        d.append(temp)
        temp = []
        m = m - 1
    return d
