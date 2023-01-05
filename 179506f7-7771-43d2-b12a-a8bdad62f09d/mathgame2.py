import os, random, time, asyncio
from replit import db
import discord
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$')
 
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
  await ctx.send('hello!')

@bot.command()
async def invite(ctx):
  await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=836275304963375114&permissions=8&scope=bot>')

@bot.command()
async def mathgame(ctx):
  flag = True
  while flag == True:
    num1 = random.randint(0,21)
    num2 = random.randint(0,21)
    answer = num1 * num2
    await ctx.send("What is " + str(num1) + " times " + str(num2) + " ?")
    try:
      msg = await bot.wait_for('message', timeout=10)
      print(msg)
      if int(msg.content) == int(answer):
        await ctx.send(str(msg.author) + " is correct!")  
      elif msg.content == ('quit'):
        flag = False
        print("test")
    except (asyncio.TimeoutError, ValueError):
      await ctx.send("You've ran out of time.")
  await ctx.send("The game has ended.") 


keep_alive() 
bot.run(os.environ['TOKEN2'])
