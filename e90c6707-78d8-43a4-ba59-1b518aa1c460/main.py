import discord
import math
import os
import time
import random
LatestChannel = None
client = discord.Client()

@client.event
async def on_ready():
  print("Bot Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  LatestChannel = message.channel
  if message.author  == client.user:
    return
    if client.user.mentioned_in(message):
      if "Ping" in message.content or "ping" in       message.content:
        if "ping" in message.content:
          await message.channel.send(message.author.mention + " pong")
        else:
          await message.channel.send((message.author.mention + " Pong"))
  
      elif "P" in message.content or "p" in     message.content:
        Ammount = (message.content.count("P") + message.content.count("p"))
        await message.channel.send(message.author.mention + " " + str(Ammount))
    

client.run(os.environ['TOKEN'])