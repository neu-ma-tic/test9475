import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.bot(commands_prefix='-',intents = discord.intents.all())

for i in range (len(cogs)):
  cogs[i].setup(client)


client.run("ODg2OTk2MTk2Njg0NjA3NTc5.YT9tlA.Yb8-jjOFwRCswSAaZON23XE4DAg")