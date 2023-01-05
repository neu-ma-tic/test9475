import discord
import youtube_dl
import os
import asyncio
import urllib.parse, urllib.request, re
from discord.ext import commands
import time

import discord
from discord.ext import commands
import bot_commands

client = commands.Bot(command_prefix = "!")
TOKEN = "OTMzMTIyNjcxODYzMDIxNjA4.Yec8NQ.hRsw5O8-W6LHi4XCNgd68VtAyTg"
processing = 0

@client.event
async def on_voice_state_update(member, before, after):
  await bot_commands.on_voice_state_update(member, before, after, client)

@client.command()
async def hello(ctx):
  await bot_commands.hello(ctx)

@client.command()
async def commands(ctx):
  await bot_commands.commands(ctx)

@client.command()
async def join(ctx):
  await bot_commands.join(ctx, client)

@client.command()
async def leave(ctx):
  await bot_commands.leave(ctx, client)
  
@client.command()
async def pause(ctx):
  await bot_commands.pause(ctx, client)

@client.command()
async def play(ctx, *, name):
  await bot_commands.play(ctx, name, client)

@client.command()
async def queue(ctx):
  await bot_commands.queue(ctx)

@client.command()
async def stop(ctx):
  await bot_commands.stop(ctx)

@client.command()
async def skip(ctx):
  await bot_commands.skip(ctx, client)

client.run(TOKEN)