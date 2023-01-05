import discord
from discord.ext import commands, tasks 
import os

secret = os.environ['TOKEN']

intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'bday ', intents = intents)

@client.event
async def on_ready():
  print(client.get_channel(817774268586000387))
  print('We have logged in as {0.user}'.format(client))
  # send_periodic_message.start()
    


# @tasks.loop(seconds=10)
# async def send_periodic_message():
#   await client.get_channel(840257250483372105)


client.run(secret)