import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="睡覺+抽卡GG人 by Juice", description="沒有反應，就只是一個抽卡機器人，以下是指令", color=0xcc25de)
        embed.add_field(name="佑樹10連抽、佑樹十連抽", value="PCR抽卡，有保底系統", inline=False)
        embed.add_field(name="佑樹抽pu、佑樹抽PU", value="PCR抽pick up，有保底系統", inline=False)
        embed.add_field(name="狼師10連抽、狼師十連抽", value="BA抽卡，有保底系統", inline=False)
        embed.add_field(name="狼師抽pu、狼師抽PU", value="BA抽pick up，有保底系統", inline=False)
        embed.add_field(name="今早跟誰睡、今午跟誰睡、今晚跟誰睡", value="請GG人幫你決定要跟哪個老婆睡", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        channel = []
        channel.append(832152942110834758)
        channel.append(812632311946412032)
        self.channel = self.bot.get_channel(channel[1])
        print (channel)
        await self.channel.send('test')


def setup(bot):
    bot.add_cog(React(bot))
