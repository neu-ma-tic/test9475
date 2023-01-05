import os
import discord
from discord.ext import commands
from webserver import keep_alive

bot = commands.Bot(command_prefix=".")

#GREETINGS
@bot.command()
async def hello(ctx):
  await ctx.send("Hello There!")
@bot.command()
async def yo(ctx):
  await ctx.send("yo, yo")
@bot.command()
async def uwu(ctx):
  await ctx.send("~~uwu~~")
@bot.command()
async def shut(ctx):
  await ctx.send("Ok, sowwyyy")
@bot.command()
async def serverded(ctx):
  await ctx.send("what can i do?")
@bot.command()
async def nothing(ctx):
  await ctx.send(":(")
@bot.command()
async def lol(ctx):
  await ctx.send("what r u laughing about?")
@bot.command()
async def die(ctx):
  await ctx.send("not in a mood to die today :)")
@bot.command()
async def hi(ctx):
  await ctx.send("Hello There!")
@bot.command()
async def morning(ctx):
  await ctx.send("Good Morning :)")
@bot.command()
async def afternoon(ctx):
  await ctx.send("Good Afternoon :)")
@bot.command()
async def evening(ctx):
  await ctx.send("Good Evening :)")
@bot.command()
async def night(ctx):
  await ctx.send("Good Night, Sweet Dreams! :)")
@bot.command()
async def bye(ctx):
  await ctx.send("Bye, have a nice day! :)")
@bot.command()
async def ping(ctx):
  await ctx.send("pong")
@bot.command()
async def getlost(ctx):
  await ctx.send("you bad 😕")
@bot.command()
async def say(ctx, textToSay):
  await ctx.send(textToSay)
@bot.command()
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#GENERAL
@bot.command()
async def helpme(ctx):
  await ctx.send("Hi, im Anant's bot! I'm all yours! if u wanna see all of the things i can do, write '.allcommands' ")

@bot.command()
async def allcommands(ctx):
  await ctx.send("hello / hi / bye / morning / afternoon / evening / night / subscribe / lol / nothing / serverded / uwu / shut / die / ping/ getlost")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit:int):
    await ctx.channel.purge(limit=limit)
    await ctx.send(f'{limit} messages have been cleared.')

  
#SUBSCRIBE
@bot.command()
async def subscribe(ctx):
  await ctx.send("SUBSCRIBE TO ANANT GAME DEV - https://www.youtube.com/channel/UCAPbJ9TZ7lf9JlBVwe2idNA?sub_confirmation=1")


@bot.command()
async def what(ctx):
  await ctx.send("what, what?")

#ON START
@bot.event
async def on_ready():
  print("Logged in!")
  await bot.change_presence(activity=discord.Game(name=".helpme"))

keep_alive()
token = os.environ['TOKEN']

bot.run(token)
