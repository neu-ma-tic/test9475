import discord
import os

client = discord.client()

@client.event 
async def on_ready():
  print("blaalbblaalb {0.user}".format(client)) 

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$hello"):
    await message.channel.send("helloyall")

client.run(os.getenv("TOKEN"))