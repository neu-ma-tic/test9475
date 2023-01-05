import discord
import os
import json
import requests

token = os.environ['token']

client = discord.Client()

def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  my_json = json.loads(response.text)
  return(my_json["postLink"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$meme'):
      meme = get_meme()
      await message.channel.send(meme)

client.run(os.getenv('token'))

