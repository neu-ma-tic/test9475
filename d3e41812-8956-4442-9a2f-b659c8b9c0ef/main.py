import discord
from discord.ext import commands
import music

cogs = [music]

_token = 'OTEzNDA5MzczMDMwNzM1ODky.GNf9u1.DzOAfPZBGMr1l_6WUCwZj3uq0oMiA4S-zE_jD8'

client = commands.Bot(command_prefix='/', intents = discord.Intents.all())

for cog in cogs:
	cog.setup(client)

client.run(_token)
print('running')