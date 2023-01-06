import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = request.get

@client.event
async def on_ready():
  print('zostałeś zalogowant jako {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$elo'):
    await message.channel.send('tofik jest słodki')

client.run(os.getenv('TOKEN'))