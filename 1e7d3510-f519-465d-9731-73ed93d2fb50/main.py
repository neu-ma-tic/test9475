import os
# Allows own configuration loading
from dotenv import load_dotenv

# Handles Discord API
# to migrate to nextcord soon
# https://github.com/nextcord/nextcord
import discord
from discord.ext import commands

# Cogs category for the commands
from Greetings import Greetings

# Handles remote mysql handling
import mysql.connector as mysql

# Miscellaneous
import random


# set bot activity
# activity = discord.Activity(type=discord.ActivityType.watching, name="owl#0614 working on this")
activity = discord.Game(name="@owl#0614")

# set up intents to include all
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', activity=activity, status=discord.Status.idle, intents=intents)

import keep_alive
keep_alive.keep_alive()
    
load_dotenv()

# Discord credentials
TOKEN = os.getenv('DISCORD_TOKEN')
SYMBOL = os.getenv('DISCORD_SYMBOL') # $

# Remote MySQL credentials
HOST = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')


## Database no longer working
# db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# print("Database connected. Server info:", db_connection.get_server_info())

# client = discord.Client()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# # DOC: For each event (messages sent by the user), recognise if any of the words
# # in hello_words list is mentioned and respond with message.
# hello_words = ['hello', 'hi']
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     for word in hello_words:
#       if word in message.content.lower():
#         await message.channel.send('Hello!!')
#     # if message.content.startswith(SYMBOL + 'hello'):
#     #     await message.channel.send('Hello!')


# COMMANDS
@bot.command(name='mhi', help="Shows message of more hi")
async def more_hi(ctx):
  response='More hi is good.'
  await ctx.send(response)

# @bot.command(name='echo')
# async def echo(ctx, msg: str):
#   await ctx.send(msg)

@bot.command(name='roll', help='Rolling a die, state number of dice rolls and number of sides')
async def roll(ctx, dice_number: int, sides: int):
  dice = [str(random.choice(range(1, sides + 1)))
  for _ in range(dice_number)]
  await ctx.send(', '.join(dice))


# There is unhandled Exception
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhanddb["key"] = "value"led message: {args[0]}\n')
        else:
            raise


# register cogs
bot.add_cog(Greetings(bot))

# client.run(TOKEN)
bot.run(TOKEN)