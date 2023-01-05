from discord.ext import commands
from datetime import date
# from ursina import *

class RequestCog(commands.Cog):
    def __init__( Self, Bot):
        Self.Bot = Bot

    @commands.command()
    async def request( Self, Context, *Arguments):
        Today = date.today()
        Request = ' '.join(Arguments)

        with open('Data/RequestLog.txt', 'a') as File:
            File.write('<' + str(Today) + '> ' + Context.author.display_name + ' sent a request: ' + Request + '\n')
            print('<' + str(Today) + '> ' + Context.author.display_name + ' sent a request: ' + Request)
    
    @commands.command()
    async def listRequests(Self, Context):
        if not Context.author.id ==  456489836614909963: return

        with open('Data/RequestLog.txt') as File:
            Reqs = File.read()
            if Reqs == '':
                return await Context.send('No requests to show')
            await Context.send(Reqs)

    @commands.command()
    async def clearRequests(Self, Context):
        if not Context.author.id ==  456489836614909963: return

        with open('Data/RequestLog.txt', 'r+') as File:
            File.truncate(0)
