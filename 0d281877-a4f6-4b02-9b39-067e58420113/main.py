import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?' , intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup()

  

client.run("OTkzNDY4NDUwNDAxOTQzNTYy.GUKW4N.SrdVh1laQAExjT78vBrDKY3Et8XOAqPe4qN2W4")