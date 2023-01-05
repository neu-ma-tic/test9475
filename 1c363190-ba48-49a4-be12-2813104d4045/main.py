import discord
from discord.ext import commands, tasks
from datetime import datetime
from discord_slash import SlashCommand
from colorama import Fore
import os
from keep_alive import keep_alive

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")


client = commands.Bot(
    command_prefix=commands.when_mentioned_or("."), description="Edit", case_insensitive=True, intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
client.remove_command("help")

@client.event
async def on_ready():
  print("The bot has started in {} servers".format(len(client.guilds)))

__version__ = "1.0.0"

@client.event
async def on_guild_join(guild):
  print(Fore.GREEN + f"I have joined {guild}" + Fore.RESET)
  for channel in guild.text_channels:
    if channel.permissions_for(guild.me).send_messages:
      embedHi = discord.Embed(
			    title="Thanks for adding me!",
			    description=
			    f"Hi! I am {client}",
          url="",
			    colour=discord.Colour.red())
      embedHi.set_thumbnail(
			    url=
			    "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
			)
      embedHi.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
      embedHi.set_footer(
			    text="© Baz - The Impostor - Among Us bot for Discord")
      await channel.send(embed=embedHi)
    break



@client.event
async def on_guild_remove(guild):
  print(Fore.GREEN + f"I have left {guild}" + Fore.RESET)


@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")



@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

Fore.RESET

keep_alive()
client.run(os.getenv("TOKEN"))