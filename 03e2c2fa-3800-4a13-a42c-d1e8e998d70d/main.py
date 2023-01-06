import discord
import os
import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
import pytz
import datetime

bot = discord.Client()
client = commands.Bot(command_prefix="!")
status1 = cycle(["Created by UrbanXD", "Offical Bot of CSSOS"])
client.remove_command("help")

@client.event
async def on_ready():
    change_status.start()
    client.load_extension(f'cogs.idonaplo')
    print("A BOT elindult! Illetve az idonaplo COG betoltve")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(
        status=discord.Status.idle, activity=discord.Game(next(status1)))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Nem letezik ez a parancs! Hasznald a !parancsok parancsot, hogy további segítséget kapj.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hianyzo ertekek!")


@client.command(name='ping',description="The ping command")
async def ping(ctx):
    await ctx.send(f"Pong!")


@client.command()
async def parancsok(ctx):
    embed = discord.Embed(
        title="Parancsok",
        description="A következő parancsok érhetőek el a szerveren:",
        color=0x005bbd)
    embed.add_field(
        name=" !parancsok", value="Parancsok listázása", inline=True)
    embed.add_field(name="!belepes", value="Szolgálatba lépés", inline=True)
    embed.add_field(
        name="!kilepes", value="Szolgálatból való kilépés", inline=True)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print("Loaded")

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print("Unloaded")

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    print("Reloaded")

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)
