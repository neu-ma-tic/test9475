import discord
import os
import random
import asyncio
from discord.ext import commands

list1 = ["Jp Suck My Dick", "JP CAN SUCK MY HAIRY BALLS", "JP FUCK YOU", "JP EAT MY DICK", "JP SUCK ME OFF", "JP EAT A DICK", "JP YOU DID GOOD I GUESSS FOR A GUY WITH A SMALL DICK","https://www.youtube.com/watch?v=jsVJ8x8INqc&feature=youtu.be"]
tommy_list = ["Suck My Dick", "CAN SUCK MY HAIRY BALLS", "FUCK YOU", "EAT MY DICK", "SUCK ME OFF", "EAT A DICK", "YOU DID GOOD I GUESSS FOR A GUY WITH A SMALL DICK", "STFU","https://www.youtube.com/watch?v=jsVJ8x8INqc&feature=youtu.be"]

#Initialize
client = commands.Bot(command_prefix = '-')
my_secret = os.environ['TOKEN']
audio_source=discord.FFmpegPCMAudio('omgstfu.mp3')
players={}

@client.event
async def on_ready():
  print('Bot Online')

@client.command()
async def hello(ctx):
  await ctx.send('Hello {0.display_name}.'.format(ctx.author))
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.event
async def helloworld(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    
    await ctx.send('Hello World!')
async def leave(ctx):
    await ctx.voice_client.disconnect()
    


##212662759094091777 Donovan
##407302203070742529 JP
##212635381391294464 CJ
##212618755921018880 Frank
##209477219158982658 Tommy

@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith('LHi'):
    for x in range(10):
      await message.channel.send("Die!")
    await message.channel.send("HAHAHAHAHHAA")


client.run(os.environ['TOKEN'])