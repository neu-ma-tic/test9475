import discord
import os
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await message.channel.send()
    
      
client.run(os.getenv('TOKEN'))