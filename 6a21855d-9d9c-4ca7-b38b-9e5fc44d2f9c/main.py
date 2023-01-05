import discord
import os
from replit import db

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
     return
    
  if message.content.startsWith("asi!"):
    await message.channel.send("Hi")

client.run("OTQ0MzIzNzQ1MDY4MjIwNDU2.Yg_8BQ.3W8euxWs9-vMQ6uEKwe5bdvr84M")