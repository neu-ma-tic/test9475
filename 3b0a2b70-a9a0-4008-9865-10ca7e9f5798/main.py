import discord
from discord.ext import commands
import music

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup()




client = commands.Bot(command_prefix='?p', intents = discord.Intents.all())

client.run("ODg5NjM1Nzk1ODk0NDA3MTg1.YUkH5g.LfcX3ljUV6x_RSUTATRe0H3ltQA")