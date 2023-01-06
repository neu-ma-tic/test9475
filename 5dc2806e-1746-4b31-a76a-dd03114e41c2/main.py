import discord
import os
import requests
import json
import threading
i = 1
client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(i)
  

client.run(os.getenv('TOKEN'))
def printit():
  threading.Timer(5.0, printit).start()
  i = i + 1
printit()