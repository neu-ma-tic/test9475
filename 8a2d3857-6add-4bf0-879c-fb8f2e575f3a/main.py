import discord
from discord.ext import commands
import os
import random


client = discord.Client()

@client.event
async def on_ready():
  print("Yaşıyoruz Baba {0.user}".format(client) )

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('sa'):
    await message.channel.send('as')

  if message.content.startswith('serdar'):
    a = random.randint(1,7)
    if a == 1:
      await message.channel.send('serdarın götünü sikiyim')
    elif a == 2:
      await message.channel.send('serdarın amcıgını sikim')
    elif a == 3:
      await message.channel.send('serdarın kollarını sikiyim')
    elif a == 4:
      await message.channel.send('serdar blowjob yapıyor müsait değil şu an')
    elif a == 5:
      await message.channel.send('serdar duşta aşko')
    elif a == 6:
      await message.channel.send('serdar şu an e5 te müşteri bekliyor')

@client.event
async def play(message):
  if message.startswith("-c "):
    await message.channel.send("Playing...")
    message.split(" ")
    message.pop(0) #-c yi sildim
    


client.run("Nzk0OTA4NTAzODYwMDUxOTY4.X_BqPA.39SwBOgYOf2_Chh-nBJ2bH0IcXw")
