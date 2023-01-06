from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "This bot has to be a webserver so it never turns off."

def run():
  app.run(host='0.0.0.0',port=8080)

def ping_self():
  t = Thread(target=run)
  t.start()