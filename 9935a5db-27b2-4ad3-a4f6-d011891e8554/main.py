import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print('Bot is ready.')

thumbnail_help = "https://i.pinimg.com/originals/ef/70/fd/ef70fd2bc2611118d5ff25f3ff65d1e2.png"

@client.command()
async def help(ctx):
    embed = discord.Embed(title="A2 Bot Help", description = 'hshsd', thumbnail = "https://i.pinimg.com/originals/ef/70/fd/ef70fd2bc2611118d5ff25f3ff65d1e2.png"

client.run(os.getenv('TOKEN'))