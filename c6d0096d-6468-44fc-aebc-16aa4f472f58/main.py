import discord
from discord.ext import commands
import music

cogs = [music]

client =commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTQ5NTk0MTY5MTkyNjIwMDUy.YiMofA.IEJVr4qf7D3zjA_j-_Qv54BJH9Y")