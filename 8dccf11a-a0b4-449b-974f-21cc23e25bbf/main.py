import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there",
  "You are a great person!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" -"+json_data[0]['a']
  return quote

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements
  
    



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]


  if msg.startswith('$hello'):
    await message.channel.send('Hello!')
  elif msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)  
  elif any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))
  elif msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New message added.")
  elif msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del ",1)[1])  
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)  


      

client.run(os.getenv('TOKEN'))
