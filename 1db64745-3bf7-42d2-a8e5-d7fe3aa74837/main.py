import discord
from discord.ext import commands
import os
from discord.ext.commands import has_permissions
import keep_alive
import time
import random

TOKEN = os.environ['token']
client = commands.Bot(command_prefix ='t$ ')
client.remove_command('help')



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="t$"))
  print('Bot ready')

@client.command()
async def weee(ctx):
  await ctx.send(" :man_cartwheeling: WEEEEEEE \n\n                     :man_golfing: ")

@client.command()
async def amogus(ctx):
  await ctx.send("ඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\nඞ sussy baka\n")

@client.command()
async def ping(ctx):
  await ctx.send(f"Ping: {round(client.latency * 1000)}ms")

@client.command()
async def help(ctx):
  await ctx.send('>>> Help/Commands:\nping - Bot Latency\nban - bans the user (use @ mentions for the user that you want to ban)\nclear - clears the selected amount of messages\nclearall\n===============Fun===============\nweee - UMMM\namogus - sus\n\n\n==============Other==============\nYoutube\n')

@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

@client.command()
@has_permissions(manage_messages=True)
async def clearall(ctx):
  await ctx.channel.purge(limit=99999999999999999999999999999999999)

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member):
  await member.ban(reason="The Ban Hammer Has Spoken")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
  await member.kick(reason="The Ban Hammer Has Spoken")

@client.command()
async def youtube(ctx):
  await ctx.send("https://www.youtube.com/channel/UC0gi9wS1G4wcmFfm_feqCwQ\nhttps://youtube.com/channel/UCTmP_QSDQdJRlCAMOPvhtjg")


@client.command()
@has_permissions(manage_messages=True)
async def count(ctx,arg,arg1):
  for i in range (int(arg1)):
    arg = int(arg)
    arg += 1
    await ctx.send(arg)



client.run(TOKEN)