import os
import discord
from discord.ext import commands

def encryptMessage(message):
  print (message)

#Line 6 is the prefix that your bot will use
bot = commands.Bot(command_prefix='.')
client = discord.Client()

'''The following Function gets called when the bot gets initiated'''
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="ping", help="pong")
async def ping(ctx):
  await ctx.send("pong")

'''The Following fuction is for the Encrypt Command'''
@bot.command(name='encrypt', help='Encrypt a message.  ', pass_context=True)
async def encrypt(ctx, msg: str):
  print (msg)
  #Deletes the original message
  await ctx.channel.purge(limit=1)
  encryptMessage(msg)


  #Content of the message is stored in msg as a string
  '''Write Code to Encrypt the string stored in msg'''
  BotMessage = await ctx.send("Send the Encrypted Message")

  

my_secret = os.environ['token']
