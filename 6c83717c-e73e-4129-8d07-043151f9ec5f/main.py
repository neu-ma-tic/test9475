import discord
from discord.ext import commands
import music

#add cogs here
cogs = [music]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

#setup all cogs
for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTM2ODY4NzgxNDA0MzQwMjU0.YfTdCw.PCE-GQg7_NPaFIpxZXnD7S8dR8k")