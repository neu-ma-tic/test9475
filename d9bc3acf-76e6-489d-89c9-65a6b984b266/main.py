# Load the dependencies
import discord=m 
import os

# Load the packages
# from packages.fun import fun

# Fun = new fun()

client = discord.Client()

appToken = os.environ['appToken']

@client.event
async def on_ready():
  print('Logged in as ' , client.user)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello !')
  
  if message.content.startswith('$def'):
    print (message.content);
    


client.run(appToken)