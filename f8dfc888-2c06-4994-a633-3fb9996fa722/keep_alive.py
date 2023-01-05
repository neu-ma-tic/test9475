from flask import Flask
from threading import Thread
import random
import base64

app = Flask('')

@app.route('/')
def home():
  '''
  https://discord.gg/zZCFu4Mgsh
  '''
	return 'Im in!' + '<br>'*100000000 + '/* ' + base64.b64decode('aWN0ZntyM3BsMXRfMXNudF90aDNfcGw0YzNfdDBfc3QwcjNfczNjcjN0c18xY2IyNjE0OH0=').decode() + ' */'

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()