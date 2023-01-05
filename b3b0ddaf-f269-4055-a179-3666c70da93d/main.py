import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We lol')

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  if message.content.startswith("!!!NEEDHELP"):
    await message.channel.send("Hoi")

  client.run(os.getenv('botpass'))


