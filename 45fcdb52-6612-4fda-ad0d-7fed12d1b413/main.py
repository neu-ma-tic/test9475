import discord
from discord.ext import commands
import os
import time
from keep_alive import keep_alive




bot = commands.Bot(command_prefix = "<",case_insensitive = True)

@bot.event
async def on_ready():
    print('Ready!')

@bot.command()
async def ping(ctx):
  await ctx.send('pong')

@bot.command()
async def clear(ctx,number):
  await ctx.channel.purge(limit = int(number)+1)



keep_alive()
bot.run(os.getenv('TOKEN'))