#!/opt/virtualenvs/python3/bin/python
import logging
import os

import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

from core import Config, keep_alive

load_dotenv()

logger = logging.getLogger("discord")
logger.setLevel(logging.WARNING)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
error_log = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")
error_log.setFormatter(formatter)
logger.addHandler(error_log)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="+", owner_id=Config.bot_owner, intents=intents)
slash = SlashCommand(bot, override_type=True, sync_commands=True, sync_on_cog_reload=True)

token = os.environ["BOT_TOKEN"]


@bot.event
async def on_ready():
    print("Bot is online")


def initialization(folders: list):
    for folder in folders:
        for f in os.listdir(f"./{folder}"):
            if f.endswith(".py"):
                try:
                    bot.load_extension(f"{folder}.{f[:-3]}")
                except Exception as e:
                    print(e)
                    print()
                else:
                    print(f"{folder}.{f[:-3]} load success.")


initialization(Config.folders)


if __name__ == "__main__":
    keep_alive()
    try:
        bot.run(token)
    except Exception as e:
        print(e)
