import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix = '!')
 
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('https://discord.com/invite/beamcookies"'))  
  print('Ready')  
 
client.run('ODYyNjYxMjUzMzczNDkzMjg4.YObl5g.cHvXFt1SZ0YIBxI0e4HUsZvMC6w') 