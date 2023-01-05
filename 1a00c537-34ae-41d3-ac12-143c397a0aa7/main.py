import discord
import os
import time
import random
from alive import alive

client = discord.Client()
guild = discord.Guild


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("prepare yourself to be amazed")
    


@client.event
async def on_message(message):
  if message.author == client.user:
    return
            
   
  if message.content.endswith('Hi'):
    time.sleep(1)
    await message.channel.send('hello')
  if message.content.endswith('sup'): 
    time.sleep(1)
    await message.channel.send('sup')
  if message.content.endswith('Good Morning'):
    time.sleep(1)  
    await message.channel.send('Good Morning ')
    

  SPAM = ('SPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAM')

  

  if message.content.endswith('!spam'):
    time.sleep(2)
    await message.channel.send('You are doomed') 
    time.sleep(3)  
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)
    await message.channel.send(SPAM)  


  Mylist = ('Edwin','Arnav','Jeeva', 'Angath', 'Madhav')
  Sorry = ('Sorry, but you will be joining during creative:sweat_smile:', 'I think it is time for you to rest:stuck_out_tongue:', 'You cant come today bro', 'Enjoy Netflix!:dissapointed:', 'Sorry bro but you cant come today for Battle Royale:confused:', 'Go and watch Shippudden', 'Go watch a movie dude', 'Hate to break it but you arent coming!:confused:', 'Go and do some sports, FATSO!:hot_face:', 'Go and do your homework!:nerd:', 'Go buy eggs and come!', 'RASENGAN!!!, PLAYER REMOVING JUTSU!, you were removed by an eormous chakra!:exploding_head:')
  if message.content.endswith('!kik'):
    time.sleep(0.7)
    await message.channel.send(random.choice(Mylist))
    time.sleep(0.7)
    await message.channel.send(random.choice(Sorry))
    time.sleep(1.5)
    await message.channel.send('everyone else enjoy:smiley:')
    time.sleep(2)
    await message.channel.send('Enter your respective names in CAPITAL letter to inform that you are playing')
    time.sleep(2)
  if message.content.endswith('ANGATH'):
    time.sleep(2) 
    await message.channel.send('You have logged for today')
  else message.content.startswith(''):
      await message.channel.send('You have already logged in for today')
      
  if message.content.endswith('JEEVA'):
    time.sleep(2)
    await message.channel.send('You have logged in for today')
  if message.content.endswith('MADHAV'):
    time.sleep(2)
    await message.channel.send('You have logged in for today')
    
  if message.content.endswith('EDWIN'):
    time.sleep(2)
    await message.channel.send('You have logged in for today')
    
  if message.content.endswith('ARNAV'):
    time.sleep(2)
    await message.channel.send('You have logged in for today')
  if message.content.endswith('SANKEERTH'):
    time.sleep(2)
    await message.channel.send('You have logged in for today')
  


















alive()
client.run(os.getenv('TOKEN'))