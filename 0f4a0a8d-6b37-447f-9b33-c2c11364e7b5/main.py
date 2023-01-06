import  discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We Have Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!Hello'):
    await message.channel.send('Hello!!')

client.run(MTAxNDMxMDI2NDIwOTk0ODczNA.GJtMmr.YXj9q_nREUNxQ9pDtdzE8PceSOvFbIl5LbB7pc)