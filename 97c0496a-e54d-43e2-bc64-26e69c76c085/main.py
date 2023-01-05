import flask
import discord
import datetime, re
import json
import urllib.parse
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import base64
import time
import datetime
import random
import typing
import sys
import signal
import re
import aiohttp
import os
import logging
import json
import requests
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='>', description='?')

@bot.event
async def on_ready():
	print(f"{bot.user.name}")
	print("I'm ready")
	await bot.change_presence(activity=discord.Game(name='Eliatopia'),afk = False)

@bot.event
async def on_disconnect():
  print("ONLINE....")

def is_owner():
    def predicate(ctx):
        return ctx.message.author.id == 707011430406422538
    return commands.check(predicate)


@bot.command(pass_context = True, aliases=['sg'])
@is_owner()
async def setgame(ctx, *, game: str):
	try:
		await bot.change_presence(activity=discord.Game(name=game), status=ctx.message.guild.me.status)
		logging.info("Set game to " + str(game))
		await ctx.channel.send("New Status was succesfully set!")
	except Exception as e:
		print( {}.format(str(e)) + "\n lol")

@bot.command(pass_context = True, aliases=['rg'])
@is_owner()
async def resetgame(ctx):
	await bot.change_presence(activity=discord.Game(name='Eliatopia'), status=ctx.message.guild.me.status)
	await ctx.channel.send("My status was succesfully reseted!")

#a simple calculator
#num1 = float(input("tell me a number \n Number here :  "))
#op = input("tell me a operator \n Operator here :  ")
#num2 = float(input("tell me another number \n Number here :  "))

#if op == "+":
 # print(num1 + num2)
#elif op == "-":
  #print(num1 - num2)
#elif op == "/":
  #print(num1 / num2)
#elif op == "*":
  #print(num1 * num2)
#else:
  #print("num1 * num2")
  

keep_alive()
#bot.run('OTU5NDg3MTE4NzM5MTE2MDYy.YkcmAw.KeT5oyR3wth5vXX31LYG29salT4')