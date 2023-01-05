from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "amitabia is dumbass"

def run():
    app.run(host="0.0.0.0", port=8070)

def keep_alive():
    server = Thread(target=run)
    server.start()