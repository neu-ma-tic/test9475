import discord

client = discord.Client()

@client.event 
async def on_ready():
  print (' We have logged in as {0.user}'. format(client))  
