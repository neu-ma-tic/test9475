import discord
from discord.ext import commands
import datetime
import pytz

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'目前延遲為 {round(self.bot.latency * 1000000) / 1000} ms')

    @commands.command()
    @commands.has_permissions(manage_messages=True) 
    async def iu(self, ctx):
        embed=discord.Embed(title="測試執行", description="此功能尚在研發中，請等待後續更新", color=0xd1fffa, timestamp= datetime.datetime.now(pytz.timezone('Asia/Taipei')))
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command() 
    async def purge(self, ctx, num : int):
        await ctx.channel.purge(limit= (num + 1))
    
    @commands.command() 
    async def help(self, ctx):
        embed=discord.Embed(title="指令列表", description="以下提供目前此機器人可使用的相關指令", color=0xc2ffe6)
        embed.add_field(name="ping", value="檢驗機器人的延遲", inline=True)
        embed.add_field(name="purge <數量>", value="刪除數則訊息", inline=True)
        embed.add_field(name="say <訊息>", value="讓機器人說出指定訊息", inline=True)
        embed.add_field(name="help", value="顯示此訊息", inline=True)
        embed.set_footer(text="若是有其他問題請詢問悠悠，指令前墜為 >>")
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(main(bot))