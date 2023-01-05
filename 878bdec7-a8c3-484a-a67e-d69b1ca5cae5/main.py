import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
  print('Ready!')

@client.command()
async def clear(ctx, amount: int):
  await ctx.channel.perge(limit = amount)
