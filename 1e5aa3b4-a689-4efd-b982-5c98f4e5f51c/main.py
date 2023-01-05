import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(
	name = "hello", 
	description = "hello world!",
)
async def _hello(ctx: SlashContext):
	await ctx.send("World!")

@slash.slash(
	name = "ping",
	description = "Pings the bot.",
)
async def _ping(ctx: SlashContext):
	await ctx.send(f"Pong! Took {round(bot.latency * 1000)}ms.")

@slash.slash(
	name = "say",
	description = "Say things with the bot.",
	options = [
		create_option(
			name = "option",
			description = "put an option",
			option_type = 3,
			required = True,
		),
	]
)
async def _say(ctx: SlashContext, option: str):
	await ctx.send(option)

bot.run(os.environ['DISCORD_TOKEN'])