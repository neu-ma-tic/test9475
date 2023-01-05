import discord
import os

client = discord.Client()

@client.event 
async def on_ready():
  print('Logged in as {0.user}'.format(client))

  @client.event
  async def on_message():
    if message.author == client.user:
      return
      
    if message.content.startswith('!coinflip'):
      await message.channel.send('Heads')

  client.run(os.getenviron('TOKEN'))