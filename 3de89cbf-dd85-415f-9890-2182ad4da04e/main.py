import os
import discord 
from discord.ext import commands
from keep_alive import keep_alive
import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print("BOTUL TRAIESTE:")
  print(client.user)
  await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name='ESC.COM'))

@client.event
async def on_member_join(member):
  print(f'{member} A INTRAT PE SERVER.')

@client.event
async def on_member_remove(member):
  print(f'{member} A IESIT DE PE SERVER.')

@client.command()
async def Ping(ctx):
  await ctx.send(f'Pong: {round(client.latency * 1000)}ms')

@client.command()
async def Info(ctx):
  await ctx.send(f'CREATOR: EMANUEL STROIA CRISTIAN | TYPE: DISCORD.PY | HOST: REPL.IT')

@client.command()
async def HELP(ctx):
  await ctx.send(f'COMENZI:')

@client.command(aliases=['8ball', 'Salut'])
async def _8ball(ctx, *, question):
  responses = ['TEXT']
  await ctx.send(f'INTREBARE: {question}\nRASPUNS: {random.choice(responses)}')

@client.event
async def on_message(message):
 if "pizda" in message.content:
    await message.channel.send("PIZDA!? Unde? O spus cineva PIZDA? VREAU...")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)