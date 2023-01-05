import random

from core import CogInit, readFile
from discord.ext import commands

statu = 0
participants = []
initiator = 0
item = ""
winner_num = 0
winners = []
botId = readFile("setting")["botId"]


class Loot(CogInit):
    @commands.command()
    async def loot(self, ctx, n: int = 1, *, arg=""):
        global statu
        global initiator
        global item
        global winner_num
        if statu == 1:
            await ctx.send(
                f"已經有抽獎正在進行中，發起人：{self.bot.get_user(initiator).mention}", delete_after=3
            )
        else:
            if n <= 0:
                await ctx.send("無效的抽出人數", delete_after=3)
            else:
                winner_num = n
                statu = 1
                initiator = ctx.author.id
                item = arg
                await ctx.send(
                    f"{ctx.author.mention} 開始了抽獎，預計抽出 ***{winner_num}*** 個人，輸入'**抽**'參加抽獎，指令'**+loot_e**'抽出得獎人"
                )
        await ctx.message.delete()

    @commands.command()
    async def loot_e(self, ctx):
        global initiator
        global item
        global participants
        global statu
        global winner_num
        global winners
        if statu == 0:
            await ctx.send("目前沒有抽獎", delete_after=3)
        else:
            if ctx.author.id != initiator:
                await ctx.send("你不是抽獎發起人", delete_after=3)
            else:
                await ctx.send(f"參加抽獎人數： {len(participants)}", delete_after=5)
                if len(participants) < winner_num:
                    await ctx.send("參加人數少於預計抽出人數", delete_after=5)
                else:
                    winners = random.sample(participants, winner_num)
                    winners_m = ""
                    for i in winners:
                        winners_m += f"{self.bot.get_user(i).mention} "
                    await ctx.send(f"恭喜\n{winners_m}\n抽到了 {item}", delete_after=15)
                participants = []
                statu = 0
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, msg):
        global participants
        global initiator
        global statu
        if msg.content == "抽" and statu == 1 and msg.author.id != botId:
            if msg.author.id == initiator:
                await msg.channel.send(
                    f"{self.bot.get_user(initiator).mention} 你不行抽你自己", delete_after=4
                )
            elif msg.author.id in participants:
                await msg.channel.send(f"{msg.author.mention} 你已參加此抽獎", delete_after=3)
            else:
                participants.append(msg.author.id)
                await msg.channel.send(f"{msg.author.mention} 參加成功", delete_after=5)
            await msg.delete(delay=3)


def setup(bot):
    bot.add_cog(Loot(bot))
