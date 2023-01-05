import discord
from discord.ext import commands

TOKEN = "MTAzOTc1ODAxNDQzMDg0NzA0Nw.G4f9fF.KOeuiwVXNCV63sh6Y1o7CEk4UB4wW-6ARXDnA0"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

#####
#####
## Insert other functions here
#####
#####

client.run(TOKEN)