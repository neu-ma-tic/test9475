import discord
from discord.ext import commands
import os
import random
import json
import time
import urllib.request


client = commands.Bot(command_prefix = '>')

illegal_words = [":stuck_out_tongue:", ":smiling_face_with_3_hearts:", ":kissing_heart:"]


@client.command()
async def join (ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("sorry")

@client.command()
async def compliment(ctx):
  url = "https://complimentr.com/api"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  #engine = pyttsx3.init()
  #engine.say(data['compliment'])
  #engine.runAndWait() 
  await ctx.send(data["compliment"])

@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        #channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def k(ctx):
  line = ":kissing_heart:"*10+"."
  await ctx.send(line)
  time.sleep(2)
  await ctx.channel.purge(limit = 2)

@client.event
async def on_ready():
  print('Bot is ready.')

@client.command()
async def c(ctx, amount= 100):
  await ctx.channel.purge(limit=amount,check=lambda msg: not msg.pinned)

#@client.command()
#async def d(ctx):
#  await ctx.channel.purge(limit = 100,check= (ctx.message.content.contains == illegal_words)) 

my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))