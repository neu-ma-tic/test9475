import discord
from discord.ext import commands
import random
import webserver
from webserver import keep_alive
import os

client = commands.Bot(command_prefix='#')


@client.event
async def on_connect():
	await client.change_presence(
	    activity=discord.Streaming(
	        name="maintence", url="https://www.twitch.tv/ninja"))


@client.command()
async def ping(ctx):
	await ctx.send(f'{round(client.latency * 1000)} ms')


@client.command(aliases=['8ball', '8'])
async def _8ball(ctx, *, question):
	responses = ['idc.', 'wdym?', 'yes.', 'no.', 'alright', 'ok', 'yes, i am!']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")
      
      
webserver.keep_alive()
client.run(os.getenv("TOKEN"))