import discord
from discord.ext import commands
from music_cog import music_cog
from host import alive

Bot = commands.Bot(command_prefix='$')
Bot.add_cog(music_cog(Bot))



@Bot.event
async def on_ready():
    Bot.remove_command("help")
    await Bot.change_presence(activity=discord.Game('Zeytin | $Help'))

token = 'OTExMTgwNDMwOTUzMzA4MTgw.YZdo5w.PGqLIlh0fn5HA4hbWDWKzD86uUA'

alive()
Bot.run(token)