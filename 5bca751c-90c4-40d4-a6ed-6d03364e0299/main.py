import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=')

bank = dict()


@bot.event
async def on_ready():
    print('Ready to rock')


@bot.command()
async def money(ctx):
    if ctx.author not in bank:
        bank[ctx.author] = 0
    await ctx.send(f'{ctx.author} has {bank[ctx.author]} spacebux')


@bot.command()
async def earn(ctx):
    if ctx.author not in bank:
        bank[ctx.author] = 0
    bank[ctx.author] = bank[ctx.author] + 1
    await ctx.send(
        f"{ctx.author} you've earned money! You now have {bank[ctx.author]} spacebux"
    )

@bot.command()
async def spend(ctx):
  if ctx.author not in bank or bank[ctx.author] == 0:
    await ctx.send(f'{ctx.author} you have no spacebux to spend :(')
  else:
    bank[ctx.author] = bank[ctx.author] - 1
    await ctx.send(f'{ctx.author} you spent 1 spacebuck. You now have {bank[ctx.author]} spacebux')

bot.run(os.getenv('TOKEN'))
