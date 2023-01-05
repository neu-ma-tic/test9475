import discord

API_KEY = "ODYzNTgzNjc2MjM4OTIxODAx.YOpA-Q.WiwIuvdGW6TIDWrEr9XcPvynwH4"

bot = discord.Client()

@bot.event
def on_ready():
  print("Connected to: {0}".format(bot.user))

@bot.event
def on_message(message):

  if message.author == bot.user:
    return
  
  if message.content.startswith('$test_string'):
    await message.channel.send("Recieved")
  
  print(message.content)


bot.run(API_KEY)

