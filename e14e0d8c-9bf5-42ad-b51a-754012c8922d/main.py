import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

sad_words=["depressed","i am sad","unhappy","crying"]

happy_stuff = ["Hang in there my boi","Dont worry you are beatiful in the way you are","Cheer up my man"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
 print("I am ready to work")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(happy_stuff))

keep_alive()
client.run(os.getenv('TOKEN'))