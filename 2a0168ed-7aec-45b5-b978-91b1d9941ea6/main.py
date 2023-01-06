import discord
import os
from alive import keep_alive
import features

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith('$search'):
      word = msg.split()
      result = features.meaning(word[1])
      await message.channel.send(result)


keep_alive()
client.run(os.environ['TOKEN'])

    
    
