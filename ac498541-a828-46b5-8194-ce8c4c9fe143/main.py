import discord 
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)




client.run("ODk4NDg0OTYxMTYwNTk3NTY0.YWk5Uw.HyaYJ9QcmpvSNVd7zQ8QQCZH8qk")