# all classes will be developed here to utilize OOP
import discord
from discord.ext import commands
import os
# from keep_alive import keep_alive
# here's a rundown of the basic overall idea:
# 1) !cmd - list of available commands
# 2) !rules - list of all rules in MD
# 3) !report/!ban/!promote/!etc. - for user/admin functions
# 4) special additions to calculate, examine, novelty, etc.
# 5) check for other alt bots to add for novelty purposes

class DiscordBot():
    def __init__(self):
        pass

    bot = commands.Bot(command_prefix='!')

    # # available commands draft
    # @bot.command()
    # async def help(ctx):
    #     # TODO: test embed with multiline comment instead of whitespace characters, etc...
    #     embed = discord.Embed(title='Command Help', 
    #                   description='**Rules**\n!rules\n*some definition of what command does.*\n\n**test**\n!test [args]\n')
    #     await ctx.send(embed=embed)

    # rules draft
    @bot.command()
    async def rules(ctx):
        '''Just some lovely text to cheer you up'''
        embed = discord.Embed(title='Rules',
                       url='https://www.youtube.com/',
                       description='The rules and guidelines that apply to this community can be found on our [rules page](https://somebogusurl.donotclickit.com). We expect all members of the community to have read and understood these.')
        await ctx.send(embed=embed)

    @bot.command()
    async def test(ctx):
        await ctx.send(ctx.message.content[::-1])

    @bot.command()
    async def randnum(ctx):
        pass

    # keep_alive()
    token = os.environ.get("DISCORD_BOT_SECRET")
    bot.run(token)
    