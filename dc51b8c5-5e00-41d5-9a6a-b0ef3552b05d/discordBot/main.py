import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from keep_alive import keep_alive
import time


client = commands.Bot(command_prefix = ':')
token = 'ODI0MDA4MzA5NTM4NDIyODc2.YFpHig.vUlsPwVPGFU0RCPVnLLwACduQgg'
ballsURL = 'https://www.youtube.com/watch?v=WmvQKGsARAk&ab'

players = {}

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def devon(ctx):
    await ctx.send('I fucking hate Devon.')

@client.command()
async def Devon(ctx):
    await ctx.send('I fucking hate Devon.')

@client.event
async def on_command_error(ctx,error):
        await ctx.send ('Invalid command you fucking idiot')

@client.command()
async def allCommands(ctx):
    await ctx.send('All Commands:\n:devon\n:jason\n:balls\n:paris\n:fuckoff')


@client.command()
async def jason(ctx):
    with open('jasonEyes.jpg', "rb") as fh:
        f = discord.File(fh, filename= 'jasonEyes.jpg')
    await ctx.send(file=f)

@client.command()
async def fuckoff(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ok fine fuck you")
    else:
        await ctx.send('I\'m not in a voice channel you fucking idiot')

@client.command(pass_context=True)
async def balls(ctx):
    if not ctx.author.voice:
        await ctx.send('You gotta connect to a voice channel first retard.')
        return
    else:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('balls.wav')
        voice.play(source)
        time.sleep(15)
        await ctx.guild.voice_client.disconnect()

@client.command(pass_context=True)
async def paris(ctx):
    if not ctx.author.voice:
        await ctx.send('You gotta connect to a voice channel first retard.')
        return
    else:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('paris.wav')
        voice.play(source)
        time.sleep(3.3)
        await ctx.guild.voice_client.disconnect()

keep_alive()
client.run(token)