import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)

@client.event
async def on_ready():

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("_hello"):
    await message.channel.send("hello")


my_secret = os.environ['TOKEN']
client.run(my_secret)