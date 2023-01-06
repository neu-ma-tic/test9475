import os
import discord
import requests
import json



client = discord.Client()
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return



  if message.content.startswith('Hi'):
    await message.channel.send('Hola, como estas!')



my_secret = os.environ['my_secret']
client.run(my_secret)
