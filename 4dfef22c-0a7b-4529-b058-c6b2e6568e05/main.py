import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Testing from {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
my_secret = os.environ['token']
