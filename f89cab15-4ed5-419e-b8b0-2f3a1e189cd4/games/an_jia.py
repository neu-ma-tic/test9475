from random import choice
from random import randint as rand

from core import CogInit, readFile
from discord.ext import commands

images = readFile("others")["an-jia"]
started = False
result = ""
way = []


def dice(side):
    if side <= 6:
        side = 6
    else:
        return rand(1, side)


"""def slot():
  pass"""


def coin(amount):
    result = ""
    for i in range(amount):
        result += choice(images["coin"])
    return result


def bzz(amount):
    result = ""
    for i in range(amount):
        result += choice(images["bzz"])
    return result


functions = [dice, coin, bzz]


class An_Jia(CogInit):
    @commands.command(
        aliases=["aj_s"],
        usage="+aj_s <安價敘述> <方法> <項目個數>(方法為擲骰時代表骰子面數)",
        help="開始安價，+aj_e 可強制結束\n方法：0:擲骰, 1:硬幣, 2:4色籤",
    )
    async def start_An_Jia(self, ctx, item="", method: int = -1, times: int = 1):
        global started
        global functions
        global result
        global way

        await ctx.message.delete()
        if not started:
            if method == -1:
                method = rand(0, len(functions))
            way = [method, times]
            result = functions[method](times)
            message = f"{ctx.author.mention}開始了安價，輸入`+aj 指示(不可省略)`參加\n{result}"
            if item:
                message += f"：{item}"
            await ctx.send(message)
            started = True
        else:
            await ctx.send("目前已有安價正在進行", delete_after=5)

    @commands.command(aliases=["aj"])
    async def join_An_Jia(self, ctx, *, arg=""):
        global started
        global result
        global functions
        global way

        await ctx.message.delete()
        if started:
            outcome = (functions[way[0]])(way[1])
            message = f"{ctx.author.mention}：\n{outcome} "
            if outcome == result:
                message += arg
                started = False
                await ctx.send(message, delete_after=20)
            else:
                await ctx.send(message, delete_after=5)
        else:
            await ctx.send("目前沒有安價在進行", delete_after=5)

    @commands.command(aliases=["aj_e"])
    async def end_an_jia(self, ctx):
        global started
        await ctx.message.delete()
        if started:
            await ctx.send("以強制結束", delete_after=5)
            started = False


def setup(bot):
    bot.add_cog(An_Jia(bot))
