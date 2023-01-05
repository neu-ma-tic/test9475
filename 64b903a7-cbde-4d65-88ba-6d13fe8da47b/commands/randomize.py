import discord

from discord.ext import commands
from random import randint, choice


class Randomize(commands.Cog, description='Commands to randomize'):
    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @commands.command(description='Choose randomly from a given range', help='rdrange <first> <second>\nEg: t.rdrange 1 100')
    async def rdrange(self, ctx: commands.Context, first: str, second: str):
      if not first.isdigit() or not second.isdigit():
        return await ctx.send('Please provide 2 integers')
      if int(first) > int(second):
        return await ctx.send('Please make sure first number less than or equal to second number')
      return await ctx.send(randint(int(first), int(second)))

    @commands.command(description='Choose randomly from a given list', help='rdchoice [list of choices]\nEg: t.random urmomfat urmomgay')
    async def rdchoice(self, ctx: commands.Context, *choices: tuple):
      return await ctx.send(choice(choices)[0])

    @commands.command(description='Do a coin flip', help='coinflip')
    async def coinflip(self, ctx: commands.Context):
      coin = randint(0, 1)
      if coin:
        return await ctx.send("***HEAD***", file=discord.File('images/coin/head.png'))
      return await ctx.send("***TAIL***", file=discord.File('images/coin/tail.png'))