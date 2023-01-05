import os
import discord
import requests
import json
import random 
from replit import db

client = discord.Client()

sad_words = ["sad", "depress", "unhappy", "boring", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!", 
  "Hang in there",
  "You are a great person / bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else: 
    db["encouragements"] = [encouraging_message]

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
  # If come from the bot
  if message.author == client.user:
    return
  if msg.startswith("$hello"):
    await message.channel.send(f"Hello {message.author}")
  if msg.startswith("$inspire"):
    await message.channel.send(get_quote())
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragements(index)
      encouragements = db["enmcouragements"]
    await message.channel.send(encouragements)

client.run(os.getenv("TOKEN"))

