from flask import flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Webserver OK, Discord Bot 

def run():
  app.rin(host="0.0.0.0",port=8080)

def keep_alive():
  t - Thread(target=run)
  t.start()