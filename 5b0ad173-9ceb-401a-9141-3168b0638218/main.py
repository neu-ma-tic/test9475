import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = 
discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run
("OTAxNDc1MzQ0OTAzNzI5MTgz.YXQaVg.w3UpZhtrKR72xkJB-xbPLeisqoU")