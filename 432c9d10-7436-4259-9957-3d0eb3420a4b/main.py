import discord
import random

client = discord.Client()

bad_words = ["fuck", "shit", "bitch", "cunt", "ass", "asshole"]

no = ["No your not allowed to say that"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

    if message.content.startswith('!quote'):
      await message.channel.send('https://api.kanye.rest')


    if any(word in message.content for word in bad_words):
        await message.channel.send(random.choice(no))
 

client.run('ODk2OTM0MTk3MTA3NzU3MDY2.YWOVEA.mi-SywtMfRDyE2loROf4uInB2bY')