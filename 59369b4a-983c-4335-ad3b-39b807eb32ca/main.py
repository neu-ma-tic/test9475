import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "triste", "deprimido", "penita", "pena"]

starter_encouragements = [
  "Arriba el animo amigo mío!",
  "Vamos a salir con tbags de esta.",
  "No te conozco pero si estas en este server debes ser una gran persona"
]

puteos = ["aweonao Culiao","imbecil de mierda","perkin", "perkin culiao"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if message.content.startswith('$hola'):
        await message.channel.send('Hola perkin!')
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('$perkin'):
        try:
          user = message.mentions[0]
          if user:
            await message.channel.send(user.mention+' '+random.choice(puteos))
        except:
          await message.channel.send('imbecil no mencionaste a nadie')


        

keep_alive()
client.run(os.getenv('TOKEN'))