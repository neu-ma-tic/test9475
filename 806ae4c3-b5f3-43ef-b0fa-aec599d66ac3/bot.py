import discord, json, time, asyncio
import random, os, string
import requests, aiohttp, datetime
from discord.ext import commands
from discord import Game, Embed, File

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = config.get("prefix")
RPC = config.get("RPC")

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Im alive bitch")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(RPC))

@bot.event
async def on_command_error(error, ctx):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send("Missing Required Arguments")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!\nLatency: {bot.latency}")

@bot.command()
async def geoip(ctx, *, ipaddr: str = '9.9.9.9'): 
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'IP Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IP Name', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.set_footer(text='\u200b')
            em.timestamp = datetime.datetime.utcnow()
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@bot.command()
async def pingweb(ctx, website = None):
    if website is None: 
        await ctx.send("No website was introduced")
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"[ERROR]: {e}")
        if r == 404:
            await ctx.send(embed=discord.Embed(title='Site is down',description=f'Responded with a status code of {r}'))
        else:
            await ctx.send(embed=discord.Embed(title='Site is up',description=f'Responded with a status code of {r}'))    

@bot.command()
async def fake_ddos(ctx):
    await ctx.message.delete()
    messageddos = await ctx.send(":skull_crossbones: DDOS ATTACK STARTED...:skull_crossbones:")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓░░░░░░░░░░░░░░░░░░░░░░ 10%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓░░░░░░░░░░░░░░░░░░░░ 20%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░ 30%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░ 40%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░ 50%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░ 60%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ 70%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ 80%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ 90%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░ 93%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 97%")
    await asyncio.sleep(2)
    await messageddos.edit(content="▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100%")
    await asyncio.sleep(2)
    await messageddos.edit(content=":skull_crossbones: __**TARGET STATUS : OFFLINE**__ :skull_crossbones:")

bot.run(token)