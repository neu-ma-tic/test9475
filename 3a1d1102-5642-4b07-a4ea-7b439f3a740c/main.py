import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("hello"):
    await message.channel.send("```I'm a bot, not your friend.```")

client.run('OTkyNjQ1NTgwMDI1MjM3NjA1.GEeCQq.SlRlar8oxvvxGQx5iZ6YuMFPY8hF5XkU9pFyoY')