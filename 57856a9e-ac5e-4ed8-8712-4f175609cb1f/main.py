import os
import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix=".")
client = discord.Client()

@bot.command()
async def evie(ctx):
  await ctx.send("EWWWW SHE STINKS!!!")

@bot.command()
async def nick(ctx):
  await ctx.send("he is soooo good smelling")

@bot.command()
async def privakii(ctx):
  await ctx.send ("EWWWWWWWWWWWW SHE SMELLS EVEN WORSE THAN EVIE ***DIES***")

@bot.command()
async def downbad(ctx):
  await ctx.send ("https://www.pornhub.com")

@bot.command()
async def striker(ctx):
  await ctx.send ("some boy that exists and evie isnt admiting she wrote the command nor she loves him")
  await ctx.send ("BUT I KNOW SHE TRIED THE COMMAND")

@bot.command()
async def game(ctx):
  await ctx.send ("Hello friend, this i a whole new game programmed by Nick and Melita. The game you are about to play is not recomanded for discord users that are not aware of the pain which can make them uncomfortable in the next seconds/minutes/hours as they continue playing it......  **YOU** - **HAVE** - **BEEN** - **WARNED**")
  await ctx.send ("If you decided to continue this game, you can do that by typing the command .start")

@bot.command()
async def start(ctx):
  await ctx.send ("You have started the Evie's game. Now you have to choose a number from 1 to 10 as your Evie dare.     *this may be used once* -- and some might have to be explained once chosen")
  await ctx.send ("**CHOOSE YOUR ANSWER WISE**")

  @bot.command()
  async def one(ctx):
    await ctx.send ("Room tour")

@bot.command()
async def two(ctx):
    await ctx.send ("Death wish for me")

@bot.command()
async def three(ctx):
    await ctx.send ("*fuck rip me*")

@bot.command()
async def four(ctx):
 await ctx.send ("gawk gawk 2secs")

@bot.command()
async def five(ctx):
  await ctx.send ("vacuum")

@bot.command()
async def six(ctx):
 await ctx.send ("NOTHING NO WAY U DID THIS")

@bot.command()
async def seven(ctx):
  await ctx.send ("octopus")

@bot.command()
async def eight(ctx):
 await ctx.send ("party")

@bot.command()
async def nine(ctx):
 await ctx.send ("Draw me shit i tell u")

@bot.command()
async def ten(ctx):
 await ctx.send ("My name on hand")
  

token = os.environ['TOKEN']
bot.run(token)
