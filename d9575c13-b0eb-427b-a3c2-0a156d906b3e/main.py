import discord
import os
from discord.ext import commands
import colorama
from colorama import Fore, Style

bot = commands.Bot(command_prefix= "sl ", case_insensitive=True)

@bot.event
async def on_connect():
  print (Fore.RED + "Loading...")
  print (Fore.BLUE + "Loaded packets")
  print (Fore.GREEN + "Loading Webserver...")
  print (Fore.CYAN + "Loading script...")
  print (Fore.MAGENTA + "Loaded Successfully!")
  print (Fore.RED + "Awakening bot...")
  print (Fore.YELLOW + "Bot online!")
bot.remove_command(name="help")

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(
    color=ctx.author.color, timestamp=ctx.message.created_at)
  embed.set_author(name="bot commands",icon_url=ctx.author.avatar_url)
  embed.add_field(name="help", value= "These are all the commands, btw our prefix for all of our commands are sl (commands are still being made)", inline=False)
  await ctx.send(embed=embed)
