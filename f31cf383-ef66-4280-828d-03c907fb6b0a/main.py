import
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
  await ctx.send("Hello! How are you doing? ")

@bot.command()
async def forest_level(ctx):
  forest_levels = ["1, A Small Forest.", "2, Amazon Rainforest", '3, ORCHARD']
  await ctx.send(random.choice(forest_levels))

  @bot.command(name='rps')
  async def rps(ctx):
    await ctx.send("What is your selection? ")
    user_selection = ctx.response
    bot_selection = random.choice['rock', 'paper', 'scissors']
    
  

bot.run("ODI5NTA0MTE2MDY1NDM1NzA5.YG5F6A.TYxJxgVlaYVGUM_H1GF8dAb7GwY")

