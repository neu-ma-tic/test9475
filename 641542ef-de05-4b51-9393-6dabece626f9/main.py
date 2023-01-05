import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Less GOOOOO!")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'Shark?':
    await message.channel.send('POG!')

client.run(os.environ["TOKEN"]) 