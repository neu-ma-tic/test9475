import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import youtube_dl
import time




client = discord.Client()



sadness = ["sad", "depressed", "unhappy", "annoyed", "angry"]

s_encourage =  ["Cheer up buddy!", "Why so sad?", "Hang in there.", "You're an amazing person!"]

ball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]


@client.event
async def on_ready():
  activity = discord.Game(name="Here to help", type=3)
  await client.change_presence (status=discord.Status.idle, activity = activity)
  print('Logged in as {0.user}'.format(client))
  while True:
    activity = discord.Game(name="Here to help", type=3)
    await client.change_presence (status=discord.Status.idle, activity = activity)


@client.event
async def on_message(message):
  if message.author == client.user:
   return
 
  
  if message.content.startswith('@Ping'):
    print("somebody used ping")
    await message.channel.send('Pong!')



  if any(word in message.content for word in sadness):
    print(message.author)
    print("is sad")
    await message.channel.send(random.choice(s_encourage))


  if message.content.startswith('@Realping'):
    print("somebody used rlping")
    await message.channel.send(f'Pong! In {round(client.latency * 1000)}ms')


  if message.content.startswith('@Suicide'):
    await message.channel.send(format(message.author.name))
    await message.channel.send("HAS DIED!")


  if message.content.startswith("@8ball"):
    print(message.author)
    print("8ball")
    time.sleep(2)
    await message.channel.send(random.choice(ball))


  if message.content.startswith('@Help'):
    await message.channel.send((message.author))
    await message.channel.send('Looks like you need help heres some helpful stuff')
    await message.channel.send('All my commands start with @ and a letter after that has to be a capital!')
    await message.channel.send("Here's a list of cammnds: @Help, @8ball, @Suicide, @Realping and @Ping @Hey")

  
  if message.content.startswith('@Say'):
      embed=discord.Embed(title="Say",  description=message.content, color=0x5733FF)
      await message.channel.send(embed=embed)

  if message.content.startswith('@Hey'):
      embed=discord.Embed(title="Bruh",  description="You are actually bored enough to get a bot to say hi?", color=0x5733FF)
      await message.channel.send(embed=embed, delete_after=1)



      ballof8=discord.Embed(title="Help",  description=random.choice(ball), color=0x5733FF)
      await message.channel.send(embed=ballf8)


  



  
    

  


 





keep_alive()
client.run('ODkzODI2OTY3MDU5NzEwMDAz.YVhHOw.2AdtGptVqHK-6jd05jxrY-rykT4')