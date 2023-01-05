import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  channel = message.channel
  if message.authro == client.user:
    return
  if message.content.startswith('$hello'):
    await channel.send('Hello!')

client.run(os.getenv('TOKEN'))


