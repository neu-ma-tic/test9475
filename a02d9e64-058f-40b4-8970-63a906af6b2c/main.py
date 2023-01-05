import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix=';;;', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("ODM4OTUzNTcyMjI5MDU0NDc1.YJCmZg.9glRueFakWPNEUNyS0qMJ3KC6As")