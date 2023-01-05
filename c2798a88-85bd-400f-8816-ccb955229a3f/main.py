import discord
from discord.ext import commands
import youtube_dl
import os
import asyncio

client = commands.Bot(command_prefix="&")


@client.command()
async def play(ctx, url: str):
	song_there = os.path.isfile("song.mp3")
	try:
		if song_there:
			os.remove("song.mp3")
	except PermissionError:
		await ctx.send(
		    "Poczekaj aż skończy się muzyka lub użyj komendy 'stop'. ")
		return

	voiceChannel = discord.utils.get(ctx.guild.voice_channels,
	                                 name='Geneal')
	await voiceChannel.connect()
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

	ydl_opts = {
	    'format':
	    'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			os.rename(file, "song.mp3")
	voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_connected():
		await voice.disconnect()
	else:
		await ctx.send("Bot nie jest połączony z kanałem głosowym.")

@client.command()
async def pause(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		await ctx.send("Aktualnie nic nie gra.")

@client.command()
async def resume(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send("Muzyka nie jest zastopowana.")

@client.command()
async def stop(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	voice.stop()

@client.command()
async def join(ctx):
	channel = ctx.author.voice.channel
	await channel.connect()


@client.command()
async def fuckoff(ctx):
	await ctx.voice_client.disconnect()


@client.command()
async def info(ctx, *, member: discord.Member):
	"""Mówi pare informacji o użytkowniku"""
	fmt = '{0} dołączył {0.joined_at} i ma {1} role.'
	await ctx.send(fmt.format(member, len(member.roles)))


@info.error
async def info_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Nie znalazłem tego użytkownika')


@client.command()
async def say(ctx, *, arg):
	await ctx.send(arg)


@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! zajęło mi to {round(client.latency * 1000)}ms')

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await ctx.kick(userName)

@client.command()
async def test(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def vcmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)

@client.command()
async def vcunmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)

@client.command()
async def vcdeafen(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(unmute=False)


client.run('ODIxODcyMDcyNjI4MTA5NDAy.YFKCAw.t0lHvi3910u1IyJqR9PSCAtLgIA')

