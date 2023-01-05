import discord
import os
import time

client = discord.Client()
token = os.environ['token']

@client.event #this function is for when the bot comes online
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event # this function is for when a message is received in a chat
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!lol'): #When the bot sees the command in this line it prints the one beneath
    await message.channel.send("I Hate Blacks")
  
  if message.content.startswith('!hello'): #When the bot sees the command in this line it prints the one beneath
    await message.channel.send('Hi! Im GAY/O, the newest valorant agent to enter your discord server! I have several cool features to look out for, from hidden commands to cool catchphrases! Im also a racist! We can be chilling out together in no time, saying "niggеr" and "kill jews" etc. Well that about sums it up, looking forward to seeing you around!')
  
  if message.content.startswith('!minecraft'):
    for i in range(0, 500):
      time.sleep(0.5)
      await message.channel.send("minecraftttminecraftttminecraft")


client.run(os.environ['token']) # login for the bot