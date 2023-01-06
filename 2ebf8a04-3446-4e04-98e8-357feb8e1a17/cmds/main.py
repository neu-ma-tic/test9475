import discord
from discord.ext import commands 
import json,random
from  core.classes import Cog_Extension

class Main(Cog_Extension):
    

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def sm(self,ctx,*,msg):
      #刪除使用者所說的訊息
      await ctx.message.delete()
      await ctx.send(msg)
    
    @commands.command()
    async def clean(self,ctx,num : int):
      await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def clean_all(self,ctx):
      await ctx.channel.purge()
      await ctx.send('成功刪除所有訊息')

def setup(bot):
    bot.add_cog(Main(bot))