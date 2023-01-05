import discord
import os

client = discord.Client()

@client.event
async def on_ready():
     print('We have logged in as {0.user}, hello'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

    if message.content.startswith('!cmds'):
      await message.channel.send('here is the list of cmds: 1. hello:this will give you a welcome greeting 2.goodbye:this will give you a cheerfull goodbye 3.howdy:this will give you some cowboy speak 4.!cmds:this will give you a list of cmds')
    
    if message.content.startswith('howdy'):
      await message.channel.send('howdy partner i hope you have a Hog-Killin’ Time on this sever')
      
  if message.content.startswith('hello'):
      await message.channel.send('hi, how are you?')
       
  if message.content.startswith('goodbye'):
      await message.channel.send('bye, see you tomorrow')

client.run('MTAwMDA1ODcyOTIyNTUzNTUxOQ.GCyGhB.jlApYBEj_fx8fjUS2qzVDD1w9Muk6O89gfWhXE')