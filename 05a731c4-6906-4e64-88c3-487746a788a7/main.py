import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix='-')
client.remove_command('help')

TOKEN = " NjY5NjAwMzMyNjQ0NjE0MTY0.XiiMEw.de5XkZs8DUARsLYdisjesMM-Q68" # Bot Token

@client.event
async def on_ready():
  print('Bot Is Online')
  await client.change_presence(status=discord.Status.online, activity=discord.Game("מולך על החנונים"))

@client.command(pass_context=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f' 😎מחקתי {amount} הודעות 😎') 


@client.command()
async def say(ctx, *, msg):
  await ctx.message.delete()
  await ctx.send(msg)


#keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
#client.run(TOKEN)
client.run(TOKEN)
