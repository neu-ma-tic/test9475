import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run
("MTAzOTQ1Mzg0NzMyOTk4NDU0Mg.GatC3u.xdwi8dL1Vr96CX7YVhgS8g_Wudxtji_ZhqImeY")