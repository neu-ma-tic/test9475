import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", case_insensitive = True)

@bot.event
async def on_ready():
  print('Pronto pra funcionar como {0.user}')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  await bot.process_commands(message)
  
  
@bot.command(name="oi")
async def send_hello(ctx):
  name = ctx.author.name

  response = "Oi " + name
  
  await ctx.send(response)

@bot.command(name="youtube")
async def send_youtube(ctx):
  
  await ctx.send("https://www.youtube.com/watch?v=zgezo5I3waM")


bot.run('OTU0MTQ0Mjk4MDkyMzU5NzIz.YjO2Hw.kqWxl22le6Se02QouciiaplQ5mw')