import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
#from replit import db


client = discord.Client()

sad_words = ["triste", "depresso", "sad", "depressed"]

risposte_iniziali = [
  "impiccati lol",
  "ok",
  "nya nya",
  "tirste",
  ":warning: FREE مجانا PUNJABI حلال مجانا تماما SKIN نقطة حمراء شوبي AMONG US :warning:"
]

def get_quote():
  response = requests.get ("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return (quote)

#def update_risposte(messaggio_risposta):
  #if "risposte" in db.keys():
    #risposte = db["risposte"]
    #risposte.appen(messaggio_risposta)
    #db["risposte"] = risposte
  #else:
    #db["risposte"]  = [messaggio_risposta]

#def delete_risposte(index)
  #risposte = db["risposte"]
  #if len(risposte) > index
    #del risposte[index]
    #db["risposte"] = risposte

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
#i nomi delle funzioni sono specifici, provengono da discord.py
async def on_message(message):

  #se il messaggio proviene dal bot
  if message.author == client.user:
    return

  msg = message.content

  #frase casuale
  if msg.startswith('$random_quote'):
    quote = get_quote()
    await message.channel.send(quote)

  #cose
  if msg.startswith('$egg'):
    await message.channel.send('an oval object, often with a hard shell, that is produced by female birds and particular reptiles and insects, and contains a baby animal that comes out when it is developed')
  if 'league of legends' in message.content or 'lega delle leggende' in message.content:
    await message.channel.send('https://www.youtube.com/watch/cFnPhs0_fI8')
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(risposte_iniziali)) 

keep_alive()
client.run(os.getenv('TOKEN'))
#il nome non deve essere per forza TOKEN, ma deve essere lo stesso del file .env
