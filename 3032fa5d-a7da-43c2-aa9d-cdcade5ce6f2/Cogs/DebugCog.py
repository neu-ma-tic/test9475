from discord.ext import commands

class DebugCog(commands.Cog):
    def __init__(Self, Bot):
        Self.Bot       = Bot
        Self.DebugFlag = False

    @commands.command()
    async def dflag(Self, Context):
        if Self.DebugFlag:
            Self.DebugFlag = False
            await Context.send('Debug has been set to false.')
        else:
            Self.DebugFlag = True
            await Context.send('Debug has been set to true.')

    @commands.command()
    async def ping(Self, Context):
        if Self.DebugFlag:
            await Context.send('Pong!')
        else:
            await Context.send('My debug flag must be set for this command')

    @commands.command()
    async def react(Self, Context):
        ...