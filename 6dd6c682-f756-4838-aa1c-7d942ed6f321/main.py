import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
  print("Bot is ready")


@bot.event
async def on_message(message):
    msg = message.content.lower()

    if(msg.startswith("-")):
        if ("rules" in msg):
            await message.channel.send("Test")

        elif ("hello" in msg or "hey" in msg or "hi" in msg or "yello" in msg):
            await message.channel.send("Hello!")


        await bot.process_commands(message)






@bot.command
async def clear(ctx, amount = 10):
    ctx.channel.purge(limit = amount)

my_secret = os.environ['Token']
keep_alive()
bot.run("ODYwMjIxMzA5MzA0ODMyMDky.YN4Fhg.EQF0j3vp5ahJK5D-JMnfeDfoHYA")