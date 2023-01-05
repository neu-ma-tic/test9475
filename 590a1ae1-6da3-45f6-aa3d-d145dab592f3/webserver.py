from flashk import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Webserver OK, Discord Bot OK"
    
 app.run(host="0.0.0.0",port=8080)

def keep-alive():
  t = Thread(target=run)
  t.start()
  def run():