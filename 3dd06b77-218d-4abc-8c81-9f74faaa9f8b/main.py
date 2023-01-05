

import discord
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        

client.run('ODcxMDIxMjE3NjIzMTkxNjAz.YQVPuQ.p7-mKL5sGxqmuHs3M21eTlJSmds')