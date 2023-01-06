import discord
from discord.ext import commands
import random
import asyncio
from webserver import keep_alive
import os

description = '''IAJ's New Bot - Still in testing

Here are some commands:'''
bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    activity = discord.Game(name="Testing")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('Prefix Changed.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
    
@bot.command(name = 'stop', aliases = ['s'], help = 'Stops the bot')
async def stop(ctx):
    await bot.close()
    
@bot.command(name = 'pp', aliases = ['p'], help = 'pp')
async def pp(ctx):
    await ctx.send('8=========>')
    
@bot.command(name = 'staff', aliases = ['f'], help = 'Shows Staff members')
async def staff(ctx):
    await ctx.send(' Owner: Minty, Bot Design/Dev: IAJ, Thumbnail Design MeNameIsDeku, Staff: georgepig_oink9')

@bot.command()
async def kick(ctx, userName: discord.User):
    """Kicks a member."""
    if ctx.message.author.server_permissions.administrator:
        await BSL.kick(userName)
    else:
        permission_error = str('Sorry ' + ctx.message.author + ' you do not have permissions to do that!')
        await BSL.send_message(ctx.message.channel, permission_error)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
    
@bot.group()
async def hello(ctx):
    """Says Hi. Usage $hello me / $hello name.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('Hello to {0.subcommand_passed}!'.format(ctx))
    bot.add_cog(Test(Hi))

@hello.command(name='me')
async def _me(ctx):
    """Is the bot cool?"""
    await ctx.send('Hello you!')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    
@cool.command(name='IAJ')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, IAJ is cool.')
    
@cool.command(name='Minty')
async def _M(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, Minty is cool.')

@bot.command(name = 'restart', aliases = ['r'], help = 'Restarts the bot')
async def restart(ctx):
    await ctx.send('Restarting...')
    await bot.close()
