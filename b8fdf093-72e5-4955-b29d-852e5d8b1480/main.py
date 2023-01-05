import discord
from discord.ext import commands
import music

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup()


client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

client.run("ODg4ODEyNTg0NjA4ODc0NTU3.YUYJOQ.3uUWnJuANXxyU7WiSDDUQyV8PAU")