from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Please don't kill me"

def run():
  app.run(host='0.0.0.0',port=8080)
def keepAlive():
  t = Thread(target=run)
  t.start()
