import discord

client = discord.Client()

@client.event

async def on_ready():
  print("We have logged in as {0.user}".format(client)) 

@client.event

async def on_message():
  if message.author == client.user:
    return
