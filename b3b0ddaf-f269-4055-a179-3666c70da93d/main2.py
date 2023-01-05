import discord
import os
import time

pass = "OTMzMDk2NzYyNzExODgzNzg2.YeckFA.inEGBqtVvCKQm2scuGutmjekF3c"

client = discord.Client()

@client.event
async def on_ready():
  print('We lol')

time.sleep(5)

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  if message.content.startswith("!!!NEEDHELP"):
    await message.channel.send("Hoi")

  client.run(pass)
