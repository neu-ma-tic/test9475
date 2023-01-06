import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix = '?',intents = discord.intents.all())
for i in range(len(cogs)):
  cogs[i].setup(client)
  





client.run("ODkwODE2MTgxMzM2OTM2NDY4.YU1TOA.TMYigqp5z3q9O5G-pVVwsgM69hk")