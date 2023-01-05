import discord
#import random
#from discord.ext import commands
#import asyncio
import os
#from keepalive import keep_alive


client = discord.Client()

@client.event #register an event

async def on_ready():#called when bot is ready to use
  print("We have logged in as {0.user}".format(client))


@client.event

async def on_message(message):
  if message.author == client.user:
    return
    if message.content.startswith == ("$hello"):
      await message.channel.send("Hello...!!!")

client.run(os.environ['Token'])

