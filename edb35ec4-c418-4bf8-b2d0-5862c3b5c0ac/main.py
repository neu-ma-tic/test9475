import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from replit import db
default_prefix = '/'
botowner = 756837435186610177, 613339769836929034


#debug -----------
del db["prefix"]
#-----------------




try:
    prefix = db["prefix"]
except KeyError:
    prefix = default_prefix
    db["prefix"] = prefix



client = commands.Bot(
    command_prefix = prefix,
    help_command = None
)


@client.event
async def on_ready():
    print('Der Bot ist nun Online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        print(f'>> {message.content}')
        return
    print(f"[{message.channel}] ({message.author}) {message.content}")
    if message.content.startswith(f'{prefix}{prefix}'):
        if message.author.id == botowner:
            if message.content.startswith(f'{prefix}{prefix}json'):
                await message.channel.send(f'botowner send: {message.content}')
                return
    if message.content.startswith(f'{prefix}'):
        await message.channel.send(f'{message.content}')
    



@client.command(
    name= 'ping',
    alias= []
)
async def ping(ctx: Context):
    await ctx.channel.send(f':ping_pong: Pong für {ctx.author.mention}:ping_pong:')











TOKEN = os.environ['TOKEN']
client.run(TOKEN)