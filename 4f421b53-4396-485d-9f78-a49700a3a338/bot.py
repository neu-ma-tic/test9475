import discord
from discord.ext import commands,tasks
import os
from itertools import cycle



status = cycle(['altitude smp','fakeman sucks'])
client = commands.Bot(command_prefix = '>')

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    change_status.start()
    print("bot rdy")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status = discord.Status.dnd, activity=discord.Game(next(status)))


if __name__ == '__main__':
    client.run('OTgyOTg5MTMzNDg2MTIxMDIw.Goelag.iKd2T0BH7cMgsBS4MRAUyVMt_8OIXx-a_rZ52Q')