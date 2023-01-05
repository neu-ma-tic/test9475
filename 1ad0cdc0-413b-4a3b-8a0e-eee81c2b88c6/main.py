import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')

client.lava_nodes = [{
    'host': 'lava.link',
    'port': '80',
    'rest_url': 'http://lava.link:80',
    'identifier': 'MAIN',
    'password': 'anything',
    'region': 'eu'
}]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))
    print('Bot is ready')




@client.command()
async def load(ctx, ext):
    client.load_extension(f'cogs.{ext}')


@client.command()
async def reload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')
    client.load_extension(f'cogs.{ext}')
    print(f'{ext} cog has been reloaded')


@client.command()
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')


for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

keep_alive()
client.run('ODg4MzM0MDY3NDUwMzg4NDkx.YURLkg.IZDVaHhDyf75n7bCAAZc1FoDJL4')
