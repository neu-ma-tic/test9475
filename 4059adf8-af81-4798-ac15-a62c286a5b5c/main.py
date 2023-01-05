# import discord
# from discord.ext import commands
# import os
# from keep_alive import keep_alive
# import random
# from time import sleep

import traceback
from models import DiscordBot
from keep_alive import keep_alive

# # client assignment using pure discord
# client = discord.Client()

# @client.event
# async def on_ready():
#     print("I'm in")
#     print(client.user)

# @client.event
# async def on_message(message):
#     if message.author != client.user:
#         await client.send(message.channel, message.content[::-1])


# keep_alive()
# token = os.environ.get("DISCORD_BOT_SECRET")
# client.run(token)

# # bot assignment using commands extension
# bot = commands.Bot(command_prefix='!')

# # test command. all new functionality will start here.
# @bot.command()
# async def test(ctx):
#     await ctx.send(ctx.message.content[::-1])

# @bot.command()
# async def reverse(ctx):
#     await ctx.send(ctx.message.content[::-1])

# @bot.command()
# async def rules(ctx):
#     # output rules in markdown
#     pass
# bot = DiscordBot()


# @bot.command()
# async def randnum(ctx):
#     a, b = ctx.message.content.split()[1:3]
#     num = random.randint(int(a), int(b))
#     await ctx.send('{}'.format(num))
    # await ctx.send('Okay, I\'m going to give you a random number. How does {} sound?'.format(random.randint(a,b)))
        # sleep(5)
    # rand_num = str(random(0, 25))
    # await ctx.send(rand_num)

# @bot.command()
# async def moon(ctx):
#     await ctx.send('I heard you! {0}'.format(ctx.author))

# keep_alive()
# token = os.environ.get("DISCORD_BOT_SECRET")
# bot.run(token)



try:
  DiscordBot()
  keep_alive()
except Exception as e:
  print(traceback.print_exc())