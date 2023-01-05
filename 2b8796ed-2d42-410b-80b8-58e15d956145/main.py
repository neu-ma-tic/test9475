import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as{0.user}".format(client))
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('#who'):
    await message.channel.send('Hello Im rady.My creator is Inzi')
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith('#pls provide my channel link'):
    await message.channel.send('https://youtube.com/c/InfoKnight')
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content==('poppat'):
    await message.author.send('Warning! This text message is not allowed in this server')
@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content==('poppat'):
    await message.delete()
    
    
client.run(os.getenv('TOKEN'))


