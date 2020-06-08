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

# POKE API :: the first most basic call !!!
def getPokemon():
    # gets the first 100 pokemon
    request = Request("https://pokeapi.co/api/v2/pokemon/?limit=100", headers=headers) 
    response = urlopen(request).read()
    data = json.loads(response)
    m = 19
    d = []
    ''' d is an array of arrays. Each array will have pokemon information in this order:
                 name, id, picture'''
    temp = [] #holds the information while parsing through pokemons
    while m >= 0:
        w = Request(data['results'][m]['url'], headers=headers)
        mon = urlopen(w).read()
        mondata = [json.loads(mon)]
        temp.append(data['results'][m]['name'])
        temp.append(mondata[0]['id'])
        temp.append(mondata[0]['sprites']['front_default'])
        d.append(temp)
        temp = []
        m = m - 1
    return d


