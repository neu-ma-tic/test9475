import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTM0OTA0NTc3MDg0NTAyMDc3.Ye23vA.X5lLtRCNfIe_9kgkqkp9ZqsMn0A")