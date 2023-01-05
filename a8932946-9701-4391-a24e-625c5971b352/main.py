import os
import discord
token = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have been logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return  

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')  

client.run(
token
)




