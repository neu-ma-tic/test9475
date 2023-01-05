import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


client = discord.Client()
my_secret = os.environ['TOKEN']
client = commands.Bot(command_prefix = '!') 

@client.event
async def on_ready():
    print("bot online") 
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!halo'):
    await message.channel.send('HALO XD')

  if message.content.startswith('!dywizja'):
    content = message.content
    await message.channel.send('plat')
  


@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.command()
async def play(ctx, url : str):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="test")
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()

client.run(os.getenv('TOKEN'))