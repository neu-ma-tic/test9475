import discord
import os

from command import predefined_commands

client = discord.Client()

@client.event
async def on_ready():
  print(f'we have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user or not message.content.startswith('@bot'):
    return
  
  words = message.content.split()
  _, command, args = words[0], words[1], words[2:]
  if command in predefined_commands:
    await predefined_commands[command].run(message.channel, args)

client.run(os.getenv('TOKEN'))
