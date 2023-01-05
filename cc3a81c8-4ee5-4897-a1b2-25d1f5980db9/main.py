import discord
import os
import requests
import json
import random
from replit import db
import randfacts

client = discord.Client()


randomfacts = randfacts.getFact()

@client.event
async def on_Ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("bad"):
      await message.channel.send('No you.')
    
    options = randomfacts
    if "facts" in db.keys():
      options = options + db["facts"]
    


    if message.content.startswith("~fact"):
      await message.channel.send(randomfacts))
    if message.content.startswith("What is Bald Baby"):
      await message.channel.send("He's bad and **BALD** and a ***BABY***")








client.run('NjkxNDYzMTg0MDk1MjQ4NDE1.XngVRQ.vlDgUh5EHy16dHYuoDtx1u_nnis')