import discord
from discord.ext import commands
import music 

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range (len(cogs)):
  cogs[i].setup(client)



client.run("ODkyMjA4NDU4NzcyOTE4MzMy.YVJj4Q.fFl_NWgu4ZwsLFotG7kJnYT3Zgs")