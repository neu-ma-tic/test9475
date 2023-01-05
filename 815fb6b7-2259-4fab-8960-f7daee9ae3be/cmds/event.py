import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='UTF8') as Rfile:
    Rdata = json.load(Rfile)

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, check):
        await ctx.send(check)

def setup(bot):
    bot.add_cog(event(bot))