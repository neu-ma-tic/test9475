from flask import Flask
from threading import Thread
app=Flask('')
@app.route('/')
def main():
    return "WELCOME TO THE THANOSBOT WEBSERVER! This is the webserver for THANOSBOT, a bot application for Discord. There isn't really much going on here, but thanks for stopping by. If you found this, you probably have access to ThanosBot-go check it out."

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
