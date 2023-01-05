import discord
import random

TOKEN = 'MTAzNTI0Mjk0OTU4MTIyNjA3NA.G6OzUU.9qlMGjis9mi-lFKtQRlHt2I45hrdKu0xmaPo5s'

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


client.run(TOKEN)
