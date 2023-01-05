import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODkzMDc0OTM0NTcyNjU0NjQz.YVWK2A.jjK5PEmmhsA-zQbjigY9zIE0ayU")