import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix = '.')
 
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
  print('Ready')  
 
client.run('ODYwMTcxMDQ4NDgxNDU2MTI4.YN3Wtw.0ffNZ8wzeANFvd7ixLYMD0v2ujI') 