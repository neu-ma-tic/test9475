import discord
from discord.ext import commands
import json
import random
import os
import keep_alive

with open('setting.json', 'r', encoding='UTF8') as Rfile:
    Rdata = json.load(Rfile)

bot = commands.Bot(command_prefix='>>',
                   owner_id=Rdata['Owner'],
                   help_command=None)


@bot.event
async def on_ready():
    print(">> Bot is online<<")


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(Rdata['TOKEN'])
