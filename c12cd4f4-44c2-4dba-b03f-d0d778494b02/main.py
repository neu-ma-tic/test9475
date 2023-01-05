import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('bot online.')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('>help'):
    await message.channel.send('Here are the list of commands: >help >hello >wanna fuck >yooO >shawty >who is your e boy >wanna be my e girl >Baby grill >who made you? >hey baby')




  if message.author == client.user:
    return

  if message.content.startswith('>wanna fuck'):
    await message.channel.send('No im loyal to elims :peach: :eggplant:')



  if message.author == client.user:
    return

  if message.content.startswith('>hello'):
    await message.channel.send('Hello! :wave:')



  if message.author == client.user:
    return

  if message.content.startswith('>yooO'):
   await message.channel.send('yooOoooooooooO!!! jugemu jugemu gokou no surikire kaijari suigyo no suigyomatsu unraimatsu fuuraimatsu kuuneru tokoro ni sumu tokoro')
  
  
  
  if message.author == client.user:
    return
  
  if message.content.startswith('>shawty'):
   await message.channel.send('UwU')



  if message.author == client.user:
    return

  if message.content.startswith('>who is your e boy'):
   await message.channel.send('Dady elims')



  if message.author == client.user:
    return

  if message.content.startswith('>wanna be my e girl'):
   await message.channel.send('No, if Elims agrees then ofc!')



  if message.author == client.user:
    return

  if message.content.startswith('>your e boy'):
   await message.channel.send('Dady elims')



  if message.author == client.user:
    return

  if message.content.startswith('>my e girl'):
   await message.channel.send('No, if Elims agrees then ofc!')



  if message.author == client.user:
    return

  if message.content.startswith('>Baby grill'):
   await message.channel.send('Wsp dady UwU')



  if message.author == client.user:
    return

  if message.content.startswith('>who made you?'):
   await message.channel.send('hiro')



  if message.author == client.user:
    return

  if message.content.startswith('>hey baby'):
   await message.channel.send('i have a bf.')




client.run(os.getenv("token"))

