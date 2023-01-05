
import discord
from discord.ext import commands
import json
import random
import keep_alive

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='::', intents=intents)


@bot.event
async def on_ready():
    print(">> bot is online <<")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(876769608080703500)
    await channel.send(f'{member}歡迎光臨!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(876769608080703500)
    await channel.send(f'{member}歡迎再度光臨!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata["pic"])
    await ctx.send(random_pic)


keep_alive.keep_alive()
bot.run(jdata["token"])
