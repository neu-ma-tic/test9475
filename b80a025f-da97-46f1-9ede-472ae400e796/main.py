import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  



keep_alive.keep_alive()
token = os.environ.get("token")
client.run(token)
























