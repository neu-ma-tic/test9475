import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from os import path

client = discord.Client()
cid = "0";

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  
  if message.author == client.user:
    return

  if message.content.startswith('+help'):
    await message.channel.send('This is a simple bot made only to reply to "1.16.5" with read the #server to change the #server use the command +setid:<#serverid> for example to change the server you could do +setid:<#109238410982093>')

  if message.content.startswith('+setid'):
    
    global cid
    await message.channel.send("Id has been changed")
    a = message.content.split(":")

    cid = a[1]

    
    return cid
  if '1.16.5' in message.content:
    
    await message.reply("Please go to " + cid)

keep_alive()
client.run(os.getenv('TOKEN'))