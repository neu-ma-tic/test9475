import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def on_start():
  await print("Bot is online")

token = ("MTAzNjY5Mjg5ODgxNDY0NDMxNA.GXevZb.R_THEAB_Bgg6t6wMPvkUQGcEGCbNzvQ89DTxPs")
bot.run(token)