from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def index():
  return 'Working bot.'

@app.route('/info')
def info():
  return 'Jian Yue'

def run():
  app.run(host="0.0.0.0", port=8080)
  
def keep_alive():
    server = Thread(target=run)
    server.start()
    