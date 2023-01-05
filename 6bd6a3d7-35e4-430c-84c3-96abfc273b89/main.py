import keep_alive
import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import music


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')


#cogs = [music]

client = commands.Bot(command_prefix='$')
status = cycle(['המשרת', 'הנאמן'])
#for i in range(len(cogs)):
    #cogs[i].setup()

client = discord.Client()




@tasks.loop(seconds=2.5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))  

#@client.event
#async def on_ready():
   #activity = discord.Game(name="Netflix", type=3)
   #await client.change_presence(status=discord.Status.online, activity=activity)
  # print("Bot is ready!")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$אהלן'):
   await message.channel.send('מה הולך! כל פקודה אצלי מתחילה ב$')


  if message.content.startswith('$קישור'):
   await message.channel.send('הקישור של השרת:https://discord.gg/ew88dsMhem')


  if message.content.startswith('$עזרה'):
   await message.channel.send('בדיקה') 



keep_alive.keep_alive()
client.run('ODg5OTkxMzUyNzE5NDA5MjAy.YUpTCQ.Jbv19Fouq9DPSvDBjeiWK_Ym4Kk')
