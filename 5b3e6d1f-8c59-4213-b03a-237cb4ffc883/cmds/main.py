import discord
from discord import channel # 將dc的模組導入
from discord.ext import commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import datetime

class main(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command() # 回傳延遲值
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)}毫秒(ms)' )
        
    @commands.command()
    async def HI(self,ctx):
        await ctx.send("HI :sunglasses: ")
        
    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="about", description="一個酷似會長的機器人", 
        timestamp= datetime.datetime.utcnow())        
        embed.set_author(name="蓮魚", icon_url="https://cdn.discordapp.com/attachments/891871112261165066/901169675751280640/d37412014174907f.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/891871112261165066/901169047431958578/1.gif")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def sayd(self, ctx, * ,msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def clean(self, ctx, num:int): 
        await ctx.channel.purge(limit=num+1)
        
    
def setup(bot):
    bot.add_cog(main(bot))