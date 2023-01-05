import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
  print('O Bot funciona')

@client.event
async def on_member_join(member):
  print('{member} está no server')

@client.command()
async def teste(ctx):
  await ctx.send('Olá')



client.run('ODQyODIzNTg5NDY3NTIxMDY0.YJ66og.sdfei1Tsf9TWqt7WKnVow_iavQs')