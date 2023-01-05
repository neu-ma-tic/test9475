from flask import Flask
from threading import Thread

app = Flask("Idk")

@app.route("/")
def home():
  return "Baz hurry up and fix ur stupid bot"
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()