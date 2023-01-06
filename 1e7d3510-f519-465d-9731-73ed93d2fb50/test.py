import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

@bot.command()
async def mhi(ctx):
  response='more hi!!!'
  await ctx.send(response)

bot.run(TOKEN)