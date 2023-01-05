from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Im working..."

def run():
    app.run(host='0.0.0.0',port=3020)

def keep_alive():
    t = Thread(target=run)
    t.start()