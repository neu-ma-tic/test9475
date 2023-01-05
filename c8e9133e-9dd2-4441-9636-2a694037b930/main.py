import discord

token='OTgwMDk3NzAzOTk4NTU0MTYy.GocUpi.ny5Uf0TUUsDxiXAfj0Ko7OxIu2AMALS2U3YRcQ'

client = discord.Client()

@client.event
async def on_ready():
  print("your bot is ready")
  
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('hello!')

client.run(token)
  