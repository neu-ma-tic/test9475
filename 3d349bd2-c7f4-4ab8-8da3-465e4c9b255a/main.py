import os
import discord

import time
from discord.ext import commands

client = commands.Bot(command_prefix = '#')
my_secret = os.environ['DISCORD_BOT_SECRET']
client.remove_command('help')


@client.command()
async def help(ctx):

  print('Help')

  send = ctx.send

  embed = discord.Embed(title = "Current Commands", description = "Here are the currently available commands", color = 0x0d0f0f)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/842992956474392596/842993177564807178/unknown.png")
  embed.add_field(name = '#help', value = '```Shows this. ```', inline = False)
  await send(embed = embed)


client.run(my_secret)