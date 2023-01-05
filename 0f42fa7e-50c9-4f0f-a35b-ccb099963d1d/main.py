import discord
import os
import requests
import urllib
import json

client=discord.Client()

#registering events
@client.event
async def on_ready():
  print('Logged in as bot-{0.user}'.format(client))

@client.event
async def on_message(message):
  if(message.author==client.user):
    return
  if(message.content.startswith('$Hello')):
    await message.channel.send('Hello')

client.run(os.getenv('TOKEN'))
