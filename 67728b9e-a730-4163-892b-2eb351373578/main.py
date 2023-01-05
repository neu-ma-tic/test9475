import discord
from discord.ext import tasks
from commands import commandList
from webserver import keep_alive

import os
import datetime

client = discord.Client()

async def nöt(message):
  await message.channel.send("nej du är nöt")

async def fuck(message):
  await message.channel.send("sådär kan du inte säga det finns småbarn här")

async def tyst(message):
  await message.channel.send("grabben ovanför är en bitch")

async def onWrongCommand(message, command):
  await message.channel.send(f"'{command}' is not a recognized command, please type '!help' for a full list of commands.")

@client.event
async def on_message(message):
    if message.author != client.user:

        words = message.content.lower().split()

        if len(words) < 1:
          return
        
        if words[0].startswith("!"):
          if words[0] in commandList:
            await commandList[words[0]]["Func"](message)
          else:
            await onWrongCommand(message, words[0])
        else:

          if "nöt" in words:
            await nöt(message)

          if "fuck"in words or "bitch" in words:
              await fuck(message)

          if "tyst" in words or "sämst" in words:
              await tyst(message)

@tasks.loop(seconds=1)
async def send_message():
  channel = client.get_channel(942377314149343332)
  time = datetime.datetime.now()
  if time.hour == 3 or time.hour == 15:
    if time.minute == 20 and time.second == 0:
      await channel.send("420")

@client.event
async def on_ready():
    send_message.start()
    print("mary im ballin")
        

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)