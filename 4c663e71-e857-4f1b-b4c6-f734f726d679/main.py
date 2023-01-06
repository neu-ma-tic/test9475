import discord
import os


client = discord.Client()

@client.event
async def on_ready():
  print('Kamy in as {0.user}.format(client)')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('#Kami'):
    await message.channel.send('Fvck <@454088875590156288>!')
  if message.content.startswith('1v9'):
    await message.channel.send('Kamizinha1v9 <@454088875590156288>!', file=discord.File(kami1v9.jpg))
  if message.content.startswith('<@454088875590156288>'):
    await message.channel.send('Oi linda solteira ?<@454088875590156288>!')

  
client.run('OTc1ODEwNzcwMjI5MTYyMDQ0.GiD7vO.8zMciACDRs8MCBEKIKtSKQFzkOpwzXP8EEAPE8')
