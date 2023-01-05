import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix=".", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)



client.run("ODkyODIxNDc5NzUyODg4NDAw.YVSezA.2O8cgklWx921wJfeZYC8d7libN8")