from replit import db
from keep_alive import keep_alive
import os
import discord
import time
import random
import json
import requests

number = 0
client = discord.Client()
repeat_number = 1
repeat_number2 = 0
repeat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
def get_quote():
  response = requests.get ("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event 
async def on_message(message):
  repeat_number = 1
  repeat_number2 = 0
  number = 27000 
  count_number = 0
  if message.author == client.user:
    return

  msg = message.content
  if "responding" not in db.keys():
    db["responding"] = True

  if msg.startswith('$count'):
    while count_number < 1:
      
       await message.channel.send(number)
       time.sleep(1)
       number +=1
  if msg.startswith('$shut'):
    count_number += 2
    await message.channel.send(count_number)
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
   
  
 

        
  if msg.startswith('$hello'):
    await message.channel.send('elpepeisgudgejm :poop:')
  if msg.startswith('$help'):
    await message.channel.send('no :middle_finger:')
  if msg.startswith('$imdepressedmf'):
    await message.channel.send('idc :exploding_head:')
  if msg.startswith('$fucku'):
    await message.channel.send('NO U BITCH SUCK MY DICK MOTHERFUCKER :middle_finger:')
  if msg.startswith('$heheboi'):
    await message.channel.send('no :french_bread:')
  if msg.startswith('$repeat'):
    repeat_number2 = random.choice(repeat)
    while repeat_number2 > repeat_number:
      await message.channel.send('gudgejm')
      time.sleep(1)
      repeat_number += 1 

      
  


  
keep_alive()
client.run('ODM1OTAzNjUyMzU0NTg4NzI1.YIWN8Q.CzaCG614VcEVLo0eJeHBX99y-3Y')
