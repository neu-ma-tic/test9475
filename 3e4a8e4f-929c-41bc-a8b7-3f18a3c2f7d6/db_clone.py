import time

import requests
from replit import db


def clone(url, start):
    keys = requests.get(url + '?prefix').content.decode().split('\n')

    print(keys)

    for i, key in enumerate(keys[start:]):
        value = requests.get(url + '/' + key).content.decode()
        print('index:', i + start)
        print(key, value)
        if value == 'null':
            db[key] = None
        elif value.isdigit():
            db[key] = int(value)
        else:
            db[key] = value
        print('db:', key, db[key])
        time.sleep(5)
