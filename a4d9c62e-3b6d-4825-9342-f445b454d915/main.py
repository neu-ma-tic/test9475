import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTIxMzk4NzExOTg3MzM5MjY2.YbyVaw.LKmoZfGKBmH5uKJ0GdWHMPoB9tY")