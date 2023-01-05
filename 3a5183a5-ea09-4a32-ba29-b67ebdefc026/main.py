import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('LISTENING TO SUPER IDOL WHILE IN SOLITARY CONFINEMENT. PLEASE SEND HELP. '))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  

#All the period/period sub removers
    if message.content.startswith("."):
      await message.channel.send(random.choice(options))
      await message.delete()
      await message.author.send('Hiya! Klee thinks you are the best, but could you please stop spamming punctuations? I do not think that is very cool. =^._.^= ∫')
    if message.content.startswith(","):
      await message.channel.send(random.choice(options))
      await message.delete()
      await message.author.send('Hiya! Klee thinks you are the best, but could you please stop spamming punctuations? I do not think that is very cool. =^._.^= ∫')
    if message.content.startswith("'"):
      await message.channel.send(random.choice(options))
      await message.delete()
      await message.author.send('Hiya! Klee thinks you are the best, but could you please stop spamming punctuations? I do not think that is very cool. =^._.^= ∫')
    if message.content.startswith("*.*"):
      await message.channel.send(random.choice(options))
      await message.delete()
      await message.author.send('Hiya! Klee thinks you are the best, but could you please stop spamming punctuations? I do not think that is very cool. =^._.^= ∫')
    if message.content.startswith("**.**"):
      await message.channel.send(random.choice(options))
      await message.delete()
      await message.author.send('Hiya! Klee thinks you are the best, but could you please stop spamming punctuations? I do not think that is very cool. =^._.^= ∫')
    if message.content.startswith("***.***"):
      await message.channel.send(random.choice(options))
      await message.author.send('That reminds me,')

#Other phrases
    if message.content.startswith("aight"):
        await message.delete()
        await message.channel.send('Hiya! Klee does not think that the word aight is gramatically correct, and will keep correcting you until you learn. :3')

    if message.content.startswith("pain"):
        await message.delete()
        await message.channel.send('My name is Klee, and you are my bestest friend! Klee does not want her bestest friends to feel pain!')
    if message.content.startswith("k."):
      await message.delete()
      await message.channel.send(random.choice(options))
    if message.content.startswith("Klee"):
        await message.channel.send('Fuck you dude')
    if message.content.startswith("klee"):
        await message.channel.send('Fuck you dude')
      
    
      
#Random Answers for ./,
rad = [
  "stfu =^._.^= ∫'",
  "Stop acting edgy =^._.^= ∫'",
  "Can you not =^._.^= ∫'"
]
options = rad
#Different triggers for ./,
dtd = [
  ".",
  ",",
  "*.*",
  "**.**",
  "***.***",
  "'"
]

      


keep_alive()
client.run(os.getenv('TOKEN'))
