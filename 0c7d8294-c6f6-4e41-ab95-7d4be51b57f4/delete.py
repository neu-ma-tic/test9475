import discord
import os
from discord.ext import commands
client = discord.Client()

client = commands.Bot(command_prefix ='.')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def clear(ctx ,amount=100):
  await ctx.channel.purge(limit=amount)

client.run(os.getenv('TOKEN'))