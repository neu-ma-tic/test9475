import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('hm'):
    await message.channel.send('thích '+ message.content +' ko?')
    await message.channel.send('đấm cho cái giờ')
  if message.content.startswith('?'):
    await message.channel.send('._.')
  if message.content.startswith('hello'):
    await message.channel.send('hello anh bạn')
  if message.content.startswith('?help'):
    await message.channel.send('công trình đang thi công, không phân sự miễn vào')
  if message.content.startswith('ok'):
    await message.channel.send('ô cê')
  if message.content.startswith('ha'):
    await message.channel.send('hihihihihihihihihihi')
    

  

client.run(os.getenv('TOKEN'))


