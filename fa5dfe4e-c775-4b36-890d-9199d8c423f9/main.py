import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def get_joke():
  joke_url = 'https://icanhazdadjoke.com'
  my_header = {'Accept': 'application/json'}
  results = requests.get(joke_url, headers = my_header)
  json_result = results.json()
  return json_result['joke']

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == "joke":
    await message.channel.send(get_joke())

keep_alive()
client.run(os.getenv('TOKEN'))