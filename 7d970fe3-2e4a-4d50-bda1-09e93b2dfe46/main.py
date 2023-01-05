from discord.ext import commands
import os

botClient = commands.Bot(command_prefix='$')

@botClient.command()
async def foo(ctx, arg):
    await ctx.send(arg)

botClient.run(os.environ['DiscordBotToken'])