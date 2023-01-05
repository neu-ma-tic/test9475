import os
import discord

my_secret = os.environ['TOKEN']
client = discord.Client()


MYID = 5026

@client.event
async def userIsConnected(id=5026):
  if (id.VoiceChannel):
    print("Connected")
  else:
    print("Not connected")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(my_secret)
