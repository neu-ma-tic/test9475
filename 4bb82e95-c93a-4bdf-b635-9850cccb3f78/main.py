import os
import discord

client = discord.client()

@client.event
async def on_ready():
  print("We have logged in as{0.user}".format(client))

@client.event
async def on_message(message):
  if message.authro == client.user:
    return

if message.content.startswith("$hello"):
  await message.channel.send("Hello1")

client.run()
my_secret = os.environ['token']
