import discord
import os
from discord.ext import commands

from keep_alive import keep_alive

client = commands.Bot(command_prefix=">")
discord.Intents.all()


async def check(ctx):
	if ctx.author.id in [640235175007223814, 237959218139889665]:
		return True
	else:
		return False


for cogpath in os.listdir("cogs"):
	try:
		if cogpath.endswith(".py"):
			client.load_extension(f'cogs.{cogpath[:-3]}')
			print(f'Loaded {cogpath}')
	except Exception as ex:
		print(
		    f'Something wen\'t wrong while loading {cogpath}\nError: {ex}\n\n')


@client.event
async def on_ready():
	print(f"Logged in as {client.user}")


@client.command(aliases=["disable"])
@commands.check(check)
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	await ctx.message.channel.send(f"Unloaded {extension}", delete_after=7)


@client.command(aliases=["enable"])
@commands.check(check)
async def load(ctx, extension=None):
	client.load_extension(f"cogs.{extension}")
	await ctx.message.channel.send(f"Loaded {extension}", delete_after=7)


@client.command()
@commands.check(check)
async def reload(ctx, extension):
	client.reload_extension(f"cogs.{extension}")
	await ctx.send(f"Reloaded {extension}", delete_after=7)


keep_alive()

client.run(os.getenv("TOKEN"))
