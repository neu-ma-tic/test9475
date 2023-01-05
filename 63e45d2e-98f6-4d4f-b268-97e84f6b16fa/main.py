import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print(f"{client.user}) logged in now")


@client.event
async def on_message(message):

  
  await message.delete()




my_secret = os.environ['TOKEN']
client.run(my_secret)