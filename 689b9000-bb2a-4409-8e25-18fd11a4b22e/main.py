import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def test(ctx):
    await ctx.send("test.ok!")


bot.run("MTAwNTI0NDAzOTA5MzgxNzQ3Ng.GoT1BE.tnJ_50_95p5rmzjzMleknlmy_A14YzjhXsp-sI")