import discord
import os
import random
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == ('-kunalrao'):
        await message.channel.send('https://cdn.discordapp.com/attachments/771136346353958912/802345784128438272/unknown.png')
    if message.content == ('-cry'):
        await message.channel.send('https://tenor.com/view/crying-black-guy-meme-sad-gif-11746329')
    if message.content == ('-laugh'):
        await message.channel.send('https://tenor.com/view/laugh-laughing-zias-blou-drole-gif-10342469')
    if message.content == ('-discord'):
        await message.channel.send("https://discord.gg/5Vg9cFQhQu")
    if message.content == ('-randomnumber'):
        await message.channel.send(random.randint(0, 100))
    if message.content == ('-commands'):
        await message.channel.send("prefix is - \nlaugh \ncry \nrandomnumber \ndiscord \nbestrapper ")
    if message.content == ('-bestrapper'):
        await message.channel.send("https://tenor.com/view/young-chop-chief-keef-trap-rap-type-beat-gif-14623876")
    if message.content == ('!corona'):
      while True:
        await message.channel.send("nigg@")
    if message.content == ('!crash'):
      while True:
        await message.channel.send("nigg@")
    if message.content == ('!crashing'):
      while True:
        await message.channel.send("ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy ayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy \nayy ")
      
        

      
        
        

       
    
    
    
    
    
    
    


client.run(os.getenv('TOKEN'))
